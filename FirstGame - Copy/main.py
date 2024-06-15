import pygame
import random
import asyncio


sets = set([0])
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('data/images/Characters/michelangelo/walk1.png').convert_alpha()
        player_walk2 = pygame.image.load('data/images/Characters/michelangelo/walk2.png').convert_alpha()
        self.player_walk = [player_walk1,player_walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load('data/images/Characters/michelangelo/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound("data/sfx/jump.wav")
        self.jump_sound.set_volume(0.3)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300 or keys[pygame.K_w] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
        if keys[pygame.K_a] and self.rect.x >= 0:
            self.rect.x -= 5
        if keys[pygame.K_d] and self.rect.x <= 760:
            self.rect.x += 5
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
            if self.player_index >= len(self.player_walk):self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

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
        self.delete()
    def delete(self):
        if self.rect.x <= 0:
            self.kill()


def display_score():
    current_time = pygame.time.get_ticks()//1000 - start_time
    sets.add(current_time)
    score_surf = test_font.render("Score: " +str(current_time),False,"#00008B")
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return [current_time,score_surf]

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else:return True

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('data/Pixeltype.ttf', 50)
game_active = True      
start_time = 0

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


sky_surface = pygame.image.load('data/images/Sky.png').convert()
black_sky_surface = pygame.image.load('data/images/black_Sky1.png').convert()

ground_surface = pygame.image.load('data/images/ground.png').convert()
# black_ground_surface = pygame.image.load('data/images/black_ground.png').convert()

score_surf = test_font.render('My game',False, (64,64,64))
score_rect = score_surf.get_rect(center = (400, 50))

#obstacle

villain_surface = pygame.image.load('data/images/Characters/villain/villain1.png').convert_alpha()


#villain fly
fly_frame1 = pygame.image.load('data/images/Characters/villain_fly/villain_fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('data/images/Characters/villain_fly/villain_fly2.png').convert_alpha()
fly_frames = [fly_frame1,fly_frame2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]


obstacle_rec_list = []

#player

player_walk1 = pygame.image.load('data/images/Characters/michelangelo/walk1.png').convert_alpha()
player_walk2 = pygame.image.load('data/images/Characters/michelangelo/walk2.png').convert_alpha()
player_walk = [player_walk1,player_walk2]
player_index = 0
player_jump = pygame.image.load('data/images/Characters/michelangelo/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_grav = 0

#max score
max_score_surf = test_font.render("Max score: "+ str(max(sets)), False, "#00008B")
max_score_rect = max_score_surf.get_rect(center = (100,18))



# timer
obsticle_timer = pygame.USEREVENT + 1

pygame.time.set_timer(obsticle_timer,1200)


fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer,200)

sky_change_timer = pygame.USEREVENT + 3
pygame.time.set_timer(sky_change_timer, 50000)

current_sky_surface = sky_surface
next_sky_surface = black_sky_surface
alpha = 255
fading = False
fade_speed = 5  


run = True
async def main():
    global run
    global current_sky_surface
    global next_sky_surface
    global alpha
    global fading
    global fade_speed
    global game_active
    global max_score_rect
    global max_score_surf
    global start_time

    
    while run:
        key = pygame.key.get_pressed()
        speed_changer = 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                run = False
                
                
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_active:
                    game_active = True
                    start_time  = pygame.time.get_ticks()//1000
                    current_sky_surface = sky_surface
                    next_sky_surface = black_sky_surface
                    alpha = 255
                    fading = False
                    fade_speed = 5  
                    player.sprite.rect.midbottom = (80,300)
                    player.sprite.gravity = 0
            if game_active:
                if event.type == obsticle_timer:
                    obstacle_group.add(Obstacle(random.choice(["fly","villain"])))
                if event.type == sky_change_timer:
                    fading = True
                    if current_sky_surface == sky_surface:
                        next_sky_surface = black_sky_surface
                    else:
                        next_sky_surface = sky_surface
            
        if game_active:
            current_time = display_score()[0]
            if fading:
                alpha -= fade_speed
                if alpha <= 0:
                    alpha = 255
                    fading = False
                    current_sky_surface = next_sky_surface
                fade_surface = current_sky_surface.copy()
                fade_surface.set_alpha(alpha)
                screen.blit(next_sky_surface, (0, 0))
                screen.blit(fade_surface, (0, 0))
            else:
                screen.blit(current_sky_surface, (0, 0))
            
            screen.blit(ground_surface, (0, 300))
            screen.blit(max_score_surf, max_score_rect)


            display_score()
            

            #player
            player.draw(screen)
            player.update()

            #obstacle
            obstacle_group.draw(screen)
            obstacle_group.update()


            #collision


            game_active = collision_sprite()
            #speed
            speed_changer += 0.05
            clock.tick(speed_changer)
        else:
            max_score_surf = test_font.render("Max score: "+ str(max(sets)), False, "#00008B")
            max_score_rect = max_score_surf.get_rect(center = (100 + len(str(max(sets)))* 3,18))

            speed_changer = 60
            pygame.time.set_timer(sky_change_timer, 50000)
            test_text = test_font.render(("Press space to restart..."), False, 	"#00008B")
            screen.blit(test_text,(220,200))
            if current_sky_surface == black_sky_surface:
                pygame.draw.rect(screen, "#262c2d", max_score_rect)
                pygame.draw.rect(screen, "#262c2d", max_score_rect, 12)
            else:
                pygame.draw.rect(screen, "#d0f4f7", max_score_rect)
                pygame.draw.rect(screen, "#d0f4f7", max_score_rect, 12)
            screen.blit(max_score_surf,max_score_rect)
            
            clock.tick(speed_changer)
        pygame.display.update()
        await asyncio.sleep(0)

        
        

    pygame.quit()
asyncio.run(main())