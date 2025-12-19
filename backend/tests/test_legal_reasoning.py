"""
Tests for Legal Reasoning API endpoints
"""
import pytest


def test_health_check(client):
    """Test legal reasoning health check endpoint"""
    response = client.get("/api/reasoning/health")
    assert response.status_code == 200
    assert response.json()["status"] == "operational"
    assert response.json()["service"] == "legal_reasoning"


def test_analyze_argument(client):
    """Test legal argument analysis endpoint"""
    argument_text = """
    All contracts require consideration to be enforceable.
    This agreement lacks consideration.
    Therefore, this agreement is unenforceable.
    """
    
    response = client.post(
        "/api/reasoning/analyze-argument",
        params={
            "argument_text": argument_text,
            "include_counter_arguments": True
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Validate response structure
    assert "argument_id" in data
    assert "syllogisms" in data
    assert "strengths" in data
    assert "weaknesses" in data
    assert "counter_arguments" in data
    assert "overall_strength" in data
    assert "improvement_suggestions" in data
    
    # Validate syllogisms structure
    assert isinstance(data["syllogisms"], list)
    if len(data["syllogisms"]) > 0:
        syllogism = data["syllogisms"][0]
        assert "major_premise" in syllogism
        assert "minor_premise" in syllogism
        assert "conclusion" in syllogism
        assert "supporting_authorities" in syllogism


def test_evaluate_precedent(client, sample_case_citation, sample_current_facts):
    """Test precedent evaluation endpoint"""
    response = client.post(
        "/api/reasoning/evaluate-precedent",
        json={
            "case_citation": sample_case_citation,
            "current_facts": sample_current_facts,
            "jurisdiction": "Federal - 9th Circuit"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Validate response structure
    assert "case_citation" in data
    assert "jurisdiction" in data
    assert "holding" in data
    assert "key_facts" in data
    assert "legal_principles" in data
    assert "distinguishing_factors" in data
    assert "applicability_score" in data
    assert "binding_authority" in data
    
    # Validate types
    assert isinstance(data["key_facts"], list)
    assert isinstance(data["legal_principles"], list)
    assert isinstance(data["applicability_score"], (int, float))
    assert isinstance(data["binding_authority"], bool)


def test_map_authorities(client, sample_document_text):
    """Test authority mapping endpoint"""
    response = client.post(
        "/api/reasoning/map-authorities",
        params={
            "document_text": sample_document_text,
            "jurisdiction": "Federal"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Validate response structure
    assert "authorities_found" in data
    assert "binding_authorities" in data
    assert "persuasive_authorities" in data
    assert "hierarchy_map" in data
