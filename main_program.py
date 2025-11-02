from pybricks.tools import hub_menu
import mission12
import sample_mission1
import sample_mission2
from advanced_base_robot import *
from base_robot import *

program = hub_menu("a", "b", "c")
if program == "a":
    br = AdvancedBaseRobot()
    mission12.Run(br)
if program == "b":
    br = BaseRobot()
    sample_mission1.Run(br)
if program == "c":
    br = BaseRobot()
    sample_mission2.Run(br)
