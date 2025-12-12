from base_robot import BaseRobot
from current_robot import current_robot
from pybricks.tools import wait


def Run(br: BaseRobot):
    br.driveForDistance(1950, 250)


if __name__ == "__main__":
    r = current_robot()
    Run(r)
