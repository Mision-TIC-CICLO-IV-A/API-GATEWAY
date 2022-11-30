import requests
from flask import Blueprint, request
from utils import load_file_config, HEADERS

tables_blueprints = Blueprint('tables_blueprints', __name__)
date_config = load_file_config()
url_base = date_config.get('url-backend-votaciones') + "/tables"


@tables_blueprints.route("/tables", methods=['GET'])
def get_all_tables() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@tables_blueprints.route("/tables/<string:id>", methods=['GET'])
def get_tables_by_id(id_: str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@tables_blueprints.route("/tables/insert", methods=['POST'])
def insert_tables() -> dict:
    tables = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=tables)
    return response.json()


@tables_blueprints.route("/tables/update/<string:id_>", methods=['PUT'])
def update_tables(id_: str) -> dict:
    tables = request.get_json()
    url = url_base + f'/update{id_}'
    response = requests.patch(url, headers=HEADERS, json=tables)
    return response.json()


@tables_blueprints.route("/tables/delete/<string:id_>", methods=['DELETE'])
def delete_tables(id_: str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()
