# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:51:22 2019

@author: Bassant
"""

import permissionsSmali
import timeit
import FeaturesIndexMapping

def extractPermissions(methodsDictionary, androidManifest, permissionRef, packageName, featuresMatrix):
    permissionDictionary = {key:set() for key in methodsDictionary.keys()}
    componentPermissions = []
    #extract requested permissions from uses-permission tag
    for permission in androidManifest.getElementsByTagName('uses-permission'):
        currentPermission = ''
        if(permission.hasAttribute('android:name')):
            currentPermission = permission.attributes['android:name'].value
        if(len(currentPermission) != 0):
            permissionDictionary['dummyMain'].add(currentPermission)
            if(currentPermission in FeaturesIndexMapping.featuresIndexDictionary):
                featuresMatrix[0][FeaturesIndexMapping.featuresIndexDictionary[currentPermission]] = 1
        #find component permissions
        #find component class name
        # check for activity
        for activity in androidManifest.getElementsByTagName('activity'):
            componentName = ''
            componentPermission = ''
            if (activity.hasAttribute('android:name')):
                componentName = activity.attributes['android:name'].value
            if (activity.hasAttribute('android:permission')):
                componentPermission = activity.attributes['android:permission'].value
                # add to orientation dictionary
                if (componentPermission != '' and componentPermission != ''):
                    if (componentName.startswith('.')):
                        componentName = 'L' + (packageName + componentName).replace('.', '/')
                    else:
                        componentName = 'L' + componentName.replace('.', '/')
                    componentPermissions.append((componentName, componentPermission))
        # check for applications
        for application in androidManifest.getElementsByTagName('application'):
            componentName = ''
            componentPermission = ''
            if (application.hasAttribute('android:name')):
                componentName = application.attributes['android:name'].value
            if (application.hasAttribute('android:permission')):
                componentPermission = application.attributes['android:permission'].value
                # add to orientation dictionary
                if (componentPermission != '' and componentPermission != ''):
                    if (componentName.startswith('.')):
                        componentName = 'L' + (packageName + componentName).replace('.', '/')
                    else:
                        componentName = 'L' + componentName.replace('.', '/')
                    componentPermissions.append((componentName, componentPermission))
        # check for receivers
        for receiver in androidManifest.getElementsByTagName('receiver'):
            componentName = ''
            componentPermission = ''
            if (receiver.hasAttribute('android:name')):
                componentName = receiver.attributes['android:name'].value
            if (receiver.hasAttribute('android:permission')):
                componentPermission = receiver.attributes['android:permission'].value
                # add to orientation dictionary
                if (componentPermission != '' and componentPermission != ''):
                    if (componentName.startswith('.')):
                        componentName = 'L' + (packageName + componentName).replace('.', '/')
                    else:
                        componentName = 'L' + componentName.replace('.', '/')
                    componentPermissions.append((componentName, componentPermission))
    #map permissions to methods
    for currentPermission in permissionDictionary['dummyMain']:
        if(currentPermission in permissionRef):
            for currentMethod in permissionRef[currentPermission]:
                if(currentMethod in methodsDictionary):
                    permissionDictionary[currentMethod].add(currentPermission)
                    if (currentPermission in FeaturesIndexMapping.featuresIndexDictionary):
                        featuresMatrix[methodsDictionary[currentMethod]][FeaturesIndexMapping.featuresIndexDictionary[currentPermission]] = 1
    #add components permissions
    for currentMethod in methodsDictionary:
        for component in componentPermissions:
            if(currentMethod.startswith(component[0])):
                permissionDictionary[currentMethod].add(component[1])
                if (component[1] in FeaturesIndexMapping.featuresIndexDictionary):
                    featuresMatrix[methodsDictionary[currentMethod]][FeaturesIndexMapping.featuresIndexDictionary[component[1]]] = 1
    return permissionDictionary
