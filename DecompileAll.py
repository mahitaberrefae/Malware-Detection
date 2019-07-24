import os

#put the folders coming from zip in form drebin-0 , drebin-1, drebin-2 , drebin-3, drebin-4, drebin-5
for filename in os.listdir("apks"):
    fileNameWithoutSpaces = filename.replace(' ','')
    os.rename(os.path.join('apks',filename), os.path.join('apks',fileNameWithoutSpaces))
    os.system('apktool d ' + os.path.join("apks" ,fileNameWithoutSpaces) +' -o '
              + os.path.join('output',fileNameWithoutSpaces))