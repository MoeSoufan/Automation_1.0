

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

    while True:
        if dialog.child_window(title=ml_button).exists() is True:
            dialog.child_window(title=ml_button).click_input()
        else:
            for filtered_button in [k for k, v in machine_learning_buttons.items()
                                    if v == machine_learning_buttons[ml_button]]:
                if dialog.child_window(title=filtered_button).exists() is True:
                    dialog.child_window(title=filtered_button).right_click_input()
                    Desktop(backend="uia").Menu.child_window(title=ml_button, control_type="MenuItem").click_input()
                    dialog.child_window(title=ml_button).click_input()

                    start = time.time()
                    dialog.window(title="cvi42").wait_not('visible', 1000)
                    end = time.time()

                    print "Time to complete ML action: ", end-start
                    break

    #     for item in machine_learning_buttons[ml_button]:
    #

    # if trial_button in machine_learning_buttons.keys():
    #     print "yes: ", machine_learning_buttons.get(trial_button)

    # if dialog.child_window(title=trial_button, control_type="SplitButton").exists() is False:
    #     pass
    #
    #
    # dialog.child_window(title="Detect Endo/Epi Contours Current Phase", control_type="SplitButton").right_click_input()
    # Desktop(backend="uia").Menu.print_control_identifiers()



    # dialog.child_window(title="Detect LV/RV Contours at ED/ES Phases", control_type="SplitButton").right_click_input()
    # Desktop(backend="uia").Menu.child_window(title="Detect LV/RV Contours Entire Stack",
    #                                                control_type="MenuItem").click_input()
    # dialog.child_window(title="Detect LV/RV Contours Entire Stack", control_type="SplitButton").click_input()
    # start = time.time()
    # dialog.child_window(title="cvi42").wait_not("visible", 1000)
    # end = time.time()
    #
    # print "Endo/Epi Stack completion time: %s" % (end-start)


# def sax_main_viewer(dialog):
#     print dialog.print_control_identifiers()
#     # print dialog.child_window(title="SA-3D Demo", control_type="Window").print_control_identifiers()
#     # print dialog.child_window(title="SAX3D Stack", control_type="Text").print_control_identifiers()
#     dialog.SAX3DStackCustom.click_input()
#     dialog.Custom29.click_input()
#     dialog.Custom30.click_input()
#     dialog.Slider.click_input()
#     dialog.Thumb.click_input()
#     dialog.Thumb2.click_input()
#     dialog.Thumb3.click_input()
#     return
