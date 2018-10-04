
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
import re
import os
import loadTest
import initialization
import supportingFunctions
import short3d
import biplanarLAX
import drawContour
import studyFunctions
import sys

# print pywinauto.__version__

# os.chdir("C:/")
# print os.getcwd()

# Launch cvi42 if not already running, grab process id. Login method called from within.
pid, dialog = initialization.initialize_session()
print "Connected to cvi42.exe ProcessID #%s" % pid

counter = 0
while counter < 10:

    # Load SA-3D Demo
    loadTest.load(dialog, 'SA-3D Demo')

    # Open module
    studyFunctions.click_module(dialog, "Short\n 3D", pid)

    # Load series Short3d on first iteration
    if counter == 0:
        sax3d = studyFunctions.load_series(dialog, 'SA-3D Demo', 7, "SAX3D Stack")

    # Click LV/RV ED/ES ML on Short3D
    short3d.click_ml_button(dialog, "Detect LV/RV Contours Current Slice")

    # Draw line contours on the SAX3D viewer
    drawContour.line_contour(dialog, sax3d, 5)

    # Delete all contours drawn on screen
    drawContour.clear_all(dialog)

    # Close the study
    loadTest.close_study(dialog)

    # Anonymize Function-Flow-Perfusion
    anon_study = loadTest.anonymize_study(dialog, "Function-Flow-Perfusion", "Demo-Trial-1")

    # Load the anonymized study
    loadTest.load(dialog, anon_study)

    # Click Biplanar LAX module
    studyFunctions.click_module(dialog, 'Biplanar\n LAX', pid)

    # Load series into 2CV and 4CV viewers
    cv2 = studyFunctions.load_series(dialog, anon_study, 2, "2CV")
    cv4 = studyFunctions.load_series(dialog, anon_study, 3, "4CV")

    # Click LA/RA ML button
    biplanarLAX.click_ml_button(dialog, "Detect LA/RA Contours Current Slice")

    # Draw some contours on 2CV and 4CV viewers
    drawContour.curved_measurement_contour(dialog, cv2, 4)
    drawContour.freehand_counter(dialog, cv4)

    # Close the study
    loadTest.close_study(dialog)

    # Delete the anonymized study
    loadTest.delete_anon_study(dialog, anon_study)

    # Increment the counter
    counter += 1

# while counter < 100:
#     anon_study = loadTest.anonymize_study(dialog, "Function-Flow-Perfusion", "Abra Malamar-Anon")
#     loadTest.load(dialog, anon_study)
#     loadTest.close_study(dialog)
#     loadTest.delete_anon_study(dialog, anon_study)
#     counter += 1

raw_input("Press Enter to continue...")
sys.exit()
