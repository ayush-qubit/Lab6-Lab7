import numpy as np

def accio(mat, k):
	return np.flip(np.argsort(mat,axis=1,kind='stable'),axis=1)[:,0:k]


arr=[[6,4,4,7],[7,8,1,0],[11,10,5,11]]
print(accio(arr,2))