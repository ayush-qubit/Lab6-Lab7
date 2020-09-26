import numpy as np

k=2
arr=np.array([[6,4,4,7],[7,8,1,0],[11,10,5,11]])
print(np.argsort(-1*arr,axis=1,kind='heap')[:,0:k])