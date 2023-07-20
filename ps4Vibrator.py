import pygame
import random
import pyfiglet
import colorama
from pystyle import Colors, Colorate

vibration = True
manette = ""

def detecter_manette():
    pygame.init()
    pygame.joystick.init()

    # Vérifier s'il y a des manettes connectées
    if pygame.joystick.get_count() == 0:
        print("No Controller Detected.")
        return None

    # Sélectionner la première manette
    manette = pygame.joystick.Joystick(0)
    manette.init()
    print("Controller : ", manette.get_name())

    return manette


def activer_vibration(manette, intensite, duree_ms):
    if not manette:
        print("No Controller Detected")
        return

    # Activer la vibration
    manette.rumble(intensite, intensite, duree_ms)

    # Attendez la durée spécifiée avant d'arrêter la vibration
    pygame.time.wait(duree_ms)
    manette.stop_rumble()


def pulsation():
    activer_vibration(manette, 0.2, 100)
    activer_vibration(manette, 0.4, 100)
    activer_vibration(manette, 0.6, 100)
    activer_vibration(manette, 0.8, 100)
    activer_vibration(manette, 1, 200)
    activer_vibration(manette, 0.8, 100)
    activer_vibration(manette, 0.6, 100)
    activer_vibration(manette, 0.4, 100)
    activer_vibration(manette, 0.2, 100)


def continue_vibra(intensiter):
    activer_vibration(manette, intensiter, 500)


def mid(level):
    if level == 0:
        activer_vibration(manette, 1.0, 500)
        return 1
    elif level == 1:
        activer_vibration(manette, 0.5, 500)
        return 0


def random_vibra():
    activer_vibration(manette, random.random(), 500)


def stop_rumble_mannette():
    manette.stop_rumble()


if __name__ == "__main__":

    manette = detecter_manette()

    custom_fig = pyfiglet.Figlet(font='graffiti')
    print(colorama.Fore.CYAN + "-------------------------------------------------------------------------------")
    print(Colorate.Horizontal(Colors.blue_to_cyan, custom_fig.renderText('Ps4 Vibrator'), 1))
    print(
        colorama.Fore.LIGHTBLUE_EX + "-------------------------------------------------------------------------------")
    print()
    print("Press Enter For Start")
    print()
    input()
    num = 0
    while True:

        print(colorama.Fore.RED + "1. " + colorama.Fore.GREEN + "Continue Vibration")
        print(colorama.Fore.RED + "2. " + colorama.Fore.GREEN + "Pulse Vibration")
        print(colorama.Fore.RED + "3. " + colorama.Fore.GREEN + "Random Vibration")

        try:
            num = int(input())
        except:
            print(colorama.Fore.RED + "Put a number")

        if num == 1:
            print(colorama.Fore.GREEN + "Power (1 - 10) : ", end="")
            intensiter = 1.0
            intensiter = int(input()) / 10
            print("Stop script for restart")

        if manette:

            while vibration:

                if num == 1:
                    continue_vibra(intensiter)
                elif num == 2:
                    pulsation()
                elif num == 3:
                    random_vibra()

                else:
                    break

manette.stop_rumble()
