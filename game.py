import pygame
import os
import random

pygame.init()

sfondo = pygame.image.load("images/background.png")
uccello = pygame.image.load("images/bird.png")
base = pygame.image.load("images/base.png")
gameover = pygame.image.load("images/gameover.png")
tubo_giu = pygame.image.load("images/tube.png")
tubo_su = pygame.transform.flip(tubo_giu, False, True)

pygame.mixer.music.load("audio/music.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1, 0.0, 5000)
print("[Flappy] Music loaded.")

schermo = pygame.display.set_mode((288, 512))
FPS = 50
VEL_AVANZ = 3

class tubi_classe:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75,150)
    def avanza_e_disegna(self):
        self.x -= VEL_AVANZ 
        schermo.blit(tubo_giu, (self.x,self.y+210))
        schermo.blit(tubo_su, (self.x,self.y-210))
    def collisione(self, uccello, uccellox, uccelloy):
        tolleranza = 5 
        uccello_lato_dx = uccellox+uccello.get_width()-tolleranza 
        uccello_lato_sx = uccellox+tolleranza 
        tubi_lato_dx = self.x + tubo_giu.get_width()
        tubi_lato_sx = self.x 
        uccello_lato_su = uccelloy+tolleranza 
        uccello_lato_giu = uccelloy+uccello.get_height()-tolleranza
        tubi_lato_su = self.y+110 
        tubi_lato_giu = self.y+210
        if uccello_lato_dx > tubi_lato_sx and uccello_lato_sx < tubi_lato_dx:
            if uccello_lato_su < tubi_lato_su or uccello_lato_giu > tubi_lato_giu:
                hai_perso()


def disegna_oggetti():
    schermo.blit(sfondo, (0,0))
    for t in tubi:
        t.avanza_e_disegna()
    schermo.blit(uccello, (uccellox,uccelloy))
    schermo.blit(base, (basex,400))

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def inizializza():
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi
    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    basex = 0
    tubi = []
    tubi.append(tubi_classe())

def hai_perso():
    schermo.blit(gameover, (50,180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()    

inizializza() 

while True:
    basex -= VEL_AVANZ  
    if basex < -45: basex = 0
    uccello_vely += 1 
    uccelloy += uccello_vely
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            uccello_vely = -10
        if event.type == pygame.QUIT:
            pygame.quit()     
    if tubi[-1].x < 150: tubi.append(tubi_classe())
    max_tubix = 0
    for t in tubi:
        t.collisione(uccello, uccellox, uccelloy)
    if uccelloy > 380:
        hai_perso()        
    disegna_oggetti()
    aggiorna()
