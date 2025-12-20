"""
Legal text parser for structured document analysis.

This module parses extracted text into structured legal document components:
- Section hierarchy detection
- Clause and paragraph segmentation
- Metadata extraction (dates, parties, case numbers)
- Legal citation detection
"""
import logging
import re
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime

logger = logging.getLogger(__name__)


@dataclass
class DocumentSection:
    """Represents a section in a legal document"""
    section_number: Optional[str]
    title: str
    content: str
    level: int  # Hierarchy level (1 = top level, 2 = subsection, etc.)
    start_position: int
    end_position: int


@dataclass
class LegalCitation:
    """Represents a legal citation found in text"""
    text: str
    citation_type: str  # case, statute, regulation, etc.
    position: int


@dataclass
class ParsedDocument:
    """Complete parsed document structure"""
    raw_text: str
    sections: List[DocumentSection]
    citations: List[LegalCitation]
    metadata: Dict[str, Any]
    paragraphs: List[str]


class LegalTextParser:
    """
    Parser for legal document text into structured components.
    
    Uses regex patterns and heuristics optimized for legal documents.
    """
    
    # Common legal document section patterns
    SECTION_PATTERNS = [
        # Roman numerals: I., II., III.
        r'^([IVX]+)\.\s+(.+)$',
        # Numbers with periods: 1., 2., 3.
        r'^(\d+)\.\s+(.+)$',
        # Letters with periods: A., B., C.
        r'^([A-Z])\.\s+(.+)$',
        # Article/Section: "ARTICLE I", "SECTION 1"
        r'^(ARTICLE|SECTION|PART)\s+([IVX\d]+)[:\.]?\s*(.*)$',
        # All caps headers
        r'^([A-Z][A-Z\s]{3,})[:\.]?\s*$',
    ]
    
    # Legal citation patterns (simplified - production would use more comprehensive patterns)
    CITATION_PATTERNS = [
        # Case citations: "123 F.3d 456", "567 U.S. 890"
        (r'\b\d+\s+[A-Z][a-z]*\.?\s*(?:\d+d|3d)?\s+\d+\b', 'case'),
        # Statute citations: "28 U.S.C. § 1331", "Cal. Civ. Code § 1234"
        (r'\b\d+\s+[A-Z][a-z.]+\s+(?:Code|Stat\.|C\.F\.R\.)\s*§\s*\d+', 'statute'),
        # U.S. Code: "42 USC 1983"
        (r'\b\d+\s+U\.?S\.?C\.?\s*§?\s*\d+', 'statute'),
        # Section references: "§ 123", "§§ 123-456"
        (r'§§?\s*\d+(?:-\d+)?', 'section'),
    ]
    
    # Date patterns
    DATE_PATTERNS = [
        r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}\b',
        r'\b\d{1,2}/\d{1,2}/\d{4}\b',
        r'\b\d{4}-\d{2}-\d{2}\b',
    ]
    
    # Case number patterns
    CASE_NUMBER_PATTERNS = [
        r'(?:Case|Docket|Civil|Criminal)\s+(?:No\.|Number|#)\s*[:\s]*([A-Z0-9-:]+)',
        r'\b\d{1,2}:\d{2}-(?:cv|cr)-\d{5}\b',  # Federal case numbers
    ]
    
    def __init__(self):
        """Initialize parser with compiled regex patterns"""
        self.compiled_section_patterns = [
            re.compile(pattern, re.MULTILINE) for pattern in self.SECTION_PATTERNS
        ]
        self.compiled_citation_patterns = [
            (re.compile(pattern), ctype) for pattern, ctype in self.CITATION_PATTERNS
        ]
        self.compiled_date_patterns = [
            re.compile(pattern) for pattern in self.DATE_PATTERNS
        ]
        self.compiled_case_patterns = [
            re.compile(pattern, re.IGNORECASE) for pattern in self.CASE_NUMBER_PATTERNS
        ]
    
    async def parse_document(self, text: str, doc_metadata: Dict[str, Any] = None) -> ParsedDocument:
        """
        Parse legal document text into structured components.
        
        Args:
            text: Raw extracted text
            doc_metadata: Optional metadata from extraction
            
        Returns:
            ParsedDocument with structured components
        """
        logger.info(f"Parsing document ({len(text)} characters)")
        
        # Extract various components
        sections = self._extract_sections(text)
        citations = self._extract_citations(text)
        paragraphs = self._extract_paragraphs(text)
        
        # Extract metadata from text
        text_metadata = {
            'dates': self._extract_dates(text),
            'case_numbers': self._extract_case_numbers(text),
            'parties': self._extract_parties(text),
            'word_count': len(text.split()),
            'character_count': len(text),
        }
        
        # Merge with extraction metadata if provided
        if doc_metadata:
            text_metadata.update(doc_metadata)
        
        return ParsedDocument(
            raw_text=text,
            sections=sections,
            citations=citations,
            metadata=text_metadata,
            paragraphs=paragraphs
        )
    
    def _extract_sections(self, text: str) -> List[DocumentSection]:
        """
        Extract document sections with hierarchy.
        
        Uses multiple patterns to identify section headers.
        """
        sections = []
        lines = text.split('\n')
        current_position = 0
        
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            if not line_stripped:
                current_position += len(line) + 1
                continue
            
            # Try each section pattern
            matched = False
            for pattern in self.compiled_section_patterns:
                match = pattern.match(line_stripped)
                if match:
                    # Determine section level and details
                    if len(match.groups()) >= 2:
                        section_num = match.group(1)
                        title = match.group(2) if len(match.groups()) >= 2 else line_stripped
                    else:
                        section_num = None
                        title = line_stripped
                    
                    # Estimate hierarchy level
                    level = self._estimate_section_level(line_stripped, section_num)
                    
                    # Collect section content (simplified - would need more sophisticated logic)
                    content_lines = []
                    for j in range(i + 1, min(i + 20, len(lines))):
                        if self._is_section_header(lines[j].strip()):
                            break
                        content_lines.append(lines[j])
                    
                    section = DocumentSection(
                        section_number=section_num,
                        title=title,
                        content='\n'.join(content_lines),
                        level=level,
                        start_position=current_position,
                        end_position=current_position + len('\n'.join([line] + content_lines))
                    )
                    sections.append(section)
                    matched = True
                    break
            
            current_position += len(line) + 1
        
        logger.info(f"Extracted {len(sections)} sections")
        return sections
    
    def _is_section_header(self, line: str) -> bool:
        """Check if a line appears to be a section header"""
        for pattern in self.compiled_section_patterns:
            if pattern.match(line):
                return True
        return False
    
    def _estimate_section_level(self, line: str, section_num: Optional[str]) -> int:
        """Estimate hierarchy level of section"""
        # Simple heuristic based on section number format
        if section_num:
            if re.match(r'^[IVX]+$', section_num):
                return 1  # Roman numerals = top level
            elif re.match(r'^\d+$', section_num):
                if len(section_num) == 1:
                    return 2  # Single digit
                else:
                    return 3  # Multi-digit
            elif re.match(r'^[A-Z]$', section_num):
                return 3  # Letters = lower level
        
        # If all caps, likely top-level header
        if line.isupper():
            return 1
        
        return 2  # Default mid-level
    
    def _extract_citations(self, text: str) -> List[LegalCitation]:
        """Extract legal citations from text"""
        citations = []
        
        for pattern, citation_type in self.compiled_citation_patterns:
            for match in pattern.finditer(text):
                citation = LegalCitation(
                    text=match.group(0),
                    citation_type=citation_type,
                    position=match.start()
                )
                citations.append(citation)
        
        logger.info(f"Extracted {len(citations)} citations")
        return citations
    
    def _extract_paragraphs(self, text: str) -> List[str]:
        """
        Extract paragraphs from text.
        
        Splits on double newlines and filters empty paragraphs.
        """
        # Split on multiple newlines (paragraph breaks)
        paragraphs = re.split(r'\n\s*\n', text)
        
        # Clean and filter
        cleaned_paragraphs = []
        for para in paragraphs:
            para = para.strip()
            if para and len(para) > 20:  # Minimum length for valid paragraph
                cleaned_paragraphs.append(para)
        
        logger.info(f"Extracted {len(cleaned_paragraphs)} paragraphs")
        return cleaned_paragraphs
    
    def _extract_dates(self, text: str) -> List[str]:
        """Extract dates from text"""
        dates = []
        for pattern in self.compiled_date_patterns:
            matches = pattern.findall(text)
            dates.extend(matches)
        
        return list(set(dates))  # Remove duplicates
    
    def _extract_case_numbers(self, text: str) -> List[str]:
        """Extract case numbers from text"""
        case_numbers = []
        for pattern in self.compiled_case_patterns:
            matches = pattern.findall(text)
            case_numbers.extend(matches)
        
        return list(set(case_numbers))
    
    def _extract_parties(self, text: str) -> List[str]:
        """
        Extract party names from text.
        
        This is a simplified implementation - production would use NER.
        """
        parties = []
        
        # Look for "v." pattern (common in case names)
        vs_pattern = re.compile(r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+v\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)')
        matches = vs_pattern.findall(text)
        
        for plaintiff, defendant in matches:
            parties.append(plaintiff.strip())
            parties.append(defendant.strip())
        
        return list(set(parties))[:10]  # Limit to first 10 unique parties
