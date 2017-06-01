# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:52:13 2017

@author: t8r
"""
import subprocess
import os
cwd = '/media/cbru/GREEN/Biling_2017_analysis/'
os.chdir(cwd)
import bl17_MRIfunc as bl17

#%% Better BET code. For single subjects to try different fractional intensity thresholds (FIT in code below)
subj = 'kh4'
FITvalue = '0.35'
Center_of_brain = '90 107 170'


def do_anat3D_single(working_dir,anat3D_dir,subj,FITvalue):
    print('Doing anatomicals...')
    working_dir = cwd + 'MRI_data/' + subj + '/'
    os.chdir(working_dir)
    subprocess.call('dcm2nii -4 Y -d N -f Y -e N -p N -x N {}/MR00001'.format(anat3D_dir),shell=True)
    subprocess.call("mv {}/oMR00001.nii.gz anat3d.nii.gz".format(anat3D_dir,working_dir),shell=True)
    subprocess.call("rm {}/coMR00001.nii.gz".format(anat3D_dir),shell=True)
    subprocess.call("rm {}/MR00001.nii.gz".format(anat3D_dir),shell=True)
    print('Doing brain extraction...')	
    subprocess.call("fsl5.0-bet anat3d.nii anat3d_brain.nii -R -f {}".format(FITvalue),shell=True)
    subprocess.call("fsl5.0-bet anat3d.nii anat3d_brain_2.nii -c {}".format(Center_of_brain),shell=True)	
    subprocess.call("cp -f anat3d.nii.gz {}/sb_anat/{}_anat3d.nii.gz".format(cwd,subj),shell=True)
    subprocess.call("cp -f anat3d_brain.nii.gz {}/sb_anat/{}_anat3d_brain.nii.gz".format(cwd,subj),shell=True)
    subprocess.call("cp -f anat3d_brain_2.nii.gz {}/sb_anat/{}_anat3d_brain_2.nii.gz".format(cwd,subj),shell=True)
    subprocess.call("fslview -m ortho {}/sb_anat/{}_anat3d.nii.gz {}/sb_anat/{}_anat3d_brain.nii.gz -l \"Red-Yellow\"".format(cwd,subj,cwd,subj),shell=True)
    print('Done!')
    

working_dir = cwd + 'MRI_data/' + subj + '/'
os.chdir(working_dir)
anat,epis,dtis = bl17.findFiles(working_dir,subj)
epi_dirs = [x[2] for x in epis]
anat3D_dir = anat[2]
do_anat3D_single(working_dir,anat3D_dir,subj,FITvalue)

