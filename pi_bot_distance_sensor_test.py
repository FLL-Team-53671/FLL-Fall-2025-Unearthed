from base_robot import BaseRobot
from current_robot import current_robot
from pybricks.tools import wait
from pybricks.pupdevices import Motor
from robots import  *
def Run(br: BaseRobot):
    PiRobot.leftDriveMotor.run(100)
    PiRobot.rightDriveMotor.run(100)
    
    
    
    



if __name__ == "__main__":
    r = current_robot()
    Run(r)