#create a web server, redner_templates load the HTML  files
from flask import Flask, render_template, request

#to send the http request to ecternal websites(weather API)
import requests

app = Flask(__name__)

API_KEY = "ffae8c6bca87b8198905d2086a7db4f3"

#GET: lading the page and POST: submitting the city name
@app.route("/", methods=["GET", "POST"])
def index():
    weather = None

    #check if the user clicked the "GET weather" button
    if request.method == "POST":
        city = request.form["city"]

        #Builds the specific web address to ask the API for weather in that city, using metric units (Celsius).
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        print(data)

        #if code 200 means everthing is OK and can porceed further
        if str(data.get("cod")) == "200":

            #putting the data into python dictonary for clean format
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }
        else:
            weather = {"error": "City not found"}

    #send the weather data back to HTMl files to be displayed
    return render_template("index.html", weather=weather)


#Starts the server. debug=True makes it restart automatically if you change the code
if __name__ == "__main__":
    app.run(debug=True)

