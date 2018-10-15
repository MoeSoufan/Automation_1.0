

        ### Created by: Moe Soufan
        ### Creation date: September 14


from pywinauto import Desktop
import time


# Click on Short 3D toolbar buttons
def click_button(dialog, button):

    # button_dict = OrderedDict([("SAX Left Atrium Contour", "Button"),
    #                            ("LAX LV Extent", "Button"),
    #                            ("Leave Draw Mode", "Button"),
    #                            ("SAX Right Atrium Contour", "Button"),
    #                            ("LAX RV Extent", "Button"),
    #                            ("Enable Freehand Drawing", "CheckBox"),
    #                            ("Enable Click-Drawing", "CheckBox"),
    #                            ("Enable Contour Dragging", "CheckBox"),
    #                            ("Enable Contour Nudging", "CheckBox"),
    #                            ("Enable Threshold Segmentation", "CheckBox"),
    #                            ("Segment Endo", "Button"),
    #                            ("Segment Epi", "Button"),
    #                            ("Segment RV Endo", "Button"),
    #                            ("Forward LAX Contour", "Button"),
    #                            ("Show Cross Reference", "CheckBox"),
    #                            ("Display Polar Map", "CheckBox"),
    #                            ("View LV/RV Volume Curve", "CheckBox"),
    #                            ("Mitral/Tricuspid Valve Plane Correction on/off", "CheckBox")])

    if dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(title=button).exists() is True:
        dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title=button, found_index=0).click_input()

    return


def click_ml(dialog, ml_button, app):

    machine_butto = {"Detect Endo/Epi Contours Current Phase": 1,
                     "Detect Endo/Epi Contours Current Slice": 1,
                     "Detect Endo/Epi Contours Entire Stack": 1,
                     "Detect Endo/Epi Contours Current Image": 1,
                     "Detect Endo Contours Current Phase": 1,
                     "Detect Endo Contours Current Slice": 1,
                     "Detect Endo Contours Entire Stack": 1,
                     "Detect Epi Contours Current Phase": 1,
                     "Detect Epi Contours Current Slice": 1,
                     "Detect Epi Contours Entire Stack": 1,
                     "Detect RV Contours Current Phase": 2,
                     "Detect RV Contours Current Slice": 2,
                     "Detect RV Contours Entire Stack": 2,
                     "Detect LV/RV Contours at ED/ES Phases": 3,
                     "Detect LV/RV Contours Current Phase": 3,
                     "Detect LV/RV Contours Entire Stack": 3,
                     "Detect LV/RV Contours Current Slice": 3,
                     "Detect LV/RV Contours Current Image": 3,
                     "Detect LV Endo/Epi Contours Current Phase": 4,
                     "Detect LV Endo Contours Current Phase": 4,
                     "Detect LV Endo/Epi Contours Entire Stack": 4,
                     "Detect LV Endo Contours Entire Stack": 4,
                     "Detect RV Contours Current Phase": 5,
                     "Detect RV Contours Entire Stack": 5}

    if dialog.child_window(title=ml_button).exists() is False:
        for filtered_button in [k for k, v in machine_butto.items()
                                if v == machine_butto[ml_button]]:
            # print filtered_button
            if dialog.child_window(title=filtered_button, found_index=0).exists() is True:
                dialog.child_window(title=filtered_button, found_index=0).right_click_input()
                Desktop(backend="uia").Menu.child_window(title=ml_button, control_type="MenuItem",
                                                         found_index=0).click_input()

                start = time.time()
                dialog.child_window(title=ml_button).click_input()
                app.wait_cpu_usage_lower(threshold=5, timeout=1000)
                end = time.time()

                print "Time to complete %s ML action: %.2f" % (ml_button, end-start)
                return end-start

    else:
        start = time.time()
        dialog.child_window(title=ml_button).click_input()
        app.wait_cpu_usage_lower(threshold=5, timeout=1000)
        end = time.time()

        print "Time to complete %s ML action: %.2f" % (ml_button, end-start)
        return end-start


def click_splitbutton(dialog, button):

    split_buttons = {"SAX LV Endocardial Contour": 6,
                     "SAX LV Open Endocardial Contour": 6,
                     "SAX LV Epicardial Contour": 7,
                     "SAX LV Open Epicardial Contour": 7,
                     "SAX Papillary Muscle Contour": 8,
                     "SAX LV Exclude Area Contour": 8,
                     "SAX Reference Point": 9,
                     "SAX Inferior Reference Point": 9,
                     "Line Contour": 10,
                     "Freehand Contour": 10,
                     "Curved Length Measurement": 10,
                     "SAX RV Endocardial Contour": 11,
                     "SAX RV Epicardial Contour": 11,
                     "SAX RV Papillary muscle Contour": 12,
                     "SAX RV Exclude Area Contour": 12}

    if dialog.child_window(title=button).exists() is False:
        for filtered_button in [k for k, v in split_buttons.items()
                                if v == split_buttons[button]]:
            if dialog.child_window(title=filtered_button).exists() is True:
                dialog.child_window(title=filtered_button).right_click_input()
                Desktop(backend="uia").Menu.child_window(title=button, control_type="MenuItem").click_input()

    else:
        dialog.child_window(title=button).click_input()
        dialog.progressbar.exists()

    return
