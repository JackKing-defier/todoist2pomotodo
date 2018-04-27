def add_todo_from_todoist(tasks,token):
    import requests
    from requests.auth import HTTPBasicAuth
    # requests.get('https://api.pomotodo.com/1/todos', auth=HTTPBasicAuth('yjunjie@csu.edu.cn',token))
    for task in tasks:
        response = requests.post('https://api.pomotodo.com/1/todos',json=task,auth=HTTPBasicAuth('yjunjie@csu.edu.cn',token),headers={"Content-Type": "application/json"})
        print(response.status_code)