import discord
import random
from discord.ext import commands

def roller(num, dice, mult): #rolls "num" amount of "dice" sided dice and adds the results and multiplies it by "mult"
    total = 0
     
    for total in range(num):
        total += random.randint(1, dice)
    
    total *= mult
    
    return total

def itable(id): #rolls individual monster loot based on CR
    out = '' #output string that we will concatinate
    row = 0 #variable to control which "row" of the table is being used
    
    #initilize tables
    itable1 = [[5, 6, 1, ' CP'], [4, 6, 1, ' SP'], [2, 6, 1, ' GP'], [3, 6, 1, ' GP'], [1, 6, 1, ' PP']]
    itable2 = [[4, 6, 100, ' CP'], [6, 6, 10, ' SP'], [2, 6, 10, ' GP'], [4, 6, 10, ' GP'], [3, 6, 1, ' PP']]
    itable3 = [[4, 6, 100, ' SP'],[1, 6, 100, ' GP'],[2, 6, 100, ' GP'],[2, 6, 10, ' PP']]
    itable4 = [[8, 6, 100, ' GP'],[1, 6, 1000, ' GP'],[2, 6, 100, ' PP']]
    
    d100 = roller(1, 100, 1)

    if(id <= 4):
        #determine which row of the table to use
        if(d100 > 30 and d100 <= 60): row = 0
        elif(d100 > 60 and d100 <= 70): row = 1
        elif(d100 > 70 and d100 <= 95): row = 2
        elif(d100 > 95): row = 3
        out += str(roller(itable1[row][0], itable1[row][1], itable1[row][2])) + itable1[row][3]
            
    elif(id > 4 and id <= 10):
        if(d100 > 30 and d100 <= 60): row = 0
        elif(d100 > 60 and d100 <= 70): row = 1
        elif(d100 > 70 and d100 <= 95): row = 2
        elif(d100 > 95): row = 3
        out += str(roller(itable2[row][0], itable2[row][1], itable2[row][2])) + itable2[row][3]
        
    elif(id > 10 and id < 17):
        if(d100 > 20 and d100 <= 35): row = 0
        elif(d100 > 35 and d100 <= 75): row = 1
        elif(d100 > 75): row = 2
        out += str(roller(itable3[row][0], itable3[row][1], itable3[row][2])) + itable3[row][3]
    elif(id >= 17):
        if(d100 > 20 and d100 <= 35): row = 0
        elif(d100 > 35 and d100 <= 75): row = 1
        elif(d100 > 75): row = 2
        out += str(roller(itable4[row][0], itable4[row][1], itable4[row][2])) + itable4[row][3]
    
    return out

def htable(id): #rolls on the treasure hoard table based on CR
    out = ''
    row = 0
    
    return out

