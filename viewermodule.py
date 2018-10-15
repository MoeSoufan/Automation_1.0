
from pywinauto import findwindows, findbestmatch


def load_series(dialog, study, window_name, series=1):
    viewer_frames = {"Viewer1": "Custom10",
                     "Viewer2": "Custom14",
                     "Viewer3": "Custom18",
                     "Viewer4": "Custom20"}

    for window in [k for k, v in viewer_frames.items()
                   if v == viewer_frames[window_name]]:
        # print viewer_frames[window]
        command = "dialog.child_window(title=study, control_type='Window', found_index=0).SplitButton.Custom%s.\
               drag_mouse_input(dst=dialog.Custom2.%s.rectangle())" % (series + 4, viewer_frames[window])

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
