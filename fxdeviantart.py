from flask import Flask, render_template
from urllib.parse import quote
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route('/<path:subpath>')
def fxdeviantart(subpath):
    origin = ("https://deviantart.com/" + subpath)
    data = json.load(urlopen(("https://backend.deviantart.com/oembed?url=" + str(quote(origin)))))

    return render_template('index.html', img=data['url'], url=origin, desc=data['title'])

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=666)