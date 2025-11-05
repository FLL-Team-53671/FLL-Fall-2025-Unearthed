from base_robot import *

# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.


def Run(br: BaseRobot):
    # br.driveForDistance(50, 677)
    # br.moveLeftAttachmentMotorForMillis(millis=1000, speed=500)
    # br.robot.straight(50)
    # br.hub.display.text("go colfax cobras!")
    #  br.robot.turn(-30)
    #  br.robot.straight(550)
    # br.robot.turn(90)
    #  br.robot.straight(450)
    # br.robot.turn(-115)
    # br.robot.straight(1000)
    #for i in range (5):
      #br.driveForDistance(640, 200)
      #br.moveArmDownIfUp()
      #br.driveForDistance(-640, 200)
      #br.moveArmUpIfDown
      #br.robot.turn(-90)
      #br.driveForDistance(100, 200)
      #br.moveArmDownIfUp
      #br.robot.turn(90)
    br.hub.display.text("YAY")


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
    for i in range (10):
      br.driveForDistance(70, 120)
      br.driveForDistance(-50, 80)
                      
    

