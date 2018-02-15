![finkeneye](https://scontent-nrt1-1.xx.fbcdn.net/v/t1.0-9/27867829_10156280685570625_1935328121628611094_n.jpg?oh=21b2ce771dc1f2bf95c99bb7d0e23301&oe=5B0AFE3E)

## FINken eYe: SVO Semi-Direct Visual Odometry Onboard the FINken Copters

Please refer our wiki for instructions on installation and detailed documentation: https://github.com/Adu143/SVO/wiki

For a summary of the project, please refer to our [presentation slides](https://www.slideshare.net/MichaelMera/finken-eye-visual-slambased-position-estimation).

Video demonstration: Coming soon.

### Abstract

Our goal was to run Visual SLAM-based Position Estimation on the FINken Copters from the SwarmLab at Otto-von-Guericke University Magdeburg. http://www.is.ovgu.de/SwarmLab.html

An approach towards positioning of the copters is based on optical tracking of the sourrounding environment. To this end, a camera together with a power-full embedded computer board was integrated on the copters. The camera observes the sourroundings of the copter an tries to find landmarks to compare them to the existing partial map. There are multiple ways to locate the copter in the map and to update the maps information. The goal of this project was to establish the hardware setup necessary to aquire visual information and process it in a seperate computing unit. Afterwards existing Visual SLAM algorithms were investigated for their usage in the indoor copter scenario. The most promising algorithm was then be implemented on the computing platform and optimized and evaluated for usage on futere projects in our lab to extend the functionality of our copter swarm.

### Disclaimer

This version of SVO has been tested under ROS Indigo with Ubuntu 14.04 LTS on ODROID C0 embedded board. This is research code, any fitness for a particular purpose is disclaimed.

### Citations

This project is based on the great `rpg_svo` developed by Forster et. al and we are using it purely for academic purposes. We express our sincere admiration for their work. For the latest updates and code please refer to https://github.com/uzh-rpg/rpg_svo.

```
@inproceedings{Forster2014ICRA,
  author = {Forster, Christian and Pizzoli, Matia and Scaramuzza, Davide},
  title = {{SVO}: Fast Semi-Direct Monocular Visual Odometry},
  booktitle = {IEEE International Conference on Robotics and Automation (ICRA)},
  year = {2014}
}
```

### Acknowledgements
We thank Dr. Christoph Steup and Prof. Dr. Sanaz Mostaghim for all the advise and support, it was key to the successful completion of our project. We also thank all the staff in the SwarmLab for precisely setting up the equipment and materials required for our work.

--------For any questions or comments: michael at meracontractors dot com or throught the repository--------
