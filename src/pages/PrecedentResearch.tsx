import { Link } from 'react-router-dom'
import { ArrowLeft, Search } from 'lucide-react'

/**
 * Precedent Research - Case law and authority research tool
 */
function PrecedentResearch() {
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
        <h1 style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>Precedent Research</h1>
        <p style={{ opacity: 0.9 }}>Case law and authority analysis with applicability scoring</p>
      </header>

      <main style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem' }}>
        <div style={{ background: 'white', padding: '2rem', borderRadius: '12px', boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)' }}>
          <h2>Search Case Law</h2>
          <div style={{ display: 'flex', gap: '1rem', marginTop: '1.5rem' }}>
            <input
              type="text"
              placeholder="Enter case citation or search terms..."
              style={{
                flex: 1,
                padding: '0.75rem',
                border: '1px solid #d1d5db',
                borderRadius: '6px',
                fontSize: '1rem'
              }}
            />
            <button style={{
              padding: '0.75rem 1.5rem',
              background: '#2563eb',
              color: 'white',
              border: 'none',
              borderRadius: '6px',
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem',
              cursor: 'pointer'
            }}>
              <Search size={20} />
              Search
            </button>
          </div>

          <div style={{ marginTop: '2rem' }}>
            <h3>Features:</h3>
            <ul style={{ marginTop: '1rem', paddingLeft: '1.5rem' }}>
              <li>Case law database search with natural language processing</li>
              <li>Precedent applicability scoring based on fact patterns</li>
              <li>Authority hierarchy mapping (Supreme Court, Circuit, District)</li>
              <li>Binding vs. persuasive authority identification</li>
              <li>Distinguishing factor analysis for current matter</li>
            </ul>
          </div>
        </div>
      </main>
    </div>
  )
}

export default PrecedentResearch
