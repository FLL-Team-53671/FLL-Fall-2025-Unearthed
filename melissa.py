from advanced_base_robot import *

# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.

def Run(br: AdvancedBaseRobot): 
    br.driveForDistance (200, 100)
    br.moveLeftAttachmentMotorForMillis(millis=1000, speed=500)

if __name__ == "__main__":
    br = AdvancedBaseRobot()
    #br = PiRobot()
    Run(br)