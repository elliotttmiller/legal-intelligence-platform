/**
 * Legal reasoning service
 */
import axios from 'axios'
import { ArgumentAnalysis, PrecedentAnalysis } from '@/types'

const API_BASE = '/api/reasoning'

export const legalReasoningService = {
  /**
   * Analyze legal argument structure
   */
  async analyzeArgument(
    argumentText: string,
    includeCounterArguments: boolean = true
  ): Promise<ArgumentAnalysis> {
    const response = await axios.post(`${API_BASE}/analyze-argument`, {
      argument_text: argumentText,
      include_counter_arguments: includeCounterArguments,
    })
    return response.data
  },

  /**
   * Evaluate precedent applicability
   */
  async evaluatePrecedent(
    caseCitation: string,
    currentFacts: string[],
    jurisdiction: string
  ): Promise<PrecedentAnalysis> {
    const response = await axios.post(`${API_BASE}/evaluate-precedent`, {
      case_citation: caseCitation,
      current_facts: currentFacts,
      jurisdiction: jurisdiction,
    })
    return response.data
  },

  /**
   * Map legal authorities in document
   */
  async mapAuthorities(
    documentText: string,
    jurisdiction: string
  ): Promise<any> {
    const response = await axios.post(`${API_BASE}/map-authorities`, {
      document_text: documentText,
      jurisdiction: jurisdiction,
    })
    return response.data
  },

  /**
   * Health check
   */
  async healthCheck(): Promise<{ status: string; service: string }> {
    const response = await axios.get(`${API_BASE}/health`)
    return response.data
  },
}
