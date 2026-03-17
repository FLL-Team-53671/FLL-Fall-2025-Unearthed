from base_robot import BaseRobot
from current_robot import current_robot

# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.

# Bucket Mission


def Run(br: BaseRobot):
    br.driveForDistance(625, 200)
    br.robot.arc(-65, 80)
    br.driveForDistance(300, 200)
    br.robot.turn(105)
    br.driveForDistance(-20, 200)
    br.moveArmDownIfUp()
    br.moveArmUpIfDown()
    br.driveForDistance(20, 200)
    br.robot.turn(-105)
    br.driveForDistance(-300, 200)
    br.robot.arc(65, 80)
    br.driveForDistance(-625, 200)


if __name__ == "__main__":
    br = current_robot()
    Run(br)
# the back right light gray piece with peggs sticking out should touch the black
# wall ,but it should line up with the 7th back square from the left to set it up
