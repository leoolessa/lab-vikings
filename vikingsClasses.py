import random

# Soldier


class Soldier ():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
     
    
    def attack(self):
        return self.strength     
        
        
    def receiveDamage(self, damage):
        self.health -= damage
        return
    


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

       
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"  
        
    
    def battleCry(self):
        return f"Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __inti__(self, health, strength):
        self.health = health
        self.strength = strength




    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"






# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

        

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
             
            
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        
        
    def vikingAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        strength_viking_attack = random_viking.attack()
        result = random_saxon.receiveDamage(strength_viking_attack)
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return  result
            
        
    def saxonAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        strength_saxon_attack = random_saxon.attack()
        result = random_viking.receiveDamage(strength_saxon_attack)
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return  result


    def showStatus(self):
        if len(self.vikingArmy) ==0:
            return f'Saxons have fought for their lives and survive another day...'
        if len(self.saxonArmy) ==0:
            return f'Vikings have won the war of the century!'
        else:
            return f'Vikings and Saxons are still in the thick of battle.'













