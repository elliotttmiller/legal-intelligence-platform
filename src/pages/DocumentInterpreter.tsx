import { useState } from 'react'
import { Link } from 'react-router-dom'
import { ArrowLeft, Upload, FileText, AlertCircle, CheckCircle } from 'lucide-react'
import { legalDocumentService } from '@/services/legalDocumentService'
import { DocumentType, DocumentInterpretation } from '@/types'
import './DocumentInterpreter.css'

/**
 * Document Interpreter - Deep legal document interpretation
 * 
 * Maintains legal precision and nuance for professional analysis
 */
function DocumentInterpreter() {
  const [file, setFile] = useState<File | null>(null)
  const [documentType, setDocumentType] = useState<DocumentType>(DocumentType.CONTRACT)
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const [result, setResult] = useState<DocumentInterpretation | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0])
      setError(null)
    }
  }

  const handleAnalyze = async () => {
    if (!file) {
      setError('Please select a document to analyze')
      return
    }

    setIsAnalyzing(true)
    setError(null)

    try {
      const interpretation = await legalDocumentService.uploadAndInterpret(file, documentType)
      setResult(interpretation)
    } catch (err) {
      setError('Failed to analyze document. Please try again.')
      console.error(err)
    } finally {
      setIsAnalyzing(false)
    }
  }

  return (
    <div className="interpreter-container">
      <header className="interpreter-header">
        <Link to="/" className="back-link">
          <ArrowLeft size={24} />
          Back to Dashboard
        </Link>
        <h1>Document Interpreter</h1>
        <p>Deep legal document interpretation maintaining precise terminology</p>
      </header>

      <main className="interpreter-main">
        {/* Upload Section */}
        <section className="upload-section">
          <div className="upload-card">
            <h2>Upload Legal Document</h2>
            
            <div className="file-input-wrapper">
              <input
                type="file"
                id="document-upload"
                accept=".pdf,.doc,.docx,.txt"
                onChange={handleFileChange}
                className="file-input"
              />
              <label htmlFor="document-upload" className="file-label">
                <Upload size={32} />
                <span>{file ? file.name : 'Choose file or drag here'}</span>
                <span className="file-hint">Supports PDF, DOC, DOCX, TXT</span>
              </label>
            </div>

            <div className="document-type-selector">
              <label htmlFor="doc-type">Document Type:</label>
              <select
                id="doc-type"
                value={documentType}
                onChange={(e) => setDocumentType(e.target.value as DocumentType)}
                className="select-input"
              >
                {Object.values(DocumentType).map((type) => (
                  <option key={type} value={type}>
                    {type.charAt(0).toUpperCase() + type.slice(1)}
                  </option>
                ))}
              </select>
            </div>

            <button
              onClick={handleAnalyze}
              disabled={!file || isAnalyzing}
              className="analyze-button"
            >
              {isAnalyzing ? 'Analyzing...' : 'Analyze Document'}
            </button>

            {error && (
              <div className="error-message">
                <AlertCircle size={20} />
                {error}
              </div>
            )}
          </div>
        </section>

        {/* Results Section */}
        {result && (
          <section className="results-section">
            <div className="results-header">
              <CheckCircle size={32} color="#16a34a" />
              <h2>Analysis Complete</h2>
            </div>

            <div className="result-card">
              <h3>Executive Summary</h3>
              <p>{result.executive_summary}</p>
            </div>

            <div className="result-card">
              <h3>Legal Framework</h3>
              <p>{result.legal_framework}</p>
            </div>

            <div className="result-card">
              <h3>Key Legal Issues</h3>
              <ul className="issues-list">
                {result.key_legal_issues.map((issue, index) => (
                  <li key={index}>{issue}</li>
                ))}
              </ul>
            </div>

            <div className="result-card">
              <h3>Legal Clauses Analysis</h3>
              {result.clauses.map((clause) => (
                <div key={clause.clause_id} className="clause-item">
                  <h4>{clause.clause_id}</h4>
                  <p className="clause-text">{clause.text}</p>
                  <p className="interpretation"><strong>Interpretation:</strong> {clause.interpretation}</p>
                  <p className="significance"><strong>Legal Significance:</strong> {clause.legal_significance}</p>
                  {clause.potential_issues.length > 0 && (
                    <div className="issues">
                      <strong>Potential Issues:</strong>
                      <ul>
                        {clause.potential_issues.map((issue, idx) => (
                          <li key={idx}>{issue}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                  <div className={`confidence-badge confidence-${clause.confidence}`}>
                    Confidence: {clause.confidence.toUpperCase()}
                  </div>
                </div>
              ))}
            </div>

            <div className="result-card">
              <h3>Authorities Referenced</h3>
              {result.authorities.map((auth, index) => (
                <div key={index} className="authority-item">
                  <div className="citation">{auth.citation}</div>
                  <div className="authority-details">
                    <span className="authority-type">{auth.authority_type}</span>
                    <span className="jurisdiction">{auth.jurisdiction}</span>
                    <span className="relevance">Relevance: {(auth.relevance_score * 100).toFixed(0)}%</span>
                  </div>
                  <p className="authority-summary">{auth.summary}</p>
                </div>
              ))}
            </div>
          </section>
        )}
      </main>
    </div>
  )
}

export default DocumentInterpreter
