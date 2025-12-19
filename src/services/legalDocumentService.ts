/**
 * Legal document analysis service
 */
import axios from 'axios'
import {
  DocumentInterpretation,
  DocumentType,
} from '@/types'

const API_BASE = '/api/legal-analysis'

export const legalDocumentService = {
  /**
   * Interpret a legal document with professional-grade analysis
   */
  async interpretDocument(
    documentText: string,
    documentType: DocumentType,
    preserveNuance: boolean = true,
    includeAuthorities: boolean = true
  ): Promise<DocumentInterpretation> {
    const response = await axios.post(`${API_BASE}/interpret`, {
      document_text: documentText,
      document_type: documentType,
      preserve_nuance: preserveNuance,
      include_authorities: includeAuthorities,
    })
    return response.data
  },

  /**
   * Upload and interpret a document file
   */
  async uploadAndInterpret(
    file: File,
    documentType: DocumentType
  ): Promise<DocumentInterpretation> {
    const formData = new FormData()
    formData.append('file', file)
    formData.append('document_type', documentType)

    const response = await axios.post(`${API_BASE}/upload-interpret`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
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
