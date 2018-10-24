
        ### Created By Moe Soufan
        ### Creation Date: October 1, 2018

from pywinauto import findbestmatch, findwindows
import time
import supportingFunctions
import outputFile
import studyFunctions


# Click LA/RA ML button
def click_ml_button(dialog, button, app):
    start = time.time()
    dialog.child_window(title=button, control_type="SplitButton").click_input()

    dialog.progressbar.exists()
    app.wait_cpu_usage_lower(threshold=5, timeout=1000)
    end = time.time()

    print "Time to complete LA/RA Current Slice: %.2f" % (end - start)
    return end-start


def full_workflow(dialog, app, pid, study, button, series2CV, series4CV):

    studyFunctions.click_module(dialog, "Biplanar\n LAX", pid)
    studyFunctions.load_series(dialog, study, "2CV", series2CV)
    studyFunctions.load_series(dialog, study, "4CV", series4CV)

    ml_time = click_ml_button(dialog, button, app)

    return ml_time
