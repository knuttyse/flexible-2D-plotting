import os
import sys
import shutil

import numpy as np
from matplotlib import mlab, cm, rcParams, colorbar, pyplot as plt
from parameters import *

def last_inn_matrise(path):
    return np.transpose(np.loadtxt(path))

def snitt_matrise(matrise, xmin, xmax, ymin, ymax):
    shape = np.shape(matrise)
    return matrise[shape[0]-ymax:shape[0]-ymin,xmin:xmax]

def get_data(path, xmin, xmax, ymin, ymax):
    full_matrix = np.transpose(np.loadtxt(path))
    return snitt_matrise(full_matrix, xmin, xmax, ymin, ymax)

def finnminmaks(filenames, xmin, xmax, ymin, ymax):
    minimum = 1
    maximum = -1
    print filenames
    for datafile in filenames:
        utsnitt = get_data(datafile, xmin, xmax, ymin, ymax)
        local_min=np.min(utsnitt)
        local_max=np.max(utsnitt)
        if local_min < minimum:
            minimum = local_min
        if local_max > maximum:
            maximum = local_max
    return minimum, maximum

datafiles =              [data_directory+dir_name+"/"+filename        for dir_name in dir_names]
overlay_datafiles =      [data_directory+dir_name+"/"+overlay_filename for dir_name in dir_names]
contour_line_datafiles = [data_directory+dir_name+"/"+contour_filename for dir_name in dir_names]

extent = (xmin, xmax, ymin, ymax)
minste_verdi, storste_verdi = finnminmaks(datafiles, xmin, xmax, ymin, ymax)
norm = cm.colors.Normalize(vmin = minste_verdi, vmax = storste_verdi)

if ca_number_of_contour_lines > 0:
    minste_conturlinje, storste_conturlinje = finnminmaks(contour_line_datafiles, xmin,xmax,ymin,ymax)
    levels = np.arange(minste_conturlinje, storste_conturlinje, (storste_conturlinje-minste_conturlinje)/ca_number_of_contour_lines)
    rcParams['contour.negative_linestyle'] = 'solid'

if not os.path.exists(save_directory):
    os.makedirs(save_directory)
else:
	print "\n\n    overwrite %s? y/n" % save_directory
	inp = raw_input()
	if 'n' in inp:
		sys.exit()

# Plot series:
for datafile, overlay_datafile, contour_datafile in zip(datafiles, overlay_datafiles, contour_line_datafiles) :
    cut = get_data(datafile, xmin, xmax, ymin, ymax)
    
    # If overlay is desired:
    if overlay_opacity > 0:
        overlay = get_data(overlay_datafile, xmin, xmax, ymin, ymax)
        cut += overlay*overlay_opacity

    plt.figure()
    plt.imshow(cut, extent=extent, cmap=cmap, norm=norm, interpolation='nearest')

    # If contour lines are desired:
    if ca_number_of_contour_lines > 0:
        Z = get_data(contour_datafile, xmin, xmax, ymin, ymax)
        v = plt.axis()
        plt.contour(Z, levels, hold='on', colors='k', origin='upper', extent=extent)
        plt.axis(v)

    plt.xlabel(xlabel, fontsize = label_fontsizex)
    plt.ylabel(ylabel, fontsize = label_fontsizey)
    
    if len(x_axis_ticks) > 1:
        plt.xticks(x_axis_ticks, fontsize = label_tick_fontsizex)
    else:
        plt.xticks(fontsize= label_tick_fontsizex)
    if len(y_axis_ticks) > 1:
        plt.yticks(y_axis_ticks, fontsize=label_tick_fontsizey)
    else:
        plt.yticks(fontsize=label_tick_fontsizey)

    if show_plots == "yes":
        plt.show()
    plt.savefig(save_directory + '/' + dir_name + savefile_extension, bbox_inches='tight', pad_inches=0)


# Make Colorbar :
if colorbar_orientation == "horizontal": # Horizontal colorbar:
    fig = plt.figure(figsize=(8, 3))
    ax1 = fig.add_axes([0.05, 0.80, 0.9, 0.15])
else: # vertical colorbar:
    fig = plt.figure(figsize=(3, 8))
    ax1 = fig.add_axes([0.05, 0.80, 0.15, 0.9])

cb1 = colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm, orientation=colorbar_orientation)
cb1.set_label(cmap_label, fontsize=colorbar_tick_fontsize)
cb1.ax.tick_params(labelsize=colorbar_labelsize, direction='out') 
plt.savefig(save_directory + '/colorbar' + savefile_extension, bbox_inches='tight', pad_inches=0)

# Log parameters:
shutil.copyfile("parameters.py", save_directory + "/parameters.py")
