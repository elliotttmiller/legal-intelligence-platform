"""Pydantic models for Legal Guard Professional API"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum


class DocumentType(str, Enum):
    """Legal document types"""
    CONTRACT = "contract"
    BRIEF = "brief"
    MOTION = "motion"
    PLEADING = "pleading"
    MEMORANDUM = "memorandum"
    OPINION = "opinion"
    STATUTE = "statute"
    REGULATION = "regulation"


class ConfidenceLevel(str, Enum):
    """Confidence levels for AI analysis"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class DocumentInterpretationRequest(BaseModel):
    """Request model for document interpretation"""
    document_id: str
    document_type: DocumentType
    preserve_legal_nuance: bool = True
    include_authority_mapping: bool = True
    include_precedent_analysis: bool = True


class LegalClause(BaseModel):
    """Represents a legal clause with interpretation"""
    clause_id: str
    text: str
    interpretation: str
    legal_significance: str
    potential_issues: List[str] = []
    related_authorities: List[str] = []
    confidence: ConfidenceLevel


class AuthorityReference(BaseModel):
    """Legal authority reference"""
    citation: str
    authority_type: str  # case_law, statute, regulation, constitutional
    jurisdiction: str
    relevance_score: float
    summary: str
    hierarchy_level: int  # Supreme Court = 1, Circuit = 2, District = 3, etc.


class DocumentInterpretation(BaseModel):
    """Complete document interpretation result"""
    document_id: str
    document_type: DocumentType
    executive_summary: str
    key_legal_issues: List[str]
    clauses: List[LegalClause]
    authorities: List[AuthorityReference]
    legal_framework: str
    argument_structure: Optional[Dict[str, Any]] = None
    overall_confidence: ConfidenceLevel
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class BatchProcessingRequest(BaseModel):
    """Request for batch document processing"""
    document_ids: List[str]
    analysis_type: str  # comparison, cross_reference, consolidation
    preserve_relationships: bool = True


class DocumentComparison(BaseModel):
    """Document comparison result"""
    document_a_id: str
    document_b_id: str
    differences: List[Dict[str, Any]]
    similarities: List[Dict[str, Any]]
    legal_implications: List[str]
    recommendation: str


class LegalSyllogism(BaseModel):
    """Legal syllogism structure"""
    major_premise: str  # Legal rule/principle
    minor_premise: str  # Factual application
    conclusion: str
    supporting_authorities: List[AuthorityReference]
    strength_assessment: ConfidenceLevel


class ArgumentAnalysis(BaseModel):
    """Legal argument analysis"""
    argument_id: str
    syllogisms: List[LegalSyllogism]
    strengths: List[str]
    weaknesses: List[str]
    counter_arguments: List[str]
    overall_strength: ConfidenceLevel
    improvement_suggestions: List[str]


class PrecedentAnalysis(BaseModel):
    """Precedent analysis result"""
    case_citation: str
    jurisdiction: str
    holding: str
    key_facts: List[str]
    legal_principles: List[str]
    distinguishing_factors: List[str]
    applicability_score: float
    binding_authority: bool


class CourtAdmissibleReport(BaseModel):
    """Court-admissible report structure"""
    report_id: str
    case_title: str
    jurisdiction: str
    report_type: str
    content: str
    citations: List[str]
    evidence_chain: List[str]
    certification_statement: str
    generated_timestamp: datetime = Field(default_factory=datetime.utcnow)
    court_specific_formatting: Dict[str, Any]


class WorkflowMetrics(BaseModel):
    """Lawyer workflow optimization metrics"""
    task_type: str
    manual_time_estimate: float  # hours
    automated_time: float  # hours
    time_savings_percentage: float
    accuracy_improvement: Optional[float] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
