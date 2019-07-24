# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:37:00 2019

@author: Bassant
"""

"""
metheod is classified as System API if it starts with:
    android.xxxxx
    java.xxxxxxx
    com.android.xxxxx
    com.java.xxxxx

method is classified as third-party API if it starts with:
    com.google.xxxxxx
    come.facebook.xxxxx
    com.yahooapis.xxxxxx

method is classified as component API if it starts with:
    android.provider.xxxx
    or contains provider anywhere
    
method is classified as other otherwise
"""
import FeaturesIndexMapping
def getMethodType(methodsDictionary, featuresMatrix):
    for m in methodsDictionary:
        if(m == 'dummyMain'):
            continue
        mSplit=m.split('/')
        if (len(mSplit) < 2):
            featuresMatrix[methodsDictionary[m]][114] = 1 # Others index is 114
        elif (mSplit[1]=="provider") | ("providers" in mSplit) | (mSplit[1]=="activity") | ("activities" in mSplit) | (mSplit[1]=="service") | ("services" in mSplit) | (mSplit[1]=="reciver") | ("recievers" in mSplit):
            featuresMatrix[methodsDictionary[m]][115] = 1  # component API index is 115
        elif (mSplit[0]=="Landroid") | (mSplit[1]=="android") | (mSplit[0]=="Ljava") | (mSplit[1]=="java"):
            featuresMatrix[methodsDictionary[m]][116] = 1  # System API index is 116
        elif (mSplit[1]=="google") | (mSplit[1]=="facebook") | (mSplit[1]=="yahooapis"):
            featuresMatrix[methodsDictionary[m]][117] = 1  # Third party API index is 117
        else:
            featuresMatrix[methodsDictionary[m]][114] = 1  # Others index is 114
