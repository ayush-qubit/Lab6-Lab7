import numpy as np
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

avada_kedavra([i for i in range(1,26)])