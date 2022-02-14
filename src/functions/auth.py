"""
Provide handler for the auth method.
"""
from typing import Any, Dict

from aws_lambda_powertools.utilities.typing import LambdaContext


def handler(event: Dict[str, Any], context: LambdaContext) -> Dict[str, Any]:
    """
    Lambda function handler.

    Arguments:
        event (dict): the event with data to process.
        context (LambdaContext): the information about the invocation, function, and runtime environment.

    Returns:
        The response as dict.
    """
    # auth_token = ...
    resource = event.get('methodArn')
    principal_id = None
    effect = 'Allow'
    response = {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2022-02-14',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': resource,
                },
            ],
        },
    }
    return response
