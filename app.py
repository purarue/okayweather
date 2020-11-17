import os
import time

import requests
from flask import Flask, render_template

this_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(this_dir, "templates")

app = Flask(__name__, template_folder=templates_dir)

with open(os.path.join(this_dir, "api_key.txt"), "r") as api_f:
    API_KEY: str = api_f.read().strip()
santa_cruz_id: int = 5393052
SLEEP_TIME = 4


def get_weather(for_location: int = santa_cruz_id):
    resp = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?id={for_location}&appid={API_KEY}"
    )
    resp.raise_for_status()
    return resp.json()


weather_data = get_weather()


@app.route("/")
def main():
    return render_template("choices.html")


@app.route("/server_side_rendered")
def server_rendered():
    time.sleep(SLEEP_TIME)  # simulate backend API request
    return render_template("server.html", weather_data=weather_data)


@app.route("/dynamic")
def dynamic():
    return render_template("dynamic.html")


@app.route("/api")
def api():
    time.sleep(SLEEP_TIME)  # simulate dynamic
    return weather_data


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
