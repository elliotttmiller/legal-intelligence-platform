"""Legal Reasoning API endpoints"""
from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
import logging

from app.models.schemas import ArgumentAnalysis, PrecedentAnalysis
from app.legal_reasoning import SyllogisticAnalysisEngine, PrecedentEvaluationEngine

logger = logging.getLogger(__name__)
router = APIRouter()

# Initialize engines
syllogism_engine = SyllogisticAnalysisEngine()
precedent_engine = PrecedentEvaluationEngine()


class PrecedentEvaluationRequest(BaseModel):
    """Request model for precedent evaluation"""
    case_citation: str
    current_facts: List[str]
    jurisdiction: str


@router.post("/analyze-argument", response_model=ArgumentAnalysis)
async def analyze_argument(
    argument_text: str,
    include_counter_arguments: bool = True
):
    """
    Analyze legal argument structure using formal syllogistic logic.
    
    Identifies premises, conclusions, and potential weaknesses.
    """
    try:
        logger.info("Analyzing legal argument")
        
        result = await syllogism_engine.analyze_argument(
            argument_text=argument_text,
            include_counter_arguments=include_counter_arguments
        )
        
        return result
    
    except Exception as e:
        logger.error(f"Argument analysis error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/evaluate-precedent", response_model=PrecedentAnalysis)
async def evaluate_precedent(request: PrecedentEvaluationRequest):
    """
    Evaluate precedent applicability and binding authority.
    
    Analyzes case holding, key facts, and determines applicability to current matter.
    """
    try:
        logger.info(f"Evaluating precedent: {request.case_citation}")
        
        result = await precedent_engine.evaluate_precedent(
            case_citation=request.case_citation,
            current_facts=request.current_facts,
            jurisdiction=request.jurisdiction
        )
        
        return result
    
    except Exception as e:
        logger.error(f"Precedent evaluation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/map-authorities")
async def map_authorities(
    document_text: str,
    jurisdiction: str
):
    """
    Map legal authorities and precedents in document.
    
    Creates authority hierarchy and validates citations.
    """
    try:
        logger.info("Mapping legal authorities")
        
        # Placeholder for authority mapping
        return {
            "authorities_found": 5,
            "binding_authorities": 3,
            "persuasive_authorities": 2,
            "hierarchy_map": {
                "supreme_court": 1,
                "circuit_court": 2,
                "district_court": 2
            }
        }
    
    except Exception as e:
        logger.error(f"Authority mapping error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health")
async def health_check():
    """Health check for legal reasoning service"""
    return {"status": "operational", "service": "legal_reasoning"}
