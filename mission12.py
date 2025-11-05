from base_robot import BaseRobot
from current_robot import current_robot

# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.


def Run(r: BaseRobot):
    # r.hub.display.text("RobBot")
    # r.moveLeftAttachmentMotorForMillis(10, 10)
    # r.robot.arc(25, 45)
    r.driveForDistance(100, 300)
    # hello="(❁´◡`❁)"
    # r.hub.display.text(hello)
    # r.hub.display.char(":")


if __name__ == "__main__":
    r = current_robot()
    Run(r)
