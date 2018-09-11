from pywinauto import application
import time


def load(dialog):

    dialog.Edit.click_input()
    dialog.Edit.double_click_input()
    dialog.Edit.set_text('Function-Flow-Perf')
    dialog.FunctionFlowPerf.double_click_input()

    start = time.time()
    dialog.LoadingStudyDone.wait('visible',1000)
    end = time.time()

    print "Loading Study Time: %.2f" % (end - start)

    # while True:
    #     try:
    #         loginDialog.Short3D.click()
    #         break
    #     except:

    return
