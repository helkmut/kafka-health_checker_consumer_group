import time as pytime
import configparser, os

#
# open config files
#

absolutepath = "/etc/attributesmonitoring.conf"
config = configparser.ConfigParser()
config.readfp(open(absolutepath))
config.read('attributes_monitoring.conf')

#
# components monitoring list
#
def getComponentsList():
    complist = []        
    complistattr = config.get('component_list', 'comp_keys').split()
    for comp in complistattr:
        complist.append(comp)
    return complist

def getAddress():
    addressurl = config.get('actuator_healthaddress','address')
    return addressurl

def getCluster():
    addresscluster = config.get('actuator_healthcluster','cluster')
    return addresscluster

def getTimeout():
    addresstimeout = config.get('actuator_healthtimeout','timeout')
    return addresstimeout
