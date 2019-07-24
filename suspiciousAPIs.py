"""

execHttpRequest()  "permission ?"
SendBroadcast() "intent filter? "

"""
Suspicious_APIs =  ['Landroid/telephony/TelephonyManager;->getDeviceId()',
                    'Landroid/telephony/TelephonyManager;->getImei()',
                    'Landroid/telephony/TelephonyManager;->getSubscriberId()',
                    'Landroid/telephony/TelephonyManager;->getSimSerialNumber()',
                    'Landroid/net/wifi/WifiManager;->setWifiEnabled()',
                    'Landroid/telephony/SmsManager;->sendTextMessage()',
                    'Landroid/telephony/SmsManager;->sendDataMessage',
                    'Landroid/location/Location;->getLatitude()',
                    'Landroid/location/Location;->getLongitude()',
                    'Landroid/location/LocationManager;->getLastKnownLocation',
                    'Landroid/location/LocationManager;->requestLocationUpdates()',
                    'Ljava/lang/Runtime;->exec()',
                    'Ldalvik.system.DexClassLoader;->Loadclass()',
                    'Ljavax/crypto/CipherCipher;->getInstance()',
                   ]

