from PIL import Image
import os
from tqdm import tqdm
import glob

def resize_images_batch_in_memory(input_folder, target_size, batch_size=32):
    file_list = glob.glob(os.path.join(input_folder, '*.png'))

    num_files = len(file_list)

    resized_images = []
    resized_images_names = []

    batch_count = 0
    for i in range(0, num_files, batch_size):
        batch_count += 1
        batch_files = file_list[i:i + batch_size]

        for filename in tqdm(batch_files, desc=f"Processing batch {batch_count}"):
            img = Image.open(filename)

            # Resize while maintaining aspect ratio
            img.thumbnail((target_size[0], target_size[1]))

            # Create a new blank image with the target size and fill with black
            new_img = Image.new("RGB", target_size, "black")
            new_img.paste(img, ((target_size[0] - img.width) // 2, (target_size[1] - img.height) // 2))

            # Append the resized image to the list
            resized_images.append(new_img)
            resized_images_names.append(os.path.basename(filename))

    return resized_images, resized_images_names

def save_resized_images(resized_images, output_folder, filenames):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    i = 0
    for img in tqdm(resized_images, desc="Saving Files"):
        filename_without_extension = os.path.splitext(filenames[i])[0]
        output_path = os.path.join(output_folder, f"{filename_without_extension}p.png") 

        #output_path = os.path.join(output_folder, filenames[i]) 
        img.save(output_path)
        i += 1

if __name__ == "__main__":
    input_folder = r"C:\Users\easha\Downloads\Prelim Detection Dataset\train\images"  # Replace with the path to your input folder
    #input_folder = r"C:\Users\easha\Downloads\Dataset-Tesselation\Dataset-Tesselation\train\images"  # Replace with the path to your input folder
    output_folder = r"C:\Users\easha\Downloads\Dataset-Tesselation\Dataset-Tesselation\train\imagesResized"  # Replace with the path to your output folder
    target_size = (640, 360)
    batch_size = 7000  # You can adjust the batch size based on your system's capacity

    print("Resizing Images...")
    resized_images, filenames = resize_images_batch_in_memory(input_folder, target_size, batch_size)
    #print(f"List size: {len(resized_images)}, {len(filenames)}")
    #print("Saving Files....")
    save_resized_images(resized_images, output_folder, filenames)