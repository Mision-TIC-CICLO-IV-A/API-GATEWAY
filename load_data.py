import requests

security_backend = "http://localhost:8080"
headers = {"Content-Type": "application/json; charset=utf-8"}

# Creación de roles
roles = [
    {"name": "Administrador", "description": "Administrador del sistema de votaciones"},
    {"name": "Candidato", "description": "Centro democrático"},
    {"name": "Partido", "description": "Ideología de derecha"}
]
url = f'{security_backend}/rol/insert'
admin = None
for rol in roles:
    response = requests.post(url, headers=headers, json=rol)
    if rol.get('name') == 'Administrador':
        admin = response.json()
    print(response.json())
print("="*30)

# Permisos básicos relacionados a admin
modules = ['tables', 'matter', 'departament', 'enrollment', 'user', 'rol']
endpoints = [('s', 'GET'), ('/?', 'GET'), ('/insert', 'POST'), ('/update/?', 'PUT'), ('/delete/?', 'DELETE')]
url = f'{security_backend}/permission/insert'
for module in modules:
    for endpoint, method in endpoints:
        permission_url = f'{module} {endpoint}'
        body = {
            "url": permission_url,
            "method": method
        }
        response = requests.post(url, headers=headers, json=body)
        print(response.json())
        permission = response.json()
        url_relation = f'{security_backend}/rol/update{admin.get("idRol")}/add_permission/{permission.get("id")}'
        response = requests.put(url_relation, headers=headers)
