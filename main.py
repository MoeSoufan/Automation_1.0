
        ### Created By Moe Soufan
        ### Creation Date: September 7, 2018

        # Main? function for automation efforts
        # Using pywinauto to detect UI elements on cvi42.exe
        # Inspect.exe used to identify elements

# from pywinauto import application
# from pywinauto import findbestmatch
# import subprocess
# import time
# import admin_test
# import pywinauto

import loadTest
import initialization

# print pywinauto.__version__

# Launch cvi42 if not already running, grab process id. Login method called from within.
pid, mainDialog = initialization.initialize_session()
print "Connected to cvi42.exe ProcessID #%s" % pid

# Load test trial
loadTest.load(mainDialog)

exit()

#
# LoadTest.load(mainDialog)

# print loginDialog.print_control_identifiers()

# loginDialog.Edit.click_input()
# loginDialog.Edit.double_click_input()
# loginDialog.Edit.set_text('Function-Flow-Perf')
#
# loginDialog.FunctionFlowPerf.double_click_input()
#
# start = time.time()
# loginDialog.LoadingStudyDone.wait('visible',1000)
# end = time.time()
#
# print "Loading Study Time: %.2f" % (end - start)
#


# app = application.Application(backend="uia").connect(path=r"D:\Moe-Testing\2018-08-15_MontrealReleaseCandidate2\cvi42_5.9.2_(1111)_win_x64\cvi42.exe")
#
# mainDialog = app.CircleCardiovascularImaging
# mainDialog.print_control_identifiers()
# #
# mainDialog.NegHRCTAnonymized.static.click_input()
# print mainDialog.NegHRCTAnonymized.static.texts()[0]

#print_control_identifiers()


# mainDialog.MenuItem9.print_control_identifiers()
# mainDialog.MenuItem9.click_input()
# test = app.MenuItem9
# test.Short3D.click_input()
#("Add Protocol Step->Short 3D")
# mainDialog.MenuItem9.#.click_input()



# counter = 0
# final_counter = 0
#
# while True:
#     try:
#         # mainDialog.Short3DList.double_click_input()
#         mainDialog.Desktop1.click_input()
#         counter += 1
#
#         if final_counter == 1:
#             break
#
#     except findbestmatch.MatchError as ME:
#         mainDialog.List.wheel_mouse_input(wheel_dist=20)
#         mainDialog.List.wheel_mouse_input(wheel_dist=-25)
#
#         if counter <= 2:
#             mainDialog.AddProtocolStep.click_input()
#             mainDialog.Short3DMenu.click_input()
#             final_counter = 1
