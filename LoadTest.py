
        ### Created by: Moatassem Soufan
        ### Creation Date: September 7, 2018

from pywinauto import application, findbestmatch, findwindows, Desktop
import time


# Loads a study from the study database
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
            dialog.child_window(title=study_name, control_type="TreeItem", found_index=0).double_click_input()
            start = time.time()

            if dialog.child_window(title="Study is already loaded.", control_type="StatusBar").exists() is True:
                dialog.child_window(title="Toolbar", control_type="ToolBar"). \
                    child_window(title="Return to Study", control_type="Button").click_input()
                break

            elif dialog.child_window(title="Study Already Open", control_type="Window").exists() is True:
                dialog.child_window().child_window(title="Study Already Open", control_type="Window").child_window(
                    title="Yes Enter", control_type="Button").click_input()

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

    if dialog.child_window(title="Select indication:", control_type="Header").exists() is True:
        for x in xrange(10):
            dialog.dialog2.wheel_mouse_input(wheel_dist=-10000000)

            if dialog.child_window(title="No Indication", control_type="TreeItem").exists() is True:
                dialog.child_window(title="No Indication", control_type="TreeItem").double_click_input()
                break

    return


# Anonymize a study
# Flow:     1) Should be called after initialization function call
#           2) Takes in a study and preferred anonymized name desired
#           3) brings up the context menu, and anonymizes the study
def anonymize_study(dialog, study, anon_name):

    if dialog.child_window(title="Toolbar", control_type="ToolBar").\
            child_window(title="Patient List", control_type="Button").exists() is True:
        dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(title="Patient List",
                                                                                  control_type="Button").click_input()

    dialog.Edit.set_text(study)
    dialog.window(title=study).right_click_input()
    Desktop(backend="uia").Menu.child_window(title="Anonymize Study", control_type="MenuItem").click_input()
    dialog.child_window(title="Anonymize", control_type="Window").Edit.set_text(anon_name)
    dialog.child_window(title="Anonymize", control_type="Window").OKEnter.click_input()

    start = time.time()
    dialog.child_window(title="Import Study done", control_type="StatusBar").wait('visible', 10000) or \
        dialog.child_window(title="Load image previews done", control_type="StatusBar").wait('visible', 10000)
    end = time.time()

    print "Time to anonymize study: %.2f" % (end - start)
    return anon_name


#  Delete anon study from the database
def delete_anon_study(dialog, anon_study):

    if "admin" not in dialog.texts()[0]:
        print "Not an Admin, cannot delete studies"
        return

    if dialog.child_window(title="Toolbar", control_type="ToolBar"). \
            child_window(title="Patient List", control_type="Button").exists() is True:
        dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(title="Patient List",
                                                                                  control_type="Button").click_input()
    dialog.Edit.set_text(anon_study)
    dialog.window(title=anon_study, found_index=0).right_click_input()
    Desktop(backend="uia").Menu.child_window(title="Delete Study", control_type="MenuItem").click_input()
    dialog.child_window(title="Delete Enter", control_type="Button").click_input()

    if dialog.child_window(title="Failed to remove study.", control_type="StatusBar").exists() is True:
        dialog.child_window(title="Cannot remove study", control_type="Window"). \
            child_window(title="OK Enter", control_type="Button").click_input()

        if dialog.child_window(title="Toolbar", control_type="ToolBar").\
                child_window(title="Return to Study", control_type="Button").exists() is True:

            delete_study(dialog, anon_study)

            dialog.child_window(title="Save workspace done.", control_type="StatusBar").wait('visible', 10000)
            dialog.Edit.set_text("")

        else:
            "Study loaded by other user"

    return


# Delete a study from the database
def delete_study(dialog, study):

    dialog.child_window(title="Workspace", control_type="MenuItem").click_input()
    Desktop(backend="uia").Menu.child_window(title="Close Study", control_type="MenuItem").click_input()
    dialog.window(title=study, found_index=0).right_click_input()
    Desktop(backend="uia").Menu.child_window(title="Delete Study", control_type="MenuItem").click_input()
    dialog.child_window(title="Delete Enter", control_type="Button").click_input()

    return


# Close a study
def close_study(dialog):

    if dialog.child_window(title="Toolbar", control_type="ToolBar"). \
            child_window(title="Patient List", control_type="Button").exists() is True \
            or dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Return to Study", control_type="Button").exists() is True:
        dialog.child_window(title="Workspace", control_type="MenuItem").click_input()
        Desktop(backend="uia").Menu.child_window(title="Close Study", control_type="MenuItem").click_input()

    return
