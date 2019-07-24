def changeFormatToSmali(method):
    temp = method.find(':')
    className = 'L' + method[1:temp].replace('.','/')
    lastSpace = method.rfind(' ')
    returnType = method[temp+2:lastSpace]
    #check return type on primitive values
    if(returnType == 'void'):
        returnType = 'V'
    elif (returnType == 'byte'):
        returnType = 'B'
    elif (returnType == 'short'):
        returnType = 'S'
    elif (returnType == 'char'):
        returnType = 'C'
    elif (returnType == 'int'):
        returnType = 'I'
    elif (returnType == 'long'):
        returnType = 'J'
    elif (returnType == 'float'):
        returnType = 'F'
    elif (returnType == 'double'):
        returnType = 'D'
    elif (returnType == 'boolean'):
        returnType = 'Z'
    elif(returnType.endswith('[]')):
        returnType = '[L' + returnType[:-2].replace('.', '/') + ';'
    else:
        returnType = 'L' + returnType.replace('.', '/') + ';'
    methodName = method[lastSpace+1:-1]
    #check for parameters in methodName
    temp = methodName.find('(')
    if(methodName[:temp] == 'static'):
        formatedMethodName = '<clinit>('
    elif(methodName[:temp] == className[className.rfind('/')+1:]):
        formatedMethodName = '<init>('
    else:
        formatedMethodName = methodName[:temp+1]
    parameters = methodName[temp+1:-1].split(',')
    for parameter in parameters:
        #check parameters on primitive values
        if(parameter == 'void'):
            formatedMethodName += 'V'
        elif (parameter == 'byte'):
            formatedMethodName += 'B'
        elif (parameter == 'short'):
            formatedMethodName += 'S'
        elif (parameter == 'char'):
            formatedMethodName += 'C'
        elif (parameter == 'int'):
            formatedMethodName += 'I'
        elif (parameter == 'long'):
            formatedMethodName += 'J'
        elif (parameter == 'float'):
            formatedMethodName += 'F'
        elif (parameter == 'double'):
            formatedMethodName += 'D'
        elif (parameter == 'boolean'):
            formatedMethodName += 'Z'
        elif (parameter.endswith('[]')):
            formatedMethodName += '[L' + parameter[:-2].replace('.', '/') + ';'
        elif(len(parameter) != 0):
            formatedMethodName += 'L' + parameter.replace('.', '/') + ';'
    formatedMethodName += ')'
    return className + ';->' + formatedMethodName + returnType


#print(changeFormatToSmali('<android.accounts.AccountManager: android.accounts.Account[] getAccounts()>'))