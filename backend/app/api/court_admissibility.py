"""Court Admissibility API endpoints"""
from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from pydantic import BaseModel
import logging

from app.models.schemas import CourtAdmissibleReport
from app.court_admissibility import ReportCertificationEngine, CitationValidator

logger = logging.getLogger(__name__)
router = APIRouter()

# Initialize engines
certification_engine = ReportCertificationEngine()
citation_validator = CitationValidator()


class ReportGenerationRequest(BaseModel):
    """Request model for report generation"""
    analysis_data: Dict[str, Any]
    case_title: str
    jurisdiction: str
    report_type: str = "analysis"


@router.post("/generate-report", response_model=CourtAdmissibleReport)
async def generate_court_report(request: ReportGenerationRequest):
    """
    Generate court-admissible report with proper certification.
    
    Ensures report meets court admissibility standards.
    """
    try:
        logger.info(f"Generating court report for {request.case_title}")
        
        report = await certification_engine.generate_court_report(
            analysis_data=request.analysis_data,
            case_title=request.case_title,
            jurisdiction=request.jurisdiction,
            report_type=request.report_type
        )
        
        return report
    
    except Exception as e:
        logger.error(f"Report generation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/validate-citation")
async def validate_citation(
    citation: str,
    format_style: str = "bluebook"
):
    """
    Validate legal citation format.
    
    Checks citation against Bluebook or other standard formats.
    """
    try:
        logger.info(f"Validating citation: {citation}")
        
        result = citation_validator.validate_citation(
            citation=citation,
            format_style=format_style
        )
        
        return result
    
    except Exception as e:
        logger.error(f"Citation validation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


class CitationFormattingRequest(BaseModel):
    """Request model for citation formatting"""
    citation_parts: Dict[str, str]
    citation_type: str
    format_style: str = "bluebook"


@router.post("/format-citation")
async def format_citation(request: CitationFormattingRequest):
    """
    Format citation according to specified style.
    
    Supports Bluebook, ALWD, and court-specific formats.
    """
    try:
        logger.info(f"Formatting {request.citation_type} citation")
        
        formatted = citation_validator.format_citation(
            citation_parts=request.citation_parts,
            citation_type=request.citation_type,
            format_style=request.format_style
        )
        
        return {"formatted_citation": formatted}
    
    except Exception as e:
        logger.error(f"Citation formatting error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/court-requirements/{jurisdiction}")
async def get_court_requirements(jurisdiction: str):
    """
    Get court-specific formatting requirements.
    
    Returns formatting rules for specified jurisdiction.
    """
    # Placeholder for court requirements database
    return {
        "jurisdiction": jurisdiction,
        "font": "Times New Roman",
        "font_size": 12,
        "line_spacing": 2.0,
        "margins": "1 inch all sides",
        "citation_format": "Bluebook"
    }


@router.get("/health")
async def health_check():
    """Health check for court admissibility service"""
    return {"status": "operational", "service": "court_admissibility"}
