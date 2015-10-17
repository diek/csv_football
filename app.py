# -*- coding: utf-8 -*-
from flask import Flask
import os

app = Flask(__name__)

# data from Think Like a Computer Scientist
csv_file = os.path.join(os.path.dirname(__file__), 'football.csv')

page = 'The following QB has a rating higher than 90.0 \n'

with open(csv_file, 'r') as qb:
    for aline in qb:
        values = aline.split()
        if float(values[10]) > 90.0:
            read_data = values[0] + ' ' + values[1] + \
                ' rating: ' + values[10]
            page += '<p>%s</p>' % read_data


@app.route("/")
def index():
    return page


if __name__ == "__main__":
    app.run(debug=True)
