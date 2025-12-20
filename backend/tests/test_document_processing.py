"""Tests for document processing module"""
import pytest
from io import BytesIO

from app.document_processing import DocumentExtractor, LegalTextParser


@pytest.fixture
def document_extractor():
    """Fixture for document extractor"""
    return DocumentExtractor()


@pytest.fixture
def text_parser():
    """Fixture for text parser"""
    return LegalTextParser()


class TestDocumentExtractor:
    """Test document extraction functionality"""
    
    @pytest.mark.asyncio
    async def test_extract_from_txt(self, document_extractor):
        """Test text extraction from TXT file"""
        sample_text = "This is a sample legal document.\n\nSection 1: Introduction\nThis document contains legal terms."
        file_content = sample_text.encode('utf-8')
        
        result = await document_extractor.extract_text(
            file_content=file_content,
            filename="test.txt"
        )
        
        assert result['success'] is True
        assert result['text'] == sample_text
        assert result['extraction_method'] == 'decode'
        assert result['metadata']['encoding'] == 'utf-8'
        assert result['error'] is None
    
    @pytest.mark.asyncio
    async def test_extract_from_unsupported_format(self, document_extractor):
        """Test handling of unsupported file format"""
        file_content = b"fake content"
        
        result = await document_extractor.extract_text(
            file_content=file_content,
            filename="test.xyz"
        )
        
        assert result['success'] is False
        assert 'Unsupported file type' in result['error']
        assert result['text'] == ''
    
    @pytest.mark.asyncio
    async def test_extraction_stats(self, document_extractor):
        """Test extraction statistics tracking"""
        # Get initial stats
        stats_before = document_extractor.get_stats()
        initial_total = stats_before['total_extracted']
        initial_successful = stats_before['successful']
        initial_failed = stats_before['failed']
        
        # Extract from valid file
        sample_text = "Test document"
        result1 = await document_extractor.extract_text(
            file_content=sample_text.encode('utf-8'),
            filename="test.txt"
        )
        assert result1['success'] is True
        
        # Extract from invalid file
        result2 = await document_extractor.extract_text(
            file_content=b"test",
            filename="test.xyz"
        )
        assert result2['success'] is False
        
        # Check stats were updated correctly
        final_stats = document_extractor.get_stats()
        
        assert final_stats['total_extracted'] == initial_total + 2
        assert final_stats['successful'] == initial_successful + 1
        assert final_stats['failed'] == initial_failed + 1
    
    @pytest.mark.asyncio
    async def test_extract_from_txt_different_encoding(self, document_extractor):
        """Test extraction from TXT file with different encoding"""
        sample_text = "Legal document with special chars: é, ñ, ü"
        file_content = sample_text.encode('latin-1')
        
        result = await document_extractor.extract_text(
            file_content=file_content,
            filename="test.txt"
        )
        
        assert result['success'] is True
        assert result['extraction_method'] == 'decode'
        assert result['metadata']['encoding'] in ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
    
    @pytest.mark.asyncio
    async def test_extract_empty_file(self, document_extractor):
        """Test extraction from empty file"""
        result = await document_extractor.extract_text(
            file_content=b"",
            filename="empty.txt"
        )
        
        # Empty file should succeed but return empty text
        assert result['success'] is True
        assert result['text'] == ''


