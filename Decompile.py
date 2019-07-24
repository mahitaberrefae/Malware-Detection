import os
def decompile(filename):
    os.system('apktool d ' + filename)