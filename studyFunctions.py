from pywinauto import application, findbestmatch, findwindows, Desktop
import time
import outputFile
import supportingFunctions


# Click on the module of choice, which is provided by the user
# Flow:     1) Checks if the module item list is visible or not
#           2) If visible, click on the module and load it
#           3) If hidden, mouse scrolls the item list twice in order to see modules that are not in view
#           4) If still not visible, click on the Add protocol menu item, and try to add the module to the list
#           5) If still not available, then exit the program
def click_module(dialog, module, pid):
    if dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title=module, control_type="Button").exists():
        return

    counter = 0
    while True:
        # print dialog.print_control_identifiers()
        if dialog.child_window(title=module, control_type="ListItem").exists(timeout=0.5) is False:
                if counter == 0:
                    dialog.List.wheel_mouse_input(wheel_dist=60)  # module list scrollbar
                    if dialog.child_window(title=module, control_type="ListItem").exists() is True:
                        dialog.child_window(title=module, control_type="ListItem").click_input()
                        return

                dialog.List.wheel_mouse_input(wheel_dist=-(20+counter*20))

                counter += 1
                if counter == 2:
                    add_protocol(dialog, module, pid)

                if counter > 3: #Add a condition to errors if modules are not in protocols (i.e CT only?)
                    print "Can't find module."
                    exit()

        else:
            dialog.child_window(title=module, control_type="ListItem").click_input()
            break
            # if_modules_hidden(dialog)

    return


# Clicks and loads series
def load_series(dialog, study, window_name, series):

    window = supportingFunctions.find_window_func(window_name)

    command = "dialog.child_window(title=study, control_type='Window', found_index=0).SplitButton.Custom%s.\
        drag_mouse_input(dst=dialog.%s.rectangle())" % (series+4, window)

    exp_as_func = eval('lambda dialog, study, series: ' + command)

    if dialog.child_window(title=study, control_type='Window',
                           found_index=0).SplitButton.Scrollbar.exists() is True:
        dialog.child_window(title=study, control_type='Window',
                            found_index=0).SplitButton.Scrollbar.wheel_mouse_input(wheel_dist=60)

        if series > 6:
            dialog.child_window(title=study, control_type='Window',
                                found_index=0).SplitButton.Scrollbar.wheel_mouse_input(wheel_dist=-4)
        else:
            pass

    exp_as_func(dialog, study, series)

    ###### CONSIDER WRITING METHOD
    if dialog.child_window(control_type="Window", found_index=0).exists() is True and \
            dialog.child_window(title="OK Enter", control_type="Button").exists() is True:
        supportingFunctions.ignore_warning_message(dialog)

    return window


# Anonymize a study
# Flow:     1) Should be called after initialization function call
#           2) Takes in a study and preferred anonymized name desired
#           3) brings up the context menu, and anonymizes the study
def test1001_anonymize_study(dialog, study, anon_name, filename):

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
    outputFile.print_timing(1001, end-start, filename)
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


def reset_workspace(dialog):

    dialog.child_window(title="Workspace", control_type="MenuItem").click_input()
    Desktop(backend="uia").Menu.child_window(title="Reset Workspace", control_type="MenuItem").click_input()

    dialog.child_window(title="Reset Workspace", control_type="Window").child_window(
        title="Reset Enter", control_type="Button").click_input()

    return


def add_protocol(dialog, module, pid):

    dialog.MenuItem9.click_input()  # Add protocol step button
    connect_to_popup = application.Application(backend="uia").connect(process=pid)
    popup_dialog = connect_to_popup.MenuItem9
    popup_dialog.child_window(title=module, control_type="MenuItem").click_input()

    return
