import numpy as np
def alohomora(n, m):
	pattern1=np.ones((m,m),dtype=int)
	pattern2=np.zeros((m,m),dtype=int)
	result=None
	for row in range(0,int(n/m)):
		temp=None
		if row%2==0:
			temp=np.copy(pattern1)
			for col in range(1,int(n/m)):
				if col%2==0:
					temp=np.hstack((temp,pattern1))
				else:
					temp=np.hstack((temp,pattern2))
		else:
			temp=np.copy(pattern2)
			for col in range(1,int(n/m)):
				if col%2==1:
					temp=np.hstack((temp,pattern1))
				else:
					temp=np.hstack((temp,pattern2))
		if row==0:
			result=np.copy(temp)
		else:
			result=np.vstack((result,temp))
	return result

print(alohomora(15,5))