import pygame

pygame.init()



SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
Fps = pygame.time.Clock()
#screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

class Nyx(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Data/images/Characters/Nyx/idle.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (200,500))
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.a_key_pressed = False
        self.a_key_was_pressed = False

        self.d_key_pressed = False
        self.d_key_was_pressed = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.a_key_pressed = True
                if event.key == pygame.K_d:
                    self.d_key_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.a_key_pressed = False
                    self.a_key_was_pressed = True
                if event.key == pygame.K_d:
                    self.d_key_pressed = False
                    self.d_key_was_pressed = True
        player_walk1_right = pygame.image.load('Data/images/Characters/Main/Right/Walk/walk1.png').convert_alpha()
        player_walk2_right = pygame.image.load('data/images/Characters/Main/Right/Walk/walk2.png').convert_alpha()
        player_walk1_left = pygame.image.load('Data/images/Characters/Main/Left/Walk/walk1.png').convert_alpha()
        player_walk2_left = pygame.image.load('data/images/Characters/Main/Left/Walk/walk2.png').convert_alpha()
        self.player_idle_left = pygame.image.load('data/images/Characters/Main/Left/idle.png').convert_alpha()
        self.player_idle_right = pygame.image.load('data/images/Characters/Main/Right/idle.png').convert_alpha()
        self.player_walk = [player_walk1_right,player_walk2_right,player_walk1_left,player_walk2_left]
        self.player_index = 0
        self.player_jump_right = pygame.image.load('data/images/Characters/Main/Right/jump.png').convert_alpha()
        self.player_jump_left = pygame.image.load('data/images/Characters/Main/Left/jump.png').convert_alpha()
        self.walk_left = False
        self.walk_right = False
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (700,500))
        self.gravity = 0
        if not self.a_key_pressed and self.a_key_was_pressed:
            self.a_key_was_pressed = False
        if not self.d_key_pressed and self.d_key_was_pressed:
            self.d_key_was_pressed = False
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]  and self.rect.bottom >= 500 or keys[pygame.K_w] and self.rect.bottom >= 500 :
            self.gravity = -20
        if keys[pygame.K_a] and self.rect.x >= 0:
            if self.a_key_pressed:
                self.walk_left = False
                self.walk_right = True
            else:
                self.walk_left = True
                self.walk_right = False
                self.a_key_was_pressed = True
                self.a_key_pressed = False
            self.rect.x -= 5
        if keys[pygame.K_d] and self.rect.x <= 950:
            if self.d_key_pressed:
                self.walk_left = True
                self.walk_right = False
            else:
                self.walk_left = False
                self.walk_right = True
                self.d_key_was_pressed = True
                self.d_key_pressed = False
            self.rect.x += 5
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
    def animation_state(self):
        keys = pygame.key.get_pressed()
        if self.rect.bottom < 500:
            if self.walk_right:
                self.image = self.player_jump_right
            else:
                self.image = self.player_jump_left
        else:
            if self.walk_right and self.rect.x <= 950:
                self.player_index += 0.1
                if self.player_index >= 2:self.player_index = 0
                if keys[pygame.K_d]:
                    self.image = self.player_walk[int(self.player_index)]
                else:
                    self.image = self.player_idle_right
            elif self.walk_left and self.rect.x >= 0:
                self.player_index += 0.05
                if self.player_index <= 2 or self.player_index>= 4:self.player_index = 2
                if keys[pygame.K_a]:
                    self.image = self.player_walk[int(self.player_index)]
                else:
                    self.image = self.player_idle_left
            
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()



player = pygame.sprite.GroupSingle()
player.add(Player())
nyx = pygame.sprite.GroupSingle()
nyx.add(Nyx())

def Main():
    #bg image
    bg = pygame.image.load("Data/Images/BgImage/Bg.png").convert()


    #sounds
    Main_sound = pygame.mixer.Sound("Data/Main.wav")

    #button images

    #play button
    P_button = pygame.image.load("Data/Images/Buttons/Play/Normal.png").convert_alpha()
    P_rect = P_button.get_rect(midbottom = (500,270))
    P_button_glow = pygame.image.load("Data/Images/Buttons/Play/Glow.png").convert_alpha()


    #Options button
    O_button = pygame.image.load("Data/Images/Buttons/Options/Normal.png").convert_alpha()
    O_rect = O_button.get_rect(midbottom = (500,380))
    O_button_glow = pygame.image.load("Data/Images/Buttons/Options/Glow.png").convert_alpha()

    #Quit button
    Q_button = pygame.image.load("Data/Images/Buttons/Quit/Normal.png").convert_alpha()
    Q_rect = Q_button.get_rect(midbottom = (500,480))
    Q_button_glow = pygame.image.load("Data/Images/Buttons/Quit/Glow.png").convert_alpha()


    #sound button
    S_button = pygame.image.load("Data/Images/Buttons/Sound/On/Normal.png").convert_alpha()
    S_rect = S_button.get_rect(midbottom = (970,70))
    S_button_glow = pygame.image.load("Data/Images/Buttons/Sound/On/Glow.png").convert_alpha()



    x = 0.1
    Sound_on = True


    run = True
    while run:
        Main_sound.set_volume(x)
        Main_sound.play(-1)
        screen.blit(bg,(0,0))
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if S_rect.collidepoint(mouse_x, mouse_y):
                    if Sound_on:
                        S_button = pygame.image.load("Data/Images/Buttons/Sound/Off/Normal.png").convert_alpha()
                        S_button_glow = pygame.image.load("Data/Images/Buttons/Sound/Off/Glow.png").convert_alpha()
                        x = 0
                        Sound_on = False

                    else:
                        S_button = pygame.image.load("Data/Images/Buttons/Sound/On/Normal.png").convert_alpha()
                        S_button_glow = pygame.image.load("Data/Images/Buttons/Sound/On/Glow.png").convert_alpha()
                        x = 0.1
                        Sound_on = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button:
                        click = True

                
                    
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if P_rect.collidepoint(mouse_x, mouse_y):
            screen.blit(P_button_glow,P_rect)
            if click:
                Play()
        else:
            screen.blit(P_button,P_rect)

        if O_rect.collidepoint(mouse_x, mouse_y):
            screen.blit(O_button_glow,O_rect)
                
        else:
            screen.blit(O_button,O_rect)

        if Q_rect.collidepoint(mouse_x, mouse_y):
            screen.blit(Q_button_glow,Q_rect)
            if click:
                pygame.quit()
        else:
            screen.blit(Q_button,Q_rect)
        if S_rect.collidepoint(mouse_x, mouse_y):
            screen.blit(S_button_glow,S_rect)
        else:
            screen.blit(S_button,S_rect)
        pygame.display.update()
        Fps.tick(60)
    pygame.quit()
