
        ### Created By Moe Soufan
        ### Creation Date: September 7, 2018

        # Main? function for automation efforts
        # Using pywinauto to detect UI elements on cvi42.exe
        # Inspect.exe used to identify elements

from pywinauto import application, Desktop, mouse, controls, findwindows
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
import viewerModule
import sys
import outputFile
import flowModule
import time
import short3d_TestSuite
import report42

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
        match = re.search('test(\d+)', str(f))
        # print match.group(1)

        try:
            f(dialog)
            outputFile.print_to_file(int(match.group(1)), filename)
        except TypeError:
            duration = f(dialog, app)
            outputFile.print_timing(int(match.group(1)), duration, filename)


if __name__ == "__main__":
    while True:
        try:

            # Initialize test
            filename = 'test.txt'

            dirname = os.path.dirname(__file__)
            a = os.path.join(dirname, 'Tests')

            sys.path.insert(0, a)
            import loadtest

            os.chdir("..")
            print os.getcwd()

            outputFile.print_header("Legend: ", filename)
            for test, description in loadtest.legend:
                outputFile.print_header("%s - %s" % (test, description), filename)

            outputFile.print_header("Test Starts: ", filename)

            # Launch cvi42 if not already running, grab process id. Login method called from within.
            pid, dialog, app = initialization.initialize_session(filename)
            print "Connected to cvi42.exe ProcessID #%s" % pid

            counter = 0
            while counter < 100:

                loadtest.run(dialog, app, pid, filename)

                counter += 1

            sys.exit()

        except:

            filename = 'test.txt'
            outputFile.print_error(filename)
            print "Exception Raised"

            try:
                supportingFunctions.ignore_warning_message(dialog)

            except findwindows.ElementNotFoundError:
                print "didn't work"
                # sys.exit()
