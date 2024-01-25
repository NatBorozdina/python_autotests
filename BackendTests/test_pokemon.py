import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'

HEADER = {"Content-Type": "application/json",
          "trainer_token": "fc5fcec17a1ff31db059bc66f344a975"
          }

def test_get_trainers_by_level():
    '''
    KTI Get trainers by level
    '''
    response = requests.get(url=f'{URL}/trainers', params={'level':1}, headers=HEADER, timeout=10)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_by_id():
    '''
    KTI-2 Get trainer by id
    '''
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':3617}, headers=HEADER, timeout=10)
    assert response.status_code == 200, 'Unexpected status code'
    assert response.json()['trainer_name'] == 'Наталья', 'Unexpected name'