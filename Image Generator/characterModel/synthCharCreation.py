import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Letter Placement")

# Load character images and labels
character_images = []
character_labels = []
character_dir = "practiceData"
label_dir = "practiceLabels"

for filename in os.listdir(character_dir):
    if filename.endswith(".png"):
        image_path = os.path.join(character_dir, filename)
        character_image = pygame.image.load(image_path)
        character_images.append(character_image)

        label_filename = os.path.splitext(filename)[0] + ".txt"
        label_path = os.path.join(label_dir, label_filename)
        with open(label_path, 'r') as file:
            data = file.read().splitlines()
            label_id = int(data[0].split()[0])  # Extract the first number (label ID)
        character_labels.append(label_id)

# Load shape images
shape_images = []
shape_dir = "outputShape"
for filename in os.listdir(shape_dir):
    if filename.endswith(".png"):
        image_path = os.path.join(shape_dir, filename)
        shape_images.append(pygame.image.load(image_path))

# Load background images
background_images = []
background_dir = "backgroundData"
for filename in os.listdir(background_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        image_path = os.path.join(background_dir, filename)
        background_image = pygame.image.load(image_path)
        background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        background_images.append(background_image)

# Create directories to save the images and labels
output_dir = "output"
label_output_dir = "labels"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(label_output_dir):
    os.makedirs(label_output_dir)

# Game loop
running = True
image_count = 0
character_index = 0
background_index = 0
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current background image
    background_image = background_images[background_index]
    window.blit(background_image, (0, 0))  # Blit the background image

    placed_images = []
    for _ in range(10):
        if character_index >= len(character_images):
            break

        character_image = character_images[character_index]
        character_rect = character_image.get_rect()

        # Find a random position that doesn't overlap with existing images
        overlap = True
        while overlap:
            character_rect.topleft = (
                random.randint(0, WINDOW_WIDTH - character_rect.width),
                random.randint(0, WINDOW_HEIGHT - character_rect.height),
            )
            overlap = False
            for placed_image_rect in placed_images:
                if placed_image_rect.colliderect(character_rect):
                    overlap = True
                    break

        if not overlap:
            # Randomly choose a shape image
            shape_image = random.choice(shape_images)
            shape_rect = shape_image.get_rect()
            shape_rect.size = (character_rect.width * 2, character_rect.height * 2)
            shape_image = pygame.transform.scale(shape_image, shape_rect.size)

            # Check for overlap with existing shapes
            shape_overlap = True
            while shape_overlap:
                shape_rect.center = character_rect.center
                shape_overlap = False
                for placed_image_rect in placed_images:
                    if placed_image_rect.colliderect(shape_rect):
                        shape_overlap = True
                        character_rect.topleft = (
                            random.randint(0, WINDOW_WIDTH - character_rect.width),
                            random.randint(0, WINDOW_HEIGHT - character_rect.height),
                        )
                        break

            # Place the shape image on the background
            window.blit(shape_image, shape_rect)

            # Place the character image on top of the shape image
            window.blit(character_image, character_rect)
            placed_images.append(shape_rect)  # Add the shape rect to the list of placed images

            character_index += 1

    # Save the image
    image_count += 1
    output_path = os.path.join(output_dir, f"output_{image_count}.png")
    label_output_path = os.path.join(label_output_dir, f"output_{image_count}.txt")
    pygame.image.save(window, output_path)

    # Save the labels for the current image
    with open(label_output_path, "w") as f:
        for placed_image_rect in placed_images:
            label_id = character_labels[character_index - placed_images.index(placed_image_rect) - 1]
            x_center = (placed_image_rect.left + placed_image_rect.right) / (2 * WINDOW_WIDTH)
            y_center = (placed_image_rect.top + placed_image_rect.bottom) / (2 * WINDOW_HEIGHT)
            width = placed_image_rect.width / WINDOW_WIDTH
            height = placed_image_rect.height / WINDOW_HEIGHT
            label_data = f"{label_id} {x_center} {y_center} {width} {height}\n"
            f.write(label_data)

    # Update the display
    pygame.display.update()

    # Fill the window with black color after saving the image
    window.fill((0, 0, 0))

    # Move to the next background image
    background_index = (background_index + 1) % len(background_images)

    # Quit Pygame if all character images have been used
    if character_index >= len(character_images):
        running = False

# Quit Pygame
pygame.quit()