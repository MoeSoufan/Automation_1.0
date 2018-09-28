
        ### Created By Moe Soufan
        ### Creation Date: September 7, 2018

        # Main? function for automation efforts
        # Using pywinauto to detect UI elements on cvi42.exe
        # Inspect.exe used to identify elements

from pywinauto import application, Desktop, mouse, controls
# from pywinauto import findbestmatch
# import subprocess
# import time
# import admin_test
# import pywinauto
import os
import loadTest
import initialization
import supportingFunctions
import short3d

# print pywinauto.__version__

# os.chdir("C:/")
# print os.getcwd()

# Launch cvi42 if not already running, grab process id. Login method called from within.
pid, dialog = initialization.initialize_session()
print "Connected to cvi42.exe ProcessID #%s" % pid

# Load test trial
loadTest.load(dialog, 'SA-3D Demo')

# Open module
supportingFunctions.click_module(dialog, "Short\n 3D", pid)
# Load series
supportingFunctions.load_series(dialog, 'SA-3D Demo', 7)
#
# Click ML on Short3D
short3d.click_ml_button(dialog, "Detect LV/RV Contours Current Slice")


exit()
