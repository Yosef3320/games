import random
import pygame
from time import sleep
from datetime import datetime  #  Import datetime for date checking

print("welcome to blooket pack opening simulator!!\nAre you ready to open some packs?(we also sell blooks here)")
sleep(4)
#  Initialize Pygame Mixer
pygame.mixer.init()

#  Define ANSI escape codes for colors
BRIGHT_YELLOW_BG = "\033[1;43m"
MAGENTA_BG = "\033[45m"
TEAL_BG = "\033[46m"
GREEN_BG = "\033[42m"
BLUE_BG = "\033[44m"
RED_BG = "\033[41m"
RESET = "\033[0m"

collected_blooks = []

#  Item categories with their items and probabilities
ITEM_CATEGORIES = {
    "mystical": (["phantom king", "rainbow astronaut"], 0.001),
    "chroma": (["blue slime monster", "rainbow panda"], 0.02),
    "legendary": (["megalodon", "mega bot"], 0.5),
    "epic": (["Bush monster", "Triceratops"], 3),
    "rare": (["UFO", "Buddy bot"], 7),
    "uncommon": (["Happy bot", "stars"], 17),
    "common": (["anaconda", "chick"], 23),
}

#  St. Patrick's Day items to add
st_patricks_items = {
    "mystical": ["leprechaun", "golden pot"],
    "chroma": ["lucky frog","lucky hamster"],
    "legendary": ["shamrock dragon"],
    "epic": ["four-leaf clover"],
    "rare": ["lucky coin"],
    "uncommon": ["rainbow hat"],
    "common": ["green bunny"],
}
# valentiens day items to add
valentiens_day_items = {
    "mystical": ["chocatate heart box", "love you teddy bare"],
    "chroma": ["lovely frog","lovely planet","lovely peackock"],
    "legendary": ["heart"],
    "epic": ["valentien card"],
    "rare": ["heart cheese"],
    "uncommon": ["rose"],
    "common": ["heart pop it"],
}
# christmas items to add
chrismas_items = {
    "mystical": ["chocatate heart box", "love you teddy bare"],
    "chroma": ["elf sweater snow man","frost wreath","london snow globe","santa cluas"],
    "legendary": ["santa"],
    "epic": ["snowman"],
    "rare": ["roudolph","ginger bread man","ginger bread house"],
    "uncommon": ["snow globe","holiday gift","hot choclate"],
    "common": ["holiday wreath","stocking"],
}
# hallaween items to add
hallaween_items = {
    "mystical": ["skeloton"],
    "chroma": ["spooky gost","pumpkin cookie","gost cookie","red gummy bear"],
    "legendary": ["gost"],
    "epic": ["were wolf"],
    "rare": ["carmel apple","mummy","zombie"],
    "uncommon": ["swamp monster","vampire"],
    "common": ["pumpkin","frankenstein"],
}
# thanksgiving items to add
thanks_giving_items = {
    "mystical": ["turkey"],
    "chroma": ["meme'ster turkey","dancing turkey","fall leaf"],
    "legendary": ["legendary guru"],
    "epic": ["guru"],
    "rare": ["crandberry salce","thanks giving meme lord"],
    "uncommon": ["sassy pilgrim"],
    "common": ["traveler","leaf"],
}
# easter items to add
easter_items = {
    "mystical": ["easter bunny"],
    "chroma": ["rainbow egg","chocalate easter bunny","chocalate egg"],
    "epic": ["vintage bunny"],
    "legendary": ["easter egg"],
    "rare": ["cross","egg hunter"],
    "uncommon": ["easter basket"],
    "common": ["carrot"],
}


#  Player coins at the start
coins = 35
# defining functions
def is_st_patricks_day():
    today = datetime.now()
    return today.month == 3
def is_valentiens_day():
    today = datetime.now()
    return today.month == 2 
def is_chrismas():
    today = datetime.now()
    return today.month == 12
def is_hallaween():
    today = datetime.now()
    return today.month == 10
def is_thanks_giving():
    today = datetime.now()
    return today.month == 11
def is_easter():
    today = datetime.now()
    return (today.month == 3 and today.day <= 22) or (today.month == 4 and today.day <= 20) 


def choose_category():
    total = sum(prob for _, prob in ITEM_CATEGORIES.values())
    rand = random.uniform(0, total)
    
    cumulative = 0
    for category, (items, prob) in ITEM_CATEGORIES.items():
        cumulative += prob
        if rand < cumulative:
            return category

def randomizer():
    category = choose_category()
    item = random.choice(ITEM_CATEGORIES[category][0])
    
    #  If it's a special day, add more items
    if is_st_patricks_day():
        item = random.choice(st_patricks_items[category] + ITEM_CATEGORIES[category][0])
    if is_valentiens_day():
        item = random.choice(valentiens_day_items[category] + ITEM_CATEGORIES[category][0])
    if is_chrismas():
        item = random.choice(chrismas_items[category] + ITEM_CATEGORIES[category][0])
    if is_hallaween():
        item = random.choice(hallaween_items[category] + ITEM_CATEGORIES[category][0])
    if is_thanks_giving():
        item = random.choice(thanks_giving_items[category] + ITEM_CATEGORIES[category][0])
    if is_easter():
        item = random.choice(easter_items[category] + ITEM_CATEGORIES[category][0])
    sleep(1.3)
    
    return category, item

def sell_item(category):
    # finding the values of each catagory
    value_map = {
        "mystical": 1000,
        "chroma": 250,
        "legendary": 200,
        "epic": 75,
        "rare": 10,
        "uncommon": 5,
        "common": 1,
    }
    return value_map.get(category, 0)

def open_packs():
    global coins
    if coins < 25:
        print("Not enough coins to buy packs. You need 25 coins.")
        return

    coins -= 25  # Deduct the cost of the five-pack
    for _ in range(5):
        category, item = randomizer()
        print(f"{BRIGHT_YELLOW_BG}{category.capitalize()}: {item}{RESET}")
        collected_blooks.append((category, item))  # Automatically keep the item
        
        sleep(1.5)  # Pause for a moment before the next item



def sell_collected_blooks():
    global coins
    if not collected_blooks:
        print("You have no Blooks to sell.")
        return

    print("Your collected Blooks:")
    for index, (category, item) in enumerate(collected_blooks):
        print(f"{index + 1}. {item} (Category: {category})")

    sell_indices = input("Enter the numbers of the Blooks you want to sell, separated by commas (or 'cancel' to go back): ").strip().lower()
    
    if sell_indices == 'cancel':
        return

    # Split input into a list and convert to integers
    try:
        sell_indices = [int(i) - 1 for i in sell_indices.split(',')]
        total_coins = 0

        # Sell each selected Blook
        for index in sell_indices:
            if 0 <= index < len(collected_blooks):
                category, item = collected_blooks.pop(index)  # Remove the item from the list
                total_coins += sell_item(category)  # Sell item for coins
                print(f"You sold {item} for {sell_item(category)} coins.")
            else:
                print(f"Invalid number: {index + 1}. It has been skipped.")

        # Add total coins earned to the player's balance
        coins += total_coins
        print(f"Total coins earned from sales: {total_coins} coins.")
        
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")







# main game loop
while True:
    print(f"You have {coins} Blook Coins.")
    print("1. Open a five-pack for 25 Blook Coins.")
    print("2. Sell collected Blooks.")
    print("3. Exit.")

    action = input("Choose an action (1/2/3): ").strip()
    if action == '1':
        open_packs()
    elif action == '2':
        sell_collected_blooks()
    elif action == '3':
        print("Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter '1', '2', or '3'.")
