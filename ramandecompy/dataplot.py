"""
docstring
"""


import h5py
import lineid_plot
import numpy as np
import matplotlib.pyplot as plt


def pseudo_voigt(x_data, amplitude, center, sigma, fraction):
    """
    Function that calculates a pseudo-voigt distribution over a given x_data range 
    """
    sigma_g = sigma/(np.sqrt(2*np.log(2)))
    gaussian = ((((1-fraction)*(amplitude))/(sigma_g*np.sqrt(2*np.pi)))
                *np.exp((-((x_data-center)**2))/(2*(sigma_g**2))))
    lorentzian = ((fraction*amplitude)/(np.pi))*(sigma/(((x_data-center)**2)+sigma**2))
    pseudo_voigt = gaussian+lorentzian
    return pseudo_voigt


def plot_component(ax, hdf5_file, key, peak_number, color=None):
    """docstring"""
    # open hdf5 file
    hdf5 = h5py.File(hdf5_file, 'r')
    # extract wavenumber data
    x_data = list(hdf5[key+'/wavenumber'])
    # add zero to the beginning of any single digit peak number
    if peak_number < 10:
        peak_number = '0{}'.format(peak_number)
    else:
        peak_number = '{}'.format(peak_number)
    # extract pseudo voigt parameters
    peak_params = hdf5[key+'/Peak_'+peak_number]
    fraction, sigma, center, amplitude = peak_params[0:4]
    # calculate pseudo voigt distribution from peak_params
    y_data = pseudo_voigt(x_data, amplitude, center, sigma, fraction)
    if color is None:
        color = next(ax._get_lines.prop_cycler)['color']
    else:
        color = color
    plt.plot(x_data, y_data, linestyle='--', color=color)
    plt.fill_between(x_data, y_data, alpha=0.3, color=color)
    hdf5.close()


def plot_components(ax, hdf5_file, key, peak_list):
    """docstring"""
    # will turn int or float into list
    if isinstance(peak_list, (int, float)):
        peak_list = [peak_list]
    else:
        pass
    for _,peak_number in enumerate(peak_list):
        plot_component(ax, hdf5_file, key, peak_number)

