from base_robot import BaseRobot
from current_robot import current_robot



def Run(br: BaseRobot):
    br.driveForDistance(625, 200)
    br.robot.arc(-150, 120)
    br.driveForDistance(50, 200)
    br.robot.turn(-90)
    br.driveForDistance(60, 200)
    br.driveForDistance(-60, 200)
    br.robot.turn(90)
    br.driveForDistance(-50, 200)
    br.robot.arc(-150, -120)
    br.driveForDistance(-625, 200)
    
    
    
    



if __name__ == "__main__":
    r = current_robot()
    Run(r)
