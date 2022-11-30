import requests
from flask import Blueprint, request
from utils import load_file_config, HEADERS

departament_blueprints = Blueprint('departament_blueprints', __name__)
date_config = load_file_config()
url_base = date_config.get('url-backend-votaciones') + "/departament"


@departament_blueprints.route("/departaments", methods=['GET'])
def get_all_departament() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@departament_blueprints.route("/departament/<string:id>", methods=['GET'])
def get_departament_by_id(id_: str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@departament_blueprints.route("/departament/insert", methods=['POST'])
def insert_departament() -> dict:
    departament = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=departament)
    return response.json()


@departament_blueprints.route("/departament/update/<string:id_>", methods=['PUT'])
def update_departament(id_: str) -> dict:
    departament = request.get_json()
    url = url_base + f'/update{id_}'
    response = requests.patch(url, headers=HEADERS, json=departament)
    return response.json()


@departament_blueprints.route("/departament/delete/<string:id_>", methods=['DELETE'])
def delete_departament(id_: str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()
