import suspiciousAPIs
import FeaturesIndexMapping
def addSuspiciousAPI(methodsDictionary, featuresMatrix):
    for method in methodsDictionary:
        suspicious = False
        for api in suspiciousAPIs.Suspicious_APIs:
            if(method.startswith(api)):
                suspicious = True
                break
        if(suspicious):
            featuresMatrix[methodsDictionary[method]][0] = 1
        else:
            featuresMatrix[methodsDictionary[method]][0] = 0

