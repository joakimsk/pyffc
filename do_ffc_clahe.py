import os
from skimage import io
from skimage import util
from skimage import color
from skimage import exposure
from skimage import filters
import numpy as np
import time

start = time.time()

input_filename = "crabs_original.jpg"
pathname, extension = os.path.splitext(input_filename)
print(pathname)

data_image = util.img_as_float(io.imread(input_filename))
data_mask = util.img_as_float(io.imread('mask.png'))

flat_field_corrected = (np.array(data_image).astype(float) / (np.array(data_mask).astype(float))) # float values must be between 0 and 1, which is why we multiply by 0.139... :)

max_pixel_value = np.max(flat_field_corrected)
print("Max value in FFC result", max_pixel_value)

# Y = (X-A)/(B-A) * (D-C) + C
gain_adjusted_ffc = (flat_field_corrected-0.0)/(max_pixel_value-0.0) * (1.0-0.0) + 0.0
print("Max value after gain adjustment", np.max(gain_adjusted_ffc))

print("Saving ffc...")
io.imsave(f'{pathname}_ffc.jpg', util.img_as_ubyte(gain_adjusted_ffc))

# Kernel size calculation
img_width = 4096
img_height = 2304
factor = 8 # Default is 8

img_adapteq = exposure.equalize_adapthist(np.clip(gain_adjusted_ffc, 0.0, 1.0), nbins=255, kernel_size=(img_width/factor, img_height/factor), clip_limit=0.007)
print("Max value after CLAHE", np.max(img_adapteq))

print("Saving clahe...")
io.imsave(f'{pathname}_ffc_clahe.jpg', util.img_as_ubyte(img_adapteq))
end = time.time()
print(f'Time used: {end - start:.2f} [s]')