"""
This model allows a user who has all their experimental data saved in a directory folder to mass import the files and have an hdf5 file created that has the data organized and fit. This module interacts closely with the dataprep.py module also
included with this package. 

The advantage of this model is that it is an automated (looped) version of the `add_experiment` function in dataprep.py thus allowing a user not to have to manually import data files one at a time.

The user needs to have had an organized filename structure as the organized hdf5 file relies on it. For this use case the compound name 'FA_' (Formic Acid) is the first part of the files in the directory and then the 

Developed by the Raman-Noodles team (2019 DIRECT Cohort, University of Washington)
"""


#initial imports
import os
import h5py
import matplotlib.pyplot as plt
from ramandecompy import dataprep


def data_import(hdf5_filename, directory):
 """
    This function adds Raman experimental data to an existing hdf5 file. It uses the
    spectrafit.fit_data function to fit the data before saving the fit result and
    the raw data to the hdf5 file. The data_filename must be in a standardized format
    to interact properly with this function. It must take the form anyname_temp_time.xlsx
    (or .csv) since this function will parse the the temp and time from the filename to
    label the data and fit result in the hdf5 file.

    Args:
        hdf5_filename (str): the filename and location of an existing hdf5 file to add the
                             experiment data too. Variable must be in a string format.



        directory (str): the folder location of raw Raman spectroscopy data in a 
                             string format.

    Returns:
        None
    """
dataprep.new_hdf5(hdf5_filename) 
for filename in os.listdir(directory):
    if filename.startswith('FA_') and filename.endswith('.csv'):
        locationandfile = directory + filename
        dataprep.add_experiment(hdf5_filename, locationandfile)
        print('Data from {} fit with compound pseudo-Voigt model. Results saved to {}.'.format(filename, hdf5_filename)) #printing out to user the status of the import (because it can take a long time if importing a lot of data, about 1 minute/data set for test files
        exp_file.close()
        continue
    else:
        print('Data from {} fit with compound pseudo-Voigt model. Results saved to {}.'.format(filename, hdf5_filename))
        exp_file.close()
        continue
return