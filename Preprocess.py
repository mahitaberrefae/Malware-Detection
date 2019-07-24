import permissionsSmali
import extractNetworkInputs
def preprocess(foldername):
    '''

    :param foldername:
    :return: dictionary in the form
        adj: N x N adjacency matrix
        features: N x E features matrix
        labels: N x M labels matrix
    '''
    #methodsDictionary = {'dummyMain': 0}
    #methodsArray = []
    permissionRef = permissionsSmali.permissionsSmali()
    #extractNetworkInputs.extractAllNetworkInputs(foldername,methodsDictionary,True,methodsArray, permissionRef)
    extractNetworkInputs.extractAllNetworkInputs(foldername, permissionRef)