"""
Test configuration for Legal Guard Professional
"""
import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def sample_document_text():
    """Sample legal document text for testing"""
    return """
    AGREEMENT
    
    This Agreement is entered into as of January 1, 2024, between Party A and Party B.
    
    1. SERVICES: Party B agrees to provide legal services as requested by Party A.
    
    2. COMPENSATION: Party A shall pay Party B $10,000 upon execution of this Agreement.
    
    3. TERM: This Agreement shall remain in effect for one year from the date of execution.
    
    4. GOVERNING LAW: This Agreement shall be governed by the laws of the State of California.
    """


@pytest.fixture
def sample_case_citation():
    """Sample case citation for testing"""
    return "Smith v. Jones, 123 F.3d 456 (9th Cir. 2020)"


@pytest.fixture
def sample_current_facts():
    """Sample facts for precedent analysis"""
    return [
        "Parties entered written agreement",
        "Consideration was exchanged",
        "Performance was completed"
    ]
