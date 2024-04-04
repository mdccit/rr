from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get-repo-info', methods=['POST'])
def get_repo_info():
    data = request.json
    repo_name = data['repo_name']
    url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Repository not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
