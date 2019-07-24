import Decompile
import Preprocess
import time

#set apk filename
foldername = 'c'
# decompile apk file
#t0 = time.time() # start time
#Decompile.decompile(filename)
# preprocess decompiled data
Preprocess.preprocess(foldername)
#print(time.time() - t0) #print total time

'''
features = open('features.txt','w')
for methodFeatures in featuresMatrix:
    features.write(str(methodFeatures) + '\n')
'''




