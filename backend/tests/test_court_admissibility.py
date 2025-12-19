"""
Tests for Court Admissibility API endpoints
"""
import pytest


def test_health_check(client):
    """Test court admissibility health check endpoint"""
    response = client.get("/api/court/health")
    assert response.status_code == 200
    assert response.json()["status"] == "operational"
    assert response.json()["service"] == "court_admissibility"


def test_generate_court_report(client):
    """Test court report generation endpoint"""
    analysis_data = {
        "analysis": "Complete legal analysis",
        "findings": "Key findings from analysis",
        "framework": "Applicable legal framework",
        "conclusions": "Professional conclusions"
    }
    
    response = client.post(
        "/api/court/generate-report",
        json={
            "analysis_data": analysis_data,
            "case_title": "Smith v. Jones",
            "jurisdiction": "Federal",
            "report_type": "analysis"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Validate response structure
    assert "report_id" in data
    assert "case_title" in data
    assert "jurisdiction" in data
    assert "report_type" in data
    assert "content" in data
    assert "citations" in data
    assert "evidence_chain" in data
    assert "certification_statement" in data
    assert "court_specific_formatting" in data
    
    # Validate values
    assert data["case_title"] == "Smith v. Jones"
    assert data["jurisdiction"] == "Federal"
    assert isinstance(data["citations"], list)
    assert isinstance(data["evidence_chain"], list)


def test_validate_citation(client, sample_case_citation):
    """Test citation validation endpoint"""
    response = client.post(
        "/api/court/validate-citation",
        params={
            "citation": sample_case_citation,
            "format_style": "bluebook"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Validate response structure
    assert "citation" in data
    assert "type" in data
    assert "format_style" in data
    assert "is_valid" in data
    assert "corrections" in data
    
    # Validate values
    assert data["citation"] == sample_case_citation
    assert data["format_style"] == "bluebook"
    assert isinstance(data["corrections"], list)


def test_format_citation(client):
    """Test citation formatting endpoint"""
    citation_parts = {
        "plaintiff": "Smith",
        "defendant": "Jones",
        "volume": "123",
        "reporter": "F.3d",
        "page": "456",
        "court": "9th Cir.",
        "year": "2020"
    }
    
    response = client.post(
        "/api/court/format-citation",
        json={
            "citation_parts": citation_parts,
            "citation_type": "case",
            "format_style": "bluebook"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Validate response structure
    assert "formatted_citation" in data
    assert isinstance(data["formatted_citation"], str)


def test_get_court_requirements(client):
    """Test court requirements endpoint"""
    response = client.get("/api/court/court-requirements/federal")
    assert response.status_code == 200
    data = response.json()
    
    # Validate response structure
    assert "jurisdiction" in data
    assert "font" in data
    assert "font_size" in data
    assert "line_spacing" in data
    assert "margins" in data
    assert "citation_format" in data
