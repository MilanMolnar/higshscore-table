from flask import Flask, request, jsonify
import json
import csv  

app = Flask(__name__)

def save(list):
    data = ""
    for k,v in list.items():
        data += v + ","
    data_res = data[:-1]
    print(data_res)
    f = open("save.csv", "a")
    f.write(data_res + "\n")
    f.close()
    return None

def load():
    with open("save.csv", "r") as f:
        reader = csv.DictReader(f)
        a = list(reader)
    print(a)
    return a
     

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
            save(content)
        return "None"
    if request.method == "GET":
        return format_view(load())


if __name__ == "__main__":
    app.run(port=4996)