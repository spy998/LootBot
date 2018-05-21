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
    marmor = ''
    
    d8 = roller(1, 8, 1)
    if(d8 == 1): fig += 'Bronze griffon'
    elif(d8 == 2): fig += 'Ebony fly'
    elif(d8 == 3): fig += 'Golden lions'
    elif(d8 == 4): fig += 'Ivory goats'
    elif(d8 == 5): fig += 'Marble elephant'
    elif(d8 == 8): fig += 'Serpentine owl'
    else: fig += 'Onyx dog'
    
    d12 = roller(1, 12, 1)
    if(d12 <= 2): marmor += 'Armor +2 half plate'
    elif(d12 == 3 or d12 == 4): marmor += 'Armor +2 plate'
    elif(d12 == 5 or d12 == 6): marmor += 'Armor +3 studded leather'
    elif(d12 == 7 or d12 == 8): marmor += 'Armor +3 breastplate'
    elif(d12 == 11): marmor += 'Armor +3 half plate'
    elif(d12 == 12): marmor += 'Armor +3 plate'
    else: marmor += 'Armor +3 splint'
    
    #initilize tables
    mtable1 = ['Potion of greater healing', 'Spell scroll (cantrip)', 'Potion of climbing', 'Spell scroll (1st level)', 'Spell scroll (2nd level)', 'Potion of greater healing', 'Bag of holding', 'Driftglobe']
    mtable2 = ['Potion of greater healing', 'Potion of fire breath breath', 'Potion of resistance', 'Ammunition +1', 'Potion of animal friendship', 'Potion of hill giant strength', 'Potion of growth', 'Potion of water breathing', 'Spell scroll (2nd level)', 'Spell scroll (3rd level)', 'Bag of holding', "Keoghtom's ointment", 'Oil of slipperiness', 'Dust of disappearance', 'Dust of dryness', 'Dust of sneezing and choking', 'Elemental gem', 'Philter of love', 'Alchemy jug', 'Cap of water breathing', 'Cloak of the manta ray', 'Driftglobe', 'Goggles of night', 'Helm of comprehending languages', 'Immovable rod', 'Lantern of revealing', "Mariner's armor", 'Mithral armor', 'Potion of poison', 'Ring of swimming', 'Robe of useful items', 'Rope of climbing', 'Saddle of the cavalier', 'Wand of magic detection', 'Wand of secrets']
    mtable3 = ['Potion of superior healing', 'Spell scroll (4th level)', 'Ammunition +2', 'Potion of clairvoyance', 'Potion of dimination', 'Potion of gaseous form', 'Potion of frost giant strength', 'Potion of stone giant strength', 'Potion of heroism', 'Potion of invulnerability', 'Potion of mind reading', 'Spell scroll (5th level)', 'Elixir of health', 'Oil of etherealness', 'Potion of fire giant strength', "Quaal's feather token", 'Scroll of protection', 'Bag of beans', 'Bead of force', 'Chime of opening', 'Decanter of endless water', 'Eyes of minute seeing', 'Folding boat', "Heward's handy haversack", 'Horseshoes of speed', 'Necklace of fireballs', 'Periapt of health', 'Sending stones']
    mtable4 = ['Potion of supreme healing', 'Potion of invisibility', 'Potion of speed', 'Spell scroll (6th level)', 'Spell scroll (7th level)', 'Ammunition +3', 'Oil of sharpness', 'Potion of flying', 'Potion of cloud giant strength', 'Potion of longevity', 'Potion of vitality', 'Spell scroll (8th level)', 'Horeseshoes of a zephyr', 'Bag of devouring', 'Portable hole']
    mtable5 = ['Spell scroll (8th level)', 'Potion of storm giant strength', 'Potion of supreme healing', 'Spell scroll (9th level)', 'Universal solvent', 'Arrow of slaying', 'Sovereign glue']
    mtable6 = ['Weapon +1', 'Shield +1', 'Sentinel shield', 'Amulet of proof against detection and location', 'Boots of elvenkind', 'Boots of striding and springing', 'Bracers of archery', 'Brooch of shielding', 'Broom of flying', 'Cloak of elvenkind', 'Cloak of protection', 'Gauntlets of ogre power', 'Hat of disguise', 'Javelin of lightning', 'Pearl of power', 'Rod of the pact keeper +1', 'Slippers of spider climbing', 'Staff of the adder', 'Staff of the python', 'Sword of vengence', 'Trident of fish command', 'Wand of magic missiles', 'Wand of the war mage +1', 'Wand of web', 'Weapon of warning', 'Adamantine armor(chain mail)', 'Adamantine armor(chain shirt)', 'Adamantine armor(scale mail)', 'Bag of tricks(gray)', 'Bag of tricks(rust)', 'Bag of tricks(tan)', 'Boots of the winterlands', 'CCirclet of blasting', 'Deck of illusions', 'Eversmoking bottle', 'Eyes of charming', 'Eyes of the eagle', 'Figurine of wondrous power(silver raven)', 'Gem of brightness', 'Gloves of missile snaring', 'Gloves of swimming and climbing', 'Gloves of thievery', 'Headband of intellect', 'Helm of telepathy', 'Instrument of the bards (Doss lute)', 'Instrument of the bards (Fochlucan bandore)', 'Instrument of the bards (Mac Fuimidh cittern)', 'Medallion of thoughts', 'Necklace of adaptation', 'Periapt of wound closure', 'Pipes of haunting', 'Pipes of the sewers', 'Ring of jumping', 'Ring of mind shielding', 'Ring of warmth', 'Ring of water walking', 'Quiver of Ehlonna', 'Stone of good luck', 'Wind fan', 'Winged boots']
    mtable7 = ['Weapon +2', 'Figurine of wondrous power('+fig+')', 'Adamantine armor (breastplate)', 'Adamantine armor (splint)', 'Amulet of health', 'Armor of vulnerability', 'Arrow-catching shield', 'Belt of dwarvenkind', 'Belt of hill giant strength', 'Berserker axe', 'Boots of levitation', 'Boots of speed', 'Bowl of commanding water elementals', 'Bracers of defense', 'Brazier of commanding fire elementals', 'Cape of the mounterbank', 'Censer of controlling air elementals', 'Armor +1 chain mail', 'Armor of resistance (chain mail)', 'Armor +1 chain shirt', 'Armor of resistance (chain shirt)', 'Cloak of displacement', 'Cloak of the bat', 'Cube of force', "Daern's instant fortress", 'Dagger of venom', 'Dimensional shackles', 'Dragon slayer', 'Elven chain', 'Flame tongue', 'Gem of seeing', 'Giant slayer', 'Glamoured studded leather', 'Helm of teleportation', 'Horn of blasting', 'Horn of valhalla (silver or brass)', 'Instrument of the bards (Canaith mandolin)', 'Instrument of the bards (Cli lyre)', 'Ioun stone (awareness)', 'Ioun stone (protection)', 'Ioun stone (reserve)', 'Ioun stone (sustenance)', 'Iron bands of Bilarro', 'Armor +1 leather', 'Armor of resistance (leather)', 'Mace of disruption', 'Mace of smiting', 'Mace of terror', 'Mantle of spell resistance', 'Necklace of prayer beads', 'Periapt of proof against poison', 'Ring of animal influence', 'Ring of evasion', 'Ring of feather falling', 'Ring of free action', 'Ring of protection', 'Ring of resistance', 'Ring of spell storing', 'Ring of the ram', 'Ring of x-ray vision', 'Robe of eyes', 'Rod of rulership', 'Rod of the pact Keeper +2', 'Rope of entanglement', 'Armor +1 scale mail', 'Armor of resistance (scale mail)', 'Shield +2', 'Shield of missile attraction', 'Staff of charming', 'Staff of healing', 'Staff of swarming insects', 'Staff of the woodlands', 'Staff of withering', 'Stone of controlling earth elementals', 'Sun blade', 'Sword of life stealing', 'Sword of wounding', 'Tentacle rod', 'Vicious rod', 'Wand of binding', 'Wand of enemy detection', 'Wand of fear', 'Wand of fireballs', 'Wand of lightning bolts', 'Wand of paralysis', 'Wand of the war mage +2', 'Wand of wonder', 'Wings of flying']
    mtable8 = ['Weapon +4', 'Amulet of the planes', 'Carpet of flying', 'Crystal ball (very rare version)', 'Ring of regeneration', 'Ring of shooting stars', 'Ring of telekinesis', 'Robe of scintillating colors', 'Robe of stars', 'Rod of absorption', 'Rod of alertness', 'Rod of security', 'Rod of the pact keeper +3', 'Scimitar of speed', 'Shield +3', 'Staff of fire', 'Staff of frost', 'Staff of power', 'Staff of striking', 'Staff of thunder and lightning', 'Sword of sharpness', 'Wand of polymorph', 'Wand of the war mage +3', 'Adamantine armor (half plate)', 'Adamantine armor (plate)', 'Animated shield', 'Belt of fire giant strength', 'Belt of frost (or stone) giant strength', 'Armor +1 breastplate', 'Armor of resistance (breastplate)', 'Candle of invocation', 'Armor +2 chain mail', 'Armor +3 chain shirt', 'Cloak of arachnida', 'Dancing sword', 'Demon armor', 'Dragon scale mail', 'Dwarven plate', 'Dwarven thrower', 'Efreeti bottle', 'Figurine of wonderous power (obsidian steed)', 'Frost brand', 'Helm of brilliance', 'Horn of Valhalla (bronze)', 'Instrument of the bards (Anstruth harp)', 'Ioun stone (absorption)', 'Ioun stone (agility)', 'Ioun stone (fortitude)', 'Ioun stone (insight)', 'Ioun stone (intellect)', 'Ioun stone (leadership)', 'Ioun stone (strength)', 'Armor +2 leather', 'Manual of bodily health', 'Manual of gainful exercise', 'Manual of golems', 'Manual of quickness of action', 'Mirror of life trapping', 'Nine lives stealer', 'Oathbow', 'Armor +2 scale mail', 'Spellguard shield', 'Armor +1 splint', 'Armor of resistance (splint)', 'Armor +1 studded leather', 'Armor of resistance (studded leather)', 'Tome of clear thought', 'Tome of leadership and influence', 'Tome of understanding']
    mtable9 = ['Defender', 'Hammer of thunderbolts', 'Luck blade', 'Sword of answering', 'Holy avenger', 'Ring of djinni summoning', 'Ring of invisibility', 'Ring of spell turning', 'Rod of lordly might', 'Staff of the magi', 'Vorpal sword', 'Belt of cloud giant strength', 'Armor +2 breastplate', 'Armor +3 chain mail', 'Armor +3 chain mail', 'Cloak of invisibility', 'Crystal ball (legendary version)', 'Armor +1 half plate', 'Iron flask', 'Armor +3 leather', 'Armor +1 plate', 'Robe of the archmagi', 'Rod of resurrection', 'Armor +1 scale mail', 'Scarab of protection', 'Armor +2 splint', 'Armor +2 studded leather', 'Well of many worlds', marmor, 'Apparatus of Kwalish', 'Armor of invulnerability', 'Belt of storm giant strength', 'Cubic gate', 'Deck of many things', 'Efreeti chain', 'Armor of resistance (half plate)', 'Horn of valhalla (iron)', 'Instrument of the bards (Ollamh harp)', 'Ioun stone (greater absorption)', 'Ioun stone (mastery)', 'Ioun stone (regeneration)', 'Plate armor of etherealness', 'Plate armor of resistance', 'Ring of air elemental command', 'Ring of earth elemental command', 'Ring of fire elemental command', 'Ring of three wishes', 'Ring of water elemental command', 'Sphere of annihilation', 'Tailsman of pure good', 'Tailsman of the sphere', 'Tailsman of elutimate evil', 'Tome of the stilled tongue']
    
    d100 = roller(1, 100, 1)
    
    if(id == 1):
        if(d100 <= 50): row = 0
        elif(d100 > 50 and d100 <= 60): row = 1
        elif(d100 > 60 and d100 <= 70): row = 2
        elif(d100 > 70 and d100 <= 90): row = 3
        elif(d100 > 90 and d100 < 95): row = 4
        elif(d100 >= 95 and d100 <= 98): row = 5
        elif(d100 == 99): row = 6
        else: row = 7
        
        out += mtable1[row]
    
    elif(id == 2):
        if(d100 <= 15): row = 0
        elif(d100 > 15 and d100 < 23): row = 1
        elif(d100 > 22 and d100 < 30): row = 2
        elif(d100 > 29 and d100 < 35): row = 3
        elif(d100 > 34 and d100 < 40): row = 4
        elif(d100 > 39 and d100 < 45): row = 5
        elif(d100 > 44 and d100 < 50): row = 6
        elif(d100 > 49 and d100 < 55): row = 7
        elif(d100 > 54 and d100 < 60): row = 8
        elif(d100 > 59 and d100 < 65): row = 9
        elif(d100 > 64 and d100 < 68): row = 10
        elif(d100 > 67 and d100 < 71): row = 11
        elif(d100 > 70 and d100 < 74): row = 12
        elif(d100 > 73 and d100 < 76): row = 13
        elif(d100 > 75 and d100 < 78): row = 14
        elif(d100 > 77 and d100 < 80): row = 15
        elif(d100 > 79 and d100 < 82): row = 16
        elif(d100 > 81 and d100 < 84): row = 17
        elif(d100 == 84): row = 18
        elif(d100 == 85): row = 19
        elif(d100 == 86): row = 20
        elif(d100 == 87): row = 21
        elif(d100 == 88): row = 23
        elif(d100 == 89): row = 24
        elif(d100 == 90): row = 25
        elif(d100 == 91): row = 26
        elif(d100 == 92): row = 27
        elif(d100 == 93): row = 28
        elif(d100 == 94): row = 29
        elif(d100 == 95): row = 30
        elif(d100 == 96): row = 31
        elif(d100 == 97): row = 32
        elif(d100 == 98): row = 33
        elif(d100 == 99): row = 34
        else: row = 35
        
        out += mtable2[row]
    
    elif(id == 3):
        if(d100 < 16): row = 0
        elif(d100 > 15 and d100 < 23): row = 1
        elif(d100 > 22 and d100 < 28): row = 2
        elif(d100 > 27 and d100 < 33): row = 3
        elif(d100 > 32 and d100 < 38): row = 4
        elif(d100 > 37 and d100 < 43): row = 5
        elif(d100 > 42 and d100 < 48): row = 6
        elif(d100 > 47 and d100 < 53): row = 7
        elif(d100 > 52 and d100 < 58): row = 8
        elif(d100 > 57 and d100 < 63): row = 9
        elif(d100 > 62 and d100 < 68): row = 10
        elif(d100 > 67 and d100 < 73): row = 11
        elif(d100 > 72 and d100 < 76): row = 12
        elif(d100 > 75 and d100 < 79): row = 13
        elif(d100 > 78 and d100 < 82): row = 14
        elif(d100 > 81 and d100 < 85): row = 15
        elif(d100 > 84 and d100 < 88): row = 16
        elif(d100 > 87 and d100 < 90): row = 17
        elif(d100 > 89 and d100 < 92): row = 18
        elif(d100 == 92): row = 19
        elif(d100 == 93): row = 20
        elif(d100 == 94): row = 21
        elif(d100 == 95): row = 22
        elif(d100 == 96): row = 23
        elif(d100 == 97): row = 24
        elif(d100 == 98): row = 25
        elif(d100 == 99): row = 26
        else: row = 27
        
        out += mtable3[row]
    
    elif(id == 4):
        if(d100 < 21): row = 0
        elif(d100 > 20 and d100 < 31): row = 1
        elif(d100 > 30 and d100 < 41): row = 2
        elif(d100 > 40 and d100 < 51): row = 3
        elif(d100 > 50 and d100 < 58): row = 4
        elif(d100 > 57 and d100 < 63): row = 5
        elif(d100 > 62 and d100 < 68): row = 6
        elif(d100 > 67 and d100 < 73): row = 7
        elif(d100 > 72 and d100 < 78): row = 8
        elif(d100 > 77 and d100 < 83): row = 9
        elif(d100 > 82 and d100 < 88): row = 10
        elif(d100 > 87 and d100 < 93): row = 11
        elif(d100 > 92 and d100 < 96): row = 12
        elif(d100 > 95 and d100 < 99): row = 13
        elif(d100 == 99): row = 14
        else: row = 15
        
        out += mtable4[row]
        
    elif(id == 5):
        if(d100 < 31): row = 0
        elif(d100 > 30 and d100 < 56): row = 1
        elif(d100 > 55 and d100 < 71): row = 2
        elif(d100 > 70 and d100 < 86): row = 3
        elif(d100 > 85 and d100 < 94): row = 4
        elif(d100 > 93 and d100 < 99): row = 5
        else: row = 6
        
        out += mtable5[row]
        
    elif(id == 6):
        if(d100 < 16): row = 0
        elif(d100 > 15 and d100 < 19): row = 1
        elif(d100 > 18 and d100 < 22): row = 2
        elif(d100 > 21 and d100 < 24): row = 3
        elif(d100 == 24 or d100 == 25): row = 4
        elif(d100 == 26 or d100 == 27): row = 5
        elif(d100 == 28 or d100 == 29): row = 6
        elif(d100 == 30 or d100 == 31): row = 7
        elif(d100 == 32 or d100 == 33): row = 8
        elif(d100 == 34 or d100 == 35): row = 9
        elif(d100 == 36 or d100 == 37): row = 10
        elif(d100 == 38 or d100 == 39): row = 11
        elif(d100 == 40 or d100 == 41): row = 12
        elif(d100 == 42 or d100 == 43): row = 13
        elif(d100 == 44 or d100 == 45): row = 14
        elif(d100 == 46 or d100 == 47): row = 15
        elif(d100 == 48 or d100 == 49): row = 16
        elif(d100 == 50 or d100 == 51): row = 17
        elif(d100 == 52 or d100 == 53): row = 18
        elif(d100 == 54 or d100 == 55): row = 19
        elif(d100 == 56 or d100 == 57): row = 20
        elif(d100 == 58 or d100 == 59): row = 21
        elif(d100 == 60 or d100 == 61): row = 22
        elif(d100 == 62 or d100 == 63): row = 23
        elif(d100 == 64 or d100 == 65): row = 24
        elif(d100 > 65):
            row = 25
            for temp1 in range(66, 101):
                if(temp1 != d100): row+=1
                else: break
        
        out += mtable6[row]
        
    elif(id == 7):
        if(d100 < 12): row = 0
        elif(d100 > 11 and d100 < 15): row = 1
        elif(d100 > 14):
            row = 2
            for temp2 in range(15, 101):
                if(temp2 != d100): row+=1
                else: break
        
        out += mtable7[row]
        
    elif(id == 8):
        if(d100 < 11): row = 0
        elif(d100 > 10 and d100 < 55):
            row = 1
            for temp3 in range(11, 54, 2):
                if(temp3 != d100 and (temp3 + 1) != d100): row+=1
                else: break
        elif(d100 > 54):
            row = 23
            for temp4 in range(55, 101):
                if(temp4 != d100): row+=1
                else: break
        print(d100)
        out += mtable8[row]
    
    return out