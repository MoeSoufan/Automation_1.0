
        ### Created By Moe Soufan
        ### Creation Date: September 7, 2018

        # Main? function for automation efforts
        # Using pywinauto to detect UI elements on cvi42.exe
        # Inspect.exe used to identify elements

# from pywinauto import application, Desktop
# from pywinauto import findbestmatch
# import subprocess
# import time
# import admin_test
# import pywinauto

import loadTest
import initialization
import supportingFunctions
import short3d

# print pywinauto.__version__

# Launch cvi42 if not already running, grab process id. Login method called from within.
pid, dialog = initialization.initialize_session()
print "Connected to cvi42.exe ProcessID #%s" % pid
# mainDialog.print_control_identifiers()

# Load test trial
loadTest.load(dialog)

# Check Toolbar Status
# supportingFunctions.check_toolbar_visible(dialog)
# supportingFunctions.check_toolbar_hidden(dialog)
# supportingFunctions.if_modules_hidden(dialog)
supportingFunctions.click_module(dialog, "Short\n 3D", pid)
short3d.checkall_toolbar_buttons(dialog)

exit()
