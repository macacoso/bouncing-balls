import pygame
import random
import time

class Bola:
    def __init__(self, tamanho, pos_x, pos_y, velocidade):
        self.tamanho = tamanho
        self.rect = pygame.Rect(pos_x, pos_y, tamanho, tamanho)
        self.velocidade = velocidade
        self.cor = random_color()
        self.hit_time = 0
    
    def move(self, dt):
        self.rect.y += self.velocidade * dt

    def bounce(self, accel, limite_velocidade, frame_time):
        if self.velocidade < 0:
            movement = 3
            if abs(self.velocidade) < limite_velocidade:
                self.velocidade += - accel
        else:
            movement = -3
            if abs(self.velocidade) < limite_velocidade:
                self.velocidade += accel
        self.rect.y += movement
        self.velocidade = -self.velocidade
        self.cor = random_color()
        self.hit_time = frame_time

    def render(self, screen, frame_time):
        circle_color = "white" if frame_time - self.hit_time < 0.1 else self.cor
        pygame.draw.circle(screen, circle_color, (self.rect.x + self.tamanho / 2, self.rect.y + self.tamanho / 2), self.tamanho / 2)
        #pygame.draw.rect(screen, "green", self.rect)

def random_color():
    red = random.randrange(0, 255)
    green = random.randrange(0, 255)
    blue = random.randrange(0, 255)
    return pygame.Color(red, green, blue)

pygame.font.init()
pygame.mixer.init()

#execucao
clock = pygame.time.Clock()
dt = 0
running = True
hit_time = 0
bounce_counter = 0
font = pygame.font.Font(None, 64)
sound = pygame.mixer.Sound("bounce.wav")
initial_time = time.monotonic()
last_decrease = 0
random_num = 1

#imagem
screen = pygame.display.set_mode((1750, 950))
background = pygame.image.load('bg2.png')

#tamanhos
tamanho = 40
rettamanho = 110
parede_top = pygame.Rect(0, 0, screen.get_width(), rettamanho)
parede_bot = pygame.Rect(0, screen.get_height() - rettamanho, screen.get_width(), rettamanho)
players = [
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450))
]
limite = 370
    
#velocidade
accel = 100
limite_velocidade = 800

#cor
parede_cor = pygame.Color(123, 96, 107)
sounds = [] 
for i in range(0, 13):
    sounds.append(pygame.mixer.Sound(f"Retro Instrument - crystal - C{i}.wav"))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                initial_time = frame_time 
                bounce_counter = 0
                parede_top = pygame.Rect(0, 0, screen.get_width(), rettamanho)
                parede_bot = pygame.Rect(0, screen.get_height() - rettamanho, screen.get_width(), rettamanho)
                players = [
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),                        Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450)),
                    Bola(tamanho, (screen.get_width() - tamanho) / 2 + random.randrange(-800, 800), (screen.get_height() - tamanho) / 2 + random.randrange(-300, 300), random.randrange(100, 450))
                ]
    frame_time = time.monotonic()
    current_time = frame_time - initial_time

    for player in players:
        player.move(dt)
        if parede_top.colliderect(player.rect) or parede_bot.colliderect(player.rect):
            player.bounce(accel, limite_velocidade, frame_time)
            bounce_counter += 1
            random_sound = random.choice(sounds)
            channel = sound.play()
        
    #teste decrease com o tempo    
    if parede_top.y < limite and frame_time - last_decrease > 0.1:
                parede_top = parede_top.move(0, 1)
                parede_bot = parede_bot.move(0, -1)
                last_decrease = frame_time

    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, parede_cor, parede_top)
    pygame.draw.rect(screen, parede_cor, parede_bot)
    
    for player in players:
        player.render(screen, frame_time)
        
    text = font.render(f"Bounces: {bounce_counter}", True, (255, 255, 255))
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=10)    
    screen.blit(text, textpos)

    text2 = font.render(f"Time: {current_time:.2f}", True, (255, 255, 255))
    textpos2 = text.get_rect(centerx=screen.get_width() / 2, y=screen.get_height() - 75)    
    screen.blit(text2, textpos2)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()