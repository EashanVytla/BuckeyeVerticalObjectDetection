import os
import shutil

def copy_and_rename_text_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of all text files in the input directory
    text_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

    for text_file in text_files:
        # Create the input and output file paths
        input_path = os.path.join(input_dir, text_file)
        output_path = os.path.join(output_dir, f"{os.path.splitext(text_file)[0]}p.txt")

        # Copy the file to the output directory with the new name
        shutil.copy2(input_path, output_path)

if __name__ == "__main__":
    input_directory = r"C:\Users\easha\Downloads\Prelim Detection Dataset\valid\labels"  # Replace with the path to your input directory
    output_directory = r"C:\Users\easha\Downloads\Dataset-Tesselation\Dataset-Tesselation\valid\labels"  # Replace with the path to your output directory

    copy_and_rename_text_files(input_directory, output_directory)