from base_robot import BaseRobot
from pybricks.tools import wait
from robots import AdvancedDrivingBaseRobot


def Run(br: BaseRobot):
    MENU()


def Wait_for_press():

    while True:

        if br.hub.buttons.pressed() == {Button.LEFT}:
            return 1
        if br.hub.buttons.pressed() == {Button.RIGHT}:
            return 2


def MENU():

    while True:
        if Wait_for_press() == 1:
            if program_number != 4:
                program_number += 1
            else:
                program_number = 1
        else:
            if program_number == 1:
                print("1")
                break
            if program_number == 2:
                print("2")
                break
            if program_number == 3:
                print("3")
            if program_number == 4:
                print("4")


program_number = 1


if __name__ == "__main__":
    r = AdvancedDrivingBaseRobot()
    Run(r)
