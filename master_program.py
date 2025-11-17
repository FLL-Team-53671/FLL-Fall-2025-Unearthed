from pybricks.tools import hub_menu

import melissa
import mission12_part1
import mission12_part2
import sample_mission1
import sample_mission2
import xbox_remote_control
from current_robot import current_robot


program = hub_menu("a", "b", "c", "x")
r = current_robot()
if program == "a":
    mission12_part1.Run(r)
elif program == "b":
    mission12_part2.Run(r)
elif program == "c":
    sample_mission2.Run(r)
elif program == "M":
    melissa.Run(r)
elif program == "x":
    xbox_remote_control.run(r)
