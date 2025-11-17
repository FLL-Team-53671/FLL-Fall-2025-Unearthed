from base_robot import BaseRobot
from current_robot import current_robot

# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.

# Forge Mission

# . make sure cuddles is on the wall to start make the right castor right in front of the theta(o with a line in the middle)


def Run(br: BaseRobot):
    br.driveForDistance(670, 200)
    br.robot.arc(-115, 50)


if __name__ == "__main__":
    r = current_robot()
    Run(r)
