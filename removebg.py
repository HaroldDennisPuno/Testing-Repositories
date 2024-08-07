import cv2 as cv
from rembg import remove
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def main():
    # Create a Tkinter root window (it won't be shown)
    root = Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
    )

    if not file_path:
        print("No file selected. Exiting.")
        return

    # Read the selected image
    image = cv.imread(file_path)
    if image is None:
        print("Error: Unable to read the image file.")
        return

     #Convert the image to RGB (OpenCV loads images in BGR by default)
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # Remove the background using the RGB image
    new_image = remove(image_rgb)

    # Convert the new image to RGB in case it's returned in RGBA
    new_image_rgb = cv.cvtColor(new_image, cv.COLOR_RGBA2RGB)

    # Save the images
    output_path_original = "original_image.jpg"
    output_path_removed = "new_image.jpg"
    cv.imwrite(output_path_original, cv.cvtColor(image_rgb, cv.COLOR_RGB2BGR))
    cv.imwrite(output_path_removed, cv.cvtColor(new_image_rgb, cv.COLOR_RGB2BGR))

    # Display the images using Matplotlib
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(new_image_rgb)
    plt.title('Image with Background Removed')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()