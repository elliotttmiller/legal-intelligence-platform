import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import ProfessionalDashboard from './pages/ProfessionalDashboard'
import DocumentInterpreter from './pages/DocumentInterpreter'
import PrecedentResearch from './pages/PrecedentResearch'
import BriefBuilder from './pages/BriefBuilder'
import WorkflowOptimizer from './pages/WorkflowOptimizer'

const queryClient = new QueryClient()

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <Routes>
          <Route path="/" element={<ProfessionalDashboard />} />
          <Route path="/interpret" element={<DocumentInterpreter />} />
          <Route path="/research" element={<PrecedentResearch />} />
          <Route path="/brief-builder" element={<BriefBuilder />} />
          <Route path="/workflow" element={<WorkflowOptimizer />} />
        </Routes>
      </Router>
    </QueryClientProvider>
  )
}

export default App
