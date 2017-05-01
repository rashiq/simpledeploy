from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hook():
  return json.dumps(request.form)


if __name__ == '__main__':
  app.run(debug=True)
