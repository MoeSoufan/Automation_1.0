

        ### Created by: Moe Soufan
        ### Creation date: September 14


from pywinauto import application, findbestmatch, findwindows, Desktop
from collections import OrderedDict
import time, re


# Click on Short 3D toolbar buttons
def clickall_toolbar_buttons(dialog):

    button_dict = OrderedDict([("SAX LV Endocardial Contour", "SplitButton"),
                               ("SAX LV Epicardial Contour", "SplitButton"),
                               ("SAX Papillary Muscle Contour", "SplitButton"),
                               ("SAX Reference Point", "SplitButton"),
                               ("SAX Left Atrium Contour", "Button"),
                               ("LAX LV Extent", "Button"),
                               ("Line Contour", "SplitButton"),
                               ("Leave Draw Mode", "Button"),
                               ("SAX RV Endocardial Contour", "SplitButton"),
                               ("SAX RV Papillary muscle Contour", "SplitButton"),
                               ("SAX Right Atrium Contour", "Button"),
                               ("LAX RV Extent", "Button"),
                               ("Enable Freehand Drawing", "CheckBox"),
                               ("Enable Click-Drawing", "CheckBox"),
                               ("Enable Contour Dragging", "CheckBox"),
                               ("Enable Contour Nudging", "CheckBox"),
                               ("Enable Threshold Segmentation", "CheckBox"),
                               ("Segment Endo", "Button"),
                               ("Segment Epi", "Button"),
                               ("Segment RV Endo", "Button"),
                               ("Detect Endo/Epi Contours Current Phase", "SplitButton"),
                               ("Detect RV Contours Current Phase", "SplitButton"),
                               ("Forward LAX Contour", "Button"),
                               ("Detect LV/RV Contours at ED/ES Phases", "SplitButton"),
                               ("Detect LV Endo/Epi Contours Current Phase", "SplitButton"),
                               ("Detect RV Contours Current Phase", "SplitButton"),
                               ("Show Cross Reference", "CheckBox"),
                               ("Display Polar Map", "CheckBox"),
                               ("View LV/RV Volume Curve", "CheckBox"),
                               ("Mitral/Tricuspid Valve Plane Correction on/off", "CheckBox")])

    for button_title, control_type in button_dict.items():
        if dialog.child_window(title=button_title, control_type=control_type).exists() is True:
            try:
                # print button_title, control_type
                # dialog.child_window(
                #     title=button_title, control_type=control_type).press_mouse_input(absolute=False)
                dialog.child_window(title=button_title, control_type=control_type).click_input()

            except findbestmatch.MatchError:
                pass #for now

            except findwindows.ElementNotFoundError:
                pass #for now

            except findwindows.ElementAmbiguousError:
                # dialog.child_window(
                #     title=button_title, control_type=control_type, found_index=0).press_mouse_input(absolute=False)
                dialog.child_window(title=button_title, control_type=control_type, found_index=0).click_input()

        else:
            print "'%s' Button is not turned on" % button_title


def click_ml_button(dialog, ml_button):

    machine_learning_buttons = {"Detect Endo/Epi Contours Current Phase": 1,
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
        for filtered_button in [k for k, v in machine_learning_buttons.items()
                                if v == machine_learning_buttons[ml_button]]:
            if dialog.child_window(title=filtered_button).exists() is True:
                dialog.child_window(title=filtered_button).right_click_input()
                Desktop(backend="uia").Menu.child_window(title=ml_button, control_type="MenuItem").click_input()

                start = time.time()
                dialog.child_window(title=ml_button).click_input()
                dialog.progressbar.exists()
                end = time.time()

                print "Time to complete ML action: ", end - start

    else:
        start = time.time()
        dialog.child_window(title=ml_button).click_input()
        dialog.progressbar.exists()
        end = time.time()

        print "Time to complete ML action: ", end - start

    return


def sax_main_viewer(dialog, study, series):

    command = "dialog.child_window(title=study, control_type='Window', found_index=0)" \
              ".SplitButton.Custom%s.double_click_input()" % (series+4)

    ###### CONSIDER WRITING METHOD
    if dialog.child_window(control_type="Window", found_index=0).exists() is True and \
            dialog.child_window(title="OK Enter", control_type="Button").exists() is True:
        dialog.child_window(title="OK Enter", control_type="Button").click_input()

    # print dialog.print_control_identifiers()
    # eval(command)

    # print dialog.child_window(title=study, found_index=0).print_control_identifiers()
    # while False:
    #     if dialog.child_window(title=series, control_type="Text").exists() is False:
    #         dialog.child_window(title=study).SplitButton.child_window(title="Custom5").click_input()
    # dialog.child_window(title=study).SplitButton.Custom5.click_input()
    # dialog.child_window(title="SA-3D Demo").SplitButton.Custom5.click_input()

    # dialog.child_window(title="SA-3D Demo").SplitButton.Custom6.click_input()
    # dialog.child_window(title="SA-3D Demo").SplitButton.Custom7.click_input()
    # dialog.child_window(title="SA-3D Demo").SplitButton.Custom8.click_input()
    # dialog.child_window(title="SA-3D Demo").SplitButton.Custom9.click_input()
    # dialog.child_window(title="SA-3D Demo").SplitButton.Custom10.click_input()
    # child_window(title="6.  TRUFI 4 CHAMBER s3p1", control_type="Text")
    return
