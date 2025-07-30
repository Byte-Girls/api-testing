import requests
import pytest
import json
import jsonschema


@pytest.mark.smoke


def test_001_Obtener_la_lista_de_object_del_sistema():
#Descripción:  El usuario debe obtener la lista completa de todos los objetos existentes en el sistema


url = "https://api.restful-api.dev/"
list_url = url + "Objects"
response = requests.get(list_url)
print(response.text)
assert response.status_code==200


#post 

def test_002_adicionar_objeto(get_url):
    """Descripcion: El usuario desea adicionar un objeto a la lista"""
    url = get_url + "objects"
    payload = json.dumps({
        "name": "Samsung s25",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200
    assert_create_object_response_schema(response)
     

    @pytest.mark.smoke
@pytest.mark.regression
def test_003_adicionar_objeto_precio_limite(get_url):
    # Descripción: El usuario desea adicionar un objeto a la lista
    url = get_url + "objects"
    payload = json.dumps({
        "name": "Apple Diplo",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200
    #schema ...json
    assert_create_object_response_schema(response)


#put 
@pytest.mark.smoke

def test_003_modificar_objeto(get_url, add_object):
    """Descripcion: El usuario desea adicionar un objeto a la lista"""
    id_object = add_object["id"]
    url = get_url + "/objects/" + id_object
    payload = json.dumps({
        "name": "Apple editadooooooooooo",
        "data": {
            "year": 2029,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.put(url, headers=headers, data=payload)
    assert response.status_code == 200
