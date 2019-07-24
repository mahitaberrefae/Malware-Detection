import FeaturesIndexMapping
def extractHardwareFeatures(methodsDictionary, permissionsDictionary, androidManifest,
                                apktoolYmlFilePath, packageName, featuresMatrix):
    #find minSdkVersion
    apktoolYml =  open(apktoolYmlFilePath, 'r')
    minSdkVersion = 1 #default value
    # get minSdkVersion
    for line in apktoolYml :
        line = line.lstrip()
        if(line.startswith('minSdkVersion:')):
            temp = ''
            for i in range(line.find("'")+1,len(line)):
                if(line[i] == "'"):

                    break
                temp += line[i]
            try:
                minSdkVersion = int(temp)
            except ValueError:
                minSdkVersion = 1
            break
    #get hardware feature from uses-feature, and android:screenOrientation from activies
    orientationDictionary = {} #key:method name , value:hardware feature of orientation
    for activity in androidManifest.getElementsByTagName('activity'):
        key = ''
        value = ''
        if(activity.hasAttribute('android:name')):
            key = activity.attributes['android:name'].value
        if (activity.hasAttribute('android:screenOrientation')):
            value = activity.attributes['android:screenOrientation'].value
            #add to orientation dictionary
            if(value != '' and key != ''):
                if (key.startswith('.')):
                    key = 'L' + (packageName + key).replace('.', '/')
                else:
                    key = 'L' + key.replace('.', '/')
                if(value == 'portrait'):
                    orientationDictionary[key] = 'android.hardware.screen.portrait'
                elif(value == 'landscape'):
                    orientationDictionary[key] = 'android.hardware.screen.landscape'
    for feature in androidManifest.getElementsByTagName('uses-feature'):
        hardwareFeature = ''
        if(feature.hasAttribute('android:name')):
            hardwareFeature = feature.attributes['android:name'].value
        if(len(hardwareFeature) != 0):
            if(hardwareFeature in FeaturesIndexMapping.featuresIndexDictionary):
                featuresMatrix[0][FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
    #assign android.hardware.screen.landscape or protrait to corresponding methods
    for method in methodsDictionary:
        #find className
        className = method[:method.find(';->')]
        if(className in orientationDictionary):
            hardwareFeature = orientationDictionary[className]
            featuresMatrix[methodsDictionary[method]][FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
    #map permissions to hardware (based on aapt code)
    for method in methodsDictionary:
        if('android.permission.CAMERA' in permissionsDictionary[method]):
            hardwareFeature = 'android.hardware.camera'
            featuresMatrix[methodsDictionary[method]][FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
        if('android.permission.ACCESS_FINE_LOCATION' in permissionsDictionary[method]):
            hardwareFeature = 'android.hardware.location'
            featuresMatrix[methodsDictionary[method]][FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
            if(minSdkVersion < 21): # 21 for SDK_LOLLIPOP
                hardwareFeature = 'android.hardware.location.gps'
                featuresMatrix[methodsDictionary[method]][FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1

        if('android.permission.ACCESS_COARSE_LOCATION' in permissionsDictionary[method]):
            hardwareFeature = 'android.hardware.location'
            featuresMatrix[methodsDictionary[method]][
                    FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
            if(minSdkVersion < 21): # 21 for SDK_LOLLIPOP
                hardwareFeature = 'android.hardware.location.network'
                featuresMatrix[methodsDictionary[method]][FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
        if (('android.permission.ACCESS_MOCK_LOCATION' in permissionsDictionary[method])
            or ('android.permission.ACCESS_LOCATION_EXTRA_COMMANDS' in permissionsDictionary[method])
            or ('android.permission.INSTALL_LOCATION_PROVIDER' in permissionsDictionary[method])):
            hardwareFeature = 'android.hardware.location'
            featuresMatrix[methodsDictionary[method]][
                    FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
        if(('android.permission.BLUETOOTH' in permissionsDictionary[method])
            or ('android.permission.BLUETOOTH_ADMIN' in permissionsDictionary[method])):
            if(minSdkVersion > 4 ): # 4 for SDK_DONUT
                hardwareFeature = 'android.hardware.bluetooth'
                featuresMatrix[methodsDictionary[method]][FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
        if('android.permission.RECORD_AUDIO' in permissionsDictionary[method]):
            hardwareFeature = 'android.hardware.microphone'
            featuresMatrix[methodsDictionary[method]][
                    FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
        if(('android.permission.ACCESS_WIFI_STATE' in permissionsDictionary[method])
            or ('android.permission.CHANGE_WIFI_STATE' in permissionsDictionary[method])
            or ('android.permission.CHANGE_WIFI_MULTICAST_STATE' in permissionsDictionary[method])):
            hardwareFeature = 'android.hardware.wifi'
            featuresMatrix[methodsDictionary[method]][
                    FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
        if(('android.permission.CALL_PHONE' in permissionsDictionary[method])
            or ('android.permission.CALL_PRIVILEGED' in permissionsDictionary[method])
            or 'android.permission.MODIFY_PHONE_STATE' in permissionsDictionary[method]
            or 'android.permission.PROCESS_OUTGOING_CALLS' in permissionsDictionary[method]
            or 'android.permission.READ_SMS' in permissionsDictionary[method]
            or 'android.permission.RECEIVE_SMS' in permissionsDictionary[method]
            or 'android.permission.RECEIVE_MMS' in permissionsDictionary[method]
            or 'android.permission.RECEIVE_WAP_PUSH' in permissionsDictionary[method]
            or 'android.permission.SEND_SMS' in permissionsDictionary[method]
            or 'android.permission.WRITE_APN_SETTINGS' in permissionsDictionary[method]
            or 'android.permission.WRITE_SMS' in permissionsDictionary[method]):
            hardwareFeature = 'android.hardware.faketouch'
            featuresMatrix[0][FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
    if(featuresMatrix[0][FeaturesIndexMapping.featuresIndexDictionary['android.hardware.touchscreen']] != 1):
        hardwareFeature = 'android.hardware.telephony'
        featuresMatrix[0][FeaturesIndexMapping.featuresIndexDictionary[hardwareFeature]] = 1
