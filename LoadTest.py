
        ### Created by: Moatassem Soufan
        ### Creation Date: September 7, 2018

from pywinauto import application, findbestmatch, findwindows
import time


def load(dialog):

    study_name = 'SA-3D Demo'
    is_any_tag = False

    while True:
        if dialog.Edit.exists() is True and dialog.Toolbar.child_window(title="Patient List").exists() is False:
            if dialog.child_window(title=study_name, control_type="Window").exists() is True:
                break

            try:
                # print dialog.Edit.print_identifiers()
                dialog.Edit.click_input()
                dialog.Edit.set_text(study_name)
                start = time.time()
                dialog.window(title=study_name).double_click_input()

                dialog.LoadingStudyDone.wait('visible', 1000)
                end = time.time()
                print "Loading Study Time: %.2f" % (end - start)
                break

            except findwindows.ElementNotFoundError:
                try:
                    dialog.Toolbar.child_window(title="Patient List").click_input()

                except findwindows.ElementNotFoundError:
                    if is_any_tag is True:
                        print "Study '%s' doesn't exist in database" % study_name
                        exit()

                    dialog.child_window(title="Tags", control_type="Custom").\
                        child_window(title="Any", control_type="CheckBox").click_input()
                    is_any_tag = True

        elif dialog.Toolbar.child_window(title="Patient List").exists(timeout=1) is True:
            dialog.Toolbar.child_window(title="Patient List").click_input()

        else:
            print "Can't find anything"
            exit()

    return
