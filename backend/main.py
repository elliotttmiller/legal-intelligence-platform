from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle manager for startup and shutdown events"""
    logger.info("Legal Guard Professional API starting up...")
    yield
    logger.info("Legal Guard Professional API shutting down...")

# Initialize FastAPI app
app = FastAPI(
    title="Legal Guard Professional API",
    description="Professional Legal Intelligence Platform for Lawyer Workflow Optimization",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Legal Guard Professional API",
        "version": "1.0.0",
        "status": "operational"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "legal-guard-professional"
    }

# Import and include routers
from app.api import legal_analysis, professional_workflow, legal_reasoning, court_admissibility

app.include_router(legal_analysis.router, prefix="/api/legal-analysis", tags=["Legal Analysis"])
app.include_router(professional_workflow.router, prefix="/api/workflow", tags=["Professional Workflow"])
app.include_router(legal_reasoning.router, prefix="/api/reasoning", tags=["Legal Reasoning"])
app.include_router(court_admissibility.router, prefix="/api/court", tags=["Court Admissibility"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
