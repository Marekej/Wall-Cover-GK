import pygame
import sys
import random
import math

class Rectangle:
    def __init__(self, width, height, x, y, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

def calculate_rectangles_for_field(width, height, rectangle_width, rectangle_height):
    rectangles = []

    def add_rectangle(x, y, width, height):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rectangles.append(Rectangle(width, height, x, y, color))

    x = 50
    y = 50

    while y < height + 50:
        while x < width + 50:
            rect_width = min(rectangle_width, width - x + 50)
            rect_height = min(rectangle_height, height - y + 50)
            add_rectangle(x, y, rect_width, rect_height)
            x += rect_width
        x = 50
        y += rectangle_height

    return rectangles

def draw_field(screen, field_width, field_height, rectangles, max_rectangles, min_rectangles):
    # Draw canvas
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, field_width + 100, field_height + 150))

    # Draw field edges
    pygame.draw.rect(screen, (0, 0, 0), (50, 50, field_width, field_height), 3)

    # Draw rectangles
    font = pygame.font.Font(None, 20)
    for idx, rect in enumerate(rectangles, start=1):
        pygame.draw.rect(screen, rect.color, (rect.x, rect.y, rect.width, rect.height), 2)

        # Display rectangle number and dimensions
        text_surface = font.render(f"{idx}\n{rect.width}x{rect.height}", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(rect.x + rect.width // 2, rect.y + rect.height // 2))
        screen.blit(text_surface, text_rect)

    # Display legend
    legend_font = pygame.font.Font(None, 24)
    legend_text = f"Max Rectangles: {max_rectangles} | Min Rectangles: {min_rectangles}"
    legend_surface = legend_font.render(legend_text, True, (0, 0, 0))
    screen.blit(legend_surface, (50, field_height + 120))

def main():
    # Get user input for field dimensions and rectangle dimensions
    field_width = int(input("Enter the field width in pixels: "))
    field_height = int(input("Enter the field height in pixels: "))
    rectangle_width = 120
    rectangle_height = 200

    # Calculate and display the result
    rectangles = calculate_rectangles_for_field(field_width, field_height, rectangle_width, rectangle_height)

    # Calculate maximum and minimum number of rectangles
    max_rectangles = len(rectangles)
    min_rectangles = math.ceil((field_width * field_height) / (rectangle_width * rectangle_height))

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((field_width + 100, field_height + 200))
    pygame.display.set_caption('Field Filling with Rectangles')

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the field with rectangles and legend
        draw_field(screen, field_width, field_height, rectangles, max_rectangles, min_rectangles)
        pygame.display.flip()

if __name__ == "__main__":
    main()
