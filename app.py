import json
import hashlib
from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['POST'])
def hook():
  if not check_signature(): abort(403)
  repository = request.get_json()['repository']['name']
  return ('', 204)


def check_signature(request):
  token = os.environ['GITHUB_TOKEN']
  digest = 'sha1=' + hashlib.sha1(token).hexdigest()
  signature request.headers.get('X-Hub-Signature')
  return digest == signature


if __name__ == '__main__':
  app.run(debug=True)
