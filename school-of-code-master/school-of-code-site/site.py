import json
import os
import requests
from flask import Flask

app = Flask(__name__)

posts = {}


@app.route("/")
def hello():
    posts = requests.get("http://school-of-code-api.live.cf.private.springer.com/blog-post/all-names").json()
    urls = ["<a href='/blog/{0}'>{0}</a>".format(name) for name in posts]
    return json.dumps(urls)

@app.route("/blog/<post_name>")
def blog_post(post_name):
    post = requests.get("http://school-of-code-api.live.cf.private.springer.com/blog-post/%s" % post_name).json()
    return json.dumps(post)

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
