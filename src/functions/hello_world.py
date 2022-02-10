"""
Provide handler for the get method.
"""
import json
from http import HTTPStatus
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
    response: Dict[str, Any] = {
        'body': json.dumps({'result': 'Hello World'}),
        'statusCode': HTTPStatus.OK,
    }
    return response
