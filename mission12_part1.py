from base_robot import BaseRobot
from current_robot import current_robot
from pybricks.tools import wait




def Run(br: BaseRobot):
    # br.hub.display.text("RobBot")
    # br.moveLeftAttachmentMotorForMillis(10, 10)
    # br.robot.arc(25, 45)
    
    br.driveForDistance(300, 200)
    
    br.driveForDistance(-350, 200)
    #8 squares from the front of the robot lined up on the wall
    

    # br.driveForDistance(100, 300)

    # hello="(❁´◡`❁)"
    # br.hub.display.text(hello)
    # br.hub.display.char(":")


if __name__ == "__main__":
    r = current_robot()
    Run(r)
