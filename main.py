import math
import pygame
import sys

pygame.init()
blue = (153, 204, 255)
red = (255, 0, 0)
green = (0, 250, 50)
black = (0, 0, 0)

fps = 30
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((700, 700))
font = pygame.font.SysFont("Times new Roman", 40)
msgWin = font.render("You Win!", True, black)
pygame.display.set_caption("Traffic Crossing Game")

line1Start = (0, 100)
line1End = (700, 100)

line2Start = (0, 600)
line2End = (700, 600)

playerImg = pygame.image.load('man.png')
playerX = 30
playerY = 20
playerStep = 5

bikeImg = pygame.image.load('motorbike.png')
bikeX = 100
bikeY = 400
bikeStep = 15

redcarImg = pygame.image.load('sport-car.png')
redcarX = 300
redcarY = 200
redcarstep = 10

yellowcarImg = pygame.image.load('car.png')
yellowcarX = 50
yellowcarY = 250
yellowcarstep = 7

scootyImg = pygame.image.load('motorcycle.png')
scootyX = 30
scootyY = 350
scootystep = 12

fastdeliveryImg = pygame.image.load('fast-delivery.png')
fastdeliveryX = 400
fastdeliveryY = 500
fastdeliverystep = 15

def player():
    screen.blit(playerImg, (playerX, playerY))


def redcar():
    screen.blit(redcarImg, (redcarX, redcarY))


def yellowcar():
    screen.blit(yellowcarImg, (yellowcarX, yellowcarY))


def scooty():
    screen.blit(scootyImg, (scootyX, scootyY))


def bike():
    screen.blit(bikeImg, (bikeX, bikeY))


def fastdelivery():
    screen.blit(fastdeliveryImg, (fastdeliveryX, fastdeliveryY))


def isCollision(carX, carY, playerX, playerY):
    distance = math.sqrt(math.pow(carX - playerX, 2) + (math.pow(carY - playerY, 2)))
    if distance < 30:
        return True
    return False


while True:

    screen.fill(blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    player()
    redcar()
    yellowcar()
    scooty()
    pygame.draw.line(screen, black, line1Start, line1End, 3)
    pygame.draw.line(screen, black, line2Start, line2End, 3)
    if playerY >= 80:
        redcarX += redcarstep
        if redcarX < 0:
            redcarstep = 10
        elif redcarX > 650:
            redcarstep = -10

        yellowcarX += yellowcarstep
        if yellowcarX < 0:
            yellowcarstep = 7
        elif yellowcarX > 650:
            yellowcarstep = -7

        scootyX += scootystep
        if scootyX < 0:
            scootystep = 12
        elif scootyX > 650:
            scootystep = -12

        if playerY > 350:
            bike()
            fastdelivery()

            bikeX += bikeStep
            if bikeX < 0:
                bikeStep = 15
            elif bikeX > 650:
                bikeStep = -15

            fastdeliveryX += fastdeliverystep
            if fastdeliveryX < 0:
                fastdeliverystep = 20
            elif fastdeliveryX > 650:
                fastdeliverystep = -20

    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        if playerX > 0:
            playerX -= playerStep
    if key_input[pygame.K_RIGHT]:
        if playerX < 650:
            playerX += playerStep
    if key_input[pygame.K_UP]:
        if playerY > 0:
            playerY -= playerStep
    if key_input[pygame.K_DOWN]:
        if playerY < 650:
            playerY += playerStep

    redCarCol = isCollision(redcarX, redcarY, playerX, playerY)
    if redCarCol:
        playerX = 30
        playerY = 20

    yellowCarCol = isCollision(yellowcarX, yellowcarY, playerX, playerY)
    if yellowCarCol:
        playerX = 30
        playerY = 20

    scootyCol = isCollision(scootyX, scootyY, playerX, playerY)
    if scootyCol:
        playerX = 30
        playerY = 20

    bikeCol = isCollision(bikeX, bikeY, playerX, playerY)
    if bikeCol:
        playerX = 30
        playerY = 20

    fastDeliveryCol = isCollision(fastdeliveryX, fastdeliveryY, playerX, playerY)
    if fastDeliveryCol:
        playerX = 30
        playerY = 20

    if playerY >= 600:
        screen.blit(msgWin, (150 - msgWin.get_width() // 2, 650 - msgWin.get_height()))

    pygame.display.update()
    fpsClock.tick(fps)