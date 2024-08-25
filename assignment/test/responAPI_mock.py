""" Name : กัมแพงเพชร สิงห์ขรณ์
    ID  : 653380120-2
    sec: 1
"""

from io import BytesIO
from requests.models import Response

def get_mock_currency_api_response():
    mock_api_response = Response()
    mock_api_response.status_code = 200
    mock_api_response.raw = BytesIO(b'{ "base": "THB", "result": {"KRW": 38.69} }')
    return mock_api_response
