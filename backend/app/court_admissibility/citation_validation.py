"""Legal citation validation and formatting"""
import logging
import re
from typing import Dict, Any, List

logger = logging.getLogger(__name__)


class CitationValidator:
    """Validate and format legal citations according to standard formats"""
    
    def __init__(self):
        self.citation_patterns = self._load_citation_patterns()
        
    def validate_citation(
        self,
        citation: str,
        format_style: str = "bluebook"
    ) -> Dict[str, Any]:
        """
        Validate legal citation format.
        
        Args:
            citation: Citation string to validate
            format_style: Citation format (bluebook, alwd, etc.)
            
        Returns:
            Validation result with corrections if needed
        """
        logger.info(f"Validating citation: {citation}")
        
        # Detect citation type
        citation_type = self._detect_citation_type(citation)
        
        # Validate format
        is_valid = self._validate_format(citation, citation_type, format_style)
        
        # Generate corrections if needed
        corrections = []
        if not is_valid:
            corrections = self._suggest_corrections(citation, citation_type)
        
        return {
            "citation": citation,
            "type": citation_type,
            "format_style": format_style,
            "is_valid": is_valid,
            "corrections": corrections
        }
    
    def format_citation(
        self,
        citation_parts: Dict[str, str],
        citation_type: str,
        format_style: str = "bluebook"
    ) -> str:
        """
        Format citation according to specified style.
        
        Args:
            citation_parts: Dictionary with citation components
            citation_type: Type of citation (case, statute, etc.)
            format_style: Target format style
            
        Returns:
            Properly formatted citation
        """
        if citation_type == "case":
            return self._format_case_citation(citation_parts, format_style)
        elif citation_type == "statute":
            return self._format_statute_citation(citation_parts, format_style)
        elif citation_type == "regulation":
            return self._format_regulation_citation(citation_parts, format_style)
        else:
            return citation_parts.get('raw', '')
    
    def _detect_citation_type(self, citation: str) -> str:
        """Detect type of legal citation"""
        # Case law patterns
        if re.search(r'\d+\s+[A-Z][a-z]*\.?\s*\d*\s+\d+', citation):
            return "case"
        
        # Statute patterns
        if re.search(r'\d+\s+U\.?S\.?C\.?\s*§?\s*\d+', citation):
            return "statute"
        
        # Regulation patterns
        if re.search(r'\d+\s+C\.?F\.?R\.?\s*§?\s*\d+', citation):
            return "regulation"
        
        # Restatement
        if 'Restatement' in citation:
            return "restatement"
        
        return "unknown"
    
    def _validate_format(
        self,
        citation: str,
        citation_type: str,
        format_style: str
    ) -> bool:
        """Validate citation against format rules"""
        patterns = self.citation_patterns.get(citation_type, {})
        pattern = patterns.get(format_style)
        
        if not pattern:
            return False
        
        return bool(re.match(pattern, citation))
    
    def _suggest_corrections(
        self,
        citation: str,
        citation_type: str
    ) -> List[str]:
        """Suggest corrections for invalid citation"""
        corrections = []
        
        if citation_type == "case":
            corrections.append("Ensure format: Party v. Party, Volume Reporter Page (Court Year)")
        elif citation_type == "statute":
            corrections.append("Ensure format: Title U.S.C. § Section")
        
        return corrections
    
    def _format_case_citation(
        self,
        parts: Dict[str, str],
        format_style: str
    ) -> str:
        """Format case citation"""
        # Bluebook format: Party v. Party, Volume Reporter Page (Court Year)
        return (
            f"{parts.get('plaintiff', '')} v. {parts.get('defendant', '')}, "
            f"{parts.get('volume', '')} {parts.get('reporter', '')} "
            f"{parts.get('page', '')} ({parts.get('court', '')} {parts.get('year', '')})"
        )
    
    def _format_statute_citation(
        self,
        parts: Dict[str, str],
        format_style: str
    ) -> str:
        """Format statute citation"""
        # Format: Title U.S.C. § Section
        return f"{parts.get('title', '')} U.S.C. § {parts.get('section', '')}"
    
    def _format_regulation_citation(
        self,
        parts: Dict[str, str],
        format_style: str
    ) -> str:
        """Format regulation citation"""
        # Format: Title C.F.R. § Section
        return f"{parts.get('title', '')} C.F.R. § {parts.get('section', '')}"
    
    def _load_citation_patterns(self) -> Dict[str, Dict[str, str]]:
        """Load regex patterns for different citation types"""
        return {
            "case": {
                "bluebook": r".+\s+v\.\s+.+,\s+\d+\s+[A-Z][a-z\.]*\s+\d+\s+\(.+\s+\d{4}\)"
            },
            "statute": {
                "bluebook": r"\d+\s+U\.S\.C\.\s+§\s+\d+"
            },
            "regulation": {
                "bluebook": r"\d+\s+C\.F\.R\.\s+§\s+\d+"
            }
        }