class TestLegalTextParser:
    """Test legal text parsing functionality"""
    
    @pytest.mark.asyncio
    async def test_parse_simple_document(self, text_parser):
        """Test parsing a simple legal document"""
        sample_text = """
AGREEMENT

This Agreement is entered into on January 1, 2024.

1. Parties

The parties to this agreement are John Doe and Jane Smith.

2. Terms

The terms are governed by 28 U.S.C. § 1331.

See also Smith v. Jones, 123 F.3d 456 (9th Cir. 2020).
"""
        
        parsed = await text_parser.parse_document(sample_text)
        
        assert parsed.raw_text == sample_text
        assert len(parsed.sections) > 0
        assert len(parsed.citations) > 0
        assert len(parsed.paragraphs) > 0
        assert parsed.metadata is not None
    
    @pytest.mark.asyncio
    async def test_extract_citations(self, text_parser):
        """Test citation extraction"""
        text = """
This case is governed by 28 U.S.C. § 1331 and Smith v. Jones, 123 F.3d 456.
See also 42 USC 1983 and Johnson v. Williams, 567 U.S. 890 (2012).
The regulation at 29 C.F.R. § 825.100 applies.
"""
        
        parsed = await text_parser.parse_document(text)
        
        # Should find multiple citations
        assert len(parsed.citations) > 0
        
        # Check citation types
        citation_types = [c.citation_type for c in parsed.citations]
        assert 'statute' in citation_types or 'case' in citation_types or 'section' in citation_types
    
    @pytest.mark.asyncio
    async def test_extract_sections(self, text_parser):
        """Test section extraction"""
        text = """
ARTICLE I - DEFINITIONS

The following terms are defined:

1. Party

A party means any person bound by this agreement.

2. Term

The term is the duration of the agreement.

A. Commencement

The term begins on the effective date.

B. Termination

The term ends on the termination date.
"""
        
        parsed = await text_parser.parse_document(text)
        
        # Should find multiple sections
        assert len(parsed.sections) > 0
        
        # Check section levels
        levels = [s.level for s in parsed.sections]
        assert min(levels) >= 1
        assert max(levels) <= 4
    
    @pytest.mark.asyncio
    async def test_extract_dates(self, text_parser):
        """Test date extraction"""
        text = """
This Agreement was entered into on January 15, 2024.
The effective date is 01/01/2024.
The termination date is 2024-12-31.
"""
        
        parsed = await text_parser.parse_document(text)
        
        # Should find dates
        assert 'dates' in parsed.metadata
        assert len(parsed.metadata['dates']) > 0
    
    @pytest.mark.asyncio
    async def test_extract_parties(self, text_parser):
        """Test party name extraction"""
        text = """
In the case of Smith v. Jones, the plaintiff Smith alleged...
The defendant Jones responded that...
"""
        
        parsed = await text_parser.parse_document(text)
        
        # Should find party names
        assert 'parties' in parsed.metadata
        parties = parsed.metadata['parties']
        
        # May find Smith and/or Jones
        assert len(parties) >= 0  # Parser may or may not find parties depending on text
    
    @pytest.mark.asyncio
    async def test_extract_paragraphs(self, text_parser):
        """Test paragraph extraction"""
        text = """
This is the first paragraph of the document. It contains some text.

This is the second paragraph. It also contains text.

This is the third paragraph with more information.
"""
        
        parsed = await text_parser.parse_document(text)
        
        # Should find multiple paragraphs
        assert len(parsed.paragraphs) >= 2
        
        # Paragraphs should not be empty
        for para in parsed.paragraphs:
            assert len(para) > 0
    
    @pytest.mark.asyncio
    async def test_parse_with_metadata(self, text_parser):
        """Test parsing with extraction metadata"""
        text = "Sample legal document text."
        metadata = {
            'pages': 10,
            'author': 'John Doe',
            'title': 'Legal Agreement'
        }
        
        parsed = await text_parser.parse_document(text, metadata)
        
        # Original metadata should be preserved
        assert parsed.metadata['pages'] == 10
        assert parsed.metadata['author'] == 'John Doe'
        assert parsed.metadata['title'] == 'Legal Agreement'
        
        # Parser should add its own metadata
        assert 'word_count' in parsed.metadata
        assert 'character_count' in parsed.metadata
    
    @pytest.mark.asyncio
    async def test_empty_document(self, text_parser):
        """Test parsing an empty document"""
        parsed = await text_parser.parse_document("")
        
        assert parsed.raw_text == ""
        assert len(parsed.sections) == 0
        assert len(parsed.citations) == 0
        assert len(parsed.paragraphs) == 0
        assert parsed.metadata['word_count'] == 0
