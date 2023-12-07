import pika
import uproot # for reading .root files
import awkward as ak # to represent nested data in columnar format
import vector # for 4-momentum calculations
#import time # to measure time to analyse
#import math # for mathematical functions such as square root
import numpy as np # for numerical calculations such as histogramming
import matplotlib.pyplot as plt # for plotting
from matplotlib.ticker import AutoMinorLocator # for minor ticks

import infofile # local file containing cross-sections, sums of weights, dataset IDs

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# queue initiated
channel.queue_declare(queue='to_workers')

#lumi = 0.5 # fb-1 # data_A only
#lumi = 1.9 # fb-1 # data_B only
#lumi = 2.9 # fb-1 # data_C only
lumi = 4.7 # fb-1 # data_D only
#lumi = 10 # fb-1 # data_A,data_B,data_C,data_D

fraction = 0.1 # reduce this is if you want the code to run quicker
                                                                                                                                  
#tuple_path = "Input/4lep/" # local 
tuple_path = "https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/4lep/" # web address

samples = {

    'data': {
        'list' : ['data_A','data_B','data_C','data_D'],
    },

    r'Background $Z,t\bar{t}$' : { # Z + ttbar
        'list' : ['Zee','Zmumu','ttbar_lep'],
        'color' : "#6b59d3" # purple
    },

    r'Background $ZZ^*$' : { # ZZ
        'list' : ['llll'],
        'color' : "#ff0000" # red
    },

    r'Signal ($m_H$ = 125 GeV)' : { # H -> ZZ -> llll
        'list' : ['ggH125_ZZ4lep','VBFH125_ZZ4lep','WH125_ZZ4lep','ZH125_ZZ4lep'],
        'color' : "#00cdff" # light blue
    },

}


# get a file path from samples
# pass it into the queue

num_sent = 0
for s in samples: # loop over samples
    print('Processing '+s+' samples') # print which sample
    frames = [] # define empty list to hold data
    for val in samples[s]['list']: # loop over each file
        if s == 'data': prefix = "Data/" # Data prefix
        else: # MC prefix
            prefix = "MC/mc_"+str(infofile.infos[val]["DSID"])+"."

        fileString = tuple_path+prefix+val+".4lep.root" # file name to open
        # put item into the queue
        # Send a message to the queue
        channel.basic_publish(exchange='', routing_key='to_workers', body=[fileString,s,val])
        num_sent += 1
        print(" [x] Sent the fileString")

# send the total number os URLs sent to the to_workers queue
channel2 = connection.channel()

# queue initiated
channel2.queue_declare(queue='assert')

channel2.basic_publish(exchange='', routing_key='assert', body=num_sent)


