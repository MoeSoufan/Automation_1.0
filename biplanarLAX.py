
        ### Created By Moe Soufan
        ### Creation Date: October 1, 2018

from pywinauto import findbestmatch, findwindows
import time
import supportingFunctions
import outputFile


# Click LA/RA ML button
def click_ml_button(dialog, button):
    start = time.time()
    dialog.child_window(title=button, control_type="SplitButton").click_input()
    dialog.progressbar.exists()
    end = time.time()

    print "Time to complete LA/RA Current Slice: %.2f" % (end - start)
    return
