
        ### Created By Moe Soufan
        ### Creation Date: October 1, 2018

from pywinauto import findbestmatch, findwindows
import time
import supportingFunctions


# Load series into 2CV window
def load_2cv_series(dialog, study, series):

    command = "dialog.child_window(title=study, control_type='Window', found_index=0).SplitButton.Custom%s.\
    drag_mouse_input(dst=dialog.Custom11.rectangle())" % (series+4) #Without SAX Window Enabled Custom 11

    supportingFunctions.load_series(dialog, study, series, command)


# Load series into 4CV window
def load_4cv_series(dialog, study, series):

    command = "dialog.child_window(title=study, control_type='Window', found_index=0).SplitButton.Custom%s.\
    drag_mouse_input(dst=dialog.Custom16.rectangle())" % (series+4)

    supportingFunctions.load_series(dialog, study, series, command) #Without SAX Window Enabled Custom 16

    return


# Click LA/RA ML button
def click_ml_button(dialog, button):
    start = time.time()
    dialog.child_window(title=button, control_type="SplitButton").click_input()
    dialog.progressbar.exists()
    end = time.time()

    print "Time to complete LA/RA Current Slice: %.2f" % (end - start)

    return
