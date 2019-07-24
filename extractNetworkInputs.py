import os
#for multiple apk folders use extractAllNetworkInputs
#for one apk folder user extractNetworkInputs
import mapping_Final
import extractHardwareFeatures
import methodType
import GetIntentFilters
import GetSuspiciousAPI
import FeaturesIndexMapping
import json
from xml.dom import minidom

def extractAllNetworkInputs(path, permissionRef):
    for filename in os.listdir(path):
        methodsDictionary = {'dummyMain':0}
        methodsArray = []
        global adjacencyIndex
        adjacencyIndex = 1
        extractNetworkInputs(os.path.join(path,filename), methodsDictionary, True, methodsArray, permissionRef)
        # parse manifest file, and get packageName
        androidManifest = minidom.parse(os.path.join(path, filename, 'androidManifest.xml'))
        packageName = androidManifest.getElementsByTagName('manifest')[0].attributes['package'].value
        featuresMatrix = [[0 for col in range(len(FeaturesIndexMapping.featuresIndexDictionary)+1)] # + 1 for index 0
                            for row in range(len(methodsDictionary))]
        #get permissions
        permissionsDict = mapping_Final.extractPermissions(methodsDictionary, androidManifest
                                                           , permissionRef, packageName, featuresMatrix)
        # get hardware features
        extractHardwareFeatures.extractHardwareFeatures(methodsDictionary, permissionsDict
                                , androidManifest, os.path.join(path,filename,'apktool.yml')
                                , packageName, featuresMatrix)
        # get method type
        methodType.getMethodType(methodsDictionary, featuresMatrix)
        # get intent filters
        GetIntentFilters.addIntentFilters(androidManifest, packageName, featuresMatrix, methodsDictionary)
        # get suspicious apis
        GetSuspiciousAPI.addSuspiciousAPI(methodsDictionary, featuresMatrix)
        features = []
        adj = []
        #handle dummy main row (all ones)
        firstRow = []
        for j in range(0,adjacencyIndex):
            firstRow.append(1)
            features.append([])
        adj.append(firstRow)
        #handle remained methods
        for i in range(1,adjacencyIndex):
            temp = []
            for j in range(0,adjacencyIndex):
                temp.append(0)
            adj.append(temp)
        for line in methodsArray:
            if(line.startswith('\t')):
                line2 = line[1:]
                adj[currentNode][methodsDictionary[line2]] = 1 # removed + (takes only 1 or 0)
            else:
                currentNode = methodsDictionary[line]

        # write data to json file
        data = {}
        data['adjacency'] = adj
        data['features'] = featuresMatrix
        data['label'] = [1] + ([0] * (len(featuresMatrix) - 1))
        networkData = open(filename + '_networkData.json', 'w')
        json.dump(data, networkData)



def extractNetworkInputs(path, methodsDictionary, firstTime, methodsArray, permissionRef):
    global adjacencyIndex
    for filename in os.listdir(path):
        nextPath = os.path.join(path,filename)
        if os.path.isdir(nextPath):
            if(firstTime):
                if(not filename.startswith('smali')):
                    continue
            #it's a directory call extractNetworkInputs again (recursively)
            extractNetworkInputs(nextPath, methodsDictionary, False, methodsArray, permissionRef)
        else:
            #check extension
            if(filename.endswith('.smali')):
                extractNetworkInputsFromSmali(nextPath, methodsDictionary, methodsArray, permissionRef)
    return 0

def extractNetworkInputsFromSmali(path, methodsDictionary, methodsArray, permissionRef):
    global adjacencyIndex
    currentClass = ''
    currentMethod = ''
    currentInvokeMethod = ''
    try:
        file = open(path, 'r', errors='ignore')
        for line in file:
            # check for current class
            if (line.startswith('.class')):
                for i in range(0, len(line)):
                    if line[i] == 'L':
                        currentClass = line[i:-1]
                        break
            # check for current method
            elif (line.startswith('.method')):
                currentMethod = line[line.rfind(' ') + 1:]
                formatedMethod = (currentClass + '->' + currentMethod)[:-1]
                methodsArray.append(formatedMethod)
                if (not (formatedMethod in methodsDictionary)):
                    methodsDictionary[formatedMethod] = adjacencyIndex
                    adjacencyIndex += 1
            # check for current invoke method
            elif (line.lstrip().startswith('invoke')):
                for j in range(0, len(line)):
                    if line[j] == 'L':
                        currentInvokeMethod = line[j:-1]
                        methodsArray.append(('\t'+currentInvokeMethod))
                        if(not (currentInvokeMethod in methodsDictionary)):
                            methodsDictionary[currentInvokeMethod] = adjacencyIndex
                            adjacencyIndex += 1
                        break

        file.close()
    except FileNotFoundError:
        return



#pass folder name to extractAllNetworkInputs
adjacencyIndex = 1
# uniq is created using permissionsSmali.py


