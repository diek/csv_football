# -*- coding: utf-8 -*-
from flask import Flask
# import os

app = Flask(__name__)

# data from Think Like a Computer Scientist
# csv_file = os.path.join(os.path.dirname(__file__), 'football.csv')
# modified python anywhere
csv_file = '/home/diek/mysite/football.csv'
page = '<h2>Data from "Think Like a Computer Scientist"</h2>'
page += '<h2>The following Quarter Backs have a rating higher than 90.0</h2>'

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
