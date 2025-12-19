import { Link } from 'react-router-dom'
import { FileText, Scale, BookOpen, Briefcase, TrendingUp } from 'lucide-react'
import './ProfessionalDashboard.css'

/**
 * Professional Dashboard - Main lawyer workflow interface
 * 
 * Focused on workflow efficiency metrics and quick access to professional tools
 */
function ProfessionalDashboard() {
  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <div className="header-content">
          <h1>Legal Guard Professional</h1>
          <p className="tagline">Lawyer Workflow Optimization Platform</p>
        </div>
      </header>

      <main className="dashboard-main">
        {/* Workflow Metrics Overview */}
        <section className="metrics-section">
          <h2>Workflow Efficiency Metrics</h2>
          <div className="metrics-grid">
            <div className="metric-card">
              <div className="metric-value">35%</div>
              <div className="metric-label">Average Time Savings</div>
            </div>
            <div className="metric-card">
              <div className="metric-value">1,250</div>
              <div className="metric-label">Documents Processed</div>
            </div>
            <div className="metric-card">
              <div className="metric-value">437.5 hrs</div>
              <div className="metric-label">Total Hours Saved</div>
            </div>
            <div className="metric-card">
              <div className="metric-value">18%</div>
              <div className="metric-label">Accuracy Improvement</div>
            </div>
          </div>
        </section>

        {/* Professional Tools */}
        <section className="tools-section">
          <h2>Professional Legal Tools</h2>
          <div className="tools-grid">
            <Link to="/interpret" className="tool-card">
              <FileText size={48} />
              <h3>Document Interpreter</h3>
              <p>Deep legal document interpretation maintaining precise terminology and nuance</p>
            </Link>

            <Link to="/research" className="tool-card">
              <BookOpen size={48} />
              <h3>Precedent Research</h3>
              <p>Case law and authority research with applicability analysis</p>
            </Link>

            <Link to="/brief-builder" className="tool-card">
              <Scale size={48} />
              <h3>Brief Builder</h3>
              <p>Legal brief construction with argument strength analysis</p>
            </Link>

            <Link to="/workflow" className="tool-card">
              <TrendingUp size={48} />
              <h3>Workflow Optimizer</h3>
              <p>Personalized workflow optimization and batch processing</p>
            </Link>
          </div>
        </section>

        {/* Quick Actions */}
        <section className="actions-section">
          <h2>Quick Actions</h2>
          <div className="actions-grid">
            <button className="action-button">
              <Briefcase size={24} />
              Upload Document
            </button>
            <button className="action-button">
              <FileText size={24} />
              Compare Documents
            </button>
            <button className="action-button">
              <Scale size={24} />
              Generate Court Report
            </button>
            <button className="action-button">
              <BookOpen size={24} />
              Validate Citations
            </button>
          </div>
        </section>
      </main>
    </div>
  )
}

export default ProfessionalDashboard
