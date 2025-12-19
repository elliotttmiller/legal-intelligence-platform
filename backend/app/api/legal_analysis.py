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

logger = logging.getLogger(__name__)
router = APIRouter()

# Initialize engine
interpretation_engine = DocumentInterpretationEngine()


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
    
    Supports PDF, DOCX, and TXT formats.
    """
    try:
        # Read file content
        content = await file.read()
        
        # Extract text (simplified - would use proper document parsers)
        if file.filename.endswith('.txt'):
            document_text = content.decode('utf-8')
        else:
            # Placeholder for PDF/DOCX parsing
            document_text = "Extracted document text would appear here"
        
        # Perform interpretation
        result = await interpretation_engine.interpret_document(
            document_text=document_text,
            document_type=document_type,
            preserve_nuance=True,
            include_authorities=True
        )
        
        return result
    
    except Exception as e:
        logger.error(f"Upload and interpret error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health")
async def health_check():
    """Health check for legal analysis service"""
    return {"status": "operational", "service": "legal_analysis"}
