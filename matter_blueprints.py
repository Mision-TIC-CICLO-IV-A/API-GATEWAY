import requests
from flask import Blueprint, request
from utils import load_file_config, HEADERS

matter_blueprints = Blueprint('matter_blueprints', __name__)
date_config = load_file_config()
url_base = date_config.get('url-backend-votaciones') + "/matter"


@matter_blueprints.route("/matter", methods=['GET'])
def get_all_matter() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@matter_blueprints.route("/matter/<string:id>", methods=['GET'])
def get_matter_by_id(id_: str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@matter_blueprints.route("/matter/insert", methods=['POST'])
def insert_matter() -> dict:
    matter = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=matter)
    return response.json()


@matter_blueprints.route("/matter/update/<string:id_>", methods=['PUT'])
def update_matter(id_: str) -> dict:
    matter = request.get_json()
    url = url_base + f'/update{id_}'
    response = requests.patch(url, headers=HEADERS, json=matter)
    return response.json()


@matter_blueprints.route("/matter/delete/<string:id_>", methods=['DELETE'])
def delete_matter(id_: str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()
