from astropy.io import fits
from createdataclass import *
from searchfile import *
import numpy as np
import matplotlib.pyplot as plt


csv_filename = 'nametrigt90.csv'
rows = read_csv(csv_filename)
target_grb = input('Input GRB name (ex: GRB080916009):')
grb_t0 = float(return_t0(rows, target_grb))
grb_t90 = float(return_t90(rows, target_grb))
neg_t90 = grb_t0 - grb_t90
plus_t90 = grb_t0 + grb_t90
grb_filesearch = '*' + target_grb[3:] + '*'
lc_path = os.path.join('fitsdata', target_grb.lower())
os.chdir(lc_path)
curves = sorted(glob.glob('*.lc'), key=os.path.getmtime)
binterval = float(input('Bin size interval:'))
bins = np.arange(.0001, 1, binterval)
print('Bin size of ', binterval, 'produces', len(bins), 'bins.')

output = []
for i in range(9999):
    lightcurve = fits.open(curves[i])
    b = bins[i]
    counts = lightcurve['RATE'].data.field('COUNTS')
    differential = np.diff(counts)
    var1 = np.var(differential[:len(differential) // 2])
    var2 = np.var(differential[len(differential) // 2:])
    output.append([b, var1, var2])
    print('file', i + 1, 'of 9999')
output = np.array(output)
os.chdir('..')
mvtdataout = target_grb.lower() + '_mvt.txt'
np.savetxt(mvtdataout, output)
