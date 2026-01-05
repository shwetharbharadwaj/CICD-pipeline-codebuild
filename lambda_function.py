#Professional Lambda handler with logging
# Returns deployment metadata
# Shows version control
# Industry-standard response format


import json
import os
from datetime import datetime

def lambda_handler(event, context):
    #get env variables
    environment = os.environ.get('ENVIRONMENT','dev')
    version = os.environ.get('VERSION','1.0.0')

    #log the invocation
    print(f"Function invoked at {datetime.now()}")
    print(f"Env {environment}")
    print(f"version {version}")

    #prepare response
    response_body = {
        'message': 'CI/CD Pipeline Successfully Deployed!',
        'environment': environment,
        'version': version,
        'timestamp': datetime.now().isoformat(),
        'status': 'healthy'
    }

    return{
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response_body, indent=2)
    }

