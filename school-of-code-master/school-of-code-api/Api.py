import json
import os

from flask import Flask, request

app = Flask(__name__)

posts = {}


@app.route("/blog-post/<name>")
def hello(name):
    return json.dumps(posts[name])


@app.route("/blog-post/all-names")
def all_posts():
    return json.dumps(list(posts.keys()))


@app.route("/blog-post/<name>", methods=['POST'])
def put_post(name):
    posts[name] = str(request.form['post'])
    return "a-ok"


@app.route('/internal/status')
def internal_status():
    return 'OK'


@app.route('/internal/config')
def internal_config():
    return json.dumps({"env": dict(os.environ)})


@app.route('/internal/version')
def internal_version():
    return json.dumps({"version": os.environ.get("BUILD_VERSION", "local"),
                "revision": os.environ.get("GIT_REVISION", "unknown")})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv('PORT', '5000')))