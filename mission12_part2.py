from base_robot import BaseRobot
from current_robot import current_robot
from pybricks.tools import wait



def Run(br: BaseRobot):
    # br.hub.display.text("RobBot")
    # br.moveLeftAttachmentMotorForMillis(10, 10)
    # br.robot.arc(25, 45)
    
    br.driveForDistance(530, 200)
    
    br.driveForDistance(-580, 200)
    #at the front of the red challenge rectangle lined up on the side

    # br.driveForDistance(100, 300)

    


if __name__ == "__main__":
    r = current_robot()
    Run(r)
