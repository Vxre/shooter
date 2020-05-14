import pygame as py
from game import Game
py.init()

#Fenetre
py.display.set_caption("Shooter Groot")
screen = py.display.set_mode((1080,720))

#Background
background = py.image.load('assets/bg.jpg')

#Charger game
game = Game()

running = True

#Boucle infini
while running:

    #Afficher le background
    screen.blit(background,(0,-200))
    
    #Afficher Joueur
    screen.blit(game.player.image, game.player.rect)

    #Afficher Projectiles
    game.player.all_projectiles.draw(screen)

    #Verifier si touche 
    if game.pressed.get(py.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    if game.pressed.get(py.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    #Update l'affichage
    py.display.flip()

    #Fermeture fenetre
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
            py.quit()
        #Si touche presser
        elif event.type == py.KEYDOWN:
            game.pressed[event.key] = True

            #Si Space est presser
            if event.key == py.K_SPACE:
                game.player.launch_projectile()
                
        elif event.type == py.KEYUP:
            game.pressed[event.key] = False