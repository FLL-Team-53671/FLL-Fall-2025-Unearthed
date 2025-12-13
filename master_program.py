from pybricks.tools import hub_menu
import go_across_the_board
import melissa
import mission12_part1
import mission12_part2
import sample_mission1
import mission6_and_5
import xbox_remote_control
from current_robot import current_robot
import mission_raise_the_roof
import mission9

while True:
    program = hub_menu("1", "2", "3", "4", "5", "x", "A")
    r = current_robot()
    if program == "1":
        mission12_part1.Run(r)
    elif program == "2":
        mission12_part2.Run(r)
    elif program == "3":
        mission6_and_5.Run(r)
    elif program =="4":
        mission_raise_the_roof.Run(r)
    elif program =="5":
        mission9.Run(r)
    elif program == "x":
        xbox_remote_control.run(r)
    elif program == "A":
        go_across_the_board.Run(r)
    
