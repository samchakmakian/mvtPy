import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os


sns.set_style('whitegrid')
sns.set_style({'font.family': 'serif', 'font.serif': 'Times New Roman'})


target_grb = input('Input GRB name (ex: GRB080916009):')
mvtfile = target_grb.lower() + '_mvt.txt'
os.chdir('fitsdata')
data = np.loadtxt(mvtfile)
plt.scatter(data[:, 0], (data[:, 2]/data[:, 1])/data[:, 0], marker='.')

# Set scaling parameters
plt.gca().set_xscale('log')
plt.gca().set_yscale('log')

# Plot labels
plt.title('Minimum Variability Timescale')
plt.ylabel('Ratio of Variances / Number of Bins')
plt.xlabel('Bin Width (s)')

# Set the start and stop point for the plot
plt.xlim(0.0001, 1)

os.chdir('..')

# Show the plot in window, don't save (comment these next two lines to save plot)
plt.show()
plt.close()
# Save the plot (uncomment these next two lines to save plot)
# plotname = input('Name of output plot file (ex: mvt1.png):)
# plt.savefig(plotname, dpi=300)
