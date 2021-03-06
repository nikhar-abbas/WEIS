from wisdem.glue_code.runWISDEM import run_wisdem
import matplotlib.pyplot as plt
import numpy as np
import os
from wisdem.commonse.mpi_tools import MPI

show_plots = False

## File management
mydir = os.path.dirname(os.path.realpath(__file__))  # get path to this file
fname_wt_input         = mydir + os.sep + 'blade.yaml'
fname_modeling_options = mydir + os.sep + 'modeling_options.yaml'
fname_analysis_options = mydir + os.sep + 'analysis_options_aero.yaml'

wt_opt, modeling_options, analysis_options = run_wisdem(fname_wt_input, fname_modeling_options, fname_analysis_options)

if MPI:
    rank = MPI.COMM_WORLD.Get_rank()
else:
    rank = 0

if rank == 0:
    print('RUN COMPLETED. RESULTS ARE AVAILABLE HERE: ' + os.path.join(mydir,analysis_options['general']['folder_output']))