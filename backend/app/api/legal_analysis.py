"""Legal Analysis API endpoints"""
from fastapi import APIRouter, HTTPException, UploadFile, File
from typing import Optional
import logging

from app.models.schemas import (
    DocumentInterpretationRequest,
    DocumentInterpretation,
    DocumentType
)
from app.legal_analysis import DocumentInterpretationEngine
from app.document_processing import DocumentExtractor, LegalTextParser

logger = logging.getLogger(__name__)
router = APIRouter()

# Initialize engines
interpretation_engine = DocumentInterpretationEngine()
document_extractor = DocumentExtractor()
text_parser = LegalTextParser()


@router.post("/interpret", response_model=DocumentInterpretation)
async def interpret_document(
    document_text: str,
    document_type: DocumentType,
    preserve_nuance: bool = True,
    include_authorities: bool = True
):
    """
    Perform deep legal interpretation of document.
    
    Maintains legal precision and nuance for professional use.
    """
    try:
        logger.info(f"Document interpretation request: {document_type}")
        
        result = await interpretation_engine.interpret_document(
            document_text=document_text,
            document_type=document_type,
            preserve_nuance=preserve_nuance,
            include_authorities=include_authorities
        )
        
        return result
    
    except Exception as e:
        logger.error(f"Document interpretation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/upload-interpret")
async def upload_and_interpret(
    file: UploadFile = File(...),
    document_type: DocumentType = DocumentType.CONTRACT
):
    """
    Upload and interpret a legal document.
    
    Supports PDF, DOCX, and TXT formats using proven extraction libraries.
    """
    try:
        # Read file content
        content = await file.read()
        
        # Extract text using professional document extractor
        extraction_result = await document_extractor.extract_text(
            file_content=content,
            filename=file.filename,
            use_fallback=True
        )
        
        # Check if extraction was successful
        if not extraction_result['success']:
            raise HTTPException(
                status_code=400,
                detail=f"Failed to extract text: {extraction_result['error']}"
            )
        
        document_text = extraction_result['text']
        
        # Validate extracted text
        if not document_text or len(document_text.strip()) < 10:
            raise HTTPException(
                status_code=400,
                detail="Extracted text is empty or too short"
            )
        
        logger.info(f"Successfully extracted {len(document_text)} characters from {file.filename}")
        
        # Perform interpretation
        result = await interpretation_engine.interpret_document(
            document_text=document_text,
            document_type=document_type,
            preserve_nuance=True,
            include_authorities=True
        )
        
        # Add extraction metadata to result
        result.metadata = {
            'extraction_method': extraction_result['extraction_method'],
            'extraction_metadata': extraction_result['metadata']
        }
        
        return result
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Upload and interpret error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health")
async def health_check():
    """Health check for legal analysis service"""
    return {"status": "operational", "service": "legal_analysis"}


@router.post("/extract-and-parse")
async def extract_and_parse(
    file: UploadFile = File(...)
):
    """
    Extract text and parse into structured components.
    
    Returns structured document with sections, citations, and metadata.
    """
    try:
        # Read file content
        content = await file.read()
        
        # Extract text
        extraction_result = await document_extractor.extract_text(
            file_content=content,
            filename=file.filename,
            use_fallback=True
        )
        
        if not extraction_result['success']:
            raise HTTPException(
                status_code=400,
                detail=f"Failed to extract text: {extraction_result['error']}"
            )
        
        # Parse document structure
        parsed_doc = await text_parser.parse_document(
            text=extraction_result['text'],
            doc_metadata=extraction_result['metadata']
        )
        
        # Return structured data
        return {
            'success': True,
            'filename': file.filename,
            'extraction_method': extraction_result['extraction_method'],
            'text_length': len(parsed_doc.raw_text),
            'sections_count': len(parsed_doc.sections),
            'citations_count': len(parsed_doc.citations),
            'paragraphs_count': len(parsed_doc.paragraphs),
            'metadata': parsed_doc.metadata,
            'sections': [
                {
                    'section_number': s.section_number,
                    'title': s.title,
                    'level': s.level,
                    'content_preview': s.content[:200] if len(s.content) > 200 else s.content
                }
                for s in parsed_doc.sections
            ],
            'citations': [
                {
                    'text': c.text,
                    'type': c.citation_type,
                    'position': c.position
                }
                for c in parsed_doc.citations[:50]  # Limit to first 50
            ]
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Extract and parse error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/extractor-stats")
async def get_extractor_stats():
    """Get document extraction statistics"""
    return {
        'stats': document_extractor.get_stats(),
        'supported_formats': list(DocumentExtractor.SUPPORTED_EXTENSIONS)
    }
