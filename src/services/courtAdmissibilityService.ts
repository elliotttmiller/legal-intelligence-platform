/**
 * Court admissibility service
 */
import axios from 'axios'
import { CourtAdmissibleReport } from '@/types'

const API_BASE = '/api/court'

export const courtAdmissibilityService = {
  /**
   * Generate court-admissible report
   */
  async generateReport(
    analysisData: Record<string, any>,
    caseTitle: string,
    jurisdiction: string,
    reportType: string = 'analysis'
  ): Promise<CourtAdmissibleReport> {
    const response = await axios.post(`${API_BASE}/generate-report`, {
      analysis_data: analysisData,
      case_title: caseTitle,
      jurisdiction: jurisdiction,
      report_type: reportType,
    })
    return response.data
  },

  /**
   * Validate legal citation
   */
  async validateCitation(
    citation: string,
    formatStyle: string = 'bluebook'
  ): Promise<any> {
    const response = await axios.post(`${API_BASE}/validate-citation`, {
      citation: citation,
      format_style: formatStyle,
    })
    return response.data
  },

  /**
   * Format citation
   */
  async formatCitation(
    citationParts: Record<string, string>,
    citationType: string,
    formatStyle: string = 'bluebook'
  ): Promise<{ formatted_citation: string }> {
    const response = await axios.post(`${API_BASE}/format-citation`, {
      citation_parts: citationParts,
      citation_type: citationType,
      format_style: formatStyle,
    })
    return response.data
  },

  /**
   * Get court-specific requirements
   */
  async getCourtRequirements(jurisdiction: string): Promise<any> {
    const response = await axios.get(`${API_BASE}/court-requirements/${jurisdiction}`)
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
