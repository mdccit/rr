import requests

url = "http://127.0.0.1:5000/get-repo-info"
data = {"repo_name": "octocat/Hello-World"}

response = requests.post(url, json=data)
print(response.json())
