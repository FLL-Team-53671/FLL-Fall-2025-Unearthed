from base_robot import BaseRobot
from current_robot import current_robot
from pybricks.tools import wait

# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.


def Run(br: BaseRobot):
    # br.hub.display.text("RobBot")
    # br.moveLeftAttachmentMotorForMillis(10, 10)
    # br.robot.arc(25, 45)
    
    br.driveForDistance(350, 100)
    
    br.driveForDistance(-400, 100)
    

    # br.driveForDistance(100, 300)

    # hello="(❁´◡`❁)"
    # br.hub.display.text(hello)
    # br.hub.display.char(":")


if __name__ == "__main__":
    r = current_robot()
    Run(r)
