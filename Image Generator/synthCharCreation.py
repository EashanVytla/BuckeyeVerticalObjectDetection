import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Letter Placement")

# Load letter images
letter_images = {}
char_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in char_list:
    image = pygame.image.load(f"characters/{char}.png")
    letter_images[char] = image

# Load background images
background_images = []
for filename in os.listdir("backgrounds"):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        background_images.append(pygame.image.load(os.path.join("backgrounds", filename)))

# Create a directory to save the images
output_dir = "output_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Game loop
running = True
image_count = 0
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for background_image in background_images:
        characters = list(char_list)
        random.shuffle(characters)
        placed_images = []
        for _ in range(10):
            if not characters:
                break

            char = characters.pop()
            image = letter_images[char]
            image_rect = image.get_rect()

            # Find a random position that doesn't overlap with existing images
            overlap = True
            while overlap:
                image_rect.topleft = (
                    random.randint(0, WINDOW_WIDTH - image_rect.width),
                    random.randint(0, WINDOW_HEIGHT - image_rect.height),
                )
                overlap = False
                for placed_image_rect in placed_images:
                    if placed_image_rect.colliderect(image_rect):
                        overlap = True
                        break

            if not overlap:
                window.blit(image, image_rect)
                placed_images.append(image_rect)

        # Save the image
        image_count += 1
        output_path = os.path.join(output_dir, f"output_{image_count}.png")
        pygame.image.save(window, output_path)

        # Clear the window for the next background
        window.fill((0, 0, 0))

    # Quit Pygame
    pygame.quit()