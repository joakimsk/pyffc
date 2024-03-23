import time
import numpy as np
import skimage

# generate_mask.py
# Used to generate a mask for FFC-processing. Requires you to pick out a few pictures without any specific features on them.
# If you are using this script for AUV-photos, it may be imperative to only select photos from a certain altitude, and use the mask only for a certain altitude.
# Also a large change in biome may require a new mask to be generated.
# Joakim Skjefstad, 2024

def imread_rgb(f):
    return skimage.io.imread(f)

def blend_images(images):
    # Ensure all images have the same shape
    shapes = [img.shape for img in images]
    if len(set(shapes)) != 1:
        raise ValueError("All images must have the same dimensions")
    # Convert images to NumPy arrays
    images = [np.array(img, dtype=np.float64) for img in images]
    # Calculate the average of pixel values for blending
    blended_image = np.mean(images, axis=0)
    # Convert back to uint8 for saving/displaying
    blended_image = np.uint8(blended_image)
    return blended_image


def main():
    start = time.time()
    print("Generating mask from .jpg-images in mask-subfolder")
    data = skimage.io.ImageCollection('mask//*.jpg', conserve_memory=False, load_func=imread_rgb)
    if not data:
        print("Missing data, cannot find any mask-files in mask-subfolder.")
        exit(-1)
    image_series = [image for image in data]
    blended_image = blend_images(image_series)
    mask = skimage.util.img_as_ubyte(blended_image)
    skimage.io.imsave('mask.png', mask)
    end = time.time()
    print(f'Time used: {end - start:.2f} [s]')

if __name__ == "__main__":
    main()