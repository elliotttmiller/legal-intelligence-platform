"""
Tests for Legal Analysis API endpoints
"""
import pytest
from app.models.schemas import DocumentType


def test_health_check(client):
    """Test legal analysis health check endpoint"""
    response = client.get("/api/legal-analysis/health")
    assert response.status_code == 200
    assert response.json()["status"] == "operational"
    assert response.json()["service"] == "legal_analysis"


def test_interpret_document(client, sample_document_text):
    """Test document interpretation endpoint"""
    response = client.post(
        "/api/legal-analysis/interpret",
        params={
            "document_text": sample_document_text,
            "document_type": DocumentType.CONTRACT.value,
            "preserve_nuance": True,
            "include_authorities": True
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Validate response structure
    assert "document_id" in data
    assert "document_type" in data
    assert "executive_summary" in data
    assert "key_legal_issues" in data
    assert "clauses" in data
    assert "authorities" in data
    assert "legal_framework" in data
    assert "overall_confidence" in data
    
    # Validate document type
    assert data["document_type"] == DocumentType.CONTRACT.value
    
    # Validate clauses structure
    assert isinstance(data["clauses"], list)
    if len(data["clauses"]) > 0:
        clause = data["clauses"][0]
        assert "clause_id" in clause
        assert "text" in clause
        assert "interpretation" in clause
        assert "confidence" in clause
    
    # Validate authorities structure
    assert isinstance(data["authorities"], list)


def test_interpret_document_without_authorities(client, sample_document_text):
    """Test document interpretation without authorities"""
    response = client.post(
        "/api/legal-analysis/interpret",
        params={
            "document_text": sample_document_text,
            "document_type": DocumentType.CONTRACT.value,
            "preserve_nuance": True,
            "include_authorities": False
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "authorities" in data
