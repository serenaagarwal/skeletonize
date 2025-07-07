"""
Some of this code is adapted from skimage/morphology/skeletonize jupyter notebook
"""


from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert
from skimage.morphology import skeletonize, thin, remove_small_holes
import imageio.v2 as imageio
import os
import numpy as np
from tifffile import imread
from PIL import Image

"""Parsing tifs"""
# tifs = imread("/Users/serenaagarwal/Desktop/skeletonize/img/simpleseg.tiff")
# os.makedirs("parsed_tifs", exist_ok=True)
# for i, frame in enumerate(tifs):
#     frame_8bit = ((frame - frame.min()) / (frame.max() - frame.min()) * 255).astype(np.uint8)
#     imageio.imwrite(f"parsed_tifs/frame_{i:04d}.png", frame_8bit)


""" Skeletonizing a folder """
input_path = "/Users/serenaagarwal/Desktop/skeletonize/parsed_tifs"
output_path_thin1 = "/Users/serenaagarwal/Desktop/skeletonize/partial_thin_1"
output_path_thin2 = "/Users/serenaagarwal/Desktop/skeletonize/partial_thin_2"
output_path_thin3 = "/Users/serenaagarwal/Desktop/skeletonize/partial_thin_3"
output_path_skeleton = "/Users/serenaagarwal/Desktop/skeletonize/skeletons"

os.makedirs(output_path_thin1, exist_ok=True)
os.makedirs(output_path_thin2, exist_ok=True)
os.makedirs(output_path_thin3, exist_ok=True)
os.makedirs(output_path_skeleton, exist_ok=True)

for filename in os.listdir(input_path):
    img_path = os.path.join(input_path, filename)
    img = Image.open(img_path)
    img = np.array(img)
    img = img > 0
    skeleton = skeletonize(img)
    thinned = thin(img)
    thinned_partial_1 = thin(img, max_num_iter=1)
    thinned_partial_2 = thin(img, max_num_iter = 2)
    thinned_partial_3 = thin(img, max_num_iter=3)

    # imageio.imwrite(os.path.join(output_path_thin1, filename), (thinned_partial_1.astype(np.uint8) * 255))
    # imageio.imwrite(os.path.join(output_path_thin2, filename), (thinned_partial_2.astype(np.uint8) * 255))
    # imageio.imwrite(os.path.join(output_path_thin3, filename), (thinned_partial_3.astype(np.uint8) * 255))
    imageio.imwrite(os.path.join(output_path_skeleton, filename), (skeleton.astype(np.uint8) * 255))




""" Plotting skeletons """

# fig, axes = plt.subplots(2, 3, figsize=(10, 8), sharex=True, sharey=True)
# ax = axes.ravel()

# ax[0].imshow(img, cmap=plt.cm.gray)
# ax[0].set_title('original')
# ax[0].axis('off')

# ax[1].imshow(skeleton, cmap=plt.cm.gray)
# ax[1].set_title('skeleton')
# ax[1].axis('off')

# ax[2].imshow(thinned, cmap=plt.cm.gray)
# ax[2].set_title('thinned')
# ax[2].axis('off')

# ax[4].imshow(thinned_partial_3, cmap=plt.cm.gray)
# ax[4].set_title('less thinned')
# ax[4].axis('off')

# ax[5].imshow(thinned_partial_2, cmap=plt.cm.gray)
# ax[5].set_title('least thinned')
# ax[5].axis('off')

# ax[3].imshow(thinned_partial_1, cmap=plt.cm.gray)
# ax[3].set_title('partially thinned')
# ax[3].axis('off')


# fig.tight_layout()
# plt.show()
