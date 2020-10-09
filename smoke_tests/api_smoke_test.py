import requests
import pytest
import json
from jsonschema import validate


BASE_URLS= {

}

def test_yan_api_get_property_list_response_is_200():
    '''
    1. Perform a GET request to endpoint
    2. Request should return 200
    '''

    param_data = {'partnerId': 'AGODA',
                  'trackingId': '12345',
                  'lastDate': '2019-01-01'
                  }

    response = requests.get('https://reqres.in/api/users', params=param_data)
    assert response.status_code == 200

