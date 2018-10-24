import studyFunctions
import time
import outputFile


def confirm_report_tab_viewed(dialog, pid):

    studyFunctions.click_module(dialog, "Report", pid)
    dialog.child_window(title="Report", control_type="TabItem").click_input()

    return


def check_report42_status(dialog, pid, filename, flag):

    start = time.time()
    studyFunctions.click_module(dialog, "Report", pid)

    dialog.child_window(title="Cardiac Imaging Reporting - Report", control_type="Document").wait(
        'visible', timeout=100)

    dialog.child_window(title="Save in progress", control_type="Image").exists()
    dialog.child_window(title="Save in progress", control_type="Image").wait_not('visible', timeout=1000)
    end = time.time()

    print "%.2f" % float(end-start)
    outputFile.print_timing(flag, end-start, filename)
    return end-start


def add_to_report(dialog):

    if dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Add Report", control_type="Button").exists() is True:
        dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Add Report", control_type="Button").click_input()

    else:
        print "Add to report button not available"
    return
