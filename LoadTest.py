
        ### Created by: Moatassem Soufan
        ### Creation Date: September 7, 2018

from pywinauto import application, findbestmatch, findwindows, controls
import time


def load(dialog, study_name):

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
            dialog.child_window(title=study_name, control_type="TreeItem").double_click_input()
            start = time.time()

            if dialog.child_window(title="Study is already loaded.", control_type="StatusBar").exists() is True:
                dialog.child_window(title="Toolbar", control_type="ToolBar"). \
                    child_window(title="Return to Study", control_type="Button").click_input()
                break

            else:
                dialog.child_window(title="Loading Study done", control_type="StatusBar").wait('visible', 10000)
                end = time.time()
                print "Loading Study Time: %.2f" % (end - start)
                break

        except findwindows.ElementNotFoundError:
            try:
                dialog.child_window(title="Tags", control_type="Custom"). \
                                        child_window(title="Any", control_type="CheckBox").click_input()
                dialog.child_window(title=study_name, control_type="TreeItem").double_click_input()

            except findwindows.ElementNotFoundError:
                print "Study '%s' doesn't exist in database" % study_name
                exit()

    return
