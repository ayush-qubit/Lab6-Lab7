import numpy as np

# ---- Task (a) -------
# Do as directed in function:
# 'my_list': a list of 25 integers
def avada_kedavra(my_list):
	# Create an array 'a0' from this list 'my_list'

	# print a0
	a0=np.array(my_list)
	print("a0 at beginning:\n{}".format(a0))

	# reshape a0 to create a 5X5 matrix a1
	a1=np.reshape(a0,(5,5))
	# print a1
	print("a1 at the beginning:\n{}".format(a1))

	# now, change the central element of a1 to 0
	a1[2][2]=0
	# print a1
	print("a1 after change:\n{}".format(a1))

	# print a0
	print("a0 after changing a1:\n{}".format(a0))
	print("reshaping doesn't create a copy of array. It just returns another view. So, changing one changed the other")

	# make a copy of a1 and flatten it (call it a1cpy)
	a1cpy=np.copy(a1)
	a1cpy=np.reshape(a1cpy,25)
	# multiply each element of a1cpy by 0.7:
	a1cpy=a1cpy*0.7
	# print a1cpy:
	print("a1cpy\n{}".format(a1cpy))
	
	# print a1:
	print("a1 after changing its copy:\n{}".format(a1))
	
	
# ---- Task (b) -------
# Do as directed in function:
# 'my_integer': an even integer
def incendio(my_integer):
	# create an array 'arng0' of shape (3,2) containing consecutive even numbers starting from 'my_integer', arranged along rows
	arng0 = np.arange(my_integer, my_integer + 12, 2).reshape(3,2)
        # print arng0
	print("arng0\n{}".format(arng0))
	# create another array 'arng1' of shape ((4,3)) containing consecutive numbers starting from 'my_integer' arranged along columns:
	arng1 = np.arange(my_integer, my_integer + 12).reshape(4, 3)
	# print arng1
	print("arng1\n{}".format(arng1))
	# multiply transpose of arng0 with transpose of arng1 to get mult0:
	arng0T = np.transpose(arng0)
	arng1T = np.transpose(arng1)
	mult0 = arng0T.dot(arng1T)
	# print mult0:
	print("mult0\n{}".format(mult0))
	# take min of mult0 along its rows and store it in v0:
	min1,min2 = mult0[0].min(), mult0[1].min()
	v0 = [min1,min2]
	v0 = np.matrix(v0)
	# print v0's shape:
	print("shape of v0: \n{}".format(v0.shape))
	# reshape v0 to make it a column vector:
	v0 = np.transpose(v0)
	# subtract v0 from each column of mult0 and store it in base0:
	base0 = mult0 - v0
	# print base0
	print("base0\n{}".format(base0))
	# square all the elements present in base0
	base0 = np.square(base0)
	# store the sum of all elements of base0 in ans
	ans = np.sum(base0)
	ans = np.around(ans, decimals=2)
	# print ans
	print("ans : {}".format(ans))


# ---- Task (c) -------
# 'n': integer
# 'm': integer that divides n
# return type: int numpy Ndarray; dim: nxn
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


# ---- Task (d) -------
# 'arr': float Ndarray; dim: Nx3, 
# 'theta': float; 0≤theta<360 (in degrees)
# 'axis': str; axis ∈ {'X','Y','Z'}
# return type: float Ndarray; dim: Nx3
def expelliarmus(arr, theta, axis):
	arr=np.array(arr)
	radian=np.radians(np.array(theta))
	if axis=='X':
		rotation_matrix=np.array([[1,0,0],[0,np.cos(radian),np.sin(radian)],[0,-np.sin(radian),np.cos(radian)]])
	elif axis=='Y':
		rotation_matrix=np.array([[np.cos(radian),0,np.sin(radian)],[0,1,0],[-np.sin(radian),0,np.cos(radian)]])
	else:
		rotation_matrix=np.array([[np.cos(radian),np.sin(radian),0],[-np.sin(radian),np.cos(radian),0],[0,0,1]])
	rotated_matrix=np.dot(rotation_matrix,np.transpose(arr))
	return np.round(np.transpose(rotated_matrix),decimals=2)


# ---- Task (e) -------
# 'arr': float Ndarray; dim: MxN
# return type: float Ndarray; dim: MxN

def crucio(arr):
	arr=np.array(arr)
	arr=arr-arr.mean(axis=0)
	arr=arr/arr.std(axis=0)
	return np.round(arr,decimals=2)


# ---- Task (f) -------
# 'arr': int 1-D array; dim: (n,)
# k: integer
# return type: int 1-D array; dim: (n+k-1,)
def leviosa(arr, k):
	pass


# ---- Task (g) -------
# 'mat': int n-D array; dim: (m,n)
# k: integer
# return type: n-D integer array; dim: (m,k)
def accio(mat, k):
	return np.flip(np.argsort(mat,axis=1,kind='stable'),axis=1)[:,0:k]
