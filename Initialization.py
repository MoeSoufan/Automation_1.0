import subprocess, re
from pywinauto import application

import Login


def initialize_session():

    a = subprocess.check_output('tasklist')
    instances = 0
    flag = False

    for string in a.split():
        if flag is True:
            process_id = string
            # print "PID of cvi42.exe:", process_id
            # print type(process_id)
            app = application.Application(backend="uia").connect(process=int(process_id))

            app2 = application.Application(backend="uia").connect(path="explorer")
            sys_tray = app2.window(class_name="Shell_TrayWnd")
            sys_tray.child_window(title="cvi42 - Shortcut - 1 running window").click()

            # Change Application identifier if cvi42.exe window changes names
            dialog = app.CircleCardiovascularImaging
            # dialog.maximize()
            # print dialog.texts()[0]


            # Login.login_to_cvi42(dialog)

            # test = re.find('Client Login', dialog.texts()[0])
            # dialog.print_control_identifiers()
            # dialog.set_focus()
            # Login.login_to_cvi42(dialog)

            # try:
            #     dialog.ServerDown.wait_not('visible', timeout=2)
            #     # Login to cvi42
            #     Login.login_to_cvi42(dialog)
            # except timings.TimeoutError:
            #     pass
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

    return process_id, dialog

