# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:04:43 2019

@author: Bassant
"""


from changeFormatToSmali import changeFormatToSmali

def permissionsSmali():
    path = 'permissions\\'
    filesG1 = ['jellybean_allmappings.txt', 'ics_allmappings.txt', 'honeycomb_allmappings.txt',\
            'froyo_allmappings.txt', 'gingerbread_allmappings.txt', 'API_09.txt', 'API_10.txt',\
            'API_14.txt', 'API_15.txt', 'API_16.txt', 'API_17.txt', 'API_18.txt', 'API_19.txt',\
            'API_21.txt','API_22.txt',\
            'API_09_publishedapimapping.txt', 'API_10_publishedapimapping.txt',\
            'API_14_publishedapimapping.txt', 'API_15_publishedapimapping.txt',\
            'API_16_publishedapimapping.txt', 'API_17_publishedapimapping.txt',\
            'API_18_publishedapimapping.txt', 'API_19_publishedapimapping.txt',\
            'API_21_publishedapimapping.txt', 'API_22_publishedapimapping.txt' ]

    filesG2 = ['jellybean_contentproviderfieldpermission.txt',\
            'ics_contentproviderfieldpermission.txt',\
            'gingerbread_contentproviderfieldpermission.txt',\
            'honeycomb_contentproviderfieldpermission.txt',\
            'froyo_contentproviderfieldpermission.txt',\
            'API_09_contentproviderfieldpermission.txt',\
            'API_10_contentproviderfieldpermission.txt',\
            'API_14_contentproviderfieldpermission.txt',\
            'API_15_contentproviderfieldpermission.txt',\
            'API_16_contentproviderfieldpermission.txt',\
            'API_17_contentproviderfieldpermission.txt',\
            'API_18_contentproviderfieldpermission.txt',\
            'API_19_contentproviderfieldpermission.txt',\
            'API_21_contentproviderfieldpermission.txt',\
            'API_22_contentproviderfieldpermission.txt']

    uniq={}

    for fg1 in filesG1:
        file = path+fg1
        with open(file) as f:
            allMethods = f.read().splitlines()
            nP=0
            for line in allMethods:
                if line[0:11]=='Permission:':
                    P=line[11:]
                    if P not in uniq.keys():
                        uniq[P] = set()
                elif line[0].isdigit():
                    None
                else:
                    e=line.find('>')
                    smaliForm = changeFormatToSmali(line[0:e+1])
                    uniq[P].add(smaliForm)
                
    for fg2 in filesG2:
        file = path+fg2
        with open(file) as f:
            allMethods = f.read().splitlines()
            nP=0
            for line in allMethods:
                if line[0:11]=='PERMISSION:':
                    P=line[11:]
                    if P not in uniq.keys():
                        uniq[P] = set()
                else:
                    e=line.find('>')
                    smaliForm = changeFormatToSmali(line[0:e+1])
                    uniq[P].add(smaliForm)
    return uniq

'''
for per in uniq.keys():
    name='permissions\\listOfPerms4\\'+per+'.txt'
    fo = open(name,'w')
    for m in uniq[per]:
        fo.write(m)
        fo.write('\n')
    fo.close()
'''
