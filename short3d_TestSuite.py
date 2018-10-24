import supportingFunctions
import drawContour
import short3d
import outputFile
import time

window = "SAX3DCUSTOM"


def assign_order(order):
    def do_assignment(to_func):
        to_func.order = order
        return to_func
    return do_assignment


@assign_order(1)
def test1003_sax_endo_contour_short3d(dialog):

    short3d.click_splitbutton(dialog, "SAX LV Endocardial Contour")
    drawContour.draw_epi_endo(dialog, window)

    return


@assign_order(2)
def test1004_sax_endo_open_contour_short3d(dialog):

    short3d.click_splitbutton(dialog, "SAX LV Open Endocardial Contour")
    drawContour.draw_epi_endo(dialog, window)

    return


@assign_order(3)
def test1005_sax_epi_contour_short3d(dialog):

    short3d.click_splitbutton(dialog, "SAX LV Epicardial Contour")
    drawContour.draw_epi_endo(dialog, window)

    return


@assign_order(4)
def test1006_sax_epi_open_contour_short3d(dialog):

    short3d.click_splitbutton(dialog, "SAX LV Open Epicardial Contour")
    drawContour.draw_epi_endo(dialog, window)

    return


@assign_order(5)
def test1007_lax_lv_extent_short3d(dialog):

    short3d.click_button(dialog, "LAX LV Extent")
    drawContour.draw_lv_extent(dialog, "Custom18")

    return


@assign_order(6)
def test1008_draw_line_contour(dialog):

    short3d.click_splitbutton(dialog, "Line Contour")
    drawContour.line_contour_splitbutton(dialog, window)

    return


@assign_order(7)
def test1009_draw_curved_len_measurement_contour(dialog):

    short3d.click_splitbutton(dialog, "Curved Length Measurement")
    drawContour.curved_measurement_contour_splitbutton(dialog, window)

    return


@assign_order(8)
def test1010_draw_freehand_contour(dialog):

    short3d.click_splitbutton(dialog, "Freehand Contour")
    drawContour.freehand_counter_splitbutton(dialog, window)

    return


@assign_order(9)
def test1011_sax_rv_endocardial_contour(dialog):

    short3d.click_splitbutton(dialog, "SAX RV Endocardial Contour")
    drawContour.draw_epi_endo(dialog, window)

    return


@assign_order(10)
def test1012_sax_rv_epicardial_contour(dialog):

    short3d.click_splitbutton(dialog, "SAX RV Epicardial Contour")
    drawContour.draw_epi_endo(dialog, window)

    return


@assign_order(11)
def test1013_sax_segment_endo(dialog):

    short3d.click_button(dialog, "Segment Endo")
    dialog.child_window(title="Segment Endo").press_mouse_input(absolute=False)
    dialog.child_window(title="Segment Endo").release_mouse_input()

    return


@assign_order(12)
def test1014_sax_segment_epi(dialog):

    short3d.click_button(dialog, "Segment Epi")
    dialog.child_window(title="Segment Epi").press_mouse_input(absolute=False)
    dialog.child_window(title="Segment Epi").release_mouse_input()

    return


@assign_order(13)
def test1015_sax_segment_rv_endo(dialog):

    short3d.click_button(dialog, "Segment RV Endo")
    dialog.child_window(title="Segment RV Endo").press_mouse_input(absolute=False)
    dialog.child_window(title="Segment RV Endo").release_mouse_input()

    return


@assign_order(14)
def test1016_ml_lvrv_edes(dialog, app):

    duration = short3d.click_ml(dialog, "Detect LV/RV Contours at ED/ES Phases", app)

    return duration


@assign_order(15)
def test1017_ml_lvrv_current_phase(dialog, app):

    duration = short3d.click_ml(dialog, "Detect LV/RV Contours Current Phase", app)

    return duration


@assign_order(16)
def test1018_ml_lvrv_entire_stack(dialog, app):

    duration = short3d.click_ml(dialog, "Detect LV/RV Contours Entire Stack", app)

    return duration


@assign_order(17)
def test1019_ml_lvrv_current_slice(dialog, app):

    duration = short3d.click_ml(dialog, "Detect LV/RV Contours Current Slice", app)

    return duration


@assign_order(18)
def test1020_ml_lvrv_current_image(dialog, app):

    duration = short3d.click_ml(dialog, "Detect LV/RV Contours Current Image", app)

    return duration


@assign_order(19)
def test1021_ml_lv_endo_epi_current_phase(dialog, app):

    duration = short3d.click_ml(dialog, "Detect LV Endo/Epi Contours Current Phase", app)

    return duration


@assign_order(20)
def test1022_ml_lv_endo_current_phase(dialog, app):

    duration = short3d.click_ml(dialog, "Detect LV Endo Contours Current Phase", app)

    return duration


@assign_order(21)
def test1023_ml_lv_endo_epi_entire_stack(dialog, app):

    duration = short3d.click_ml(dialog, "Detect LV Endo/Epi Contours Entire Stack", app)

    return duration


@assign_order(22)
def test1024_ml_lv_endo_entire_stack(dialog, app):

    duration = short3d.click_ml(dialog, "Detect LV Endo Contours Entire Stack", app)

    return duration


@assign_order(23)
def test1025_ml_rv_contour_current_phase(dialog, app):

    duration = short3d.click_ml(dialog, "Detect RV Contours Current Phase", app)

    return duration


@assign_order(24)
def test1026_ml_rv_contour_entire_stack(dialog, app):

    duration = short3d.click_ml(dialog, "Detect RV Contours Entire Stack", app)

    return duration


@assign_order(25)
def test1027_show_cross_reference(dialog):

    short3d.click_button(dialog, "Show Cross Reference")

    return


@assign_order(26)
def test1028_display_polar_map(dialog):

    short3d.click_button(dialog, "Display Polar Map")

    return


@assign_order(27)
def test1029_check_aha_segments(dialog):

    if dialog.child_window(title="AHA Segments", control_type="CheckBox").exists() is True:
        dialog.child_window(title="AHA Segments", control_type="CheckBox").click_input()

    else:
        try:
            short3d.click_button(dialog, "Display Polar Map")

        except Exception as d:
            raise d
    return


@assign_order(28)
def test1030_check_coronary_territories(dialog):

    if dialog.child_window(title="Coronary Territories", control_type="CheckBox").exists() is True:
        dialog.child_window(title="Coronary Territories", control_type="CheckBox").click_input()

    else:
        try:
            short3d.click_button(dialog, "Display Polar Map")

        except Exception as d:
            raise d
    return


# @assign_order(29)
# def test1031_check_wall_thickness(dialog):
#
#     if dialog.child_window(title="Wall Thickness", control_type="ListItem").exists() is True:
#         dialog.child_window(title="Wall Thickness", control_type="ListItem").click_input()
#
#     else:
#         try:
#             short3d.click_button(dialog, "Display Polar Map")
#
#         except Exception as d:
#             raise d
#     return
#
#
# @assign_order(30)
# def test1032_check_wall_thickening_motion(dialog):
#
#     if dialog.child_window(title="Wall Thickening/Motion", control_type="ListItem").exists() is True:
#         dialog.child_window(title="Wall Thickening/Motion", control_type="ListItem").click_input()
#
#     else:
#         try:
#             short3d.click_button(dialog, "Display Polar Map")
#
#         except Exception as d:
#             raise d
#         return


@assign_order(31)
def test1033_view_lv_rv_volume_curve(dialog):

    short3d.click_button(dialog, "View LV/RV Volume Curve")

    return
