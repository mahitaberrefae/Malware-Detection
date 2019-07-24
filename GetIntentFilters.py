from xml.dom import minidom
import FeaturesIndexMapping

def addIntentFilters(androidManifest, packageName, featuresMatrix, methodsDictionary):
    intentDictionary = {}
    for intent in androidManifest.getElementsByTagName('intent-filter'): # get all intent-filters and loop on them
        parent = intent.parentNode
        className = ''
        action = []
        category = []
        # get className
        if(parent.hasAttribute('android:name')):
            className = parent.attributes['android:name'].value
            for child in intent.childNodes: #loop on all childes of the current intnt-filter
                if(child.nodeType == minidom.Node.ELEMENT_NODE): #check if the node represents a tag
                    if(child.tagName == 'action'): #check for action
                        #get action
                        action.append(child.attributes['android:name'].value)
                    elif(child.tagName == 'category'): #check for category
                        #get category
                        category.append(child.attributes['android:name'].value)
        if(len(className) != 0):
            if(className.startswith('.')):
                className = packageName + className
            className = 'L' + className.replace('.','/')
            intentDictionary[className] = []
            if(len(action)  != 0):
                intentDictionary[className] += action
            if(len(category) != 0):
                intentDictionary[className] += category
    # write to featuresMatrix
    for method in methodsDictionary:
        for intentClass in intentDictionary:
            if(method.startswith(intentClass)):
                for feature in intentDictionary[intentClass]:
                    if (feature in FeaturesIndexMapping.featuresIndexDictionary):
                        featuresMatrix[methodsDictionary[method]][
                            FeaturesIndexMapping.featuresIndexDictionary[feature]] = 1

