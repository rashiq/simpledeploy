import os
import json
import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hook():
  if not check_signature(request): abort(403)
  repository = request.get_json()['repository']['name']
  execute_steps(repository)
  return ('', 204)

def check_signature(request):
  token = os.environ['GITHUB_TOKEN']
  digest = 'sha1=' + hashlib.sha1(token).hexdigest()
  signature = request.headers.get('X-Hub-Signature')
  return digest == signature

def execute_steps(repository):
  with open('config.json', 'r') as f:
    config = json.loads(f.read())
  match = filter(lambda x: x['repository'] == repository, config)
  if not match: return
  steps = ' && '.join(match[0]['steps'])
  os.system(steps)

if __name__ == '__main__':
  app.run(debug=True)

