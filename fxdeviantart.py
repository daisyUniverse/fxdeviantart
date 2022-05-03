from flask import Flask, render_template
from configparser import ConfigParser
from urllib.parse import quote
from urllib.request import urlopen
import json

# Initialise Flask
app = Flask(__name__)

# Initialise ConfigParser and make it read the config file
config = ConfigParser()
config.read("config.ini")

# Main Function
@app.route("/<path:subpath>")
def fxdeviantart(subpath):
    # Original link to submission, to be used for the `url` parameter in the template
    origin = "https://deviantart.com/" + subpath

    # Get the submission's JSON data
    data = json.load(
        urlopen(("https://backend.deviantart.com/oembed?url=" + str(quote(origin))))
    )

    # Return the template with the data
    return render_template(
        "index.html",
        user=data["author_name"],
        img=data["url"],
        url=origin,
        desc=data["title"],
        site_name=config.get("site_config", "site_name"),
        colour="#" + config.get("site_config", "colour"),
    )

# Debugging stuff here
if __name__ == "__main__":
    app.run(debug=config.getboolean("debug_config", "debug"))
    app.run(
        host=config.get("debug_config", "host"),
        port=config.getint("debug_config", "port"),
    )