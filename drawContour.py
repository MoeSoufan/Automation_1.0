import re, time
import supportingFunctions
from random import randint


def get_rect(dialog, window, viewer=False):

    window_name = "dialog.%s.rectangle()" % window

    if viewer is True:
        window_name = "dialog.Custom2.%s.rectangle()" % window

    window_rect = str(eval(window_name))
    [left, top, right, bottom] = map(int, re.sub("[^0-9\,]", "", window_rect).split(','))

    return left, top, right, bottom


def get_rect_circular(dialog, window):

    window_name = "dialog.%s.rectangle()" % window
    window_rect = eval(window_name)

    x, y = window_rect.mid_point()

    return x, y


def line_contour(dialog, window_name, number=1):

    viewer = False
    if "Viewer" in window_name:
        viewer = True

    window = supportingFunctions.find_window_func(window_name)

    if dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Line Contour").exists() is True:
        dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Line Contour").click_input()
    else:
        print "Line Contour not available"
        return

    if viewer is True:
        left, top, right, bottom = get_rect(dialog, window, True)

    else:
        left, top, right, bottom = get_rect(dialog, window)

    counter = 0
    while counter < number:
        dialog.press_mouse_input(
            coords=(randint((left+50), (right-150)), randint((top+50), (bottom-50))), absolute=True)
        dialog.click_input(
            coords=(randint((left+50), (right-150)), randint((top+50), (bottom-50))), absolute=True)
        counter += 1

    dialog.type_keys('{VK_ESCAPE}')
    # dialog.type_keys('^{BACKSPACE}')

    return


def line_contour_splitbutton(dialog, window_name, number=1):

    viewer = False
    if "Viewer" in window_name:
        viewer = True

    window = supportingFunctions.find_window_func(window_name)

    if viewer is True:
        left, top, right, bottom = get_rect(dialog, window, True)

    else:
        left, top, right, bottom = get_rect(dialog, window)

    counter = 0
    while counter < number:
        dialog.press_mouse_input(
            coords=(randint((left+50), (right-150)), randint((top+50), (bottom-50))), absolute=True)
        dialog.click_input(
            coords=(randint((left+50), (right-150)), randint((top+50), (bottom-50))), absolute=True)
        counter += 1

    dialog.type_keys('{VK_ESCAPE}')
    # dialog.type_keys('^{BACKSPACE}')

    return


def curved_measurement_contour(dialog, window_name, number=5):

    viewer = False
    if "Viewer" in window_name:
        viewer = True

    window = supportingFunctions.find_window_func(window_name)

    if dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Curved Length Measurement").exists() is True:
        dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Curved Length Measurement").click_input()

    else:
        print "Curved Measurement Contour not available."
        return

    if viewer is True:
        left, top, right, bottom = get_rect(dialog, window, True)

    else:
        left, top, right, bottom = get_rect(dialog, window)

    counter = 0
    while counter < number-1:
        dialog.click_input(
            coords=(randint((left+50), (right-150)), randint((top+50), (bottom-50))), absolute=True)
        counter += 1

    dialog.click_input(
        coords=(randint((left + 50), (right - 150)), randint((top+50), (bottom-50))), absolute=True, double=True)

    dialog.type_keys('{VK_ESCAPE}')
    return


def curved_measurement_contour_splitbutton(dialog, window_name, number=5):

    window = supportingFunctions.find_window_func(window_name)
    left, top, right, bottom = get_rect(dialog, window)

    counter = 0
    while counter < number-1:
        dialog.click_input(
            coords=(randint((left+50), (right-150)), randint((top+50), (bottom-50))), absolute=True)
        counter += 1

    dialog.click_input(
        coords=(randint((left + 50), (right - 150)), randint((top+50), (bottom-50))), absolute=True, double=True)

    dialog.type_keys('{VK_ESCAPE}')
    return


def freehand_counter(dialog, window_name):

    viewer = False
    if "Viewer" in window_name:
        viewer = True

    window = supportingFunctions.find_window_func(window_name)

    if dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Freehand Contour").exists() is True:
        dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Freehand Contour").click_input()

    else:
        print "Freehand Contour not available"
        return

    if viewer is True:
        left, top, right, bottom = get_rect(dialog, window, True)

    else:
        left, top, right, bottom = get_rect(dialog, window)

    dialog.press_mouse_input(
        coords=(randint((left + 50), (right - 150)), randint((top + 50), (bottom - 50))), absolute=True)

    counter = 0
    while counter < 4:
        dialog.move_mouse_input(
            coords=(randint((left + 50), (right - 150)), randint((top + 50), (bottom - 50))), absolute=True)
        counter += 1

    dialog.release_mouse_input(
        coords=(randint((left + 50), (right - 150)), randint((top + 50), (bottom - 50))), absolute=True)

    dialog.type_keys('{VK_ESCAPE}')
    return


def freehand_counter_splitbutton(dialog, window_name):

    window = supportingFunctions.find_window_func(window_name)
    left, top, right, bottom = get_rect(dialog, window)

    dialog.press_mouse_input(
        coords=(randint((left + 50), (right - 150)), randint((top + 50), (bottom - 50))), absolute=True)

    counter = 0
    while counter < 4:
        dialog.move_mouse_input(
            coords=(randint((left + 50), (right - 150)), randint((top + 50), (bottom - 50))), absolute=True)
        counter += 1

    dialog.release_mouse_input(
        coords=(randint((left + 50), (right - 150)), randint((top + 50), (bottom - 50))), absolute=True)

    dialog.type_keys('{VK_ESCAPE}')
    return


def clear_all(dialog):

    dialog.type_keys('^{BACKSPACE}')

    return


def draw_epi_endo(dialog, window_name):

    window = supportingFunctions.find_window_func(window_name)
    left, top, right, bottom = get_rect(dialog, window)

    dialog.press_mouse_input(
        coords=(randint((left + 50), (right - 150)), randint((top + 50), (bottom - 50))), absolute=True)

    counter = 0
    while counter < 4:
        dialog.move_mouse_input(
            coords=(randint((left + 50), (right - 150)), randint((top + 50), (bottom - 50))), absolute=True)
        counter += 1

    dialog.release_mouse_input(
        coords=(randint((left + 50), (right - 150)), randint((top + 50), (bottom - 50))), absolute=True)

    dialog.type_keys('{VK_ESCAPE}')
    return


def flow_contour(dialog, window_name):

    window = supportingFunctions.find_window_func(window_name)
    x, y = get_rect_circular(dialog, window)

    dialog.press_mouse_input(coords=((x + 30), (y + 30)))
    dialog.move_mouse_input(coords=((x + 20), (y - 20)))
    dialog.move_mouse_input(coords=((x - 20), (y - 20)))
    dialog.release_mouse_input(coords=((x - 10), (y - 10)))


def draw_lv_extent(dialog, window_name):

    window = supportingFunctions.find_window_func(window_name)

    left, top, right, bottom = get_rect(dialog, window)
    # print left, top, right, bottom
    counter = 0
    while counter < 3:
        dialog.click_input(
            coords=(randint((left + 50), (right - 70)), randint((top + 50), (bottom - 50))), absolute=True)
        counter += 1

    return
