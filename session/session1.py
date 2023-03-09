#!/usr/bin/env python
     # BCI Data collection
import os
import ctypes
import sys
from ctypes import *
from numpy import *
import numpy as np
import time
from scipy import signal
from time import gmtime, strftime
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from ctypes.util import find_library
print (ctypes.util.find_library('edk.dll'))
print (os.path.exists('edk.dll'))
libEDK = ctypes.CDLL("edk.dll",'ascii')
print(libEDK)
import xlwt
import shutil
import csv
import pandas as pd
#import MySQLdb
#import firebase
import time
import datetime
#firebase = firebase.FirebaseApplication("https://pythontojs-b1623.firebaseio.com/",None)

class CollectData:
    def __init__(self):  
        
        self.exit = 0
        self.ED_COUNTER = 0
        self.ED_INTERPOLATED=1
        self.ED_RAW_CQ=2
        self.ED_AF3=3
        self.ED_F7=4
        self.ED_F3=5
        self.ED_FC5=6
        self.ED_T7=7
        self.ED_P7=8
        self.ED_O1=9
        self.ED_O2=10
        self.ED_P8=11
        self.ED_T8=12
        self.ED_FC6=13
        self.ED_F4=14
        self.ED_F8=15
        self.ED_AF4=16
        self.ED_GYROX=17
        self.ED_GYROY=18
        self.ED_TIMESTAMP=19
        self.ED_ES_TIMESTAMP=20
        self.ED_FUNC_ID=21
        self.ED_FUNC_VALUE=22
        self.ED_MARKER=23
        self.ED_SYNC_SIGNAL=24

        self.targetChannelList = [self.ED_RAW_CQ,self.ED_AF3, self.ED_F7, self.ED_F3, self.ED_FC5, self.ED_T7,self.ED_P7, self.ED_O1, self.ED_O2, self.ED_P8, self.ED_T8,self.ED_FC6, self.ED_F4, self.ED_F8, self.ED_AF4, self.ED_GYROX, self.ED_GYROY, self.ED_TIMESTAMP, self.ED_FUNC_ID, self.ED_FUNC_VALUE, self.ED_MARKER, self.ED_SYNC_SIGNAL]
        self.eEvent      = libEDK.EE_EmoEngineEventCreate()
        self.eState      = libEDK.EE_EmoStateCreate()
        self.userID            = ctypes.c_uint(0)
        self.nSamples   = ctypes.c_uint(0)
        self.nSam       = ctypes.c_uint(0)
        self.nSamplesTaken  = ctypes.pointer(self.nSamples)
        self.data     = ctypes.pointer(ctypes.c_double(0))
        self.user     = ctypes.pointer(self.userID)
        self.composerPort          = ctypes.c_uint(1726)
        self.secs      = ctypes.c_float(1)
        self.datarate    = ctypes.c_uint(0)
        self.readytocollect    = False
        self.option      = ctypes.c_int(0)
        self.state     = ctypes.c_int(0) 

        print (libEDK.EE_EngineConnect("Emotiv Systems-5"))
        #if libEDK.EE_EngineConnect("Emotiv Systems-5") != 0:
        #print ("Emotiv Engine start up failed.")

        print ("Start receiving EEG Data! Press any key to stop logging...\n")

        self.hData = libEDK.EE_DataCreate()
        libEDK.EE_DataSetBufferSizeInSec(self.secs)

        print ("Buffer size in secs:")

        

    
    def data_acq(self):
        
        self.feature_names=['delta_m', 'theta_m','alpha_m','smr_m','beta_m','highbeta_m','gamma_m']
        self.column_names=['Bands','Time','Channel_1','Channel_2','Channel_3','Channel_4','Channel_5','Channel_6',
                           'Channel_7','Channel_8','Channel_9','Channel_10','Channel_11','Channel_12','Channel_13','Channel_14'] 
        store_action_Features=pd.DataFrame(columns= self.column_names)
        j=1
        q=1
        delta_overall_mean1 = [];delta_overall_mean2 = [];delta_overall_mean3 = [];delta_overall_mean4 = [];delta_overall_mean5 = [];delta_overall_mean6 = [];delta_overall_mean7 = [];
        delta_overall_mean8 = [];delta_overall_mean9 = [];delta_overall_mean10 = [];delta_overall_mean11 = [];delta_overall_mean12 = [];delta_overall_mean13 = [];delta_overall_mean14 = [];
        theta_overall_mean1 = [];theta_overall_mean2 = [];theta_overall_mean3 = [];theta_overall_mean4 = [];theta_overall_mean5 = [];theta_overall_mean6 = [];theta_overall_mean7 = [];
        theta_overall_mean8 = [];theta_overall_mean9 = [];theta_overall_mean10 = [];theta_overall_mean11 = [];theta_overall_mean12 = [];theta_overall_mean13 = [];theta_overall_mean14 = [];
        alpha_overall_mean1 = [];alpha_overall_mean2 = [];alpha_overall_mean3 = [];alpha_overall_mean4 = [];alpha_overall_mean5 = [];alpha_overall_mean6 = [];alpha_overall_mean7 = [];
        alpha_overall_mean8 = [];alpha_overall_mean9 = [];alpha_overall_mean10 = [];alpha_overall_mean11 = [];alpha_overall_mean12 = [];alpha_overall_mean13 = [];alpha_overall_mean14 = [];
        beta_overall_mean1 = [];beta_overall_mean2 = [];beta_overall_mean3 = [];beta_overall_mean4 = [];beta_overall_mean5 = [];beta_overall_mean6 = [];beta_overall_mean7 = [];
        beta_overall_mean8 = [];beta_overall_mean9 = [];beta_overall_mean10 = [];beta_overall_mean11 = [];beta_overall_mean12 = [];beta_overall_mean13 = [];beta_overall_mean14 = [];
        gamma_overall_mean1 = [];gamma_overall_mean2 = [];gamma_overall_mean3 = [];gamma_overall_mean4 = [];gamma_overall_mean5 = [];gamma_overall_mean6 = [];gamma_overall_mean7 = [];
        gamma_overall_mean8 = [];gamma_overall_mean9 = [];gamma_overall_mean10 = [];gamma_overall_mean11 = [];gamma_overall_mean12 = [];gamma_overall_mean13 = [];gamma_overall_mean14 = [];

        smr_overall_mean1 = [];smr_overall_mean2 = [];smr_overall_mean3 = [];smr_overall_mean4 = [];smr_overall_mean5 = [];smr_overall_mean6 = [];smr_overall_mean7 = [];
        smr_overall_mean8 = [];smr_overall_mean9 = [];smr_overall_mean10 = [];smr_overall_mean11 = [];smr_overall_mean12 = [];smr_overall_mean13 = [];smr_overall_mean14 = [];
        highbeta_overall_mean1 = [];highbeta_overall_mean2 = [];highbeta_overall_mean3 = [];highbeta_overall_mean4 = [];highbeta_overall_mean5 = [];highbeta_overall_mean6 = [];highbeta_overall_mean7 = [];
        highbeta_overall_mean8 = [];highbeta_overall_mean9 = [];highbeta_overall_mean10 = [];highbeta_overall_mean11 = [];highbeta_overall_mean12 = [];highbeta_overall_mean13 = [];highbeta_overall_mean14 = []
        self.column_number=['Channel 1','Channel 2','Channel 3','Channel 4','Channel 5','Channel 6','Channel 7','Channel 8','Channel 9','Channel 10','Channel 11','Channel 12','Channel 13','Channel 14'] 
        store_raw=pd.DataFrame(columns= self.column_number)
        
        
        for i in range(301):
                state = libEDK.EE_EngineGetNextEvent(self.eEvent)
                if state == 0:
                    eventType = libEDK.EE_EmoEngineEventGetType(self.eEvent)
                    libEDK.EE_EmoEngineEventGetUserId(self.eEvent, self.user)
                    if eventType == 16:
                        libEDK.EE_DataAcquisitionEnable(self.userID,True)
                        self.readytocollect = True
                
                if self.readytocollect==True:
                    libEDK.EE_DataUpdateHandle(0, self.hData)
                    libEDK.EE_DataGetNumberOfSample(self.hData,self.nSamplesTaken)
                    if self.nSamplesTaken[0] == 128:
                        self.nSam=self.nSamplesTaken[0]
                        arr=(ctypes.c_double*self.nSamplesTaken[0])()
                        ctypes.cast(arr, ctypes.POINTER(ctypes.c_double))                        
                        data = array('d')
                        y = np.zeros((128,14))
                        for sampleIdx in range(self.nSamplesTaken[0]):
                            x = np.zeros(14)
                            for i in range(1,15):
                                libEDK.EE_DataGet(self.hData,self.targetChannelList[i],byref(arr), self.nSam)
                                x[i-1] = arr[sampleIdx]
                                
                            y[sampleIdx] = x
                        
                        
                        y = np.transpose(y)
                        raw_dict={
                            
                            'Channel 1':y[0],
                            'Channel 2':y[1],
                            'Channel 3':y[2],
                            'Channel 4':y[3],
                            'Channel 5':y[4],
                            'Channel 6':y[5],
                            'Channel 7':y[6],
                            'Channel 8':y[7],
                            'Channel 9':y[8],
                            'Channel 10':y[9],
                            'Channel 11':y[10],
                            'Channel 12':y[11],
                            'Channel 13':y[12],
                            'Channel 14':y[13]
                            
                            }
            
                        df_raw=pd.DataFrame(raw_dict,columns= self.column_number )
                        store_raw=store_raw.append(df_raw)
                        q+=1
                        pwelch = signal.welch(y, 128, window="hanning", nperseg=128, noverlap= 64, nfft =128)
                        f=pwelch[1]
                        delta=map(lambda x: x[0:3],f) # from 1 to 4 Hz
                        theta=map(lambda x: x[3:7],f)# from 4 to 8 Hz
                        alpha=map(lambda x: x[7: 12],f) # from 8 to 13 Hz
                        smr=map(lambda x: x[12: 14],f) # from 13 to 15 Hz
                        beta=map(lambda x: x[14 : 19],f) # from 15 to 20 Hz
                        highbeta=map(lambda x: x[19 : 29],f) # from 20 to 30 Hz
                        gamma=map(lambda x: x[29:49],f) # from 30 to 50 Hz
                        print ("a")

                        
                        delta_m= np.mean(delta, axis=1)
                        theta_m= np.mean(theta, axis=1)
                        alpha_m= np.mean(alpha, axis=1)
                        smr_m= np.mean(smr, axis=1)
                        beta_m= np.mean(beta, axis=1)
                        highbeta_m= np.mean(highbeta,axis=1)
                        gamma_m= np.mean(gamma, axis=1)


                        theta_overall_mean1.append(theta_m[0])
                        theta_overall_mean2.append(theta_m[1])
                        theta_overall_mean3.append(theta_m[2])
                        theta_overall_mean4.append(theta_m[3])
                        theta_overall_mean5.append(theta_m[4])
                        theta_overall_mean6.append(theta_m[5])
                        theta_overall_mean7.append(theta_m[6])
                        theta_overall_mean8.append(theta_m[7])
                        theta_overall_mean9.append(theta_m[8])
                        theta_overall_mean10.append(theta_m[9])
                        theta_overall_mean11.append(theta_m[10])
                        theta_overall_mean12.append(theta_m[11])
                        theta_overall_mean13.append(theta_m[12])
                        theta_overall_mean14.append(theta_m[13])
                        
                                            
                        alpha_overall_mean1.append(alpha_m[0])
                        alpha_overall_mean2.append(alpha_m[1])
                        alpha_overall_mean3.append(alpha_m[2])
                        alpha_overall_mean4.append(alpha_m[3])
                        alpha_overall_mean5.append(alpha_m[4])
                        alpha_overall_mean6.append(alpha_m[5])
                        alpha_overall_mean7.append(alpha_m[6])
                        alpha_overall_mean8.append(alpha_m[7])
                        alpha_overall_mean9.append(alpha_m[8])
                        alpha_overall_mean10.append(alpha_m[9])
                        alpha_overall_mean11.append(alpha_m[10])
                        alpha_overall_mean12.append(alpha_m[11])
                        alpha_overall_mean13.append(alpha_m[12])
                        alpha_overall_mean14.append(alpha_m[13])

                        smr_overall_mean1.append(smr_m[0])
                        smr_overall_mean2.append(smr_m[1])
                        smr_overall_mean3.append(smr_m[2])
                        smr_overall_mean4.append(smr_m[3])
                        smr_overall_mean5.append(smr_m[4])
                        smr_overall_mean6.append(smr_m[5])
                        smr_overall_mean7.append(smr_m[6])
                        smr_overall_mean8.append(smr_m[7])
                        smr_overall_mean9.append(smr_m[8])
                        smr_overall_mean10.append(smr_m[9])
                        smr_overall_mean11.append(smr_m[10])
                        smr_overall_mean12.append(smr_m[11])
                        smr_overall_mean13.append(smr_m[12])
                        smr_overall_mean14.append(smr_m[13])

                        beta_overall_mean1.append(beta_m[0])
                        beta_overall_mean2.append(beta_m[1])
                        beta_overall_mean3.append(beta_m[2])
                        beta_overall_mean4.append(beta_m[3])
                        beta_overall_mean5.append(beta_m[4])
                        beta_overall_mean6.append(beta_m[5])
                        beta_overall_mean7.append(beta_m[6])
                        beta_overall_mean8.append(beta_m[7])
                        beta_overall_mean9.append(beta_m[8])
                        beta_overall_mean10.append(beta_m[9])
                        beta_overall_mean11.append(beta_m[10])
                        beta_overall_mean12.append(beta_m[11])
                        beta_overall_mean13.append(beta_m[12])
                        beta_overall_mean14.append(beta_m[13])

                        highbeta_overall_mean1.append(highbeta_m[0])
                        highbeta_overall_mean2.append(highbeta_m[1])
                        highbeta_overall_mean3.append(highbeta_m[2])
                        highbeta_overall_mean4.append(highbeta_m[3])
                        highbeta_overall_mean5.append(highbeta_m[4])
                        highbeta_overall_mean6.append(highbeta_m[5])
                        highbeta_overall_mean7.append(highbeta_m[6])
                        highbeta_overall_mean8.append(highbeta_m[7])
                        highbeta_overall_mean9.append(highbeta_m[8])
                        highbeta_overall_mean10.append(highbeta_m[9])
                        highbeta_overall_mean11.append(highbeta_m[10])
                        highbeta_overall_mean12.append(highbeta_m[11])
                        highbeta_overall_mean13.append(highbeta_m[12])
                        highbeta_overall_mean14.append(highbeta_m[13])
                     
      
                        gamma_overall_mean1.append(gamma_m[0])
                        gamma_overall_mean2.append(gamma_m[1])
                        gamma_overall_mean3.append(gamma_m[2])
                        gamma_overall_mean4.append(gamma_m[3])
                        gamma_overall_mean5.append(gamma_m[4])
                        gamma_overall_mean6.append(gamma_m[5])
                        gamma_overall_mean7.append(gamma_m[6])
                        gamma_overall_mean8.append(gamma_m[7])
                        gamma_overall_mean9.append(gamma_m[8])
                        gamma_overall_mean10.append(gamma_m[9])
                        gamma_overall_mean11.append(gamma_m[10])
                        gamma_overall_mean12.append(gamma_m[11])
                        gamma_overall_mean13.append(gamma_m[12])
                        gamma_overall_mean14.append(gamma_m[13])

                        delta_overall_mean1.append(delta_m[0])
                        delta_overall_mean2.append(delta_m[1])
                        delta_overall_mean3.append(delta_m[2])
                        delta_overall_mean4.append(delta_m[3])
                        delta_overall_mean5.append(delta_m[4])
                        delta_overall_mean6.append(delta_m[5])
                        delta_overall_mean7.append(delta_m[6])
                        delta_overall_mean8.append(delta_m[7])
                        delta_overall_mean9.append(delta_m[8])
                        delta_overall_mean10.append(delta_m[9])
                        delta_overall_mean11.append(delta_m[10])
                        delta_overall_mean12.append(delta_m[11])
                        delta_overall_mean13.append(delta_m[12])
                        delta_overall_mean14.append(delta_m[13])
                        
                        
                        features_action_dict={
                            'Bands': self.feature_names,
                            'Time':[j for i in range (7)],
                            'Channel_1':[delta_m[0],theta_m[0],alpha_m[0],smr_m[0],beta_m[0],highbeta_m[0],gamma_m[0]],
                            'Channel_2':[delta_m[1],theta_m[1],alpha_m[1],smr_m[1],beta_m[1],highbeta_m[1],gamma_m[1]],
                            'Channel_3':[delta_m[2],theta_m[2],alpha_m[2],smr_m[2],beta_m[2],highbeta_m[2],gamma_m[2]],
                            'Channel_4':[delta_m[3],theta_m[3],alpha_m[3],smr_m[3],beta_m[3],highbeta_m[3],gamma_m[3]],
                            'Channel_5':[delta_m[4],theta_m[4],alpha_m[4],smr_m[4],beta_m[4],highbeta_m[4],gamma_m[4]],
                            'Channel_6':[delta_m[5],theta_m[5],alpha_m[5],smr_m[5],beta_m[5],highbeta_m[5],gamma_m[5]],
                            'Channel_7':[delta_m[6],theta_m[6],alpha_m[6],smr_m[6],beta_m[6],highbeta_m[6],gamma_m[6]],
                            'Channel_8':[delta_m[7],theta_m[7],alpha_m[7],smr_m[7],beta_m[7],highbeta_m[7],gamma_m[7]],
                            'Channel_9':[delta_m[8],theta_m[8],alpha_m[8],smr_m[8],beta_m[8],highbeta_m[8],gamma_m[8]],
                            'Channel_10':[delta_m[9],theta_m[9],alpha_m[9],smr_m[9],beta_m[9],highbeta_m[9],gamma_m[9]],
                            'Channel_11':[delta_m[10],theta_m[10],alpha_m[10],smr_m[10],beta_m[10],highbeta_m[10],gamma_m[10]],
                            'Channel_12':[delta_m[11],theta_m[11],alpha_m[11],smr_m[11],beta_m[11],highbeta_m[11],gamma_m[11]],
                            'Channel_13':[delta_m[12],theta_m[12],alpha_m[12],smr_m[12],beta_m[12],highbeta_m[12],gamma_m[12]],
                            'Channel_14':[delta_m[13],theta_m[13],alpha_m[13],smr_m[13],beta_m[13],highbeta_m[13],gamma_m[13]]
                            
                            }
                        
                        #print(features_action_dict)
                        df_action_features=pd.DataFrame(features_action_dict,columns=self.column_names)
                        store_action_Features=store_action_Features.append(df_action_features)
                        #result = firebase.post('/Data',features_action_dict)
                        j+=1
                       
                        store_action_Features.to_csv("session_set.csv")
                        if os.path.exists("stop.txt"):
                          break

     

          

            
                time.sleep(1)
            
            
      
       
        store_raw.to_csv("rawdata.csv")
        #store_action_Features.to_csv("session_set.csv")
        theta1=np.mean(theta_overall_mean1)
        theta2=np.mean(theta_overall_mean2)
        theta3=np.mean(theta_overall_mean3)
        theta4=np.mean(theta_overall_mean4)
        theta5=np.mean(theta_overall_mean5)
        theta6=np.mean(theta_overall_mean6)
        theta7=np.mean(theta_overall_mean7)
        theta8=np.mean(theta_overall_mean8)
        theta9=np.mean(theta_overall_mean9)
        theta10=np.mean(theta_overall_mean10)
        theta11=np.mean(theta_overall_mean11)
        theta12=np.mean(theta_overall_mean12)
        theta13=np.mean(theta_overall_mean13)
        theta14=np.mean(theta_overall_mean14)

        alpha1=np.mean(alpha_overall_mean1)
        alpha2=np.mean(alpha_overall_mean2)
        alpha3=np.mean(alpha_overall_mean3)
        alpha4=np.mean(alpha_overall_mean4)
        alpha5=np.mean(alpha_overall_mean5)
        alpha6=np.mean(alpha_overall_mean6)
        alpha7=np.mean(alpha_overall_mean7)
        alpha8=np.mean(alpha_overall_mean8)
        alpha9=np.mean(alpha_overall_mean9)
        alpha10=np.mean(alpha_overall_mean10)
        alpha11=np.mean(alpha_overall_mean11)
        alpha12=np.mean(alpha_overall_mean12)
        alpha13=np.mean(alpha_overall_mean13)
        alpha14=np.mean(alpha_overall_mean14)

        smr1=np.mean(smr_overall_mean1)
        smr2=np.mean(smr_overall_mean2)
        smr3=np.mean(smr_overall_mean3)
        smr4=np.mean(smr_overall_mean4)
        smr5=np.mean(smr_overall_mean5)
        smr6=np.mean(smr_overall_mean6)
        smr7=np.mean(smr_overall_mean7)
        smr8=np.mean(smr_overall_mean8)
        smr9=np.mean(smr_overall_mean9)
        smr10=np.mean(smr_overall_mean10)
        smr11=np.mean(smr_overall_mean11)
        smr12=np.mean(smr_overall_mean12)
        smr13=np.mean(smr_overall_mean13)
        smr14=np.mean(smr_overall_mean14)

        beta1=np.mean(beta_overall_mean1)
        beta2=np.mean(beta_overall_mean2)
        beta3=np.mean(beta_overall_mean3)
        beta4=np.mean(beta_overall_mean4)
        beta5=np.mean(beta_overall_mean5)
        beta6=np.mean(beta_overall_mean6)
        beta7=np.mean(beta_overall_mean7)
        beta8=np.mean(beta_overall_mean8)
        beta9=np.mean(beta_overall_mean9)
        beta10=np.mean(beta_overall_mean10)
        beta11=np.mean(beta_overall_mean11)
        beta12=np.mean(beta_overall_mean12)
        beta13=np.mean(beta_overall_mean13)
        beta14=np.mean(beta_overall_mean14)

        highbeta1=np.mean(highbeta_overall_mean1)
        highbeta2=np.mean(highbeta_overall_mean2)
        highbeta3=np.mean(highbeta_overall_mean3)
        highbeta4=np.mean(highbeta_overall_mean4)
        highbeta5=np.mean(highbeta_overall_mean5)
        highbeta6=np.mean(highbeta_overall_mean6)
        highbeta7=np.mean(highbeta_overall_mean7)
        highbeta8=np.mean(highbeta_overall_mean8)
        highbeta9=np.mean(highbeta_overall_mean9)
        highbeta10=np.mean(highbeta_overall_mean10)
        highbeta11=np.mean(highbeta_overall_mean11)
        highbeta12=np.mean(highbeta_overall_mean12)
        highbeta13=np.mean(highbeta_overall_mean13)
        highbeta14=np.mean(highbeta_overall_mean14)


            
        gamma1=np.mean(gamma_overall_mean1)
        gamma2=np.mean(gamma_overall_mean2)
        gamma3=np.mean(gamma_overall_mean3)
        gamma4=np.mean(gamma_overall_mean4)
        gamma5=np.mean(gamma_overall_mean5)
        gamma6=np.mean(gamma_overall_mean6)
        gamma7=np.mean(gamma_overall_mean7)
        gamma8=np.mean(gamma_overall_mean8)
        gamma9=np.mean(gamma_overall_mean9)
        gamma10=np.mean(gamma_overall_mean10)
        gamma11=np.mean(gamma_overall_mean11)
        gamma12=np.mean(gamma_overall_mean12)
        gamma13=np.mean(gamma_overall_mean13)
        gamma14=np.mean(gamma_overall_mean14)

        delta1=np.mean(delta_overall_mean1)
        delta2=np.mean(delta_overall_mean2)
        delta3=np.mean(delta_overall_mean3)
        delta4=np.mean(delta_overall_mean4)
        delta5=np.mean(delta_overall_mean5)
        delta6=np.mean(delta_overall_mean6)
        delta7=np.mean(delta_overall_mean7)
        delta8=np.mean(delta_overall_mean8)
        delta9=np.mean(delta_overall_mean9)
        delta10=np.mean(delta_overall_mean10)
        delta11=np.mean(delta_overall_mean11)
        delta12=np.mean(delta_overall_mean12)
        delta13=np.mean(delta_overall_mean13)
        delta14=np.mean(delta_overall_mean14)
        

        c=[["Mean of bands","Channel 1","Channel 2", "Channel 3","Channel 4","Channel 5, Channel 6","Channel 7","Channel 8", "Channel 9",
            " Channel 10", "Channel 11", "Channel 12", "Channel 13", "Channel 14"]]
        t=[('theta',theta1,theta2,theta3,theta4,theta5,theta6,theta7,theta8,theta9,theta10,theta11,theta12,theta13,theta14),
        ('alpha',alpha1,alpha2,alpha3,alpha4,alpha5,alpha6,alpha7,alpha8,alpha9,alpha10,alpha11,alpha12,alpha13,alpha14),
        ('smr',smr1,smr2,smr3,smr4,smr5,smr6,smr7,smr8,smr9,smr10,smr11,smr12,smr13,smr14),
        ('beta',beta1,beta2,beta3,beta4,beta5,beta6,beta7,beta8,beta9,beta10,beta11,beta12,beta13,beta14),
        ('highbeta',highbeta1,highbeta2,highbeta3,highbeta4,highbeta5,highbeta6,highbeta7,highbeta8,highbeta9,highbeta10,highbeta11,highbeta12,highbeta13,highbeta14),
        ('gamma',gamma1,gamma2,gamma3,gamma4,gamma5,gamma6,gamma7,gamma8,gamma9,gamma10,gamma11,gamma12,gamma13,gamma14),
        ('delta',delta1,delta2,delta3,delta4,delta5,delta6,delta7,delta8,delta9,delta10,delta11,delta12,delta13,delta14)]

        st=pd.DataFrame(t,columns = ["Mean of bands","Channel 1","Channel 2", "Channel 3","Channel 4","Channel 5", "Channel 6","Channel 7","Channel 8", "Channel 9"," Channel 10", "Channel 11", "Channel 12", "Channel 13", "Channel 14"])
        st.to_csv("Mean_session.csv")

        if self.exit==1:
             self.disconnect_engine()
             print("Engine Disconnected")

             #break
        
    def disconnect_engine(self):
        libEDK.EE_DataFree(self.hData)
        libEDK.EE_EngineDisconnect()
        libEDK.EE_EmoStateFree(self.eState)
        libEDK.EE_EmoEngineEventFree(self.eEvent)

    def disconnect(self):
        self.exit=1

    

cd = CollectData()

pid=os.getpid()
pidfile="run_file.pid"
if os.path.exists(pidfile):
    os.kill(pid)
    
else:
    file (pidfile,"w").write(str(pid))
    cd.data_acq()


 
