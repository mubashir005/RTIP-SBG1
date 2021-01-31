from osgeo import gdal
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable

# gdal constants
from gdalconst import *

# inform to use GDAL exceptions
gdal.UseExceptions()

# Load datasetRaster images
test_image = r"C:\Users\Maliks\Desktop\4.tiff"
dataset = gdal.Open(test_image, GA_ReadOnly)
# retrieve metadata from raster
i_rows = min(dataset.RasterXSize, dataset.RasterYSize)
i_columns = min(dataset.RasterXSize, dataset.RasterYSize)
N = i_rows * i_columns
bands = dataset.RasterCount

# print basic metadata
print("image metadata(details):")
print(i_rows, "rows xd", i_columns, "columns xd", bands, "bands")

# retrieve arrays from input image
array_R = dataset.GetRasterBand(1).ReadAsArray()[0:i_rows, 0:i_columns]
array_G = dataset.GetRasterBand(2).ReadAsArray()[0:i_rows, 0:i_columns]
array_B = dataset.GetRasterBand(3).ReadAsArray()[0:i_rows, 0:i_columns]
# find the intensity image (the average of RGB channels) for computing the integral image
array_intensity_avg = (array_R.astype(float) + array_G.astype(float) + array_B.astype(float)) / 3
array_intensity_avg *= 255 / array_intensity_avg.max()

# create the array of integral image
array_integral = np.zeros_like(array_intensity_avg)

# figure out values for integral image
figure_steps = 0
for r in range(i_rows):
    print(r)
    for c in range(i_columns):

        # compute the integral image (fast way)
        B = 0
        C = 0
        D = 0
        if r > 0:
            B = array_integral[r - 1, c]
        if c > 0:
            C = array_integral[r, c - 1]
        if r > 0 and c > 0:
            D = array_integral[r - 1, c - 1]

        array_integral[r, c] = array_intensity_avg[r, c] + B + C - D

        if r != c:
            continue

        # show result in animation file
        output_path = r'C:\Users\Maliks\Desktop' + str(figure_steps).zfill(6) + '.png'
        figure_border = 25

        # create 2 columns figure
        output_fig, (input_ax, integral_ax) = plt.subplots(figsize=(8, 4), ncols=2)

        # draw input image from rectangle
        divider_input = make_axes_locatable(input_ax)
        ax_input = divider_input.new_horizontal(size="5%", pad=0.05)
        fig0 = integral_ax.get_figure()
        # fig0.add_axes(ax_input)
        input_ax.imshow(array_intensity_avg, cmap='gray', vmin=0, vmax=255)
        # define rectangle of integral: (0,0) -> (r, c)
        x = [0, c, c, 0, 0]
        y = [0, 0, r, r, 0]
        input_ax.fill(x, y, fill=None, linewidth=1, alpha=0.5, color='red')
        input_ax.set_xlim([0 - figure_border, i_columns + figure_border])
        input_ax.set_ylim([i_rows + figure_border, 0 - figure_border])

        # draw integral image with scale
        divider = make_axes_locatable(integral_ax)
        ax_cb = divider.new_horizontal(size="5%", pad=0.05)
        fig1 = integral_ax.get_figure()
        fig1.add_axes(ax_cb)
        im = integral_ax.imshow(array_integral, vmin=0, vmax=131439465.33333834)

        plt.colorbar(im, cax=ax_cb)
        ax_cb.yaxis.tick_right()
        ax_cb.yaxis.set_tick_params(labelright=False)

        integral_ax.set_xlim([0 - figure_border, i_columns + figure_border])
        integral_ax.set_ylim([i_rows + figure_border, 0 - figure_border])

        output_fig.savefig(output_path, format='png', dpi=200)
        plt.close()

        figure_steps = figure_steps + 1

print(array_integral.max())
np.save(test_image + '.array_integral_image.npy', array_integral)

# close dataset
dataset = None