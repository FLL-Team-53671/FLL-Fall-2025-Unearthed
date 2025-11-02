from base_robot import BaseRobot
import robots

# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.


def Run(r: BaseRobot):
    # r.hub.display.text("RobBot")
    # r.moveLeftAttachmentMotorForMillis(10, 10)
    # r.robot.arc(25, 45)

    hello = "(❁´◡`❁)"
    r.hub.display.text(hello)
    # br.hub.display.char(":")


if __name__ == "__main__":
    r = robots.AdvancedDrivingBaseRobot()
    Run(r)
