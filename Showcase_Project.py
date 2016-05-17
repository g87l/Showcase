import sys
import pickle


class Rooms:
    def __init__(self, name, north, south, east, west, up, down, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        
    def move(self, direction):
        global node
        node = globals()[getattr(self, direction)]

class Enemy(object):
    def __init__(self, name, health):
                self.name
                self.health
        
    def attacks(self,Enemy):
            Enemy.remove_health(self.attack)
            if Enemy.health <=0:
                    print 'Enemy down.'
            else:
                return Enemy.health
        
            def remove_health(self,amount):
                self.health -= amount

start = Rooms("start", 'room_1', None, None, None, None, None, "Welcome to Zombie Town! The objective we have for you is to get every or most people in a safe place. Use: 'North', 'East', 'South', 'West', 'Up', and 'Down' to move around the map. If you want so see your inventory input 'inventory', if you want to see your health input 'health'. If you want to save your game input 'save'. If you want to load your game input 'load'. Type in 'North' to start. MOST OF THE FUNCTIONS DON'T WORK YET.")                             
room_1 = Rooms("room_1", None, None,'hallway', None, None, None, "You wake up in a dim room with blood all over the floor, and it is very messy and unorganized as if there had been an earthquake. Then you noticed that you are in a hospital, but there is no one there. There is a flashlight next to the bed. Input 'take' to take the flashlight. ")
hallway = Rooms("hallway", None, 'door_hw2', 'room_2', 'room_1', None, None, "You are now in a hallway with flickering lights. It is very dark, and bloody all around the hospital. Everything is destroyed and broken. Input 'use flashlight' to use your flash light.")
room_2 = Rooms("room_2", None, None, None, 'hallway', None, None, "The room is dark and there is a desk at the top right corner and one on the top left. Input 'search top right desk' or 'search top left desk' to find out what is in each desk.")
door_hw2 = Rooms("door_hw2", 'hallway' , 'hallway_2', None, None, None, None, "This is the door to hallway_2, but it is locked. Find the key to get in. Input 'unlock hallway_2' to go inside.")
hallway_2 = Rooms("hallway_2", 'room_2', 'bathroom', 'room_3', 'stairs', None, None, "You are in hall number 2. It is very dark and you can go any direction you want.")
room_3 = Rooms("room_3", None, None, None, 'hallway_2', None, None, "The room has many ancient weapons but you can't get any of them except a sword. Input 'take sword' to take the sword.")
bathroom = Rooms("bathroom", 'hallway_2', None, None, None, None, None, "You are in the bathroom. The light is flickering and you hear some weird noises. There is a zombie trying to eat you! Kill the zombie! Input 'attack zombie' to attack the zombie. Input 'choose' and the item you want from your inventory to use it.")
stairs = Rooms("stairs", None, None, 'hallway_2', None, None, 'room_4', "You are at the stairs. They only head down.")
room_4 = Rooms("room_4", None, 'outside', None, None, 'stairs', None,  "There is a zombie that is trying to eat you. There is also a desk at each corner. Try searching the desks. Maybe you'll find something useful. Input 'search' and 'top left', 'top right', 'bottom left', 'or bottom right' to search any of the desks.")
outside = Rooms("outside", 'first_intersection' , 'room_4', 'police_department', 'store' , None, None, "You are out of the building. There is a mansion three miles north. To the west there is a grocery store. To the east there is a police department.")
police_department = Rooms("police_department", 'police_hw' , 'outside' , None, None, None, None, "You are in the police department. There are many zombies in there, but you can get many weapons as well.")
police_hw = Rooms("police_hw", 'zombies1', 'police_department', 'police_rm1', 'police_rm6', None, None, "This is a hallway with doors in every direction. But you prepare yourself because you hear many noises.")
zombies1 = Rooms("zombies1", 'police_rm4', 'police_hw', None, None, None, None, "OHHH NOOO!!! There are alot of zombies in here! Run through all of them or kill them, but that is very risky.")
police_rm4 = Rooms("police_rm4", 'police_rm5', 'zombies1', None, 'police_k1', None, None, "It is dark, and you can\'t see. Input 'use flashlight' to use your flashlight. There is a door to the north, south, and west of you.")
police_rm5 = Rooms("police_rm5", None, 'police_rm4', None, None, None, None, "This room seems to be empty. There is a health pack here. Input 'pick up health1' to get health.")
police_k1 = Rooms("police_k1", None, None, 'police_rm4', None, None, None, "This room is very dark. There's three boxes with a bunch of stuff in them. Input 'search boxes' to search in the boxes. There is also a red desk here. Input 'search red desk' to search the desk.")
police_rm6 = Rooms("police_rm6", 'police_k2', None, 'police_hw' , None, None, None, "This room is empty, but there is a locked door ahead. You need a key to open this door. Find the key. If you already have the key, input 'unlock police_rm6'.")
police_k2 = Rooms("police_k2", None, 'police_rm6', None, None, None, None, "There are four boxes on the ground with a desk at three of the room corners. Input 'search 4 boxes' to search the boxes. Search them and maybe you'll find something. To search them input 'search' and '1 desk', '2 desk', '3 desk'.")
police_rm1 = Rooms('police_rm1', 'police_rm2', 'zombies2', None, 'police_hw', None, None, "This room is empty, but there's doors on the north and south of you.")
police_rm2 = Rooms('police_rm2', None, 'police_rm1', 'police_k3', None, None, None, "There is one zombie standing in front of the door to the east.")
police_k3 = Rooms('police_k3', None , None, None, 'police_rm2', None, None, "There is a desk here with a zombie sitting down. Kill the zombie and search the desk. Input 'search police desk' to search the desk.")
zombies2 = Rooms('zombies2', 'police_rm1', None, 'weapon_room',None, None, None, "You hear someone screaming so you bust through the door and see a zombie. Kill the zombie! You see a door to the east.")
weapon_room = Rooms('weapon_room', None, None, None, 'zombies2', None, None, "You see a person getting attacked by a zombie!! Save the person! This is the weapon room. There are manys guns and weapons here. You should probably take some. Input 'take' and the name of the weapons you can take. Weapons: axe, ak-47, shotgun, crossbow, throwing knives, shurikens, grenade, grenade1, grenade2, grenade3, grenade4.")
store = Rooms('store', None, None, 'outside', None, None, None, "There isn't much here, but there is health. Input 'take health' to add more health.")
first_intersection = Rooms('first_intersection', 'second_intersection', 'outside', 'zombies3', 'zombies4', None, None, "You are at the first intersection.")
zombies3 = Rooms('zombies3', None, None, None, 'first_intersection', None, None, " There is many zombies here, but that's about it!! You don't see anything else.")
zombies4 = Rooms('zombies4', None, None, 'first_intersection', 'land1',None, None, "There are zombies here, but you see clothes on the ground and wonder if there is a person around here. You see something to the west of you.")
land1 = Rooms('land1', None, 'land2', 'zombies4',None, None, None, "There is just land with zombies in it. Go past them.")
land2 = Rooms('land2', 'land1', None, None, 'park', None, None, "There is more land and more zombies as well. Go past them.")
park = Rooms('park', None, None, 'land2', None, None, None, "There is many zombies trying to eat a person!! Save her!!!")
second_intersection = Rooms('second_intersection', 'third_intersection', 'first_intersection', 'zombies6', 'zombies5', None, None, "You are at the second intersection.")
zombies5 = Rooms('zombies5', None, None, 'second_intersection', None, None, None, "There are zombies here!")
zombies6 = Rooms('zombies6', None, None, 'park2', 'second_intersection', None, None, "There are zombies here, but you hear screaming in the park!! You see a person getting attacked by a zombie!")
park2 = Rooms('park2', None, None, None, 'zombies6', None, None, "There is a zombie chasing a person around. Save them!")
third_intersection = Rooms('third_intersection', 'mansion', 'second_intersection', 'zombies8', 'zombies7', None, None, "You are at the third intersection.")
zombies7 = Rooms('zombies7', None, None, 'third_intersection', 'house1',None, None, " There is a house and you hear a person scream. You see a zombie with a key. Get the key!")
zombies8 = Rooms('zombies8', None, None, None, 'third_intersection', None, None, "There are only zombies here!")
house1 = Rooms('house1', None, None, 'zombies7', None, None, None, "Get the key from the zombie!")
mansion = Rooms('mansion', 'stairs2', 'third_intersection', 'living_room', 'kitchen', None, None, "The mansion is locked but you can open with a key. Find the key. If you have the key already, input 'unlock mansion' to unlock the mansion and go inside.")
living_room = Rooms('living_room', None, None, None, 'mansion', None, None, "You are in the living room. There are zombies here!")
kitchen = Rooms('kitchen', None, None, 'mansion', None, None, None, "You are in the kitchen. The only thing here is health.")
stairs2 = Rooms('stairs2', None, 'mansion', 'mansion_r3', None, 'main_room', None, "You see stairs heading up, and a door to the east.")
mansion_r3 = Rooms('mansion_r3', None, None, 'garage', 'stairs2', None, None, "You are in room number three. There isn't much here but health.")
main_room = Rooms('main_room', None, None, None, 'mansion_r2', None, 'stairs2', "This is the main room. There is a person here.")
mansion_r2 = Rooms('mansion_r2', None, None, 'main_room', None, None, None, "There isn't much health here but health.")
garage = Rooms('garage', None , 'backyard', None, 'mansion_r3', None, None, "You are in the garage.")
backyard = Rooms('backyard', 'garage', None,None, 'the_exit', None, None, "You are in the backyard with alot of zombies!")
the_exit = Rooms('the_exit', None, 'wall', 'backyard', None, None , None, " This is the exit, but you see a wall ahead of you.")
wall = Rooms('wall', 'the_exit', None, 'amusement_park', None, None, None, " There is a wall blocking the road. Clear the road.")
amusement_park = Rooms('amusement_park',None,'end', None, 'wall', None, None, "You have to go through the amusement park to get to a safe place, but there is alot of zombies here.")
end = Rooms('end','amusement_park', None, None, None, None, None, "You are in a safe place now.You have save most or all of the people. You have won the game!")


node = start

inventory = []
items = ['flashlight', 'key', 'pistol', 'shotgun', 'sword', 'health', 'key_rm6', 'health1', 'axe', 'ak-47', 'shotgun', 'crossbow', 'throwing knives', 'shurikens', 'grenade', 'grenade1', 'grenade2', 'grenade3', 'grenade4']


def save():
    global Rooms, node,inventory, items
    with open('savegame.dat', 'wb') as f:
        pickle.dump([Rooms, node,inventory, items], f, protocol = 2 ) 
    print "Game successfully saved"
       
def load():
    global Rooms, node,inventory, items
    with open('savegame.dat', 'rb') as f:
        Rooms, node,inventory, items = pickle.load(f)
    print "Game successfully loaded"


while True:
    print node.name
    print node.description
    directions = ['north', 'south', 'east', 'west', 'up', 'down']
    command = raw_input('>').strip().lower()
   
    if command in ['q','exit','quit']:
           sys.exit(0)
                 
    if command in directions:   
        try: 
            node.move(command)
        except:
            print 'You can\'t go that way.'
            
    elif command in ["save"]:       
        save()
    elif command in ["load"]:
        load()      
            
    if node == room_1:
        if command == 'take':
            if items[0] in inventory:
                 print 'You already have this item.'
            else:
                if items[0] not in inventory:
                    inventory.append(items[0])
                    print 'You have picked up the item.'
                    print inventory
                    
    if command == 'inventory':
        print inventory
        
    if command == 'use flashlight':
        print 'You are using the flashlight.'
        
        
    if node == room_2:
        if command == 'search top right desk':
            if items[1] in inventory:
                 print 'You already have this item.'
            else:
                if items[1] not in inventory:
                    inventory.append(items[1])
                    print 'You have found the hallway_2 key!!'
                    print inventory
                    
    if command == 'search top left desk':
        print 'This desk is empty. Goodluck next time! >:)'
        
    if node == door_hw2:
        if command == 'unlock hallway_2':
            if items[1] in inventory:
                print 'You have unlocked the door.'
            else:
                if items[1] not in inventory:
                    print 'You can not go in the room it is locked. Find the key to get in hallway_2.'
                    
    if node == room_3:
        if command == 'take sword':
            if items[4] in inventory:
                 print 'You already have this item.'
            else:
                if items[4] not in inventory:
                    inventory.append(items[4])
                    print 'You have taken the sword!'
                    print inventory
                    
    if node == room_4:
        if command == 'search top left':
            if items[2] in inventory:
                 print 'You already have this item.'
            else:
                if items[2] not in inventory:
                    inventory.append(items[2])
                    print 'You have taken the pistol!'
                    print inventory
                    
    if command == 'search top right':
        print 'This desk is empty. Goodluck next time! >:)'
        
    if command == 'search bottom right':
        print 'Nope. Nothing here try somewhere else.'
        
    if command == 'search bottom left':
        print 'Nothing here either. Empty! >:)'
        
    if node == store:
        if command == 'take health':
            if items[5] in inventory:
                 print 'You already have this item.'
            else:
                if items[5] not in inventory:
                    inventory.append(items[5])
                    print 'You have taken health.'
                    print inventory
    
    if node == police_k3:
        if command == 'search police desk':
            if items[6] in inventory:
                 print 'You already have this item.'
            else:
                if items[6] not in inventory:
                    inventory.append(items[6])
                    print 'You have taken the key_rm6.'
                    print inventory
                    
    if command == 'search boxes':
        print ' The boxes don\'t have anything useful.'
        
    if command == 'search red desk':
        print ' The red desk is empty!' 
        
    if command == 'search 4 boxes':
        print 'These boxes don\'t have anything either. Goodluck next time! >:)'
        
    if command == 'search 1 desk':
        print 'Nope! Nothing here!'
        
    if command == 'search 2 desk':
        print 'This desk is empty as well.'
        
    if command == 'search 3 desk':
        print 'Geez! All empty desks... bummer.'
        
    if node == weapon_room:
        if command == 'take axe':
            if items[9] in inventory:
                 print 'You already have this item.'
            else:
                if items[9] not in inventory:
                    inventory.append(items[9])
                    print 'You have taken the axe.'
                    print inventory
                    
    if node == weapon_room:
        if command == 'take ak-47':
            if items[10] in inventory:
                 print 'You already have this item.'
            else:
                if items[10] not in inventory:
                    inventory.append(items[10])
                    print 'You have taken the ak-47.'
                    print inventory
                
    if node == weapon_room:
        if command == 'take shotgun':
            if items[11] in inventory:
                 print 'You already have this item.'
            else:
                if items[11] not in inventory:
                    inventory.append(items[11])
                    print 'You have taken the shotgun.'
                    print inventory
                    
    if node == weapon_room:
        if command == 'take crossbow':
            if items[12] in inventory:
                 print 'You already have this item.'
            else:
                if items[12] not in inventory:
                    inventory.append(items[12])
                    print 'You have taken the crossbow.'
                    print inventory
                    
    if node == weapon_room:
        if command == 'take throwing knives':
            if items[13] in inventory:
                 print 'You already have this item.'
            else:
                if items[13] not in inventory:
                    inventory.append(items[13])
                    print 'You have taken the throwing knives.'
                    print inventory
                    
    if node == weapon_room:
        if command == 'take shurikens':
            if items[14] in inventory:
                 print 'You already have this item.'
            else:
                if items[14] not in inventory:
                    inventory.append(items[14])
                    print 'You have taken the shurikens.'
                    print inventory
                    
    if node == weapon_room:
        if command == 'take grenade':
            if items[15] in inventory:
                 print 'You already have this item.'
            else:
                if items[15] not in inventory:
                    inventory.append(items[15])
                    print 'You have taken the grenade.'
                    print inventory
                    
    if node == weapon_room:
        if command == 'take grenade1':
            if items[16] in inventory:
                 print 'You already have this item.'
            else:
                if items[16] not in inventory:
                    inventory.append(items[16])
                    print 'You have taken the grenade1.'
                    print inventory
                    
    if node == weapon_room:
        if command == 'take grenade2':
            if items[17] in inventory:
                 print 'You already have this item.'
            else:
                if items[17] not in inventory:
                    inventory.append(items[17])
                    print 'You have taken the grenade2.'
                    print inventory
                    
    if node == weapon_room:
        if command == 'take grenade3':
            if items[18] in inventory:
                 print 'You already have this item.'
            else:
                if items[18] not in inventory:
                    inventory.append(items[18])
                    print 'You have taken the grenade3.'
                    print inventory
                    
    if node == weapon_room:
        if command == 'take grenade4':
            if items[19] in inventory:
                 print 'You already have this item.'
            else:
                if items[19] not in inventory:
                    inventory.append(items[19])
                    print 'You have taken the grenade4.'
                    print inventory