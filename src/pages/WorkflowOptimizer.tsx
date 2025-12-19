import { Link } from 'react-router-dom'
import { ArrowLeft, TrendingUp, Clock, Target } from 'lucide-react'

/**
 * Workflow Optimizer - Personalized workflow optimization
 */
function WorkflowOptimizer() {
  return (
    <div style={{ minHeight: '100vh', background: '#f9fafb' }}>
      <header style={{
        background: 'linear-gradient(135deg, #2563eb 0%, #1e40af 100%)',
        color: 'white',
        padding: '2rem',
        boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)'
      }}>
        <Link to="/" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', color: 'white', textDecoration: 'none', marginBottom: '1rem' }}>
          <ArrowLeft size={24} />
          Back to Dashboard
        </Link>
        <h1 style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>Workflow Optimizer</h1>
        <p style={{ opacity: 0.9 }}>Personalized workflow optimization and efficiency tracking</p>
      </header>

      <main style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem' }}>
        {/* Optimization Metrics */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1.5rem', marginBottom: '2rem' }}>
          <div style={{ background: 'white', padding: '2rem', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)', textAlign: 'center' }}>
            <Clock size={48} style={{ color: '#2563eb', margin: '0 auto 1rem' }} />
            <div style={{ fontSize: '2rem', fontWeight: 700, color: '#2563eb' }}>437.5 hrs</div>
            <div style={{ color: '#6b7280', marginTop: '0.5rem' }}>Time Saved This Month</div>
          </div>
          
          <div style={{ background: 'white', padding: '2rem', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)', textAlign: 'center' }}>
            <Target size={48} style={{ color: '#2563eb', margin: '0 auto 1rem' }} />
            <div style={{ fontSize: '2rem', fontWeight: 700, color: '#2563eb' }}>85%</div>
            <div style={{ color: '#6b7280', marginTop: '0.5rem' }}>Workflow Efficiency</div>
          </div>
          
          <div style={{ background: 'white', padding: '2rem', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)', textAlign: 'center' }}>
            <TrendingUp size={48} style={{ color: '#16a34a', margin: '0 auto 1rem' }} />
            <div style={{ fontSize: '2rem', fontWeight: 700, color: '#16a34a' }}>+23%</div>
            <div style={{ color: '#6b7280', marginTop: '0.5rem' }}>Productivity Increase</div>
          </div>
        </div>

        {/* Batch Processing */}
        <div style={{ background: 'white', padding: '2rem', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)', marginBottom: '2rem' }}>
          <h2 style={{ marginBottom: '1.5rem' }}>Batch Document Processing</h2>
          <p style={{ color: '#6b7280', marginBottom: '1.5rem' }}>
            Process multiple related documents simultaneously with cross-reference analysis.
            Optimized for contract negotiations, case file review, and multi-document research.
          </p>
          
          <button style={{
            padding: '1rem 2rem',
            background: '#2563eb',
            color: 'white',
            border: 'none',
            borderRadius: '6px',
            fontSize: '1rem',
            fontWeight: 600,
            cursor: 'pointer'
          }}>
            Upload Document Set
          </button>
        </div>

        {/* Document Comparison */}
        <div style={{ background: 'white', padding: '2rem', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)', marginBottom: '2rem' }}>
          <h2 style={{ marginBottom: '1.5rem' }}>Document Comparison Tool</h2>
          <p style={{ color: '#6b7280', marginBottom: '1.5rem' }}>
            Advanced document comparison with detailed redlining and legal analysis of changes.
            Perfect for contract negotiation workflows.
          </p>
          
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
            <button style={{
              padding: '1rem',
              background: '#f0f9ff',
              color: '#2563eb',
              border: '2px solid #2563eb',
              borderRadius: '6px',
              cursor: 'pointer'
            }}>
              Upload Original Document
            </button>
            <button style={{
              padding: '1rem',
              background: '#f0f9ff',
              color: '#2563eb',
              border: '2px solid #2563eb',
              borderRadius: '6px',
              cursor: 'pointer'
            }}>
              Upload Modified Document
            </button>
          </div>
        </div>

        {/* Optimization Insights */}
        <div style={{ background: 'white', padding: '2rem', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)' }}>
          <h2 style={{ marginBottom: '1.5rem' }}>Workflow Optimization Insights</h2>
          
          <div style={{ padding: '1rem', background: '#f0fdf4', borderLeft: '4px solid #16a34a', borderRadius: '4px', marginBottom: '1rem' }}>
            <strong style={{ color: '#16a34a' }}>Most Efficient Task:</strong>
            <p style={{ marginTop: '0.5rem' }}>Document interpretation - 70% time reduction compared to manual review</p>
          </div>
          
          <div style={{ padding: '1rem', background: '#fef3c7', borderLeft: '4px solid #d97706', borderRadius: '4px', marginBottom: '1rem' }}>
            <strong style={{ color: '#d97706' }}>Optimization Opportunity:</strong>
            <p style={{ marginTop: '0.5rem' }}>Consider batch processing related contracts to save additional 15% time</p>
          </div>
          
          <div style={{ padding: '1rem', background: '#f0f9ff', borderLeft: '4px solid #2563eb', borderRadius: '4px' }}>
            <strong style={{ color: '#2563eb' }}>Recommendation:</strong>
            <p style={{ marginTop: '0.5rem' }}>Enable automated citation validation to improve accuracy by 25%</p>
          </div>
        </div>
      </main>
    </div>
  )
}

export default WorkflowOptimizer
