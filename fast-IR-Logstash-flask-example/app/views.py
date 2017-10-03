from flask.ext.elasticsearch import FlaskElasticsearch


from app import app
import os

import json

import pygal
es = FlaskElasticsearch(app)
@app.route('/')
def line_route():



    filename = os.path.join(app.instance_path, 'output.txt')
    with open(filename) as f:
        data = f.read()
    parsed = json.loads(data)
    parsed_new = parsed['hits']['hits']


    xy_chart = pygal.XY(stroke=False)
    xy_chart.title = 'Graph of Runtime vs date'

    timeline = []

    for i in range(344):


        MODIFICATION_TIME = parsed_new[i]['_source']['MODIFICATION_TIME'].encode('utf-8')
        EXEC_NAME = parsed_new[i]['_source']['EXEC_NAME'].encode('utf-8')
        RUN_COUNT = parsed_new[i]['_source']['RUN_COUNT'].encode('utf-8')

        if RUN_COUNT != "RUN_COUNT":
            RUN_COUNT_int = int(RUN_COUNT)
            timeline.append(MODIFICATION_TIME)
            xy_chart.add(EXEC_NAME,[(i,RUN_COUNT_int)])
        else:
            continue


    xy_chart.x_labels = timeline
    return xy_chart.render()
