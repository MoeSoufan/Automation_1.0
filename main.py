
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
import biplanarLAX

# print pywinauto.__version__

os.chdir("C:/")
print os.getcwd()

# Launch cvi42 if not already running, grab process id. Login method called from within.
pid, dialog = initialization.initialize_session()
print "Connected to cvi42.exe ProcessID #%s" % pid
# # Check Toolbar status
# supportingFunctions.turn_on_toolbar(dialog)
counter = 0
while counter < 30:
###########################################Short3D Demo
    # Load SA-3D Demo
    loadTest.load(dialog, 'SA-3D Demo')
    # Open module
    supportingFunctions.click_module(dialog, "Short\n 3D", pid)
    # Load series Short3d
    short3d.load_sax_series(dialog, 'SA-3D Demo', 7)
    # Click LV/RV ED/ES ML on Short3D
    short3d.click_ml_button(dialog, "Detect LV/RV Contours Current Slice")

    # Load Function Flow Perfusion
    loadTest.load(dialog, 'Function-Flow-Perfusion')
    # Click Biplanar LAX module
    supportingFunctions.click_module(dialog, 'Biplanar\n LAX', pid)
    # Load series 2CV
    biplanarLAX.load_2cv_series(dialog, "Function-Flow-Perfusion", 2)
    biplanarLAX.load_4cv_series(dialog, "Function-Flow-Perfusion", 3)
    # Click LA/RA ML button
    biplanarLAX.click_ml_button(dialog, "Detect LA/RA Contours Current Slice")
    counter += 1

raw_input("Press Enter to continue...")
exit()
