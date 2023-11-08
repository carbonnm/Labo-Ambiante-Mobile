import pygame
import keyboard

pygame.mixer.pre_init(44100,-16,2,2048)
pygame.mixer.init()
ambi1 = pygame.mixer.Sound('test.wav')
ambi2 = pygame.mixer.Sound('test.wav')
ambi3 = pygame.mixer.Sound('test.wav')
ambi4 = pygame.mixer.Sound('test.wav')
sound1 = pygame.mixer.Sound('test.wav')
sound2 = pygame.mixer.Sound('test.wav')

def run(c1,c2):
    while True:     
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
            c1.play(ambi1,loops=-1)
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'x':
            c1.play(ambi2,loops=-1)
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'c':
            c1.play(ambi3,loops=-1)
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'v':
            c1.play(ambi4,loops=-1)
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'b':
            c1.stop()
        elif event.event_type == keyboard.KEY_DOWN and event.name == 's':
            c2.play(sound1)
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'q':
            c2.play(sound2)

c1 = pygame.mixer.Channel(1)
c2 = pygame.mixer.Channel(2)
run(c1,c2)