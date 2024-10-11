import random
import pygame #type ignore
from time import sleep


# Define ANSI escape codes for bright yellow background
BRIGHT_YELLOW_BG = "\033[1;43m"
MAGENTA_BG = "\033[45m"
RESET = "\033[0m"
TEAL_BG = "\033[46m"
GREEN_BG = "\033[42m"
BLUE_BG = "\033[44m"
red = "\033[41m"

pygame.mixer.init()


def randomizer():
    # Define items for each category
    mystical_items = ["phantom king","rainbow astronaut","tim the alien","spooky gost","spooky pumpkin"]

    chroma_items = ["blue slime monster", "rainbow panda", "teal platypus","lovely frog","lucky frog","lime astrounaut","rainbow narwal"]

    legendary_items = ["megalodon", "mega bot", "king", "t-rex","captain black beard","baby shark","lion","king of hearts","santa cluas","yeti","sugar glider"]

    epic_items = ["Bush monster", "Triceratops", "french toast", "pizza", "narwhal", "dolphin", "chameleon", "rocket ship", "caterpillar", "kraken","madd hatter","were wolf","unicorn","craken"]

    rare_items = ["UFO", "Buddy bot", "Waffle", "pancake", "blobfish", 
                  "Puffer fish", "Dragon", "Watson", "Lemur", "Joey",
                  "Kangaroo", "Velociraptor", "Peacock", "Cheshire cat", "Mummy", "donk", "platypus", "reindeer", "octopus", "jester","queen"]
    
    uncommon_items = ["Happy bot", "stars", "earth", "toast", "milk", 
                      "fossil", "Amber", "orange juice", "breakfast combo", "alien", 
                      "frog", "panda", "Sloth", "crab", "Jellyfish", 
                      "zebra", "witch", "wizard", "buccaneer", "deckhand", "queen of hearts", "stegosaurus", "flamingo", "cereal", "yogurt", "frankenstein", "pumpkin", "ice bat", "vampire", "treasure map", "crater's","angry bot","holiday gift","hot chocalate","lovely bot","fairy","elf","swamp monster","alice","drink me","eat me","two of spaids","boot",""]
    common_items = ["anoconda","chick","chicken","cow","goat","duck","brown sheep","dog","cat","bunny","goldfish","hamster","turtle","kitten","huskie","bear","moose","fox","raccoon","squirrel","owl","hedgehog","dear","wolf","beaver","tiger","orangatang","Cockatoo","parrot","jaguar","macaw","toucan","panther","Capuchin","gorilla","hippo","rino","girraf","snowy owl","polar bear","hare","baby penguin","penguin","artic fox","seal","walrus"]
    # Define the probabilities for each category in decimal percentages
    probabilities = {
        "mystical": 0.001,   # 0.001%
        "chroma": 0.02,     # 0.02%
        "legendary": 0.5,  # 0.5%
        "epic": 3,       # 3%
        "rare": 7,       # 7%
        "uncommon": 17,   # 17%
        "common": 23,
    }

    # Create a cumulative probability list
    categories = []
    for category, weight in probabilities.items():
        count = int(weight * 100)  # Convert to integer count for selection
        categories.extend([category] * count)

    # Randomly select a category
    random_category = random.choice(categories)

    # Select a random item based on the category
    if random_category == "legendary":
        item = random.choice(legendary_items)
        sound = pygame.mixer.Sound(r"C:\Users\joe\OneDrive\Documents\python\Joe Games\Music files\lazer.mp3")
        sound.play()
        return BRIGHT_YELLOW_BG + f"Legendary: {item}" + RESET
    elif random_category == "epic":
        item = random.choice(epic_items)
        return red + f"Epic: {item}" + RESET
    elif random_category == "chroma":
        item = random.choice(chroma_items)
        return TEAL_BG + f"Chroma: {item}" + RESET
    elif random_category == "mystical":
        item = random.choice(mystical_items)
        return MAGENTA_BG + f"Mystical: {item}" + RESET
    elif random_category == "rare":
        item = random.choice(rare_items)
        return BLUE_BG + f"Rare: {item}" + RESET
    elif random_category == "uncommon":
        item = random.choice(uncommon_items)
        return GREEN_BG + f"Uncommon: {item}" + RESET
    else:  #common
        item = random.choice(common_items)
        return f"common: {item}"
    
def open_packs():
    for i in range(10):
        random_category = randomizer()
        print(random_category)
        sleep(2)

while True:
    open_packs()
    continue_choice = input("Do you want to open another ten packs? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Thank you for playing!")
        break

