from advanced_base_robot import *

# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.


def Run(br: BaseRobot):
    # br.hub.display.text("RobBot")
    # br.moveLeftAttachmentMotorForMillis(10, 10)
    # br.robot.arc(25, 45)
    
    hello="(❁´◡`❁)"
    br.hub.display.text(hello)
    #br.hub.display.char(":")

if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
