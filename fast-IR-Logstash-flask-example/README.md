This project is to integrate FastIR, logstash, Elasticsearch, Python/Flask and PyGal to create visualisations for Security analytics purposes.

go to https://github.com/SekoiaLab/Fastir_Collector and follow their instructions. Would end up with a directory of .csv files and .evtx files which are 
Windows Artefacts that could be analysed. 

These artefacts are then imported to elasticsearch through logstash, following the guidelines on https://github.com/elastic/logstash

A python/Flask backend is created and instantiates the elasticsearch object, retrieving JSON files which is parsed to get the data required.

The data is imported to Pygal in order to create a visualisation.

 