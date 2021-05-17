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

def save_drift(list):
    data = ""
    for k,v in list.items():
        data += v + ","
    data_res = data[:-1]
    print(data_res)
    f = open("save_drift.csv", "a")
    f.write(data_res + "\n")
    f.close()
    return None

def load_drift():
    with open("save_drift.csv", "r") as f:
        reader = csv.DictReader(f)
        a = list(reader)
    print(a)
    return a


@app.route("/", methods=["GET"])     
def index():
    return "<div> \
        <a href='http://127.0.0.1:4000/highscores' style='display:block; margin:20px; width: 115px;height:25px; background: lightcoral; padding: 10px; text-align: center; border-radius: 5px; color: white; font-weight: bold; line-height:25px; border: 1px solid black'>Dawn Sprint</a> \
        <a href='http://127.0.0.1:4000/highscores_drift' style='margin: 20px; display:block; width: 115px;height:25px; background: lightblue; padding: 10px; text-align: center; border-radius: 5px; color: white; font-weight: bold; line-height:25px; border: 1px solid black'>Drift</a> \
    </div>"



def format_view(list):
    view = ""
    list_top = "<h1 style='font: size 20;text-align:center; font-family: Arial;'>Highscores</h1>"+"<ul>"
    #view +="| Driver: " + lap["driver_name"] + " | Lap Time: " + lap["finish_time"] + " | Map: " + lap["map_name"] + " |<br>"
    list.sort(key=lambda item: float(item.get("finish_time_raw")))
    #laps = sorted(list, key = lambda i: i('finish_time_raw'))
    for lap in list:
        if str(list.index(lap) + 1) != "1":
            view += "<li style='text-align: center; list-style-type: none;margin-left: calc(50% - 230px);'>" \
                        "<div style='background-color:lightblue;width: 400px; height: 60px; border-radius:6px; border: 1px solid black; margin-top: 20px'>" \
                            "<div style=' background-color:lightblue; margin-top: 18px; margin-left:15px;  float:left;font-size:20;font-family: Arial'>" + str(list.index(lap) + 1) + ". "  + lap["driver_name"] + "</div>" \
                            "<div style=' background-color:lightcoral ;margin-top: 18px;margin-right: 15px; float:right ;font-size:20;font-family: Arial;'>" + lap["finish_time"] + "</div>" \
                        "</div>" \
                    "</li>"
        else:
            view += "<li style='text-align: center; list-style-type: none;margin-left: calc(50% - 230px);'>" \
                        "<div style='background-color:lightcoral;width: 400px; height: 60px; border-radius:6px; border: 1px solid black; margin-top: 20px'>" \
                            "<div style=' background-color:lightblue; margin-top: 18px; margin-left:15px;  float:left;font-size:20;font-family: Arial'>" + str(list.index(lap) + 1) + ". "  + lap["driver_name"] + "</div>" \
                            "<div style=' background-color:lightcoral ;margin-top: 18px;margin-right: 15px; float:right ;font-size:20;font-family: Arial;'>" + lap["finish_time"] + "</div>" \
                        "</div>" \
                    "</li>"

    list_bot = "</ul>"
    return list_top + view + list_bot

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


@app.route("/highscores_drift", methods=["GET", "POST", "PUT"])
def highscores_drift():
    if request.method == "POST":
        req_data = request.data
        if req_data != None:
            content = json.loads(req_data.decode("utf-8").replace("'",'"'))
            save_drift(content)
        return "None"
    if request.method == "GET":
        return format_view(load_drift())


if __name__ == "__main__":
    app.run(port=4000)