
        ### Created By Moe Soufan
        ### Creation Date: September 7, 2018

        # Main? function for automation efforts
        # Using pywinauto to detect UI elements on cvi42.exe
        # Inspect.exe used to identify elements

import time
from pywinauto import controls


def login_to_cvi42(app, dialog, status):

    while True:
        if app.LoginFailure.exists(timeout=2) is True:
            # print app.LoginFailure.exists()
            # dialog.print_control_identifiers()
            print app.LoginFailure.OKEnterButton
            app.LoginFailure.OKEnterButton.click()
            exit()
        # dialog.print_control_identifiers()
        dialog.ServerDown.click_input()
        dialog.ZombieAdmin.click_input()
        dialog.child_window(title="User ID Alt+I", control_type="Edit").set_text('moeadmin')
        dialog.child_window(title="Password Alt+P", control_type="Edit").set_text('moeadmin')
        dialog.child_window(title="Login Enter").invoke()
        start = time.time()

        # print app.LoginFailure.exists()
        if app.LoginFailure.exists(timeout=1.5) is True:
            # print app.LoginFailure.exists()
            # dialog.print_control_identifiers()
            print app.LoginFailure.OKEnterButton
            app.LoginFailure.OKEnterButton.click()

        else:
            break

    if status == 1:
        dialog.LoadImagePreviewsDone.wait('visible', 1000) or dialog.SaveWorkspaceDone.wait('visible', 1000)
        end = time.time()
        print "Login Time: %.2f" % (end - start)

    return

