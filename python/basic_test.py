print("starting basic_test.py")

# test 1: with our color matrix from assets, try replacing noise-y black elements with white elements and do a side by side comparison with pyplot
from color_matrix import get_color_matrix
from clean_noise import *
import matplotlib.pyplot as plt
import json
import os


# Constants relevant to processing algo
THRESHOLD = 1
POSITIVITY_RATIO = 0.5
WALL = 0
GROUND = 1
# TODO: no definite value for UNDEFINED in this implementation
#       this can be corrected in color_matrix.py
TARGET_TYPE = WALL
REPLACEMENT_TYPE = GROUND

  
# Opening JSON file
f = open('/Users/administrator/Documents/GitHub/parse-.umap/assets/map.umap')
data = json.load(f)
mapdata = data["mapdata"]
# process umap data
color_matrix = get_color_matrix(mapdata)
# run processing algos (that this script is currently testing)
updated_color_matrix = clean_color_matrix(color_matrix, TARGET_TYPE, REPLACEMENT_TYPE, THRESHOLD, POSITIVITY_RATIO)
# visually plot output
print("starting plot")
# updated_color_matrix = plt.imclose(color_matrix)
plt.figure(figsize=(8,8))
plt.subplot(121)

plt.imshow(color_matrix) #, cmap="Greys")
plt.axis('off')
plt.title('unprocessed')

plt.subplot(122)

plt.imshow(updated_color_matrix) #, cmap="Greys")
plt.axis('off')
plt.title('subset-radius: {} -- threshold: {}'.format(THRESHOLD, POSITIVITY_RATIO))
plt.savefig('/Users/administrator/Documents/GitHub/Auto-Beautify/test-results/imageth{}pos{}.png'.format(THRESHOLD, POSITIVITY_RATIO))
plt.show()
plt.close()
print("ending basic_test.py")