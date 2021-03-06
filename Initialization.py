
        ### Created By Moe Soufan
        ### Creation Date: September 12, 2018

        # Initializes the program, login or connect to existing process


import os
from pywinauto import application, findbestmatch

import login
import supportingFunctions


def initialize_session(filename):

    process_id = [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if "cvi42.exe" in item.split()]
    # print process_id

    if len(process_id) >= 1:
        app = application.Application(backend="uia").connect(process=int(process_id[0]))
        dialog = app.CircleCardiovascularImaging

        # If cvi42 window is minimized
        try:
            dialog.set_focus()
            pass

        except findbestmatch.MatchError:
            supportingFunctions.if_cvi42_minimized()

        if "Client Login" in str(dialog.texts()) or dialog.window(
                title="Circle Cardiovascular Imaging - Client Login").exists() is True:
            # print dialog.print_control_identifiers()
            # print dialog.window(title="Circle Cardiovascular Imaging - Client Login").exists()
            print "Login Required"

            if dialog.child_window(title="Circle Cardiovascular Imaging - Client Login").exists() is True:
                login.test1000_login_to_cvi42(app, dialog, 2, filename)
            else:
                login.test1000_login_to_cvi42(app, dialog, 1, filename)
        else:
            # dialog.print_control_identifiers()
            print "This is the main window, user: %s" % str(dialog.texts()[0]).split('-')[1]
            # dialog.maximize()

    elif len(process_id) == 0:
        # Streamline this call to support different machines
        app = application.Application(backend="uia").start(
            r"D:\Moe-Testing\2018-08-15_MontrealReleaseCandidate2\cvi42_5.9.3_(1130)_win_x64\cvi42.exe")
        dialog = app.CirclecardiovascularImaging
        dialog.set_focus()
        process_id = [app.dialog.process_id()]
        login.test1000_login_to_cvi42(app, dialog, 1, filename)

    return int(process_id[0]), dialog, app

