
        ### Created by: Moatassem Soufan
        ### Creation Date: September 7, 2018

from pywinauto import application, findbestmatch, findwindows
import time


def load(dialog):

    study_name = 'SA-3D Demo'

    while True:
        if dialog.Edit.exists() is True and dialog.Toolbar.child_window(title="Patient List").exists() is False:
            try:
                # print dialog.Edit.print_identifiers()
                dialog.Edit.click_input()
                dialog.Edit.set_text(study_name)
                dialog.window(title=study_name).double_click_input()

                start = time.time()
                dialog.LoadingStudyDone.wait('visible', 1000)
                end = time.time()
                print "Loading Study Time: %.2f" % (end - start)
                break

            except findwindows.ElementNotFoundError:
                try:
                    dialog.Toolbar.child_window(title="Patient List").click_input()
                except findwindows.ElementNotFoundError:
                    print "Study '%s' doesn't exist in database" % study_name
                    exit()

        elif dialog.Toolbar.child_window(title="Patient List").exists(timeout=1) is True:
            dialog.Toolbar.child_window(title="Patient List").click_input()

        else:
            print "Can't find anything"

    return
