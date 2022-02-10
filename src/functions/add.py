"""
Provide handler for the post method.
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
    request_body = json.loads(event['body'])

    first = request_body.get('first')
    second = request_body.get('second')

    result = None
    if not first or not second:
        response: Dict[str, Any] = {
            'body': json.dumps({'result': result}),
            'statusCode': HTTPStatus.BAD_REQUEST,
        }
        return response

    result = first + second
    response: Dict[str, Any] = {
        'body': json.dumps({'result': result}),
        'statusCode': HTTPStatus.OK,
    }

    return response
