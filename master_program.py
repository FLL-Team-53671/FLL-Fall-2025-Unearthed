from pybricks.tools import hub_menu
import mission12
import sample_mission1
import sample_mission2
import xbox_remote_control
from robots import *


program = hub_menu("a", "b", "c", "x")
if program == "a":
    r = AdvancedDrivingBaseRobot()
    mission12.Run(r)
elif program == "b":
    r = BaseRobot()
    sample_mission1.Run(r)
elif program == "c":
    r = BaseRobot()
    sample_mission2.Run(r)
elif program == "x":
    r = AdvancedDrivingBaseRobot()
    xbox_remote_control.run(r)
