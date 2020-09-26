import numpy as np
import matplotlib.pyplot as plt

arr = np.load('decode_this.npy')
#print(arr.shape)
amin = np.amin(arr)
amax = np.amax(arr)

arr = 255 * (arr - amin)/(amax - amin)
plt.imshow(arr.astype('uint8'))
plt.savefig('result.png')
#plt.show()