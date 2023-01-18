
dinosaur_one = ('Little Foot', 50)

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        if self.health > 0:
            robot.health -= self.attack_power
            print(f'Dinosaur {self.name} attacked {robot.name} for {self.attack_power} damage!')
            print(f'Robot {robot.name} has {robot.health} health remaining.')
            print("")


