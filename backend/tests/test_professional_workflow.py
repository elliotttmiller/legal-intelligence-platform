"""
Tests for Professional Workflow API endpoints
"""
import pytest


def test_health_check(client):
    """Test professional workflow health check endpoint"""
    response = client.get("/api/workflow/health")
    assert response.status_code == 200
    assert response.json()["status"] == "operational"
    assert response.json()["service"] == "professional_workflow"


def test_batch_process_documents(client):
    """Test batch document processing endpoint"""
    response = client.post(
        "/api/workflow/batch-process",
        json={
            "document_ids": ["doc1", "doc2", "doc3"],
            "analysis_type": "comparison",
            "preserve_relationships": True
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Validate response structure
    assert "batch_id" in data
    assert "documents_processed" in data
    assert "analysis_type" in data
    assert "workflow_metrics" in data
    
    # Validate metrics
    metrics = data["workflow_metrics"]
    assert "task_type" in metrics
    assert "manual_time_estimate" in metrics
    assert "automated_time" in metrics
    assert "time_savings_percentage" in metrics


def test_compare_documents(client, sample_document_text):
    """Test document comparison endpoint"""
    doc_a = sample_document_text
    doc_b = sample_document_text.replace("$10,000", "$15,000")
    
    response = client.post(
        "/api/workflow/compare",
        params={
            "doc_a_text": doc_a,
            "doc_b_text": doc_b,
            "doc_a_id": "original",
            "doc_b_id": "modified"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Validate response structure
    assert "doc_a_id" in data
    assert "doc_b_id" in data
    assert "differences" in data
    assert "similarities" in data
    assert "legal_implications" in data
    assert "recommendation" in data
    assert "change_count" in data
    assert "similarity_score" in data
    
    # Validate IDs
    assert data["doc_a_id"] == "original"
    assert data["doc_b_id"] == "modified"


def test_get_workflow_metrics(client):
    """Test workflow metrics endpoint"""
    response = client.get("/api/workflow/metrics")
    assert response.status_code == 200
    data = response.json()
    
    # Validate metrics structure
    assert "average_time_savings" in data
    assert "documents_processed" in data
    assert "total_hours_saved" in data
