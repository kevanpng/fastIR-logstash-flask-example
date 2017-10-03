from flask.ext.elasticsearch import FlaskElasticsearch


from app import app
import os

import json

import pygal
#instantiate the elasticsearch object
es = FlaskElasticsearch(app)
@app.route('/')
def line_route():


#import the cleaned Prefetch file in JSON format
    filename = os.path.join(app.instance_path, 'output.txt')
    with open(filename) as f:
        data = f.read()
    parsed = json.loads(data)
	#parse the JSON file to get to the layer we want
    parsed_new = parsed['hits']['hits']

	#instantiate xy_chart 
    xy_chart = pygal.XY(stroke=False)
    xy_chart.title = 'Graph of Runtime vs date'

		
	#instantiate empty timeline list to populate later	
    timeline = []

	# 344 is the number of records in the prefetch file. 
	#we want to get the modification time, executable name and its run count for each record and plot it on the graph
    for i in range(344):

		#requires encoding as the variables are in unicode format
        MODIFICATION_TIME = parsed_new[i]['_source']['MODIFICATION_TIME'].encode('utf-8')
        EXEC_NAME = parsed_new[i]['_source']['EXEC_NAME'].encode('utf-8')
        RUN_COUNT = parsed_new[i]['_source']['RUN_COUNT'].encode('utf-8')
		
		#there is a record named RUN_COUNT which is throwing errors. Need to bypass it. 
        if RUN_COUNT != "RUN_COUNT":
            RUN_COUNT_int = int(RUN_COUNT)
            timeline.append(MODIFICATION_TIME)
			#adds objects to the chart
            xy_chart.add(EXEC_NAME,[(i,RUN_COUNT_int)])
        else:
            continue

	#labels for the chart
    xy_chart.x_labels = timeline
    return xy_chart.render()
