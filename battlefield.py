from robot import Robot
from dinosaur import Dinosaur



robot_one = Robot("Atom")
dinosaur_one = Dinosaur('Little Foot', 50) 

class Battlefield:
    def __init__(self):
        self.robot = Robot
        self.dinosaur = Dinosaur

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to the game!')
       
    
    def battle_phase(self):
        while dinosaur_one.health > 0 and robot_one.health > 0: 
            robot_one.attack(dinosaur_one)
            dinosaur_one.attack(robot_one)    
        else:
            print('Game over!')
        
    def display_winner(self):
        if robot_one.health > dinosaur_one.health:
            print(f'Robot {robot_one.name} wins!')
        else:
            print(f'Dinosaur {dinosaur_one.name} wins!')




    