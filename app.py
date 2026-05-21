from flask import Flask, render_template
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

cities = [
    {"city": "London", "timezone": "Europe/London"},
    {"city": "New York", "timezone": "America/New_York"},
    {"city": "Tokyo", "timezone": "Asia/Tokyo"},
    {"city": "Dubai", "timezone": "Asia/Dubai"},
    {"city": "Sydney", "timezone": "Australia/Sydney"},
    {"city": "Toronto", "timezone": "America/Toronto"},
    {"city": "Paris", "timezone": "Europe/Paris"},
    {"city": "Lagos", "timezone": "Africa/Lagos"}
]

@app.route("/")
def home():
    world_times = []

    for item in cities:
        current_time = datetime.now(ZoneInfo(item["timezone"]))
        world_times.append({
            "city": item["city"],
            "time": current_time.strftime("%H:%M:%S"),
            "date": current_time.strftime("%A, %d %B %Y")
        })

    return render_template("index.html", world_times=world_times)

if __name__ == "__main__":
    app.run(debug=True)