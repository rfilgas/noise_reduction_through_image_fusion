import cv2
import numpy as np
from skimage import exposure
from skimage.io import imread_collection

# Ryan Filgas
# Computational Photography
# Noise avoidance through image fusion

# Use a look up table to invert the image and apply a contrast curve
def apply_lut(img):
    #keep starting values as evenly distributed as possible
    lut_input = [0, 85,170, 255]
    #invert and ramp highlights and shadows closer to min and max to create a contrast curve
    lut_output = [255, 230, 35, 0]
    lut_result = np.uint8(np.interp(np.arange(0, 256), lut_input, lut_output))
    return cv2.LUT(img, lut_result)

# Convert input to rgb
def convert_input(img_1, img_2):
    img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
    img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
    return img_1, img_2

# Convert to greyscale, apply look up table, and return mask.
def generate_alpha_mask(img):
    img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_apply_lut = apply_lut(img_grayscale)
    img_alpha_mask  = np.uint8(np.clip(img_apply_lut,0,255))
    return img_alpha_mask

# Normalize luminosity mask to use points as transparency values
def merge_images(img_1, histogram_match, alpha_mask):
    alpha_mask_2 = (alpha_mask/255).reshape(*alpha_mask.shape,1)
    return np.uint8((img_1 * (1 - alpha_mask_2)) + (histogram_match * (alpha_mask_2)))


# To use the program, the user must provide an input directory in their project folder.
# There must be ordered sets of 2 where the first image is darker and the second is lighter.
# Image exposures should be far apart for best results and to avoid artifacts.
inputs = imread_collection('input/*.jpg')
i = 0
filename_count = 1
while i < len(inputs):
    #Step 1: Import and convert images to desired color space
    img_1, img_2 = convert_input(inputs[i], inputs[i+1])
    #Step 2: Convert base exposure to grayscale and generate an alpha mask.
    alpha_mask = generate_alpha_mask(img_2)
    #Step 3: Match histogram from brighter image to dark
    histogram_match = exposure.match_histograms(img_2, img_1, channel_axis=False)
    #Step 4: Composite images
    img_merged = merge_images(img_1, histogram_match, alpha_mask)

    #Step 5: Output results

    #Increase exposure to show noise in an example image.
    bright_result = cv2.convertScaleAbs(img_merged, alpha=6, beta=0)
    bright_original = cv2.convertScaleAbs(img_1, alpha=6, beta=0)

    #output all results to file
    input_filename = "output/" + str(filename_count) + "_1_input.jpg"
    input_filename2 = "output/" + str(filename_count) + "_2_input.jpg"
    matched_filename = "output/" + str(filename_count) + "_3_histogram_match.jpg"
    mask_filename = "output/" + str(filename_count) + "_4_alpha_mask.jpg"
    merged_filename = "output/" + str(filename_count) + "_5_merged.jpg"
    bright_input_filename = "output/" + str(filename_count) + "_6_bright_input.jpg"
    bright_output_filename = "output/" + str(filename_count) + "_7_bright_output.jpg"

    cv2.imwrite(input_filename,img_1)
    cv2.imwrite(input_filename2,img_2)
    cv2.imwrite(matched_filename,histogram_match)
    cv2.imwrite(mask_filename, alpha_mask)
    cv2.imwrite(merged_filename,img_merged)
    cv2.imwrite(bright_input_filename,bright_original)
    cv2.imwrite(bright_output_filename,bright_result)
    
    i += 2
    filename_count += 1
