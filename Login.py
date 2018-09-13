
        ### Created By Moe Soufan
        ### Creation Date: September 7, 2018

        # Main? function for automation efforts
        # Using pywinauto to detect UI elements on cvi42.exe
        # Inspect.exe used to identify elements

import time


def login_to_cvi42(app, dialog, status):

    while True:
        if app.LoginFailure.exists(timeout=1.5) is True:
            # print app.LoginFailure.exists()
            # dialog.print_control_identifiers()
            app.LoginFailure.OKEnterButton.click_input()
            exit()

        # dialog.set_focus()
        dialog.ServerDown.click_input()
        dialog.Zombie.click_input()
        dialog.Edit1.set_text('moe')
        dialog.Edit2.set_text('moe')
        dialog.LoginEnterButton.click_input()
        start = time.time()

        if app.LoginFailure.exists(timeout=1.5) is True:
            # print app.LoginFailure.exists()
            # dialog.print_control_identifiers()
            app.LoginFailure.OKEnterButton.click_input()
        else:
            break

    if status == 1:
        dialog.LoadImagePreviewsDone.wait('visible', 1000) or dialog.SaveWorkspaceDone.wait('visible', 1000)
        end = time.time()
        print "Login Time: %.2f" % (end - start)

    return

