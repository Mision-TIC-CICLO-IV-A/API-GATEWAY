import requests
from flask import Blueprint, request
from utils import load_file_config, HEADERS

enrollment_blueprints = Blueprint('enrollment_blueprints', __name__)
date_config = load_file_config()
url_base = date_config.get('url-backend-votaciones') + "/enrollment"


@enrollment_blueprints.route("/enrollment", methods=['GET'])
def get_all_enrollment() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@enrollment_blueprints.route("/enrollment/<string:id>", methods=['GET'])
def get_enrollment_by_id(id_: str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@enrollment_blueprints.route("/enrollment/insert", methods=['POST'])
def insert_enrollment() -> dict:
    enrollment = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=enrollment)
    return response.json()


@enrollment_blueprints.route("/enrollment/update/<string:id_>", methods=['PUT'])
def update_enrollment(id_: str) -> dict:
    enrollment = request.get_json()
    url = url_base + f'/update{id_}'
    response = requests.patch(url, headers=HEADERS, json=enrollment)
    return response.json()


@enrollment_blueprints.route("/enrollment/delete/<string:id_>", methods=['DELETE'])
def delete_enrollment(id_: str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()
