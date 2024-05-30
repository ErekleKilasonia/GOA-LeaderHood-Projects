import pygame
import random

pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Runner')

# Clock and font
clock = pygame.time.Clock()
test_font = pygame.font.Font('data/Pixeltype.ttf', 50)

# Game state
game_active = True
start_time = 0

# Sets to store scores
sets = set([0])

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('data/images/Characters/michelangelo/walk1.png').convert_alpha()
        player_walk2 = pygame.image.load('data/images/Characters/michelangelo/walk2.png').convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load('data/images/Characters/michelangelo/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(200, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] and self.rect.bottom >= 300) or (keys[pygame.K_w] and self.rect.bottom >= 300):
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "fly":
            fly_frame1 = pygame.image.load('data/images/Characters/villain_fly/villain_fly1.png').convert_alpha()
            fly_frame2 = pygame.image.load('data/images/Characters/villain_fly/villain_fly2.png').convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210
        else:
            villain_surface = pygame.image.load('data/images/Characters/villain/villain1.png').convert_alpha()
            villain_surface1 = pygame.image.load('data/images/Characters/villain/villain1.png').convert_alpha()
            self.frames = [villain_surface, villain_surface1]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        if self.rect.right < 0:
            self.kill()

# Function to display score
def display_score():
    current_time = pygame.time.get_ticks() // 1000 - start_time
    sets.add(current_time)
    score_surf = test_font.render("Score: " + str(current_time), False, "#00008B")
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return [current_time, score_surf]

# Function to check collisions
def collisions(player, obstacles):
    global game_active
    if pygame.sprite.spritecollide(player.sprite, obstacles, False):
        return False
    return True

# Game variables
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Backgrounds and surfaces
sky_surface = pygame.image.load('data/images/Sky.png').convert()
black_sky_surface = pygame.image.load('data/images/black_Sky1.png').convert()

ground_surface = pygame.image.load('data/images/ground.png').convert()

score_surf = test_font.render('My game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

# Timer events
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

sky_change_timer = pygame.USEREVENT + 3
pygame.time.set_timer(sky_change_timer, 10000)

current_sky_surface = sky_surface
next_sky_surface = black_sky_surface
alpha = 255
fading = False
fade_speed = 5

# Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.sprite.rect.collidepoint(event.pos) and player.sprite.rect.bottom >= 300:
                    player.sprite.gravity = -20

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE and player.sprite.rect.bottom >= 300) or (event.key == pygame.K_w and player.sprite.rect.bottom >= 300):
                    player.sprite.gravity = -20

            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(random.choice(["fly", "villain"])))

            if event.type == sky_change_timer:
                fading = True
                if current_sky_surface == sky_surface:
                    next_sky_surface = black_sky_surface
                else:
                    next_sky_surface = sky_surface

    if game_active:
        current_time = display_score()[0]
        
        screen.blit(current_sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # Check collisions
        game_active = collisions(player, obstacle_group)

        clock.tick(60)
    else:
        max_score_surf = test_font.render("Max score: " + str(max(sets)), False, "#00008B")
        max_score_rect = max_score_surf.get_rect(center=(100 + len(str(max(sets))) * 3, 18))
        obstacle_group.empty()
        player.sprite.rect.midbottom = (80, 300)
        player.sprite.gravity = 0

        test_text = test_font.render("Press space to restart...", False, "#00008B")
        screen.blit(test_text, (220, 200))
        screen.blit(max_score_surf, max_score_rect)

        clock.tick(60)

    pygame.display.update()

pygame.quit()
