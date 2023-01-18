from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon

weapon_robot = Weapon('Power Punch', 20)
robot_one = Robot("Atom")
dinosaur_one = Dinosaur('Little Foot', 20) 

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
        while dinosaur_one.health != 0: 
            robot_one.attack(dinosaur_one)
            print((f'{robot_one.name} attacked {dinosaur_one.name} with {weapon_robot.name} for {weapon_robot.attack_power} damage!'))
            print(f'{dinosaur_one.name} has {dinosaur_one.health} health remaining.')
            print("")
            if robot_one.health != 0:
                dinosaur_one.attack(robot_one)
                print(f'{dinosaur_one.name} attacked {robot_one.name} for {dinosaur_one.attack_power} damage!')
                print(f'{robot_one.name} has {robot_one.health} health remaining.')
                print("")
            elif dinosaur_one.health == 0:
                break
        else:
            if dinosaur_one.health == 0:
                print('Game over!')
            
    def display_winner(self):
        if robot_one.health > dinosaur_one.health:
            print(f'Robot {robot_one.name} wins!')
        else:
            print(f'Dinosaur {dinosaur_one.name} wins!')


# print(dinosaur_one.health)
# robot_one.attack(dinosaur_one)
# print(dinosaur_one.health)


    