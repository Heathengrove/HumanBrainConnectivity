# -*- coding: utf-8 -*-
"""
@author: tatuh
"""
#%% Preprocessing
# Do anatomicals first with bl17_anat.py
import os
cwd = '/media/cbru/GREEN/Biling_2017_analysis/'
os.chdir(cwd)
import bl17_MRIfunc as bl17


subjects = ['kh3']
for subj in subjects:
    working_dir = cwd + 'MRI_data/' + subj + '/'
    os.chdir(working_dir)
    #
    do_logs   = 1   #Process logfiles, this has to be run at least once before do_epi, as it creates a simple timing file for removing extra 
    do_epi    = 1   #Process epis
    do_mc     = 1  #Do motion correction
    do_dti    = 0   #Do dti, nothing here yet
#
    anat,epis,dtis = bl17.findFiles(working_dir,subj)
    epi_dirs = [x[2] for x in epis]
    anat3D_dir = anat[2]

    if do_logs:
        bl17.processLogs(cwd,subj)
    if do_epi:
        bl17.processEpis(cwd,epi_dirs,subj)
    if do_mc:
        bl17.motionCorr(cwd,working_dir,subj)
