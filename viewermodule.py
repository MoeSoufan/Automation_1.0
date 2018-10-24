
from pywinauto import findwindows, findbestmatch
import supportingFunctions
import studyFunctions
import drawContour


def load_series(dialog, study, window_name, series=1):

    window = supportingFunctions.find_window_func(window_name)

    command = "dialog.child_window(title=study, control_type='Window', found_index=0).SplitButton.Custom%s.\
           drag_mouse_input(dst=dialog.Custom2.%s.rectangle())" % (series + 4, window)

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

    return


def add_measurement_capture(dialog):

    dialog.Button4.click_input()

    if dialog.child_window(title="Choose Capture(s)", control_type="Window").child_window(
            title=" Down", control_type="ComboBox").child_window(
            title="Report", control_type="ListItem").exists() is False:

        dialog.child_window(title="Choose Capture(s)", control_type="Window").child_window(
            title=" Down", control_type="ComboBox").click_input()

        dialog.child_window(title="Choose Capture(s)", control_type="Window").child_window(
            title=" Down", control_type="ComboBox").child_window(
            title="Report", control_type="ListItem").click_input()

    dialog.child_window(title="Choose Capture(s)", control_type="Window").SelectAllEnterButton.click_input()

    dialog.child_window(title="Choose Capture(s)", control_type="Window").child_window(
        title="OK", control_type="Button").click_input()

    return


def viewer_module_full_workflow(dialog, pid, study, window, series):

    studyFunctions.click_module(dialog, "Viewer", pid)

    load_series(dialog, study, window, series)

    drawContour.freehand_counter(dialog, window)
    drawContour.line_contour(dialog, window, 3)
    drawContour.curved_measurement_contour(dialog, window, 3)

    return
