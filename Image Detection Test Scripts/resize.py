from PIL import Image
import os
import time

def resize_images_yolo(input_folder, output_folder, target_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    counter = 0
    tic = time.time()

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            counter += 1
            if(counter % 10 == 0):
                print(f"{counter}/6912")
                elapsed = time.time() - tic
                time_estimate = (elapsed * 691.2)/3600.0
                print(f"Estimated Time: {time_estimate} hours")
                tic = time.time()

            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            img = Image.open(input_path)

            # Resize while maintaining aspect ratio
            img.thumbnail((target_size[0], target_size[1]))

            # Create a new blank image with the target size and fill with black
            new_img = Image.new("RGB", target_size, "black")
            new_img.paste(img, ((target_size[0] - img.width) // 2, (target_size[1] - img.height) // 2))

            # Save the resized image
            new_img.save(output_path)

if __name__ == "__main__":
    input_folder = r"C:\Users\easha\Downloads\Dataset-Tesselation\Dataset-Tesselation\valid\images"  # Replace with the path to your input folder
    output_folder = r"C:\Users\easha\Downloads\Dataset-Tesselation\Dataset-Tesselation\valid\imagesResized"  # Replace with the path to your output folder
    target_size = (640, 360)

    resize_images_yolo(input_folder, output_folder, target_size)
