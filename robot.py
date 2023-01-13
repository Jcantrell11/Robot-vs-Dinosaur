from weapon import Weapon

weapon_robot = Weapon('Power Punch', 20)

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon
        
    def attack(self, dinosaur):
        dinosaur.health -= weapon_robot.attack_power
        

   
   
   
   
   
    # print(weapon_robot.name)
    # print(weapon_robot.attack_power)

 