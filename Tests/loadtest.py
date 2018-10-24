import report42, studyFunctions, viewerModule, flowModule, outputFile, loadTest, short3d, biplanarLAX
from collections import OrderedDict

legend = [(1000, "Login to cvi42"),
          (1001, "Anonymize a study"),
          (1002, "Load a study"),
          (1003, "Add viewer frame to report"),
          (1004, "Add capture image to report"),
          (1005, "Add viewer frame to report"),
          (1006, "Add systemic flow to report"),
          (1007, "Add pulmonary flow to report"),
          (1008, "Add comparison tab to report"),
          (1009, "Short3D LV Endo/Epi Current Phase"),
          (1010, "Short3D add to report"),
          (1011, "Biplanar ML time"),
          (1012, "Biplanar add to report")]


# Step 2 - Anonymize Annulus-016
# annulus16 = studyFunctions.anonymize_study(dialog, "Annulus_016",
#                                            "AutomationTest1-Annulus16", filename)
def run(dialog, app, pid, filename):

    # Step 3 - Anonymize Function-Flow-Perfusion
    functionFlow = studyFunctions.test1001_anonymize_study(dialog, "Function-Flow-Perfusion",
                                                           "AutomationTest2-FuncFlow", filename)

    # Step 4 - Load Function-Flow-Perfusion
    loadTest.test1002_load(dialog, functionFlow, filename)

    # Step 5 - Draw 5 contours in viewer module
    viewerModule.viewer_module_full_workflow(dialog, pid, functionFlow, "Viewer1", 1)

    report42.add_to_report(dialog)
    report42.check_report42_status(dialog, pid, filename, 1003)

    # Step 6 - add to report from capture measurements
    studyFunctions.click_module(dialog, "Viewer", pid)
    viewerModule.add_measurement_capture(dialog)

    report42.check_report42_status(dialog, pid, filename, 1004)

    # Step 7 - Repeat step 5 for a different series
    viewerModule.viewer_module_full_workflow(dialog, pid, functionFlow, "Viewer2", 3)

    report42.add_to_report(dialog)
    report42.check_report42_status(dialog, pid, filename, 1005)

    # Step 8 - Load series 5 into systemic flow and draw/forward an ROI
    flowModule.flow_full_workflow(dialog, pid, functionFlow, "s", 5)

    report42.add_to_report(dialog)
    report42.check_report42_status(dialog, pid, filename, 1006)

    # Step 9 - Load series 6 into pulmonary flow and draw/forward an ROI
    flowModule.flow_full_workflow(dialog, pid, functionFlow, "p", 6)

    report42.add_to_report(dialog)
    report42.check_report42_status(dialog, pid, filename, 1007)

    # Step 10 - Go to comparison tab and add to report
    studyFunctions.click_module(dialog, "Flow", pid)
    flowModule.comparison_tab_select(dialog)

    report42.add_to_report(dialog)
    report42.check_report42_status(dialog, pid, filename, 1008)

    # Step 11 - Short 3D Module ML Phase series 1
    time_short3d_ml = short3d.ml_full_workflow(dialog, app, pid, functionFlow,
                                               "Detect LV Endo/Epi Contours Current Phase", 1)
    outputFile.print_timing(1009, time_short3d_ml, filename)

    # Step 12 - add ML Short3d to report
    report42.add_to_report(dialog)
    report42.check_report42_status(dialog, pid, filename, 1010)

    # Step 14 - reset the workspace
    studyFunctions.reset_workspace(dialog)

    # Step 16 - Biplanar LAX assessment
    time_biplanar_ml = biplanarLAX.full_workflow(dialog, app, pid, functionFlow,
                                                 "Detect LA/RA Contours Current Slice", 2, 3)
    outputFile.print_timing(1011, time_biplanar_ml, filename)

    report42.add_to_report(dialog)
    report42.check_report42_status(dialog, pid, filename, 1012)

    studyFunctions.close_study(dialog)
    # studyFunctions.delete_anon_study(dialog, annulus16)
    studyFunctions.delete_anon_study(dialog, functionFlow)

    return
