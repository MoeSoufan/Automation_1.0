
        ### Created by: Moatassem Soufan
        ### Creation Date: September 7, 2018

from pywinauto import application, findbestmatch, findwindows, Desktop
import time
import outputFile


# Loads a study from the study database
def test1002_load(dialog, study_name, filename):

    if dialog.child_window(title=study_name, control_type="Window").exists() is True:
        print "Study already Loaded."
        return

    if dialog.child_window(title="Toolbar", control_type="ToolBar").\
            child_window(title="Patient List", control_type="Button").exists() is True:
        dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(title="Patient List",
                                                                                  control_type="Button").click_input()

    while True:
        try:
            dialog.Edit.set_text(study_name)
            dialog.child_window(title=study_name, control_type="TreeItem", found_index=0).double_click_input()
            start = time.time()

            if dialog.child_window(title="Study is already loaded.", control_type="StatusBar").exists() is True:
                dialog.child_window(title="Toolbar", control_type="ToolBar"). \
                    child_window(title="Return to Study", control_type="Button").click_input()
                break

            elif dialog.child_window(title="Study Already Open", control_type="Window").exists() is True:
                dialog.child_window(title="Yes Enter", control_type="Button", found_index=0).click_input()
                break

            else:
                dialog.child_window(title="Loading Study done", control_type="StatusBar").wait('visible', 10000)
                end = time.time()
                # print "Loading Study Time: %.2f" % (end - start)
                outputFile.print_timing(1002, end - start, filename)
                break

        except findwindows.ElementNotFoundError:
            try:
                dialog.child_window(title="Tags", control_type="Custom"). \
                                        child_window(title="Any", control_type="CheckBox").click_input()
                dialog.child_window(title=study_name, control_type="TreeItem").double_click_input()

            except findwindows.ElementNotFoundError:
                print "Study '%s' doesn't exist in database" % study_name
                exit()

    if dialog.child_window(title="Select indication:", control_type="Header").exists() is True:
        for x in xrange(10):
            dialog.dialog2.wheel_mouse_input(wheel_dist=-10000000)

            if dialog.child_window(title="No Indication", control_type="TreeItem").exists() is True:
                dialog.child_window(title="No Indication", control_type="TreeItem").double_click_input()
                break

    return


