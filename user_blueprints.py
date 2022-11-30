import requests
from flask import Blueprint, request
from utils import load_file_config, HEADERS

user_blueprints = Blueprint('user_blueprints', __name__)
date_config = load_file_config()
url_base = date_config.get('url-backend-security') + "/user"


@user_blueprints.route("/user", methods=['GET'])
def get_all_user() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@user_blueprints.route("/user/<int:id>", methods=['GET'])
def get_user_by_id(id_: int) -> dict:
    url = url_base + f'/by_id{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@user_blueprints.route("/user/insert", methods=['POST'])
def insert_user() -> dict:
    user = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=user)
    return response.json()


@user_blueprints.route("/user/update/<int:id_>", methods=['PUT'])
def update_user(id_: int) -> dict:
    user = request.get_json()
    url = url_base + f'/update{id_}'
    response = requests.patch(url, headers=HEADERS, json=user)
    return response.json()


@user_blueprints.route("/user/delete/<int:id_>", methods=['DELETE'])
def delete_user(id_: int) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()
