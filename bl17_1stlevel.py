# -*- coding: utf-8 -*-
"""
@author: t8r
"""

#%% First level analysis
import os
cwd = '/media/cbru/GREEN/Biling_2017_analysis/'
os.chdir(cwd)
import subprocess


subjects = ['kh3']

for subj in subjects:
    for run in ['1','2']:
        print "Creating template"
        design_file= cwd + '1st_level/1st_level_template.fsf'
        
        n_vols = str(int(os.popen('fsl5.0-fslnvols {}MRI_data/{}/epi_{}'.format(cwd,subj,run)).readlines()[0]))

        out=open('{}1st_level/{}_epi{}_design.fsf'.format(cwd,subj,run),'w')
        lines=open(design_file,'r').readlines()
        for line in lines:
            line=line.replace('$path',cwd)
            line=line.replace('$subj',subj)
            line=line.replace('$run',run)
            line=line.replace('$n_vols',n_vols)
            out.write(line)
        out.close()
        print('Starting {} run{} feat analysis...'.format(subj,run))
        subprocess.call('fsl5.0-feat {}1st_level/{}_epi{}_design.fsf'.format(cwd,subj,run),shell=True)
        print('Done with {} run{}.'.format(subj,run))
        
        
    design_file= cwd + '1st_level/combine_runs_template.fsf'  
    out=open('{}1st_level/{}_combine_design.fsf'.format(cwd,subj),'w')
    lines=open(design_file,'r').readlines()
    for line in lines:
        line=line.replace('$path',cwd)
        line=line.replace('$subj',subj)
        out.write(line)
    out.close()
    print('Combining {} runs...'.format(subj))
    subprocess.call('fsl5.0-feat {}1st_level/{}_combine_design.fsf'.format(cwd,subj),shell=True)
