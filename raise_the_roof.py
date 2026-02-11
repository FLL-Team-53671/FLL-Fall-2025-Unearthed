from base_robot import BaseRobot
from current_robot import current_robot

# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.

# Raise The Roof Mission


def Run(br: BaseRobot):
    br.hub.display.char("1")
    br.driveForDistance(625, 200)
    br.hub.display.char("2")
    br.robot.arc(-65, 80)
    br.hub.display.char("3")
    br.driveForDistance(300, 200)
    br.hub.display.char("4")
    br.robot.turn(-150)
    br.hub.display.char("5")
    br.driveForDistance(315, 200)
    # br.driveForDistance(-35, 200)
    # br.robot.arc(-115, -50)
    # br.driveForDistance(-670, 200)
    br.driveForDistance(-150, 200)
    br.robot.turn(-30)
    br.driveForDistance(400, 200)
    br.robot.turn(45)
    br.driveForDistance(551, 200)


if __name__ == "__main__":
    br = current_robot()
    Run(br)
# the back right light gray piece with peggs sticking out should touch the black
# wall ,but it should line up with the 7th back square from the left to set it up
