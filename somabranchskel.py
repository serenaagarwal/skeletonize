from PIL import Image
import numpy as np
from skimage.morphology import skeletonize, thin
import os

soma_path = "/Users/serenaagarwal/Desktop/skeletonize/soma1.png"
branch_path = "/Users/serenaagarwal/Desktop/skeletonize/branch1.png"

soma = Image.open(soma_path)
soma = np.array(soma)
#soma = soma > 0
output = np.zeros_like(soma)
output[soma > 0] = 255

branches = Image.open(branch_path)
branches = np.array(branches)
branches = branches > 0

branches = skeletonize(branches)
output[branches > 0] = 255

#output[(branches == 0) & (soma == 0)] = 100

filename = 'somabranch1.png'
output_path = os.path.join('/Users/serenaagarwal/Desktop/skeletonize', filename)
output = output.astype(np.uint8)
img = Image.fromarray(output)
img.save(output_path)
# #img = soma + branches
# plt.imshow(output, cmap='GnBu')
# plt.show()
#imageio.imwrite('/Users/serenaagarwal/Desktop/skeletonize', output)


