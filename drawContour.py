
from pywinauto import findwindows, findbestmatch
import re, time
from random import randint


def get_rect(dialog, window):

    window_name = "dialog.%s.rectangle()" % window
    window_rect = str(eval(window_name))
    # print window_rect

    [left, top, right, bottom] = map(int, re.sub("[^0-9\,]", "", window_rect).split(','))

    return left, top, right, bottom


def line_contour(dialog, window, number=1):
    if dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Line Contour").exists() is True:
        dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Line Contour").click_input()
    else:
        print "Line Contour not available"
        return

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


def line_contour_splitbutton(dialog, window, number=1):
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


def curved_measurement_contour(dialog, window, number=5):
    if dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Curved Length Measurement").exists() is True:
        dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Curved Length Measurement").click_input()

    else:
        print "Curved Measurement Contour not available."
        return

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


def curved_measurement_contour_splitbutton(dialog, window, number=5):
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


def freehand_counter(dialog, window):
    if dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Freehand Contour").exists() is True:
        dialog.child_window(title="Toolbar", control_type="ToolBar").child_window(
            title="Freehand Contour").click_input()

    else:
        print "Freehand Contour not available"
        return

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


def freehand_counter_splitbutton(dialog, window):
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


def draw_epi_endo(dialog, window):
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


def draw_lv_extent(dialog, window):
    left, top, right, bottom = get_rect(dialog, window)

    counter = 0
    while counter < 3:
        dialog.click_input(
            coords=(randint((left + 50), (right - 150)), randint((top + 50), (bottom - 50))), absolute=True)
        counter += 1

    return
