from flask import Flask, render_template
from data_scrap import get_extracted_data
from json_data_manimulation import get_json_data

app = Flask(__name__)


@app.route("/")
def home():
    extracted_table_data = get_extracted_data()
    return render_template("index.html", table_data=extracted_table_data)


@app.route("/corona-live")
def getDataFromCoronaLive():
    data = get_json_data()
    return render_template("corona_live.html", json_data=data)


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
