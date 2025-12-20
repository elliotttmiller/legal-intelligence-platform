import { useState } from 'react'
import { Link } from 'react-router-dom'
import { ArrowLeft, FileText, CheckCircle, Scale } from 'lucide-react'
import './BriefBuilder.css'

/**
 * Brief Builder - Legal brief construction assistant
 */

// Mock analysis data
const mockAnalysis = {
  overallStrength: 82,
  syllogisms: [
    {
      major: 'All evidence obtained in violation of the Fourth Amendment is inadmissible in criminal prosecutions (Mapp v. Ohio).',
      minor: 'The evidence in this case was obtained without a valid warrant and without exigent circumstances.',
      conclusion: 'Therefore, the evidence must be suppressed and is inadmissible at trial.'
    }
  ],
  strengths: [
    'Strong precedential support from binding Supreme Court authority',
    'Clear chain of legal reasoning with well-established major premise',
    'Factual pattern closely aligns with controlling case law',
    'Multiple supporting authorities strengthen the argument'
  ],
  weaknesses: [
    'Opposing counsel may argue good faith exception applies',
    'Recent circuit split on similar fact patterns could create uncertainty',
    'Need to address potential distinguish ing factors more thoroughly'
  ],
  suggestions: [
    'Add analysis of recent Supreme Court decisions on digital searches',
    'Strengthen minor premise with more detailed factual development',
    'Include preemptive counter-arguments to good faith exception',
    'Consider adding alternative arguments based on state constitutional grounds'
  ]
}

function BriefBuilder() {
  const [briefType, setBriefType] = useState('motion-dismiss')
  const [argument, setArgument] = useState('')
  const [showAnalysis, setShowAnalysis] = useState(false)

  const handleAnalyze = () => {
    if (argument.trim()) {
      setShowAnalysis(true)
    }
  }

  return (
    <div className="brief-container">
      <header className="brief-header">
        <Link to="/" className="back-link">
          <ArrowLeft size={24} />
          Back to Dashboard
        </Link>
        <h1>Brief Builder</h1>
        <p>Legal brief construction with argument strength analysis</p>
      </header>

      <main className="brief-main">
        {/* Builder Form */}
        <div className="builder-card">
          <h2>Construct Legal Brief</h2>
          
          <div className="form-group">
            <label htmlFor="brief-type">Brief Type:</label>
            <select
              id="brief-type"
              className="form-select"
              value={briefType}
              onChange={(e) => setBriefType(e.target.value)}
            >
              <option value="motion-dismiss">Motion to Dismiss</option>
              <option value="summary-judgment">Summary Judgment Brief</option>
              <option value="appellate">Appellate Brief</option>
              <option value="trial">Trial Brief</option>
              <option value="memorandum">Memorandum of Law</option>
              <option value="opposition">Opposition Brief</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="legal-argument">Legal Argument:</label>
            <textarea
              id="legal-argument"
              className="form-textarea"
              placeholder="Enter your legal argument...

Example:
The evidence obtained during the search of defendant's vehicle must be suppressed. The Fourth Amendment protects against unreasonable searches and seizures. Here, law enforcement conducted a warrantless search without probable cause or exigent circumstances. Under Mapp v. Ohio, evidence obtained in violation of the Fourth Amendment is inadmissible. Therefore, the court should grant the motion to suppress."
              value={argument}
              onChange={(e) => setArgument(e.target.value)}
            />
          </div>

          <button
            className="analyze-button"
            onClick={handleAnalyze}
            disabled={!argument.trim()}
          >
            <Scale size={20} />
            Analyze Argument Strength
          </button>

          <div className="features-card">
            <h3>Brief Builder Features:</h3>
            <ul className="features-list">
              <li>Syllogistic argument structure analysis</li>
              <li>Identification of major and minor premises</li>
              <li>Logical coherence assessment</li>
              <li>Authority support validation</li>
              <li>Counter-argument prediction</li>
              <li>Weakness identification and improvement suggestions</li>
            </ul>
          </div>
        </div>

        {/* Analysis Results */}
        {showAnalysis && (
          <div className="analysis-section">
            <div className="analysis-header">
              <CheckCircle size={32} />
              <h2>Argument Analysis Complete</h2>
            </div>

            {/* Overall Strength */}
            <div className="analysis-card">
              <h3>Overall Argument Strength</h3>
              <div className="strength-score">
                <div className="score-value">{mockAnalysis.overallStrength}%</div>
                <div className="score-label">Strong argument with solid precedential support</div>
              </div>
            </div>

            {/* Syllogistic Analysis */}
            <div className="analysis-card">
              <h3>Syllogistic Structure</h3>
              {mockAnalysis.syllogisms.map((syllogism, index) => (
                <div key={index} className="syllogism-item">
                  <div className="syllogism-part">
                    <div className="syllogism-label">Major Premise</div>
                    <div className="syllogism-text">{syllogism.major}</div>
                  </div>
                  <div className="syllogism-part">
                    <div className="syllogism-label">Minor Premise</div>
                    <div className="syllogism-text">{syllogism.minor}</div>
                  </div>
                  <div className="syllogism-part">
                    <div className="syllogism-label">Conclusion</div>
                    <div className="syllogism-text">{syllogism.conclusion}</div>
                  </div>
                </div>
              ))}
            </div>

            {/* Strengths */}
            <div className="analysis-card">
              <h3>Argument Strengths</h3>
              <ul className="analysis-list strengths">
                {mockAnalysis.strengths.map((strength, index) => (
                  <li key={index}>{strength}</li>
                ))}
              </ul>
            </div>

            {/* Weaknesses */}
            <div className="analysis-card">
              <h3>Potential Weaknesses</h3>
              <ul className="analysis-list weaknesses">
                {mockAnalysis.weaknesses.map((weakness, index) => (
                  <li key={index}>{weakness}</li>
                ))}
              </ul>
            </div>

            {/* Improvement Suggestions */}
            <div className="analysis-card">
              <h3>Improvement Suggestions</h3>
              <ul className="analysis-list suggestions">
                {mockAnalysis.suggestions.map((suggestion, index) => (
                  <li key={index}>{suggestion}</li>
                ))}
              </ul>
            </div>
          </div>
        )}
      </main>
    </div>
  )
}

export default BriefBuilder
