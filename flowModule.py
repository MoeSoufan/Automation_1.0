import supportingFunctions
import drawContour
import studyFunctions


def systemic_flow_select(dialog):

    dialog.child_window(title="Systemic Flow", control_type="TabItem").click_input()

    return


def pulmonary_flow_select(dialog):

    dialog.child_window(title="Pulmonary Flow", control_type="TabItem").click_input()

    return


def comparison_tab_select(dialog):

    dialog.child_window(title="Comparison", control_type="TabItem").click_input()

    return


def flow_roi_1(dialog, window):

    dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
        title="Flow ROI 1 Contour", control_type="Button").click_input()

    drawContour.flow_contour(dialog, window)
    segment_forward_flow_contour(dialog)

    return


def flow_roi_2(dialog, window):

    dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
        title="Flow ROI 2 Contour", control_type="Button").click_input()

    drawContour.flow_contour(dialog, window)
    segment_forward_flow_contour(dialog)

    return


def flow_roi_3(dialog, window):

    dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
        title="Flow ROI 3 Contour", control_type="Button").click_input()

    drawContour.flow_contour(dialog, window)
    segment_forward_flow_contour(dialog)

    return


def flow_roi_4(dialog, window):

    dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
        title="Flow ROI 4 Contour", control_type="Button").click_input()

    drawContour.flow_contour(dialog, window)
    segment_forward_flow_contour(dialog)

    return


def segment_forward_flow_contour(dialog):

    dialog.child_window(title="Segment Flow Contour", control_type="Button").press_mouse_input(absolute=False)

    counter = 0
    while counter < 50:
        pass
        counter += 1

    dialog.child_window(title="Segment Flow Contour", control_type="Button").release_mouse_input(absolute=False)

    dialog.child_window(title="Forward Flow Contour", control_type="Button").click_input()

    return


def flow_full_workflow(dialog, pid, study_name, flow_type, series):

    studyFunctions.click_module(dialog, "Flow", pid)

    if flow_type == "s":
        systemic_flow_select(dialog)

    elif flow_type == "p":
        pulmonary_flow_select(dialog)

    else:
        print "Wrong flow_type input"
        return

    studyFunctions.load_series(dialog, study_name, "Magnitude", series)
    flow_roi_1(dialog, "Magnitude")

    return
