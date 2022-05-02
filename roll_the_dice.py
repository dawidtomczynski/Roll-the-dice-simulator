from random import randint


def roll_the_dice():
    dice_list = [3, 4, 6, 8, 10, 12, 20, 100]
    a_list = []
    while True:
        try:
            dy = int(input("Ile ścian ma kostka? "))
            if dy in dice_list:
                x = int(input("Ile rzutów kostką chcesz wykonać? "))
                z = int(input("Jaką liczbę dodać / odjąć od wyniku? "))
                for i in range(x):
                    a_list.append(randint(1, dy))
                    roll = sum(a_list) + z
                print(roll)
                return None
            else:
                print("Nie ma takiej kostki.")
        except ValueError:
            print("Możesz podać tylko liczbę.")


roll_the_dice()
