
        ### Created By Moe Soufan
        ### Last Edit: September 7

        # Initializes the program, login or connect to existing process


import subprocess
from pywinauto import application, findbestmatch

import Login


def initialize_session():

    a = subprocess.check_output('tasklist')
    instances = 0
    flag = False

    for string in a.split():
        if flag is True:
            process_id = string
            # print "PID of cvi42.exe:", process_id
            app = application.Application(backend="uia").connect(process=int(process_id))
            dialog = app.CircleCardiovascularImaging
            # dialog.print_control_identifiers()

            # If cvi42 window is minimized
            try:
                dialog.set_focus()
            except findbestmatch.MatchError:
                icon_app = application.Application(backend="uia").connect(path="explorer")
                tray_dialog = icon_app.window(class_name="Shell_TrayWnd")
                tray_dialog.child_window(title="cvi42 - Shortcut - 1 running window").click()

            if "Client Login" in str(dialog.texts()) or dialog.window(
                    title="Circle Cardiovascular Imaging - Client Login").exists() is True:
                # print dialog.window(title="Circle Cardiovascular Imaging - Client Login").exists()
                print "Login Required"
                # dialog.print_control_identifiers
                Login.login_to_cvi42(app, dialog)
            else:
                # dialog.print_control_identifiers()
                print "This is the main window, user: %s" % str(dialog.texts()[0]).split('-')[1]
                # dialog.maximize()
            break

        # If string = 'cvi42.exe', then the next string read from TASKLIST is the process id.
        if string == "cvi42.exe":
            flag = True
            instances += 1

    if instances == 0:
        # Streamline this call to support different machines
        app = application.Application(backend="uia").start(
            r"D:\Moe-Testing\2018-08-15_MontrealReleaseCandidate2\cvi42_5.9.2_(1111)_win_x64\cvi42.exe")
        dialog = app.CirclecardiovascularImaging
        process_id = app.dialog.process_id()
        Login.login_to_cvi42(app, dialog)

    return process_id, dialog

