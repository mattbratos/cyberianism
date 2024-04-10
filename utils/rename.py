import os

# Define the folder containing the images
folder_path = '../cible/assets/madness'  # Change this to your folder's path

# List all files in the folder
files = os.listdir(folder_path)

# Filter out non-image files, specifically looking for .webp files
image_extensions = ['.webp']
images = [file for file in files if any(file.endswith(ext) for ext in image_extensions)]

# Rename images and generate Markdown syntax for each new image name
markdown_lines = []
for index, image in enumerate(images, start=1):
    # Generate the new file name
    new_name = f"{os.path.basename(folder_path)}_{index}.webp"
    new_path = os.path.join(folder_path, new_name)

    # Rename the file (commented out for safety in this demonstration)
    os.rename(os.path.join(folder_path, image), new_path)

    # Create Markdown line for the renamed image
    markdown_line = f'![{os.path.basename(folder_path)}_{index}](./{folder_path}/{new_name})'
    markdown_lines.append(markdown_line)

# Join the lines to form the final Markdown text
markdown_text = '\n'.join(markdown_lines)

print(markdown_text)
