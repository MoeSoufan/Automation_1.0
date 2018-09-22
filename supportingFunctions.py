

        ###   Created by: Moe Soufan
        ###   Creation Date: September 12, 2018

from pywinauto import application, findbestmatch, findwindows
import re


# If the toolbar is hidden and un-docked, Auto hide button is clicked and toolbar is re-docked
# Flow:     1) Checks if the toolbar is visible or hidden
#           2) If hidden, moves the cursor to the workspace tab, the hidden widget should appear
#           3) If the widget is hidden, and shows when the mouse is nearby the detection area, click the dock button
def check_toolbar_visible(dialog):
    if dialog.window(title="Toolbar").exists() is False:
        dialog.child_window(title="Workspace", control_type="MenuItem").move_mouse_input(absolute=False)
        dialog.window(title="Toolbar").CheckBox.click_input()

    return


# If the toolbar is visible and docked, un-docks the toolbar
# Flow:     1) Checks if the toolbar is visible or hidden
#           2) If visible, click the hide button
def check_toolbar_hidden(dialog):
    if dialog.window(title="Toolbar").exists() is True:
        dialog.window(title="Toolbar").CheckBox.click_input()

    return


# If the cvi42 window is minimized, connects to the system tray and finds the icon
# Flow:     1) Connect to the explorer application in order to connect to the system tray toolbar
#           2) Find the cvi42 icon in the toolbar, and click the icon to bring the window back to the foreground
def if_cvi42_minimized():
    icon_app = application.Application(backend="uia").connect(path="explorer")
    tray_dialog = icon_app.window(class_name="Shell_TrayWnd")
    tray_dialog.child_window(title="cvi42 - Shortcut - 1 running window").click()

    return


# If the module widget is hidden, check it back on
# Flow:     1) move the mouse cursor to the left edge of the cvi42 application window
#           2) Hover in the midpoint of the edge, in case the application window is too large/small
#           3) When the hidden widget appears, clicks the button to dock it
def if_modules_hidden(dialog):
    # print re.sub(r'[^\w]', '', str(dialog.rectangle())).split('B')[1] #Left, Top, Right,Bottom
    dialog.move_mouse_input(coords=(10, int(re.sub(r'[^\w]', '', str(dialog.rectangle())).split('B')[1])/2),
                            absolute=False)
    # dialog.print_control_identifiers()
    dialog.CheckBox2.click_input()

    return


# Click on the module of choice, which is provided by the user
# Flow:     1) Checks if the module item list is visible or not
#           2) If visible, click on the module and load it
#           3) If hidden, mouse scrolls the item list twice in order to see modules that are not in view
#           4) If still not visible, click on the Add protocol menu item, and try to add the module to the list
#           5) If still not available, then exit the program
def click_module(dialog, module, pid):

    counter = 0
    while True:
        # print dialog.print_control_identifiers()
        if dialog.child_window(title=module, control_type="ListItem").exists(timeout=0.5) is False:
                if counter == 0:
                    dialog.List.wheel_mouse_input(wheel_dist=60)
                dialog.List.wheel_mouse_input(wheel_dist=-(20+counter*20))

                counter += 1
                if counter == 2:
                    dialog.MenuItem9.click_input()
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


# Return all children windows and visible objects
def find_visible_buttons(dialog, window_name):
    button_list = filter(None, re.findall(r"'(.*?)'", str(dialog.window(title=window_name).descendants()), re.DOTALL))
    print button_list
    #
    # for button in button_list:
    #     dialog.child_window(title=button, found_index=0).click_input()
    return