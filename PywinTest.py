
        ### Created By Moe Soufan
        ### Last Edit: September 7

        # Main? function for automation efforts
        # Using pywinauto to detect UI elements on cvi42.exe
        # Inspect.exe used to identify elements

# from pywinauto import application
# from pywinauto import findbestmatch
# import subprocess
# import time
# import admin_test
# import pywinauto

import LoadTest
import Initialization

# print pywinauto.__version__
# admin_test.execute()
# subprocess.call("TASKKILL /IM cvi42.exe")
# subprocess.call("TASKKILL /IM cvi42.exe")

# Launch cvi42 if not already running, grab process id. Login method called from within.
pid, mainDialog = Initialization.initialize_session()
print "ProcessID of cvi42.exe: %s" % pid

# mainDialog.print_control_identifiers()

# # Load test trial
# LoadTest.load(mainDialog)

exit()




#r"D:\Moe-Testing\2018-08-15_MontrealReleaseCandidate2\cvi42_5.9.2_(1111)_win_x64\cvi42.exe"
# app.start().connect(path="cvi42.exe")

# mainDialog = app.CircleCardiovascularImaging

# print loginDialog.print_control_identifiers()

# mainDialog.ServerDown.click_input()
# mainDialog.Zombie.click_input()
# mainDialog.Edit1.set_text('moe')
# mainDialog.Edit2.set_text('moe')
# mainDialog.LoginEnterButton.click_input()
#
# start = time.time()
# mainDialog.LoadImagePreviewsDone.wait('visible', 1000)
# end = time.time()
#
# print "Login Time: %.2f" % (end - start)
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
