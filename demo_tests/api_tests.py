import requests
import pytest
import json
from jsonschema import validate


def test_request_response():
    # Confirm that the request-response cycle completed successfully.
    response = requests.get('https://reqres.in/api/users')
    assert response.status_code == 200


def test_request_body_is_not_empty():
    # Send a request to the API server and store the response.
    response = requests.get('https://reqres.in/api/users')

    # Confirm that the response is not empty
    res_body = response.json()
    assert len(res_body) != 0
    assert res_body is not None


def test_request_with_url_parameter():
    # Pass data parameter to the request
    param_data = {'page': '2'}
    response = requests.get('https://reqres.in/api/users', params=param_data)

    assert response.url == 'https://reqres.in/api/users?page=2'


def test_response_body_is_correct():
    # Pass data parameter to the request
    param_data = {'page': '2'}
    response = requests.get('https://reqres.in/api/users', params=param_data)

    # Converts response JSON object to python dictionary
    res_body = response.json()

    # Dictionary object
    expected_data = {
        "page": 2,
        "per_page": 6,
        "total": 12,
        "total_pages": 2,
        "data": [
            {
                "id": 7,
                "email": "michael.lawson@reqres.in",
                "first_name": "Michael",
                "last_name": "Lawson",
                "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/follettkyle/128.jpg"
            },
            {
                "id": 8,
                "email": "lindsay.ferguson@reqres.in",
                "first_name": "Lindsay",
                "last_name": "Ferguson",
                "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/araa3185/128.jpg"
            },
            {
                "id": 9,
                "email": "tobias.funke@reqres.in",
                "first_name": "Tobias",
                "last_name": "Funke",
                "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/vivekprvr/128.jpg"
            },
            {
                "id": 10,
                "email": "byron.fields@reqres.in",
                "first_name": "Byron",
                "last_name": "Fields",
                "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/russoedu/128.jpg"
            },
            {
                "id": 11,
                "email": "george.edwards@reqres.in",
                "first_name": "George",
                "last_name": "Edwards",
                "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/mrmoiree/128.jpg"
            },
            {
                "id": 12,
                "email": "rachel.howell@reqres.in",
                "first_name": "Rachel",
                "last_name": "Howell",
                "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/hebertialmeida/128.jpg"
            }
        ],
        "ad": {
            "company": "StatusCode Weekly",
            "url": "http://statuscode.org/",
            "text": "A weekly newsletter focusing on software development, infrastructure, the server, performance, and the stack end of things."
        }
    }

    # Request body should be same as expected response_body
    assert res_body == expected_data


def test_verify_data_in_response_body():

    domain = 'https://api-staging.zenrooms.com/yan'
    url = domain + '/properties'
    param_data = {'partnerId': 'AGODA',
                  'trackingId': '12345',
                  'lastDate': '2019-01-01'
                  }

    response = requests.get(url, params=param_data)

    res_body = response.json()
    assert type(res_body) is dict

    expected_data = {'code': 200, 'data': {'propertyIds': [
        'ZEN_2632', 'ZEN_6215', 'ZEN_9013', 'ZEN_9248', 'ZEN_9252']}}

    assert type(expected_data) is dict

    # Request body should be same as expected response_body
    assert res_body == expected_data
    assert res_body['code'] == 200


def test_verify_jsonschema_in_response_body():

    domain = 'https://api-staging.zenrooms.com/yan'
    url = domain + '/properties'
    param_data = {'partnerId': 'AGODA',
                  'trackingId': '12345',
                  'lastDate': '2019-01-01'
                  }

    schema = {
        "type": "object",
        "properties": {
            "code": {"type": "integer"},
            "data": {
                "type": "object",
                "properties": {
                    "propertyIds": {"type": "array"}
                }
            }
        }
    }

    # Converts python object to JSON object
    jschema = json.dumps(schema)

    response = requests.get(url, params=param_data)

    # Converts JSON object to python dictionary
    json_data = json.loads(response.text)

    # Converts response JSON object to python dictionary
    res_body = response.json()

    assert type(res_body) is dict
    assert type(json_data) is dict

    # Validate schema against the response data
    validate(res_body, schema)
    validate(json_data, schema)
