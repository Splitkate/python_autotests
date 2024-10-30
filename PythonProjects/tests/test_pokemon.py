import requests
import pytest



URL =  'https://api.pokemonbattle.ru/v2'
TOKEN = '98f59cad947d78ffd6ce47b1bff68676'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
trainer_id = 8107


def test_status_code():
    response =  requests.get(url = f'{URL}/trainers',  params = {'trainer_id': trainer_id} )
    assert response.status_code == 200


def  test_trainer():
    response_trainer = requests.get (url = f'{URL}/me', headers=HEADER, params = {'trainer_id': trainer_id})
    assert response_trainer.json()["data"][0]["trainer_name"] == 'Splitkate'


