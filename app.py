from flask import Flask, render_template
from data_scrap import get_extracted_data

app = Flask(__name__)


@app.route("/")
def home():
    extracted_table_data = get_extracted_data()
    return render_template("index.html", table_data=extracted_table_data)


if __name__ == '__main__':
    app.run('0.0.0.0', 8085)
