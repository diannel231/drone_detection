# Drone Detection
This repository contains the blocks used in GNU Radio used for drone detection and classification. The OFDM and Energy code is adapted from [Radio Frequency Toolbox](https://digitalcommons.odu.edu/ece_etds/160/) and [gr-inspector](https://github.com/gnuradio/gr-inspector).

## Modules and Blocks

The following are the modules and blocks contained in the module:
- OFDM_Estimator: OFDM_Estimator
- Energy_Detector: Energy_Detector, Energy_Detector_V2
- Drone_ML: ml_testing

OFDM_Estimator is written using C++. Energy_Detector and Drone_ML is written in 

*Note: Energy_Detector_V2 is simply the same block as Energy_Detector but it contains prints to output signal presence.*

## Installation

The following are used to run the Energy Detector and OFDM Estimator Blocks:
- Virtual Box: https://www.virtualbox.org/wiki/Downloads
- Kali VM: https://www.kali.org/get-kali/#kali-virtual-machines
- GNU Radio 3.10: https://wiki.gnuradio.org/index.php/InstallingGR
- gr-osmosdr: https://osmocom.org/projects/gr-osmosdr/wiki/GrOsmoSDR
- HackRF: https://www.kali.org/tools/hackrf/

Install the blocks with the following shell commands:
```
$ gr_modtool newmod module_name
$ cd gr-module_name
$ gr_modtool add block_name
```

In the gr folder, either add the blocks and copy the main code from the lib (C++) or python folder and yaml from the grc folder, or replace all folders with the ones from this repository. The modules were created and installed in the main Kali home directory.

After the files have been replaced, run the following commands in the gr-Energy_Detector_ff folder:
```
$ mkdir build
$ cd build
$ cmake ..
$ make -j4
$ sudo make install
$ sudo ldconfig
```
