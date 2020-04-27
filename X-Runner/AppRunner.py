'''

@ Author - Karan Pandya
@ Creation date - 08/27/2018
@ Description - Take the inputs from input GUI and run the script accordingly
'''

from Utilites.InputGUI import InputGUI
from Utilites.Execution import Execution
from Utilites.LogFileUtility import LogFileUtility

class AppRunner:

    ig = InputGUI()
    ig.window_creation()
    ig.validation(ig.username_flag, ig.team_flag, ig.task_type_flag)
    V_USER_NAME = ig.username
    V_TEAM = ig.team
    V_TASK_TYPE = ig.task_type
    lo = LogFileUtility(V_TASK_TYPE)
    ex = Execution(V_USER_NAME, V_TEAM, V_TASK_TYPE, lo)
    ex.main_execution()







