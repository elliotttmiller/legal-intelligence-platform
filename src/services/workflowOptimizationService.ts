/**
 * Professional workflow optimization service
 */
import axios from 'axios'
import { DocumentComparison, WorkflowMetrics } from '@/types'

const API_BASE = '/api/workflow'

export const workflowOptimizationService = {
  /**
   * Process multiple documents in batch
   */
  async batchProcessDocuments(
    documentIds: string[],
    analysisType: 'comparison' | 'cross_reference' | 'consolidation',
    preserveRelationships: boolean = true
  ): Promise<any> {
    const response = await axios.post(`${API_BASE}/batch-process`, {
      document_ids: documentIds,
      analysis_type: analysisType,
      preserve_relationships: preserveRelationships,
    })
    return response.data
  },

  /**
   * Compare two documents
   */
  async compareDocuments(
    docAText: string,
    docBText: string,
    docAId: string = 'doc_a',
    docBId: string = 'doc_b'
  ): Promise<DocumentComparison> {
    const response = await axios.post(`${API_BASE}/compare`, {
      doc_a_text: docAText,
      doc_b_text: docBText,
      doc_a_id: docAId,
      doc_b_id: docBId,
    })
    return response.data
  },

  /**
   * Get workflow metrics
   */
  async getMetrics(): Promise<any> {
    const response = await axios.get(`${API_BASE}/metrics`)
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
