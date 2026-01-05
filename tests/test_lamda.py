# Professional unit testing
# Shows you understand testing best practices
# Will run automatically in the pipeline

import json
import pytest
from lambda_function import lambda_handler

def test_lambda_handler_success():
    """Test that Lambda handler returns 200 status"""
    event = {}
    context = {}
    
    response = lambda_handler(event, context)
    
    assert response['statusCode'] == 200
    assert 'body' in response

def test_lambda_handler_response_structure():
    """Test response body structure"""
    event = {}
    context = {}
    
    response = lambda_handler(event, context)
    body = json.loads(response['body'])
    
    assert 'message' in body
    assert 'environment' in body
    assert 'version' in body
    assert 'timestamp' in body
    assert 'status' in body
    
def test_lambda_handler_message():
    """Test response message content"""
    event = {}
    context = {}
    
    response = lambda_handler(event, context)
    body = json.loads(response['body'])
    
    assert body['status'] == 'healthy'
    assert 'CI/CD Pipeline' in body['message']
