from matplotlib import  cm

# Parameters:
xmin = 0
xmax = 512
ymin = 0
ymax = 512

# What colormap should be used?:
cmap = cm.Reds_r

# Do you want a vertical or horizontal colorbar?:
colorbar_orientation = 'vertical' #'horizontal'

# What is the name of the datafiles you want to plot?:
filename = 'j.txt'

# What is the name extension you want to save your images as?:
savefile_extension = 'J.png'

# The list of the directories you want to collect data from:
# Manually or automated by a list comprehension:
dir_names = ['n0048', 'n0049']
# dir_names = ['n00' + i for i in range(100)]

# What is the relative path to the directory storing directories containing the datafiles?:
data_directory = "../"
# Where do you want to store the resulting plots?:
save_directory = "../test/J"

# Do you want an overlay with another datafile type?:
# In that case: What is the filename of those files?:
overlay_filename = "jc.txt"
# How opaque do you want the overlay?:
overlay_opacity = 0.1 # 0 means no colorbar

# What should be the label of the colorbar?
cmap_label = r"$J/J_0+0.05\tilde{J}_c$ [dimensionalless]" # label for the colorbar

# What are the axes labels:
xlabel = "$x$ [grid points]"
ylabel = "$y$ [grid points]"

# For contour lines, specify the filename of the datafiles that
# are used for the contour lines:
contour_filename = "g.txt"
# If you don't want any contour lines set 0 below:
ca_number_of_contour_lines = 8

# Here you can adjust the size of the axis labels:
# If you for some reason don't want any labels, you can set 
# them to a very small number like 0.001
label_fontsizex = 16
label_fontsizey = 16
label_tick_fontsizex = 16
label_tick_fontsizey = 16

# If you want customized axis-ticks, then specify below:
#x_axis_ticks = [360, 380, 400, 420, 440, 460]
# If you just want the default axis ticks, just create a
# one element list like below:
x_axis_ticks = [0] # length 1 means default axis ticks
y_axis_ticks = [0]

# The tick and labelsize for the colorbar:
colorbar_tick_fontsize = 16
colorbar_labelsize = 16

# Do you want to show the plots while the program is running?
show_plots = "no" # or "yes" if you want that
