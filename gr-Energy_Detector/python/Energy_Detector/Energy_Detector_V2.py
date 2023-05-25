#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 gr-Energy_Detector author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import scipy
import scipy.special as scs
import numpy
from gnuradio import gr
import pmt

class Energy_Detector_V2(gr.decim_block):
    """
    docstring for block Energy_Detector_V2
    """
    def __init__(self, samples, Pfa):
        self.samples = samples
        gr.decim_block.__init__(self,
            name="Energy_Detector_V2",
            in_sig=[numpy.float32, numpy.float32],
            out_sig=[numpy.float32], decim = self.samples)
        self.Pfa = Pfa
        self.message_port_register_out(pmt.intern("ED_out"))


    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]
        
        # <+signal processing here+>
        Avg = scipy.mean(in0)
        signalAvg = round(Avg,8)
        NoisePower = in1**2
        NoiseAvg = scipy.mean(NoisePower)
        var = scipy.var(NoisePower)
        stdev = scipy.sqrt(var)
        Qinv = scipy.sqrt(2) * scs.erfinv(1 - 2*self.Pfa)
        Threshold = round((NoiseAvg + Qinv*stdev) ,8)
        
        if signalAvg > Threshold:
        	out[:] = signalAvg
        	print("signal is present", signalAvg)
        	detection = 1
        	
        else:
            out[:] = Threshold
            detection = 0

            print("signal is absent", signalAvg)

        msg = pmt.make_tuple(pmt.from_double(signalAvg), pmt.from_double(detection))
        self.message_port_pub(pmt.intern("ED_out"), msg)

        return len(output_items[0])
