#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 gr-Drone_ML author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


# Libraries
import numpy as np
import pandas as pd
import pickle
import random
import re

## Models
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB

## Model evaluators
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics

# using binary relevance
from sklearn.naive_bayes import GaussianNB

from sklearn.model_selection import KFold


import warnings
warnings.simplefilter('ignore')


from gnuradio import gr
import pmt

class ml_testing(gr.sync_block):
    """
    docstring for block ml_testing
    """
    def __init__(self, fname = ''):
        gr.sync_block.__init__(self,
            name="ML Testing",
            in_sig=None,
            out_sig=None)
            
        self.file = fname
        
        #print("name is: ", self.file)
            
        self.sub_space = ''
        self.sym_time = ''
        self.subcarriers = ''
        self.cp_len = ''
        self.sig_avg = ''
        self.thresh = ''
        
        #self.data_row = ()
        
        self.selectPortName = 'ofdm_in'
        self.message_port_register_in(pmt.intern(self.selectPortName))
        self.set_msg_handler(pmt.intern(self.selectPortName), self.handle_msg)
        
        # create ml frame/hold data
        
        

            
    def handle_msg(self, msg):
    
        #print(type(pmt.tuple_ref(msg, 0)))
        
        # ml frame/data = ""
        
        # push data below to frame
    
        self.sub_space = str(pmt.tuple_ref(pmt.tuple_ref(msg, 0), 1))
        self.sym_time = str(pmt.tuple_ref(pmt.tuple_ref(msg, 1), 1))
        self.subcarriers = str(pmt.tuple_ref(pmt.tuple_ref(msg, 2), 1))
        self.cp_len = str(pmt.tuple_ref(pmt.tuple_ref(msg, 3), 1))
        self.sig_avg = str(pmt.tuple_ref(pmt.tuple_ref(msg, 4), 1))
        self.thresh = str(pmt.tuple_ref(pmt.tuple_ref(msg, 5), 1))
        

        
        #self.data_row = msg
        
        #print("row starts here")
        
        #print(self.sub_space)
        #print(self.sig_avg)
        
        #print(self.data_row)
        
        #print("row ends here")
        
        # ml magic happens here
        
        # loading model and dataframe
        loaded_model = pickle.load(open(self.file, 'rb'))
        df = pd.DataFrame(columns=['Subc Space', 'Sym time', 'Subcarriers', 'CP len', 'Signal Average', 'Threshold'])
        
        #loading the variables into the dataframe
        df.loc[0] = [self.sub_space] + [self.sym_time] + [self.subcarriers] + [self.cp_len] + [self.sig_avg] + [self.thresh]
        
        #model prediction
        pred = loaded_model.predict(df)
        
        print(pred)
        

    def work(self, input_items, output_items):
        in0 = input_items[0]
        # <+signal processing here+>'
        return len(input_items[0])
