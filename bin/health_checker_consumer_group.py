#!/usr/bin/env python
# Author : Gabriel Prestes (gabriel.prestes@ilegra.com)
# Modified : 11/07/2017 (created)
#            13/07/2017 (v01 - finished)
# Version : 0.1
# Workflow : 
# 
# 1 -> Get allproperties (cluster, timeout, url, objects_statuslist) ;
# 2 -> Get consumergrouplist ;
# 3 -> Foreach array consumergrouplist call getStatus and getLag and populate hashResults;
# 4 -> In function showMetricList print metric results.
#
# Wishlist: 
#
# 1 -> Timeout agent; 
# 2 -> Timestamp per URLrequest;
# 3 -> Refactor code. 

# --- Libraries --- #

from collections import defaultdict
import health_checker_config_parser as configparser
import sys
import requests
import socket

metricsList = defaultdict(lambda :defaultdict())

def main(argv):
    
    cluster = configparser.getCluster()
    timeout = configparser.getTimeout()
    url = configparser.getAddress()

    if len(sys.argv) > 1:
       
         debug = sys.argv[1]
  
    else:
    
         debug = "0"

    if debug == "1":
       print("--- Init debug mode ---")
       print("Cluster: " + cluster + " Timeout : " + timeout + " " + url + " Debug level : " + debug)
       print("---")
    pass

    requestURL = url+"/v2/kafka/"+cluster+"/consumer/"

    if debug == "1":
       print("Request URL to get consumer groups : " + requestURL)
       print("---")
     
    resultURL = requests.get(requestURL)
    responseStruct = resultURL.json() 

    ListOfConsumers = responseStruct['consumers']

    if debug == "1":
       print("Total consumer groups : ")
       for p in ListOfConsumers: print(p)
       print("---")

    for group in ListOfConsumers: getResults(cluster, requestURL, group, debug)

    showMetricList(cluster, debug)

    exit()


def getResults(cluster, requestURL, group, debug):

    componentList  = configparser.getComponentsList()
    URL1 = requestURL + group + "/status"

    if debug == "1":
       print("Request URL to get attributes : " + URL1)
       print("Component list : ")
       for p in componentList: print(p)
       print("---")

    resultURL = requests.get(URL1)
    responseStruct = resultURL.json()
    results = responseStruct['status']

    if debug == "1":
       print("Component to check : ")
       for p in results: print(p)
       print("---")

    for i, component in enumerate(componentList): 
	
         for n, metric in enumerate(results):
		
             if metric in component:
		 
                 value = results[metric] 

                 if debug == "1": 
                       
                       print("Value '" + str(value) + "' Metric '" + metric + "' of " + group)
                       print("---")

                 setMetrics(cluster, group, metric, value, debug) 

def setMetrics(cluster, group, metric, value, debug):

        metricsList[group][metric] = value

        if debug == "1":

           print("Cluster: "+ cluster + " Groupconsumer: " + group + " Metric: " + metric + " Value: " + str(value))
           print("Value to import in dictionary is : ")
           print(metricsList[group][metric])
           print("---")

def showMetricList(cluster, debug):

    output = []
    jtemplist = []
    

    for i in metricsList: 

           jtemplist = []

           for j in metricsList[i]:

                if j == "status":

                     if metricsList[i][j] == "OK": 
                     
                          metricsList[i][j] = "1"
                 
                     else:
                     
                          metricsList[i][j] = "0" 
 
                jtemp = j + "=" + str(metricsList[i][j])
                jtemplist.append(jtemp)

                if debug == "1":
 
                       print (cluster, i, j, metricsList[i][j])
                       print("---")

           totalmetrics = ','.join(jtemplist)
           temp = "burrow_metrics,cluster=" + cluster + ",consumergroup=" + i + " " + totalmetrics
           output.append(temp)

    pass

    alloutput = '\n'.join(output)
    print(alloutput)

if __name__ == "__main__":

    main(sys.argv)

