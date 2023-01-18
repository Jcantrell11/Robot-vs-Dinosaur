from weapon import Weapon

weapon_robot = Weapon('Power Punch', 50)

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon
        
    def attack(self, dinosaur):
        if self.health > 0:
            dinosaur.health -= weapon_robot.attack_power
            print((f'Robot {self.name} attacked {dinosaur.name} with {weapon_robot.name} for {weapon_robot.attack_power} damage!'))
            print(f'Dinosaur {dinosaur.name} has {dinosaur.health} health remaining.')
            print("")
        
        

   
   
   
   
   
    # print(weapon_robot.name)
    # print(weapon_robot.attack_power)

 