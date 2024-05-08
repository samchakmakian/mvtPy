from createdataclass import *
from searchfile import *
from yesno import *
from pathlib import Path
import numpy as np
import subprocess
import shutil


def construct_lc():
    grb_filesearch = '*' + target_grb[3:] + '*'
    grb_t0 = float(return_t0(rows, target_grb))
    grb_t90 = float(return_t90(rows, target_grb))
    neg_t90 = grb_t0 - grb_t90
    plus_t90 = grb_t0 + grb_t90
    grb_filename = find_file(grb_filesearch, 'fitsdata')
    print('Found fits file:', grb_filename)
    print('t90:  ', grb_t90)
    print('-t90: ', neg_t90)
    print('t0:   ', grb_t0)
    print('+t90: ', plus_t90)
    binterval = float(input('Bin size interval:'))
    bins = np.arange(.0001, 1, binterval)
    print('Bin size of ', binterval, 'produces', len(bins), 'bins.')
    genyn = yn('Generate curves for given binning?', default="yes")
    while genyn:
        for x in range(len(bins)):
            # Create output file string from input file name and bin size
            lc_out = (grb_filename.split('.')[0] + '_' + str(x+1) + '.lc')

            # Create a list of desired gtbin parameters
            gtbin = ['gtbin evfile=', grb_filename, ' scfile=NONE outfile=', lc_out, ' algorithm=LC tbinalg=LIN tstart=', neg_t90, ' tstop=', plus_t90, ' dtime=', bins[x], ' chatter=0']

            # Convert above list into string for output to gtbin command
            gtbin = ''.join(map(str, gtbin))

            # Prints progress to terminal
            print('Generating curve', + (x+1), 'of', len(bins))

            # Run gtbin in terminal using generated string as input
            subprocess.run(gtbin, shell=True)
        Path(target_grb.lower()).mkdir(parents=True, exist_ok=True)
        thispath = os.getcwd()
        lc_files = os.listdir(thispath)
        movepath = os.path.join(thispath, target_grb.lower())
        for file in lc_files:
            if file.endswith('.lc'):
                shutil.move(os.path.join(thispath, file), os.path.join(movepath, file))
        break


csv_filename = 'nametrigt90.csv'
rows = read_csv(csv_filename)
target_grb = input('Input GRB name (ex: GRB080916009):')

construct_lc()
print('Done\n')
