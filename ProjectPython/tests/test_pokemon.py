import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = 'e58aa25edcb20c27b4642e296789d011'

def test_status_code():

    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1357})
    assert response.status_code == 200

def test_part_of_answer():

    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1357})
    assert response.json()['trainer_name'] == 'Linoks95'