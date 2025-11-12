from base_robot import BaseRobot
from current_robot import current_robot
from pybricks.tools import wait
# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.


def Run(br: BaseRobot):
    # r.hub.display.text("RobBot")
    # r.moveLeftAttachmentMotorForMillis(10, 10)
    # r.robot.arc(25, 45)
    br.robot.arc(1000, distance=248)
    br.driveForDistance(-100, 100)
    br.robot.arc(1000, distance=105)
    br.robot.arc(1000, distance=100)
    br.driveForDistance(-700, 100)
    
    #br.driveForDistance(100, 300)

    # hello="(❁´◡`❁)"
    # r.hub.display.text(hello)
    # r.hub.display.char(":")


if __name__ == "__main__":
    r = current_robot()
    Run(r)
