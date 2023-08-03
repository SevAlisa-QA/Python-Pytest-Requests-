import requests
host = 'https://api.pokemonbattle.me:9104/'
token = '8ddc500e9a9b49764fef25e8b39f7053'

def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get (f'{host}/trainers', params= {'trainer_id': 1382})
    assert response.json()['trainer_name'] == 'Sev_Alisa'