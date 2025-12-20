import { useState } from 'react'
import { Link } from 'react-router-dom'
import { ArrowLeft, Search, BookOpen, FileText, ExternalLink } from 'lucide-react'
import './PrecedentResearch.css'

/**
 * Precedent Research - Case law and authority research tool
 */

// Mock data for demonstration
const mockCases = [
  {
    id: 1,
    citation: 'Miranda v. Arizona, 384 U.S. 436 (1966)',
    jurisdiction: 'United States Supreme Court',
    year: 1966,
    relevanceScore: 94,
    binding: true,
    holding: 'The prosecution may not use statements stemming from custodial interrogation unless it demonstrates the use of procedural safeguards effective to secure the Fifth Amendment\'s privilege against self-incrimination.',
    keyFacts: [
      'Defendant was interrogated while in police custody',
      'No warning of constitutional rights was provided',
      'Confession was obtained and used at trial'
    ],
    legalPrinciples: ['Fifth Amendment Rights', 'Self-Incrimination', 'Due Process']
  },
  {
    id: 2,
    citation: 'Mapp v. Ohio, 367 U.S. 643 (1961)',
    jurisdiction: 'United States Supreme Court',
    year: 1961,
    relevanceScore: 89,
    binding: true,
    holding: 'Evidence obtained in violation of the Fourth Amendment cannot be used in state criminal prosecutions (exclusionary rule applies to states).',
    keyFacts: [
      'Police conducted warrantless search of defendant\'s home',
      'Obscene materials were discovered and used as evidence',
      'State conviction was based on illegally obtained evidence'
    ],
    legalPrinciples: ['Fourth Amendment', 'Search and Seizure', 'Exclusionary Rule']
  },
  {
    id: 3,
    citation: 'Terry v. Ohio, 392 U.S. 1 (1968)',
    jurisdiction: 'United States Supreme Court',
    year: 1968,
    relevanceScore: 86,
    binding: true,
    holding: 'Police may conduct a limited search for weapons (frisk) when they have reasonable suspicion that a person may be armed and dangerous.',
    keyFacts: [
      'Officer observed suspicious behavior suggesting criminal activity',
      'Conducted pat-down search for weapons',
      'Weapons were discovered and defendant was arrested'
    ],
    legalPrinciples: ['Reasonable Suspicion', 'Stop and Frisk', 'Officer Safety']
  },
  {
    id: 4,
    citation: 'United States v. Jones, 565 U.S. 400 (2012)',
    jurisdiction: 'United States Supreme Court',
    year: 2012,
    relevanceScore: 82,
    binding: true,
    holding: 'Installation of GPS tracking device on a vehicle, and its use to monitor movements, constitutes a "search" under the Fourth Amendment.',
    keyFacts: [
      'GPS device installed on defendant\'s vehicle without valid warrant',
      'Device tracked movements for 28 days',
      'Location data used in criminal prosecution'
    ],
    legalPrinciples: ['Fourth Amendment', 'Technology and Privacy', 'Reasonable Expectation of Privacy']
  }
]

function PrecedentResearch() {
  const [searchQuery, setSearchQuery] = useState('')
  const [showResults, setShowResults] = useState(false)
  const [jurisdiction, setJurisdiction] = useState('all')
  const [authorityType, setAuthorityType] = useState('all')

  const handleSearch = () => {
    setShowResults(true)
  }

  return (
    <div className="research-container">
      <header className="research-header">
        <Link to="/" className="back-link">
          <ArrowLeft size={24} />
          Back to Dashboard
        </Link>
        <h1>Precedent Research</h1>
        <p>Case law and authority analysis with applicability scoring</p>
      </header>

      <main className="research-main">
        {/* Search Section */}
        <div className="search-card">
          <h2>Search Case Law</h2>
          <div className="search-form">
            <input
              type="text"
              placeholder="Enter case citation, legal issue, or search terms..."
              className="search-input"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
            />
            <button className="search-button" onClick={handleSearch}>
              <Search size={20} />
              Search
            </button>
          </div>

          <div className="filters-section">
            <div className="filter-group">
              <label>Jurisdiction</label>
              <select 
                className="filter-select"
                value={jurisdiction}
                onChange={(e) => setJurisdiction(e.target.value)}
              >
                <option value="all">All Jurisdictions</option>
                <option value="supreme">U.S. Supreme Court</option>
                <option value="circuit">Circuit Courts</option>
                <option value="district">District Courts</option>
                <option value="state">State Courts</option>
              </select>
            </div>

            <div className="filter-group">
              <label>Authority Type</label>
              <select 
                className="filter-select"
                value={authorityType}
                onChange={(e) => setAuthorityType(e.target.value)}
              >
                <option value="all">All Types</option>
                <option value="binding">Binding Authority</option>
                <option value="persuasive">Persuasive Authority</option>
              </select>
            </div>

            <div className="filter-group">
              <label>Date Range</label>
              <select className="filter-select">
                <option value="all">All Time</option>
                <option value="recent">Last 5 Years</option>
                <option value="decade">Last 10 Years</option>
                <option value="modern">Since 2000</option>
              </select>
            </div>
          </div>
        </div>

        {/* Results Section */}
        {showResults && (
          <div className="results-section">
            <div className="results-header">
              <div className="results-count">
                Found <strong>{mockCases.length} cases</strong> matching your search
              </div>
              <div className="sort-controls">
                <span className="sort-label">Sort by:</span>
                <select className="filter-select" style={{ minWidth: '150px' }}>
                  <option value="relevance">Relevance</option>
                  <option value="date">Date</option>
                  <option value="jurisdiction">Jurisdiction</option>
                </select>
              </div>
            </div>

            {mockCases.map((caseItem) => (
              <div key={caseItem.id} className="case-card">
                <div className="case-header">
                  <div>
                    <div className="case-citation">{caseItem.citation}</div>
                    <div className="case-jurisdiction">{caseItem.jurisdiction} • {caseItem.year}</div>
                  </div>
                  <div className="relevance-badge">
                    <div className="relevance-score">{caseItem.relevanceScore}%</div>
                    <div className="relevance-label">Relevance</div>
                  </div>
                </div>

                <div className="case-tags">
                  <span className={`tag ${caseItem.binding ? 'binding' : 'persuasive'}`}>
                    {caseItem.binding ? 'Binding Authority' : 'Persuasive Authority'}
                  </span>
                  {caseItem.legalPrinciples.slice(0, 2).map((principle, idx) => (
                    <span key={idx} className="tag" style={{ 
                      background: 'rgba(255, 255, 255, 0.05)', 
                      color: 'var(--text-secondary)',
                      border: '1px solid var(--border-default)'
                    }}>
                      {principle}
                    </span>
                  ))}
                </div>

                <div className="case-holding">
                  <h4>Holding:</h4>
                  <p>{caseItem.holding}</p>
                </div>

                <div className="key-facts">
                  <h4>Key Facts:</h4>
                  <ul className="facts-list">
                    {caseItem.keyFacts.map((fact, idx) => (
                      <li key={idx}>{fact}</li>
                    ))}
                  </ul>
                </div>

                <div className="case-actions">
                  <button className="case-action-btn">
                    <BookOpen size={16} style={{ display: 'inline', marginRight: '0.5rem' }} />
                    View Full Opinion
                  </button>
                  <button className="case-action-btn">
                    <FileText size={16} style={{ display: 'inline', marginRight: '0.5rem' }} />
                    Add to Brief
                  </button>
                  <button className="case-action-btn">
                    <ExternalLink size={16} style={{ display: 'inline', marginRight: '0.5rem' }} />
                    Shepardize
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  )
}

export default PrecedentResearch
