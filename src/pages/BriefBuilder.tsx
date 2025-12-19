import { Link } from 'react-router-dom'
import { ArrowLeft, FileText } from 'lucide-react'

/**
 * Brief Builder - Legal brief construction assistant
 */
function BriefBuilder() {
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
        <h1 style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>Brief Builder</h1>
        <p style={{ opacity: 0.9 }}>Legal brief construction with argument strength analysis</p>
      </header>

      <main style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem' }}>
        <div style={{ background: 'white', padding: '2rem', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)' }}>
          <h2>Construct Legal Brief</h2>
          
          <div style={{ marginTop: '1.5rem' }}>
            <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 600 }}>Brief Type:</label>
            <select style={{
              width: '100%',
              padding: '0.75rem',
              border: '1px solid #d1d5db',
              borderRadius: '6px',
              fontSize: '1rem'
            }}>
              <option>Motion to Dismiss</option>
              <option>Summary Judgment Brief</option>
              <option>Appellate Brief</option>
              <option>Trial Brief</option>
              <option>Memorandum of Law</option>
            </select>
          </div>

          <div style={{ marginTop: '1.5rem' }}>
            <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 600 }}>Legal Argument:</label>
            <textarea
              placeholder="Enter your legal argument..."
              style={{
                width: '100%',
                minHeight: '200px',
                padding: '0.75rem',
                border: '1px solid #d1d5db',
                borderRadius: '6px',
                fontSize: '1rem',
                fontFamily: 'inherit'
              }}
            />
          </div>

          <button style={{
            marginTop: '1.5rem',
            padding: '1rem 2rem',
            background: '#2563eb',
            color: 'white',
            border: 'none',
            borderRadius: '6px',
            fontSize: '1rem',
            fontWeight: 600,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem'
          }}>
            <FileText size={20} />
            Analyze Argument Strength
          </button>

          <div style={{ marginTop: '2rem', padding: '1.5rem', background: '#f0f9ff', borderRadius: '8px' }}>
            <h3>Brief Builder Features:</h3>
            <ul style={{ marginTop: '1rem', paddingLeft: '1.5rem' }}>
              <li>Syllogistic argument structure analysis</li>
              <li>Identification of major and minor premises</li>
              <li>Logical coherence assessment</li>
              <li>Authority support validation</li>
              <li>Counter-argument prediction</li>
              <li>Weakness identification and improvement suggestions</li>
            </ul>
          </div>
        </div>
      </main>
    </div>
  )
}

export default BriefBuilder
