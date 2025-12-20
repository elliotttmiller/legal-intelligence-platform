import { Link } from 'react-router-dom'
import { ArrowLeft, TrendingUp, Clock, Target, Upload, FileText } from 'lucide-react'
import './WorkflowOptimizer.css'

/**
 * Workflow Optimizer - Personalized workflow optimization
 */
function WorkflowOptimizer() {
  return (
    <div className="workflow-container">
      <header className="workflow-header">
        <Link to="/" className="back-link">
          <ArrowLeft size={24} />
          Back to Dashboard
        </Link>
        <h1>Workflow Optimizer</h1>
        <p>Personalized workflow optimization and efficiency tracking</p>
      </header>

      <main className="workflow-main">
        {/* Optimization Metrics */}
        <div className="metrics-overview">
          <div className="metric-card">
            <div className="metric-icon">
              <Clock size={48} color="var(--accent-primary)" />
            </div>
            <div className="metric-value">437.5 hrs</div>
            <div className="metric-label">Time Saved This Month</div>
          </div>
          
          <div className="metric-card">
            <div className="metric-icon">
              <Target size={48} color="var(--accent-primary)" />
            </div>
            <div className="metric-value">85%</div>
            <div className="metric-label">Workflow Efficiency</div>
          </div>
          
          <div className="metric-card">
            <div className="metric-icon">
              <TrendingUp size={48} color="var(--success)" />
            </div>
            <div className="metric-value">+23%</div>
            <div className="metric-label">Productivity Increase</div>
          </div>
        </div>

        {/* Batch Processing */}
        <div className="workflow-card batch-processing-section">
          <h2>Batch Document Processing</h2>
          <p>
            Process multiple related documents simultaneously with cross-reference analysis.
            Optimized for contract negotiations, case file review, and multi-document research.
          </p>
          
          <div className="file-upload-area">
            <Upload size={48} />
            <p>Click to upload documents or drag and drop</p>
            <p style={{ fontSize: '0.875rem', marginTop: '0.5rem', color: 'var(--text-tertiary)' }}>
              Supports PDF, DOC, DOCX • Max 20 files at once
            </p>
          </div>

          <div className="stats-grid">
            <div className="stat-item">
              <div className="stat-value">156</div>
              <div className="stat-label">Batches Processed</div>
            </div>
            <div className="stat-item">
              <div className="stat-value">2,847</div>
              <div className="stat-label">Total Documents</div>
            </div>
            <div className="stat-item">
              <div className="stat-value">92%</div>
              <div className="stat-label">Accuracy Rate</div>
            </div>
          </div>
        </div>

        {/* Document Comparison */}
        <div className="workflow-card comparison-section">
          <h2>Document Comparison Tool</h2>
          <p>
            Advanced document comparison with detailed redlining and legal analysis of changes.
            Perfect for contract negotiation workflows.
          </p>
          
          <div className="button-grid">
            <button className="workflow-button secondary">
              <Upload size={18} style={{ display: 'inline', marginRight: '0.5rem', verticalAlign: 'middle' }} />
              Upload Original Document
            </button>
            <button className="workflow-button secondary">
              <Upload size={18} style={{ display: 'inline', marginRight: '0.5rem', verticalAlign: 'middle' }} />
              Upload Modified Document
            </button>
          </div>

          <div className="stats-grid" style={{ marginTop: '1.5rem' }}>
            <div className="stat-item">
              <div className="stat-value">89</div>
              <div className="stat-label">Comparisons Run</div>
            </div>
            <div className="stat-item">
              <div className="stat-value">1,234</div>
              <div className="stat-label">Changes Detected</div>
            </div>
            <div className="stat-item">
              <div className="stat-value">65%</div>
              <div className="stat-label">Time Saved</div>
            </div>
          </div>
        </div>

        {/* Optimization Insights */}
        <div className="insights-card">
          <h2>Workflow Optimization Insights</h2>
          
          <div className="insight-item success">
            <strong>Most Efficient Task</strong>
            <p>Document interpretation - 70% time reduction compared to manual review</p>
          </div>
          
          <div className="insight-item warning">
            <strong>Optimization Opportunity</strong>
            <p>Consider batch processing related contracts to save additional 15% time</p>
          </div>
          
          <div className="insight-item info">
            <strong>Recommendation</strong>
            <p>Enable automated citation validation to improve accuracy by 25%</p>
          </div>

          <div className="insight-item success">
            <strong>Recent Achievement</strong>
            <p>Processed 45 documents this week - 3x faster than average</p>
          </div>
        </div>
      </main>
    </div>
  )
}

export default WorkflowOptimizer
