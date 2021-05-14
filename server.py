from flask import Flask, request, jsonify
import json

app = Flask(__name__)

list_of_scores = []

def format_view(list):
    view = ""
    laps = sorted(list, key = lambda i: i['finish_time_raw'])
    for lap in laps:
        view +="| Driver: " + lap["driver_name"] + " | Lap Time: " + lap["finish_time"] + " | Map: " + lap["map_name"] + " |<br>"
    return view

@app.route("/highscores", methods=["GET", "POST", "PUT"])
def highscores():
    if request.method == "POST":
        req_data = request.data
        if req_data != None:
            content = json.loads(req_data.decode("utf-8").replace("'",'"'))
            list_of_scores.append(content)
    if len(list_of_scores) > 0:
        list_view = format_view(list_of_scores)
    else:
        list_view = "no record yet :c"
    return list_view


if __name__ == "__main__":
    app.run(port=4996)