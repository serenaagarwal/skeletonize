from PIL import Image
import numpy as np
from skimage.morphology import skeletonize
import imageio.v2 as imageio
import os

soma_path = "/Users/serenaagarwal/Desktop/skeletonize/parsed_somas"
branch_path = "/Users/serenaagarwal/Desktop/skeletonize/parsed_branches"
output_path = "/Users/serenaagarwal/Desktop/skeletonize/somabranches"
pure_skeleton_path = "/Users/serenaagarwal/Desktop/skeletonize/full_skeletons"

os.makedirs(output_path, exist_ok=True)
os.makedirs(pure_skeleton_path, exist_ok=True)


for filename in os.listdir(branch_path): 
    branch_image_path = os.path.join(branch_path, filename)
    branch_img = Image.open(branch_image_path)
    branch_img = np.array(branch_img)
    branch_img = branch_img > 0
    skeleton = skeletonize(branch_img)

    imageio.imwrite(os.path.join(pure_skeleton_path, filename), (skeleton.astype(np.uint8) * 255))

    soma_img_path = os.path.join(soma_path, filename)
    soma_img = Image.open(soma_img_path)
    soma_img = np.array(soma_img) > 0

    combo_img = np.zeros_like(soma_img, dtype=np.uint8)
    combo_img[soma_img] = 255
    combo_img[skeleton] = 255

    imageio.imwrite(os.path.join(output_path, filename), combo_img)

    # imageio.imwrite(os.path.join(output_path_thin1, filename), (thinned_partial_1.astype(np.uint8) * 255))
    # imageio.imwrite(os.path.join(output_path_thin2, filename), (thinned_partial_2.astype(np.uint8) * 255))
    # imageio.imwrite(os.path.join(output_path_thin3, filename), (thinned_partial_3.astype(np.uint8) * 255))
    



# soma = Image.open(soma_path)
# soma = np.array(soma)
# #soma = soma > 0
# output = np.zeros_like(soma)
# output[soma > 0] = 255

# branches = Image.open(branch_path)
# branches = np.array(branches)
# branches = branches > 0

# branches = skeletonize(branches)
# output[branches > 0] = 255

# #output[(branches == 0) & (soma == 0)] = 100

# filename = 'somabranch1.png'
# output_path = os.path.join('/Users/serenaagarwal/Desktop/skeletonize', filename)
# output = output.astype(np.uint8)
# img = Image.fromarray(output)
# img.save(output_path)
# #img = soma + branches
# plt.imshow(output, cmap='GnBu')
# plt.show()
#imageio.imwrite('/Users/serenaagarwal/Desktop/skeletonize', output)
