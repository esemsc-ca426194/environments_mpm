from envtest import smooth_image
from scipy import misc
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

image = misc.ascent()
sigma = 5

def smooth_image(a, sigma = 1):
    return gaussian_filter(a, sigma=sigma)

smoothed_image = smooth_image(image, sigma)

f = plt.figure()
f.add_subplot(1, 2, 1)
plt.imshow(image)
f.add_subplot(1, 2, 2)
plt.imshow(smoothed_image)
plt.show(block = True)

