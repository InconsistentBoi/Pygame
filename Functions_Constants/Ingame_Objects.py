import pygame
import sys
import os
from pygame.locals import *
from Functions_Constants import constants, Transition_moving, Level1




def player_movement(keys_pressed, Player_Hitbox):
    if keys_pressed[K_a]:
        if maze_collision(Player_Hitbox) != True:  # Leftttttt
            Player_Hitbox.x -= constants.VEL
            
        else:
            Player_Hitbox.x, Player_Hitbox.y = 250, 590
            
    if keys_pressed[K_d]:
        if maze_collision(Player_Hitbox) != True:
            Player_Hitbox.x += constants.VEL
            
        else:
            Player_Hitbox.x, Player_Hitbox.y = 250, 590
            
    if keys_pressed[K_s]:
        if maze_collision(Player_Hitbox) != True:  # down
            Player_Hitbox.y += constants.VEL
           
        else:
            Player_Hitbox.x, Player_Hitbox.y = 250, 590
            
    if keys_pressed[K_w]:
        if maze_collision(Player_Hitbox) != True:  # up
            Player_Hitbox.y -= constants.VEL
            
        else:
            Player_Hitbox.x, Player_Hitbox.y = 250, 590
           


def maze_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x, Player_Hitbox.y)) == (255, 255, 255):
        constants.Health -= 1
        return True


def fin_line_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x, Player_Hitbox.y)) == (14, 209, 69):
        return True


def laser_collision(Player_Hitbox,Laser_Hitbox):
    if Player_Hitbox.colliderect(Laser_Hitbox):
        constants.Health -= 7
        Laser_Hitbox.x, Laser_Hitbox.y = 0, 0
        Player_Hitbox.x, Player_Hitbox.y = 250, 590


def rocket_collision(Player_Hitbox,Rocket_Hitbox):
    if Player_Hitbox.colliderect(Rocket_Hitbox):
        constants.Health -= 11
        Rocket_Hitbox.x, Rocket_Hitbox.y = 1280, 0
        Player_Hitbox.x, Player_Hitbox.y = 250, 590


def landmine1_collision(Player_Hitbox,Landmine1_Hitbox):
    if Player_Hitbox.colliderect(Landmine1_Hitbox):
        constants.Health -= 15 
        Player_Hitbox.x, Player_Hitbox.y = 250, 590

def landmine2_collision(Player_Hitbox,Landmine2_Hitbox):
    if Player_Hitbox.colliderect(Landmine2_Hitbox):
        constants.Health -= 15 
        Player_Hitbox.x, Player_Hitbox.y = 250, 590

def landmine3_collision(Player_Hitbox,Landmine3_Hitbox):
    if Player_Hitbox.colliderect(Landmine3_Hitbox):
        constants.Health -= 15 
        Player_Hitbox.x, Player_Hitbox.y = 250, 590


def laser_pressed(Laser_Hitbox,a):
    Laser_Hitbox.y -= 15
    if Laser_Hitbox.y == 0:
        a=0

def rocket_pressed(Rocket_Hitbox,b):
    Rocket_Hitbox.y -= 9
    if Rocket_Hitbox.y == 0:
        b=0





# def Mine1_Button_pressed(Mine1_Button,Used_Num):
#     if Used_Num<=2:
#         Active_Landmine1=constants.WIN.blit(constants.Active_Landmine,(393,365))
#         Used_Num+=1

# def Mine2_Button_pressed(Mine2_Button,Used_Num):
#     if Used_Num<=2:
#         Active_Landmine2=constants.WIN.blit(constants.Active_Landmine,(790,565))       
#         Used_Num+=1

# def Mine3_Button_pressed(Mine3_Button,Used_Num):
#     if Used_Num<=2:
#         Active_Landmine3=constants.WIN.blit(constants.Active_Landmine,(710,270))
#         Used_Num+=1