def Play():
    run = True
    bg = pygame.image.load("Data/Images/BgImage/Bg_blur.png").convert()
    keys = pygame.key.get_pressed()


    #level1
    l1 = pygame.image.load("Data/Images/Buttons/Levels/Level1/Normal.png").convert_alpha()
    l1_glow = pygame.image.load("Data/Images/Buttons/Levels/Level1/Glow.png").convert_alpha()
    l1_rect = l1.get_rect(midbottom = (300,250))
    
    
    #locked levels
    x= 400
    locked = pygame.image.load("Data/Images/Buttons/Levels/Locked/Normal.png").convert_alpha()
    locked_glow = pygame.image.load("Data/Images/Buttons/Levels/Locked/Glow.png").convert_alpha()
    
   
    
    locked_rect_list1 = []
    for i in range(4):
        locked_rect = locked.get_rect(midbottom = (x,250))
        locked_rect_list1.append(locked_rect)
        x += 100
    locked_rect_list2 = []
    x = 300
    for i in range(5):
        locked_rect = locked.get_rect(midbottom = (x,350))
        locked_rect_list2.append(locked_rect)
        x += 100
    
    while run:
        click = False
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button:
                    click = True
        
        for i in range(4):
            if locked_rect_list1[i].collidepoint(mouse_x,mouse_y):
                screen.blit(locked_glow,locked_rect_list1[i])
            else:
                screen.blit(locked,locked_rect_list1[i])
        for i in range(5):
            if locked_rect_list2[i].collidepoint(mouse_x,mouse_y):
                screen.blit(locked_glow,locked_rect_list2[i])
            else:
                screen.blit(locked,locked_rect_list2[i])
        if l1_rect.collidepoint(mouse_x,mouse_y):
            screen.blit(l1_glow,l1_rect)
            if click:
                Level1()
        else:
            screen.blit(l1,l1_rect)
        pygame.display.update()
        Fps.tick(60)
def Level1():
    run = True
    bg = pygame.image.load("Data/Images/BgImage/Bg_blur.png").convert()
    agreement = pygame.image.load("Data/Images/Agreement/Agreement.png").convert_alpha()
    agreement_rect = agreement.get_rect(midbottom = (500,550))

    #I agree button
    agree = pygame.image.load("Data/Images/Agreement/Buttons/Agree/Normal.png").convert_alpha()
    agree_glow = pygame.image.load("Data/Images/Agreement/Buttons/Agree/Glow.png").convert_alpha()
    agree_rect = agree.get_rect(midbottom = (630,530))
    

    exits = pygame.image.load("Data/Images/Agreement/Buttons/Exit/Normal.png").convert_alpha()
    exits_glow = pygame.image.load("Data/Images/Agreement/Buttons/Exit/Glow.png").convert_alpha()
    exits_rect = exits.get_rect(midbottom = (350,530))


    while run:
        click = False
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button:
                    click = True
        
        screen.blit(bg,(0,0))
        screen.blit(agreement,agreement_rect)

        if exits_rect.collidepoint(mouse_x,mouse_y):
            screen.blit(exits_glow,exits_rect)
            if click:
                pygame.quit()
        else:
            screen.blit(exits,exits_rect)
        if agree_rect.collidepoint(mouse_x,mouse_y):
            screen.blit(agree_glow,agree_rect)    
            if click:
                Start()
        else:
            screen.blit(agree,agree_rect)
        
        pygame.display.update()
        Fps.tick(60)
def Start():
    surface = pygame.image.load("Data/Images/Level1-1/Bg images/surface.png").convert()
    bg = pygame.image.load("Data/Images/Level1-1/Bg images/background.png").convert()
    run = True
    type_font = pygame.font.Font('Data/Daydream.ttf')
    text_to_write = "Hello my friend, my name is"
    snip = type_font.render('',False,'white')
    counter = 0
    speed = 3
    while run:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if counter < speed * len(text_to_write):
            counter += 1
        elif counter >= speed * len(text_to_write):
            done = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        snip = type_font.render(text_to_write[0:counter//speed],False,'white')
        
            
        screen.blit(bg,(0,0))
        screen.blit(surface,(0,500))
        player.draw(screen)
        nyx.draw(screen)
        screen.blit(snip,(200,310))
        player.update()
        pygame.display.update()
        Fps.tick(60)
    

Main()