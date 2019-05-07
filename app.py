from flask import Flask, request, render_template, jsonify

import pymysql
import numpy as np
from config import MYSQLPASS

db = pymysql.connect("localhost", "root", MYSQLPASS, "lottery")

app = Flask(__name__)
#api = Api(app)

@app.route('/')
def someName():
    cursor = db.cursor()
    sql = "SELECT WinningDate, Winner, JackpotPrize FROM winners"
    cursor.execute(sql)
    results = cursor.fetchall()

    all_winners = list(np.ravel(results))
    return jsonify(all_winners)
    #return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)