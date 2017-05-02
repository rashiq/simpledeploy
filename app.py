import os
import hmac
import json
import hashlib
from flask import Flask, request, abort
from utils import compare_digest

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hook():
  if not check_signature(request): abort(403)
  repository = request.get_json()['repository']['name']
  execute_steps(repository)
  return ('', 204)

def check_signature(request):
  secret = os.environ.get('GITHUB_SECRET', '')
  signature = request.headers.get('X-Hub-Signature')
  if not signature: return False
  mac = hmac.new(secret, request.data, hashlib.sha1).hexdigest()
  return compare_digest("sha1=" + mac, str(signature))

def execute_steps(repository):
  with open('config.json', 'r') as f:
    config = json.loads(f.read())
  match = filter(lambda x: x['repository'] == repository, config)
  if not match: return
  steps = ' && '.join(match[0]['steps'])
  os.system(steps)

if __name__ == '__main__':
  app.run(debug=True)

