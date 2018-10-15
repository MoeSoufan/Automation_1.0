
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
import viewermodule
import sys
import outputFile
import time
import short3d_TestSuite
from collections import OrderedDict
# print pywinauto.__version__


def some_magic():

    functions = sorted(
        [
            getattr(short3d_TestSuite, func) for func in dir(short3d_TestSuite)
            if hasattr(getattr(short3d_TestSuite, func), "order")
        ],
        key=(lambda func: func.order)
        )
    for f in functions:
        print f
        try:
            f(dialog, filename)
        except TypeError:
            f(dialog, filename, app)


if __name__ == "__main__":
    try:

        filename = 'test.txt'

        # Initialize test
        os.chdir("..")
        print os.getcwd()

        # Launch cvi42 if not already running, grab process id. Login method called from within.
        pid, dialog, app = initialization.initialize_session(filename)
        print "Connected to cvi42.exe ProcessID #%s" % pid
        counter = 0

        while counter < 100:
            # Anonymize SA-3D Demo
            # anon_study = loadTest.anonymize_study(dialog, "SA-3D Demo", "Demo-Trial-1", filename)

            # Load the study
            loadTest.load(dialog, "SA-3D Demo", filename)

            # Open module
            studyFunctions.click_module(dialog, "Short\n 3D", pid)

            # Load series Short3d
            sax3d = studyFunctions.load_series(dialog, "SA-3D Demo", "SAX3D Stack", 7)

            # Run Test-suite
            some_magic()

            # Reset the workspace
            loadTest.reset_workspace(dialog)

            # Close the study
            loadTest.close_study(dialog)

        # # Delete the anonymized study
        # loadTest.delete_anon_study(dialog, anon_study)

            counter += 1

    except:

        filename = 'test.txt'
        outputFile.print_error(filename)
        print "Exception Raised"

# counter = 0
# while counter < 2:
#     # Anonymize SA-3D Demo
#     anon_study = loadTest.anonymize_study(dialog, "SA-3D Demo", "Demo-Trial-1")
#
#     # Load the anonymized study
#     loadTest.load(dialog, anon_study)
#
#     # Open module
#     studyFunctions.click_module(dialog, "Short\n 3D", pid)
#
#     # Load series Short3d
#     sax3d = studyFunctions.load_series(dialog, anon_study, "SAX3D Stack", 7)
#
#     # Click LV/RV ED/ES ML on Short3D
#     short3d.click_ml_button(dialog, "Detect LV/RV Contours Current Slice")
#
#     # Draw line contours on the SAX3D viewer
#     drawContour.line_contour(dialog, sax3d, 5)
#
#     # Delete all contours drawn on screen
#     drawContour.clear_all(dialog)
#
#     # Close the study
#     loadTest.close_study(dialog)
#
#     # Delete the anonymized study
#     loadTest.delete_anon_study(dialog, anon_study)
#
#     # Anonymize Function-Flow-Perfusion
#     anon_study2 = loadTest.anonymize_study(dialog, "Function-Flow-Perfusion", "Demo-Trial-1")
#
#     # Load the anonymized study
#     loadTest.load(dialog, anon_study2)
#
#     # Click Biplanar LAX module
#     studyFunctions.click_module(dialog, 'Biplanar\n LAX', pid)
#
#     # Load series into 2CV and 4CV viewers
#     cv2 = studyFunctions.load_series(dialog, anon_study, "2CV", 2)
#     cv4 = studyFunctions.load_series(dialog, anon_study, "4CV", 3)
#
#     # Click LA/RA ML button
#     biplanarLAX.click_ml_button(dialog, "Detect LA/RA Contours Current Slice")
#
#     # Draw some contours on 2CV and 4CV viewers
#     drawContour.curved_measurement_contour(dialog, cv2, 4)
#     drawContour.freehand_counter(dialog, cv4)
#
#     # Close the study
#     loadTest.close_study(dialog)
#
#     # Delete the anonymized study
#     loadTest.delete_anon_study(dialog, anon_study2)
#
#     # Increment the counter
#     counter += 1

# dialog.child_window(title="Segment SAX - ML", control_type="SplitButton").print_control_identifiers()
# dialog.Custom2.print_control_identifiers()
# viewermodule.load_series(dialog, "SA-3D Demo", "Viewer1", 2)
# viewermodule.load_series(dialog, "SA-3D Demo", "Viewer2", 5)
# dialog.Custom2.ListBox1.click_input()

# raw_input("Press Enter to continue...")
#
# sys.exit()
