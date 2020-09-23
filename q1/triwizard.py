import numpy as np

# ---- Task (a) -------
# Do as directed in function:
# 'my_list': a list of 25 integers
def avada_kedavra(my_list):
	# Create an array 'a0' from this list 'my_list'

	# print a0
	print("a0 at beginning:\n{}".format(a0))

	# reshape a0 to create a 5X5 matrix a1

	# print a1
	print("a1 at the beginning:\n{}".format(a1))

	# now, change the central element of a1 to 0

	# print a1
	print("a1 after change:\n{}".format(a1))

	# print a0
	print("a0 after changing a1:\n{}".format(a0))
	print("reshaping doesn't create a copy of array. It just returns another view. So, changing one changed the other")

	# make a copy of a1 and flatten it (call it a1cpy)

	# multiply each element of a1cpy by 0.7:

	# print a1cpy:
	print("a1cpy\n{}".format(a1cpy))

	# print a1:
	print("a1 after changing its copy:\n{}".format(a1))


# ---- Task (b) -------
# Do as directed in function:
# 'my_integer': an even integer
def incendio(my_integer):
	# create an array 'arng0' of shape (3,2) containing consecutive even numbers starting from 'my_integer', arranged along rows

	# print arng0
	print("arng0\n{}".format(arng0))

	# create another array 'arng1' of shape ((4,3)) containing consecutive numbers starting from 'my_integer' arranged along columns:

	# print arng1
	print("arng1\n{}".format(arng1))

	# multiply transpose of arng0 with transpose of arng1 to get mult0:

	# print mult0:
	print("mult0\n{}".format(mult0))

	# take min of mult0 along its rows and store it in v0:

	# print v0's shape:
	print("shape of v0: \n{}".format(v0.shape))

	# reshape v0 to make it a column vector:

	# subtract v0 from each column of mult0 and store it in base0:

	# print base0
	print("base0\n{}".format(base0))

	# square all the elements present in base0

	# store the sum of all elements of base0 in ans

	# print ans
	print("ans : {}".format(ans))


# ---- Task (c) -------
# 'n': integer
# 'm': integer that divides n
# return type: int numpy Ndarray; dim: nxn
def alohomora(n, m):
	pass


# ---- Task (d) -------
# 'arr': float Ndarray; dim: Nx3, 
# 'theta': float; 0≤theta<360 (in degrees)
# 'axis': str; axis ∈ {'X','Y','Z'}
# return type: float Ndarray; dim: Nx3
def expelliarmus(arr, theta, axis):
	pass


# ---- Task (e) -------
# 'arr': float Ndarray; dim: MxN
# return type: float Ndarray; dim: MxN
def crucio(arr):
	pass


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
	pass
