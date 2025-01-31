import pygame
import random
import tkinter as tk
from tkinter import messagebox

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 4
CARD_SIZE = WIDTH // GRID_SIZE
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Load Pygame sounds
pygame.mixer.init()
flip_sound = pygame.mixer.Sound("flipcard.wav")
match_sound = pygame.mixer.Sound("match.wav")

def generate_cards():
    """Generate shuffled card pairs."""
    numbers = list(range(1, (GRID_SIZE * GRID_SIZE // 2) + 1)) * 2
    random.shuffle(numbers)
    return [numbers[i * GRID_SIZE:(i + 1) * GRID_SIZE] for i in range(GRID_SIZE)]

class MemoryGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Memory Puzzle Game")
        self.running = True
        self.cards = generate_cards()
        self.revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.first_pick = None
        self.second_pick = None
        self.matched_pairs = 0
        
    def draw_grid(self):
        """Draw the game grid."""
        self.screen.fill(WHITE)
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x, y = col * CARD_SIZE, row * CARD_SIZE
                if self.revealed[row][col]:
                    pygame.draw.rect(self.screen, GRAY, (x, y, CARD_SIZE, CARD_SIZE))
                    number = self.cards[row][col]
                    font = pygame.font.Font(None, 50)
                    text = font.render(str(number), True, BLACK)
                    self.screen.blit(text, (x + 20, y + 20))
                else:
                    pygame.draw.rect(self.screen, BLACK, (x, y, CARD_SIZE, CARD_SIZE))
                pygame.draw.rect(self.screen, WHITE, (x, y, CARD_SIZE, CARD_SIZE), 2)
        pygame.display.flip()

    def check_match(self):
        """Check if two selected cards match."""
        if self.first_pick and self.second_pick:
            r1, c1 = self.first_pick
            r2, c2 = self.second_pick
            if self.cards[r1][c1] == self.cards[r2][c2]:
                self.matched_pairs += 1
                match_sound.play()
            else:
                pygame.time.delay(500)
                self.revealed[r1][c1] = False
                self.revealed[r2][c2] = False
            self.first_pick, self.second_pick = None, None

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.draw_grid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.second_pick:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // CARD_SIZE, x // CARD_SIZE
                    if not self.revealed[row][col]:
                        flip_sound.play()
                        self.revealed[row][col] = True
                        if not self.first_pick:
                            self.first_pick = (row, col)
                        else:
                            self.second_pick = (row, col)
                            self.check_match()
            if self.matched_pairs == (GRID_SIZE * GRID_SIZE) // 2:
                self.running = False
            clock.tick(FPS)
        pygame.quit()
        show_game_over()

# Tkinter Start Screen
def start_game():
    root.destroy()
    game = MemoryGame()
    game.run()

# Tkinter Game Over Screen
def show_game_over():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Game Over", "Congratulations! You've matched all pairs.")
    root.destroy()

# Tkinter Main Menu
root = tk.Tk()
root.title("Memory Puzzle Game")
tk.Label(root, text="Memory Puzzle Game", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="Start Game", command=start_game, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12)).pack(pady=5)
root.mainloop()