
<div align="center">
  
<h3 align="center">mvtPy</h3>

  <p align="center">
    mvtPy is a Python based toolkit that aims to ease the use of tools like gtbin through automation, as well as provide the tools necessary for minimum variability timescale (MVT) estimation of gamma-ray bursts (GRBs) sourced from the Fermi GBM Burst Catalog.

  </p>
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#goals">Goals</a></li>
    <li><a href="#links">Helpful Links</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



## Getting Started


<!-- PREREQUISITES -->
### Prerequisites

- This project was built using a Linux-based system, as the Fermitools wiki states MacOS or Linux are required. As such, a Unix-based system is recommended. Besides the tools used, it is unclear if my code will run on a Windows-based system- it's definitely worth a try if you wanted to give it a go, and Dr. Rob might have some insight on this. Nonetheless, I'm going to give install instructions for each item as it would be done on a Debian-based Linux system (as I feel like you're most likely to use Ubuntu if you do use Linux), and if you end up successfully utilizing Windows, you should be familiar with installing programs anyway. Links to everything will be provided at the bottom of this documentation.
- Furthermore, it may be helpful to go through the short tutorial located at the 'GBM Data Extraction and Gamma-Ray Burst Analysis' webpage linked at the bottom of this file. This is a good way to get a hands-on feel for how `gtbin` works, how to navigate the Fermi burst catalog, and why we are trying to automate this process.

##### Anaconda Navigator:
- Installing prerequisites:

    ```shell
    apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
    ```

- Download Anaconda (replace `<INSTALLER_VERSION>` with the latest version of the installer, check the link in the links section)

    ```shell
    curl -O https://repo.anaconda.com/archive/Anaconda3-<INSTALLER_VERSION>-Linux-x86_64.sh
    ```

- Install:
    ```shell
    bash ~/Downloads/Anaconda3-<INSTALLER_VERSION>-Linux-x86_64.sh
    ```

- Anaconda recommends you enter “yes” to initialize Anaconda Distribution by running `conda init`.  If you enter “no”, then conda will not modify your shell scripts at all. In order to initialize conda after the installation process is done, run the following commands:

    ```shell
    source <PATH_TO_CONDA>/bin/activate
    conda init
	```

##### Fermitools:
- After installing Anaconda, setup your Fermitools environment as `fermi`:

	```shell
	conda create -n fermi -c conda-forge -c fermi fermitools numpy=1.20
	```

- To enter the `fermi` environment once it is created:

	```shell
	conda activate fermi
	```

- Python coding can be done using many different types of software. I used PyCharm Professional IDE to code this project, and found it quite helpful (if you want to try it, you can get a free license using your URI credentials!) You may find it more comfortable to use Jupyter Notebook. Whatever you decide should be fine.
- If you choose to download the project via the command line, you may need to install `git` first:
	```shell
	sudo apt install git-all
	```


<!-- INSTALLATION -->
### Installation

- Clone the repo (alternatively: [download manually](https://github.com/samchakmakian/mvtPy))
	```shell
	git clone https://github.com/samchakmakian/mvtPy.git
	```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE -->
## Usage


##### Acquiring GRB data

1. Head to the [Fermi Burst Catalog](https://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3table.pl?tablehead=name%3Dfermigbrst&Action=More+Options)
2. Search for a GRB using whichever parameter you choose
3. Under the 'Services' tab, select 'D' to access the GRB's data
4. After clicking 'DIRECTORY' next to 'GBM Trigger Products (current)', you can select individual files to download.
	- The relevant files are ones with the '.fit' extension near the bottom of the page. Use the 'GBM Trigger Quicklook Light Curves GIF' on the previous page to select an appropriate detector and corresponding .fit file.
5. Move the .fit file to the project's 'fitsdata' directory.

##### Generating light curve files

1. Run `genLC.py`
2. Input the name of the GRB for which you downloaded data using the naming scheme provided in the prompt
3. The module will tell you whether or not it located the appropriate fits file in the fitsdata folder. If it did not, investigate
	- It will also provide you with the relevant t90 data for your burst as grabbed from 'nametrigt90.csv'
4. Input bin size interval. The code is currently set up to start at a bin size of 0.0001s and end at 1s, with the given interval in between
5. The module will generate the .lc files before moving them all to their own folder, so as to not clutter the fitsdata directory. Note that this can take quite some time to complete for a small bin size interval

##### Generating the MVT data

1. Run `mvtscan.py`
2. Input the name of the GRB for which you are generating MVT data
3. Input the bin size interval used when generating light curve files
4. After the statistical calculations are complete, the .txt file containing the data we need to generate our MVT curve is placed into the fitsdata folder

##### Generating the MVT curve

1. Run `makeplot.py`
2. Input the name of the GRB
3. That's it! Sort of:
	- `makeplot.py` requires a bit more interaction with the code than the other modules.
	- If you want to show the plot in the current window, run the code as is. If you want to save the plot to a file, you need to comment out the lines that show the plot and uncomment the lines that save it. See the code for more information

#### Usage Information on the other modules in the package

- There are some other modules included in the package that you probably will not have to interact with, as they are either dependencies for the main three modules or exist to generate necessary files that have already been included. Nonetheless, I'll detail them briefly in case you need to use them:

###### fitsviewer

- Software used to view fits and lc files. May be useful for sanity-checking or doing the tutorial discussed in the 'Prerequisites' section

###### `createdataclass.py`

- This module creates the data class that the rest of our code uses to reference the GRB data necessary to work. It sources the data from the `nametrigt90.csv`

###### `searchfile.py`

- This module defines a function that allows the other modules to locate files (for instance, locating the initial .fit file used in light curve generation)

###### `trigtimeconvert.py`

- This module allows the conversion of a csv containing a large number of times in 'mjd' format to the Fermi MET (mission elapsed time) required by our code. This would be used if we needed to re-generate `nametrigt90.csv`, for instance

###### `yesno.py`

- This module allows us to use a simple yes/no prompt in our other modules

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GOALS -->
## Goals

Dr. Coyne can provide you with some goals for the project. Some initial ideas from my perspective:

- It would be nice if the three main modules interacted with could be combined in some way. Mainly, the MVT data and plot generation
- There is quite a lot of weirdness and noise produced by the code. It's unclear what the source is, though Dr. Coyne and I suggest it may be a result of the method used to source data from the catalog: we use the data from a single NaCl detector, when it would likely be useful to use the data from multiple detectors. For more information on this or the project in general, I've included a copy of the paper I wrote after working on this project
- It would be very helpful if data acquisition could be automated through the code rather than having to be done manually

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LINKS -->
## Helpful Links

- [Anaconda](https://docs.anaconda.com/free/anaconda/install/)
- [Fermitools](https://github.com/fermi-lat/Fermitools-conda/wiki)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [mvtPy](https://github.com/samchakmakian/mvtPy)
- [GBM Data Extraction and Gamma-Ray Burst Analysis](https://fermi.gsfc.nasa.gov/ssc/data/p7rep/analysis/scitools/gbm_grb_analysis.html)
- [Fermi GBM Burst Catalog](https://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3table.pl?tablehead=name%3Dfermigbrst&Action=More+Options)
- [Fermi Burst Catalog documentation](https://heasarc.gsfc.nasa.gov/w3browse/fermi/fermigbrst.html)
- [xTime - A Date/Time Conversion Utility](https://heasarc.gsfc.nasa.gov/cgi-bin/Tools/xTime/xTime.pl)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Sam Chakmakian - samchakmakian@gmail.com

Project Link: [https://github.com/samchakmakian/mvtPy](https://github.com/samchakmakian/mvtPy)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Dr. Rob Coyne for assigning this project, guiding me through it, and putting up with all my crap](https://web.uri.edu/physics/meet/robert-coyne/)
* [Julian Pawlowski, for making the template for this readme](https://github.com/jpawlowski)

<p align="right">(<a href="#readme-top">back to top</a>)</p>