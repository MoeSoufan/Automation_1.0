from pywinauto import application, findbestmatch, findwindows, Desktop
import time

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
                dialog.List.wheel_mouse_input(wheel_dist=-(20+counter*20))

                counter += 1
                if counter == 2:
                    dialog.MenuItem9.click_input()  # Add protocol step button
                    connect_to_popup = application.Application(backend="uia").connect(process=pid)
                    popup_dialog = connect_to_popup.MenuItem9
                    popup_dialog.child_window(title=module, control_type="MenuItem").click_input()

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

    windows_dict = {"MultipleLong": "MultipleLongCustom",
                    "2CV": "Custom11",              #If SAX window not on
                    "4CV": "Custom16",              #If SAX window not on
                    "SAX3D Stack": "SAX3DCustom"}

    for window in [k for k, v in windows_dict.items()
                   if v == windows_dict[window_name]]:
        # print windows_dict[window]
        command = "dialog.child_window(title=study, control_type='Window', found_index=0).SplitButton.Custom%s.\
            drag_mouse_input(dst=dialog.%s.rectangle())" % (series+4, windows_dict[window])

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

    return windows_dict[window]
