import numpy as np

k=2
arr=np.array([[6,4,4,7],[7,8,1,0],[11,11,10,5]])
print(np.flip(np.argsort(arr,axis=1,kind='stable'),axis=1)[:,0:k])