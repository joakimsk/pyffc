import numpy as np
import skimage

def imread_rgb(f):
    '''
    Function used to read in rgb images properly through
    skimage ImageCollection.
    '''
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
    print("Generating mask from .jpg-images in mask-subfolder")
    data = skimage.io.ImageCollection('mask//*.jpg', conserve_memory=False, load_func=imread_rgb)
    if not data:
        print("Missing data, cannot find any mask-files in mask-subfolder.")
        exit(-1)
    image_series = [image for image in data]
    blended_image = blend_images(image_series)
    mask = skimage.util.img_as_ubyte(blended_image)
    skimage.io.imsave('mask.png', mask)

if __name__ == "__main__":
    main()