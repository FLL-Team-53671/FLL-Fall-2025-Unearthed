from base_robot import BaseRobot
from current_robot import current_robot
def Run(br: BaseRobot):
    br.moveArmUpIfDown()
    br.driveForDistance(625, 200)
    br.robot.arc(-65, 80)
    br.driveForDistance(300, 200)
    br.robot.turn(180)
    br.driveForDistance(-300,200)
    br.robot.turn(-73)
    br.driveForDistance(-104,200)
    br.moveArmUpIfDown()
    br.moveArmDownIfUp()    
    
if __name__ == "__main__":
    br = current_robot()
    Run(br)
# line up base hub between the two left-most bold lines with the arm up (: