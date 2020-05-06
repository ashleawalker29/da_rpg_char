import random

def roll(num_of_dice, dice_sides):
    return sum([random.randint(1, dice_sides) for _ in range(0, num_of_dice)])