def mtable(id): #rolls on the magic item tables
    out = ''
    row = 0
    fig = ''
    
    d8 = roller(1, 8, 1)
    if(d8 == 1): fig += 'Bronze griffon'
    elif(d8 == 2): fig += 'Ebony fly'
    elif(d8 == 3): fig += 'Golden lions'
    elif(d8 == 4): fig += 'Ivory goats'
    elif(d8 == 5): fig += 'Marble elephant'
    elif(d8 == 8): fig += 'Serpentine owl'
    else: fig += 'Onyx dog'
    
    #initilize tables
    mtable1 = ['Potion of greater healing', 'Spell scroll (cantrip)', 'Potion of climbing', 'Spell scroll (1st level)', 'Spell scroll (2nd level)', 'Potion of greater healing', 'Bag of holding', 'Driftglobe']
    mtable2 = ['Potion of greater healing', 'Potion of fire breath breath', 'Potion of resistance', 'Ammunition +1', 'Potion of animal friendship', 'Potion of hill giant strength', 'Potion of growth', 'Potion of water breathing', 'Spell scroll (2nd level)', 'Spell scroll (3rd level)', 'Bag of holding', "Keoghtom's ointment", 'Oil of slipperiness', 'Dust of disappearance', 'Dust of dryness', 'Dust of sneezing and choking', 'Elemental gem', 'Philter of love', 'Alchemy jug', 'Cap of water breathing', 'Cloak of the manta ray', 'Driftglobe', 'Goggles of night', 'Helm of comprehending languages', 'Immovable rod', 'Lantern of revealing', "Mariner's armor", 'Mithral armor', 'Potion of poison', 'Ring of swimming', 'Robe of useful items', 'Rope of climbing', 'Saddle of the cavalier', 'Wand of magic detection', 'Wand of secrets']
    mtable3 = ['Potion of superior healing', 'Spell scroll (4th level)', 'Ammunition +2', 'Potion of clairvoyance', 'Potion of dimination', 'Potion of gaseous form', 'Potion of frost giant strength', 'Potion of stone giant strength', 'Potion of heroism', 'Potion of invulnerability', 'Potion of mind reading', 'Spell scroll (5th level)', 'Elixir of health', 'Oil of etherealness', 'Potion of fire giant strength', "Quaal's feather token", 'Scroll of protection', 'Bag of beans', 'Bead of force', 'Chime of opening', 'Decanter of endless water', 'Eyes of minute seeing', 'Folding boat', "Heward's handy haversack", 'Horseshoes of speed', 'Necklace of fireballs', 'Periapt of health', 'Sending stones']
    mtable4 = ['Potion of supreme healing', 'Potion of invisibility', 'Potion of speed', 'Spell scroll (6th level)', 'Spell scroll (7th level)', 'Ammunition +3', 'Oil of sharpness', 'Potion of flying', 'Potion of cloud giant strength', 'Potion of longevity', 'Potion of vitality', 'Spell scroll (8th level)', 'Horeseshoes of a zephyr', 'Bag of devouring', 'Portable hole']
    mtable5 = ['Spell scroll (8th level)', 'Potion of storm giant strength', 'Potion of supreme healing', 'Spell scroll (9th level)', 'Universal solvent', 'Arrow of slaying', 'Sovereign glue']
    mtable6 = ['Weapon +1', 'Shield +1', 'Sentinel shield', 'Amulet of proof against detection and location', 'Boots of elvenkind', 'Boots of striding and springing', 'Bracers of archery', 'Brooch of shielding', 'Broom of flying', 'Cloak of elvenkind', 'Cloak of protection', 'Gauntlets of ogre power', 'Hat of disguise', 'Javelin of lightning', 'Pearl of power', 'Rod of the pact keeper +1', 'Slippers of spider climbing', 'Staff of the adder', 'Staff of the python', 'Sword of vengence', 'Trident of fish command', 'Wand of magic missiles', 'Wand of the war mage +1', 'Wand of web', 'Weapon of warning', 'Adamantine armor(chain mail)', 'Adamantine armor(chain shirt)', 'Adamantine armor(scale mail)', 'Bag of tricks(gray)', 'Bag of tricks(rust)', 'Bag of tricks(tan)', 'Boots of the winterlands', 'CCirclet of blasting', 'Deck of illusions', 'Eversmoking bottle', 'Eyes of charming', 'Eyes of the eagle', 'Figurine of wondrous power(silver raven)', 'Gem of brightness', 'Gloves of missile snaring', 'Gloves of swimming and climbing', 'Gloves of thievery', 'Headband of intellect', 'Helm of telepathy', 'Instrument of the bards (Doss lute)', 'Instrument of the bards (Fochlucan bandore)', 'Instrument of the bards (Mac Fuimidh cittern)', 'Medallion of thoughts', 'Necklace of adaptation', 'Periapt of wound closure', 'Pipes of haunting', 'Pipes of the sewers', 'Ring of jumping', 'Ring of mind shielding', 'Ring of warmth', 'Ring of water walking', 'Quiver of Ehlonna', 'Stone of good luck', 'Wind fan', 'Winged boots']
    mtable7 = ['Weapon +2', 'Figurine of wondrous power('+fig, 'Adamantine armor (breastplate)', 'Adamantine armor (splint)', 'Amulet of health', 'Armor of vulnerability', 'Arrow-catching shield', 'Belt of dwarvenkind', 'Belt of hill giant strength', 'Berserker axe', 'Boots of levitation', 'Boots of speed', 'Bowl of commanding water elementals', 'Bracers of defense', 'Brazier of commanding fire elementals', 'Cape of the mounterbank', 'Censer of controlling air elementals', 'Armor +1 chain mail', 'Armor of resistance (chain mail)', 'Armor +1 chain shirt', 'Armor of resistance (chain shirt)', 'Cloak of displacement', 'Cloak of the bat', 'Cube of force', "Daern's instant fortress", 'Dagger of venom', 'Dimensional shackles', 'Dragon slayer', 'Elven chain', 'Flame tongue', 'Gem of seeing', 'Giant slayer', 'Glamoured studded leather', 'Helm of teleportation', 'Horn of blasting', 'Horn of valhalla (silver or brass)', 'Instrument of the bards (Canaith mandolin)', 'Instrument of the bards (Cli lyre)', 'Ioun stone (awareness)', 'Ioun stone (protection)', 'Ioun stone (reserve)', 'Ioun stone (sustenance)', 'Iron bands of Bilarro', 'Armor +1 leather', 'Armor of resistance (leather)', 'Mace of disruption', 'Mace of smiting', 'Mace of terror', 'Mantle of spell resistance', 'Necklace of prayer beads', 'Periapt of proof against poison', 'Ring of animal influence', 'Ring of evasion', 'Ring of feather falling', 'Ring of free action', 'Ring of protection', 'Ring of resistance', 'Ring of spell storing', 'Ring of the ram', 'Ring of x-ray vision', 'Robe of eyes', 'Rod of rulership', 'Rod of the pact Keeper +2', 'Rope of entanglement', 'Armor +1 scale mail', 'Armor of resistance (scale mail)', 'Shield +2', 'Shield of missile attraction', 'Staff of charming', 'Staff of healing', 'Staff of swarming insects', 'Staff of the woodlands', 'Staff of withering', 'Stone of controlling earth elementals', 'Sun blade', 'Sword of life stealing', 'Sword of wounding', 'Tentacle rod', 'Vicious rod', 'Wand of binding', 'Wand of enemy detection', 'Wand of fear', 'Wand of fireballs', 'Wand of lightning bolts', 'Wand of paralysis', 'Wand of the war mage +2', 'Wand of wonder', 'Wings of flying']
    mtable8 = ['Weapon +4', 'Amulet of the planes', 'Carpet of flying', 'Crystal ball (very rare version)', 'Ring of regeneration', 'Ring of shooting stars', 'Ring of telekinesis', 'Robe of scintillating colors', 'Robe of stars', 'Rod of absorption', 'Rod of alertness', 'Rod of security', 'Rod of the pact keeper +3', 'Scimitar of speed', 'Shield +3', 'Staff of fire', 'Staff of frost', 'Staff of power', 'Staff of striking', 'Staff of thunder and lightning', 'Sword of sharpness', 'Wand of polymorph', 'Wand of the war mage +3', 'Adamantine armor (half plate)', 'Adamantine armor (plate)', 'Animated shield', 'Belt of fire giant strength', 'Belt of frost (or stone) giant strength', 'Armor +1 breastplate', 'Armor of resistance (breastplate)', 'Candle of invocation', 'Armor +2 chain mail', 'Armor +3 chain shirt', 'Cloak of arachnida', 'Dancing sword', 'Demon armor', 'Dragon scale mail', 'Dwarven plate', 'Dwarven thrower', 'Efreeti bottle', 'Figurine of wonderous power (obsidian steed)', 'Frost brand', 'Helm of brilliance', 'Horn of Valhalla (bronze)', 'Instrument of the bards (Anstruth harp)', 'Ioun stone (absorption)', 'Ioun stone (agility)', 'Ioun stone (fortitude)', 'Ioun stone (insight)', 'Ioun stone (intellect)', 'Ioun stone (leadership)', 'Ioun stone (strength)', 'Armor +2 leather', 'Manual of bodily health', 'Manual of gainful exercise', 'Manual of golems', 'Manual of quickness of action', 'Mirror of life trapping', 'Nine lives stealer', 'Oathbow', 'Armor +2 scale mail', 'Spellguard shield', 'Armor +1 splint', 'Armor of resistance (splint)', 'Armor +1 studded leather', 'Armor of resistance (studded leather)', 'Tome of clear thought', 'Tome of leadership and influence', 'Tome of understanding']
    mtable9 = []
    
    return out