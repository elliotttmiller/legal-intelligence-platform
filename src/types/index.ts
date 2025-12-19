/**
 * TypeScript types for Legal Guard Professional
 */

export enum DocumentType {
  CONTRACT = 'contract',
  BRIEF = 'brief',
  MOTION = 'motion',
  PLEADING = 'pleading',
  MEMORANDUM = 'memorandum',
  OPINION = 'opinion',
  STATUTE = 'statute',
  REGULATION = 'regulation',
}

export enum ConfidenceLevel {
  HIGH = 'high',
  MEDIUM = 'medium',
  LOW = 'low',
}

export interface LegalClause {
  clause_id: string
  text: string
  interpretation: string
  legal_significance: string
  potential_issues: string[]
  related_authorities: string[]
  confidence: ConfidenceLevel
}

export interface AuthorityReference {
  citation: string
  authority_type: string
  jurisdiction: string
  relevance_score: number
  summary: string
  hierarchy_level: number
}

export interface DocumentInterpretation {
  document_id: string
  document_type: DocumentType
  executive_summary: string
  key_legal_issues: string[]
  clauses: LegalClause[]
  authorities: AuthorityReference[]
  legal_framework: string
  argument_structure?: Record<string, any>
  overall_confidence: ConfidenceLevel
  timestamp: string
}

export interface DocumentComparison {
  doc_a_id: string
  doc_b_id: string
  differences: Array<Record<string, any>>
  similarities: Array<Record<string, any>>
  legal_implications: string[]
  recommendation: string
  change_count?: number
  similarity_score?: number
}

export interface LegalSyllogism {
  major_premise: string
  minor_premise: string
  conclusion: string
  supporting_authorities: AuthorityReference[]
  strength_assessment: ConfidenceLevel
}

export interface ArgumentAnalysis {
  argument_id: string
  syllogisms: LegalSyllogism[]
  strengths: string[]
  weaknesses: string[]
  counter_arguments: string[]
  overall_strength: ConfidenceLevel
  improvement_suggestions: string[]
}

export interface PrecedentAnalysis {
  case_citation: string
  jurisdiction: string
  holding: string
  key_facts: string[]
  legal_principles: string[]
  distinguishing_factors: string[]
  applicability_score: number
  binding_authority: boolean
}

export interface CourtAdmissibleReport {
  report_id: string
  case_title: string
  jurisdiction: string
  report_type: string
  content: string
  citations: string[]
  evidence_chain: string[]
  certification_statement: string
  generated_timestamp: string
  court_specific_formatting: Record<string, any>
}

export interface WorkflowMetrics {
  task_type: string
  manual_time_estimate: number
  automated_time: number
  time_savings_percentage: number
  accuracy_improvement?: number
  timestamp: string
}
