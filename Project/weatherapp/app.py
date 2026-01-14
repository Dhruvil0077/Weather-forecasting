from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "ffae8c6bca87b8198905d2086a7db4f3"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None

    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        print(data)

        if str(data.get("cod")) == "200":
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }
        else:
            weather = {"error": "City not found"}

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
