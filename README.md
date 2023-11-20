# ME6401
The project of ME6401(2023)
This page contains all relevant content about the Robot imagination project of ME6401 (Autumn 2023) Group 14. Since the Canvas system only allows submission of pdf files, the complete results are attached here for reference.


This program refers to the original pouring experiment (https://github.com/ChirikjianLab/container-imagination-only.git) and adds experiments on the vibration process. Among them, the doc, data, calibrate folders,  LICENSE , and utils.py are consistent with the original ones. The setup is basically the same as the original file, and the parts that need to be added are added at the end. The unmodified subcode is located in the sub_program folder, which also contains the subcode from this vibration experiment. The main_program folder contains partially modified pouring.py, pouring.py files and two summarized and integrated main vibration programs.example_gif, example_vedio respectively store the vibration simulation format files under the experimental parameters mentioned in the report , the appendix contains two introduced sensor software source files, please refer to: https://github.com/ar1vm0ndal/Mass-Sensor_SciOly_2022.git, https://github.com/Dheeraj1998/Pehchaan.git.The zip file is a compressed package of all files.

Note: To ensure the normal operation of the program, please set the path in all files (D:/Graduate/6401/container-imagination-only-container-visualize/) as the real-time file storage path and add it to the system environment variables.
The following is the readme part of the original file:










# Container Imagination
__Can I Pour into it? Robot Imagining Open Containability Affordance of Previously Unseen Objects via Physical Simulations (RA-L with ICRA 2021)__

__This repo is sourced from the [original repo](https://github.com/hongtaowu67/container_imagine) by [Hongtao Wu](https://hongtaowu67.github.io/), [Gregory Chirikjian](https://me.jhu.edu/faculty/gregory-s-chirikjian/), but for Imagination only (no Real Robot Experiment)__

Container Imagination is a method which enables robot to imagine the open containability affordance of an unseen object. With the understanding of the containability, the robot is able to identify whether the object is able to contain materials (e.g., M&M candies!) and pour a cup of the material into the object if it is identified as an open container.

<p align="center">
<img src="doc/teaser.gif" width=80% alt="Drawing">
</p>

* [Introductory video](https://youtu.be/n6dGRaLTv88)
* [Paper on IEEE Xplore](https://ieeexplore.ieee.org/document/9269438)
* [Paper on arxiv](https://arxiv.org/abs/2008.02321)
* [Project Page & Video Results](https://chirikjianlab.github.io/realcontainerimagination/)
* [Data](https://www.dropbox.com/s/fpnxhigttq06w1w/contain_imagine_data_RAL2021.zip?dl=0)

If you have any questions or find any bugs, please let me know: <hwu67@jhu.edu>

The following image summarize our method. Click the image to watch the video:

[![introductory video](doc/thumbnail0.png)](https://youtu.be/n6dGRaLTv88)

__(This repo only contains the code for step 2 & 3 - Open Containability Imagination and Pouring Imagination)__

# Abstract
Open containers, i.e., containers without covers, are an important and ubiquitous class of objects in human life. We propose a novel method for robots to "imagine" the open containability affordance of a previously unseen object via physical simulations. We implement our imagination method on a UR5 manipulator. The robot autonomously scans the object with an RGB-D camera. The scanned 3D model is used for open containability imagination which quantifies the open containability affordance by physically simulating dropping particles onto the object and counting how many particles are retained in it. This quantification is used for open-container vs. non-open-container binary classification. If the object is classified as an open container, the robot further imagines pouring into the object, again using physical simulations, to obtain the pouring position and orientation for real robot autonomous pouring. We evaluate our method on open container classification and autonomous pouring of granular material on a dataset containing 130 previously unseen objects with 57 object categories. Although our proposed method uses only 11 objects for simulation calibration (training), its open container classification aligns well with human judgements. In addition, our method endows the robot with the capability to autonomously pour into the 55 containers in the dataset with a very high success rate.

# Citation
If you find this code and/or the data useful in your work, please consider citing
```
@article{wu2020can,
  title={Can I Pour Into It? Robot Imagining Open Containability Affordance of Previously Unseen Objects via Physical Simulations},
  author={Wu, Hongtao and Chirikjian, Gregory S},
  journal={IEEE Robotics and Automation Letters},
  volume={6},
  number={1},
  pages={271--278},
  year={2020},
  publisher={IEEE}
}
```

# Dependencies
The project has been tested on Ubuntu 16.04 with python 2.7. We are working on transfering the code to python 3 on later version of Ubuntu release.

To install the dependencies, please refer to [here](Setup.md).

# Usage

## Imagination
<p align="center">
<img src="doc/imagine_object.png" height=180px alt="Ash Tray">
<img src="doc/contain_imagine.gif" height=180px alt="Containability Imagination">
<img src="doc/pouring_imagine.gif" height=180px alt="Pouring Imagination">
</p>

The imagination contains two part: open containability imagination and pouring imagination. The main script for imagination is [main_imagination.py](main_imagination.py).
```
python main_imagination.py <root_dir> <data_root_dir> <data_name> <mesh_name> [-p] [-v] [-m] 
```
- root_dir: root directory of the code
- data_root_dir: root directory of the data
- data_name: name of the data in data_root_dir. Note that a data represent a capture of a scene. There may be more than one object in the scene.
- mesh_name: name of the mesh / object for imagination
- [-p]: if set as True, pouring imagination will be activated
- [-v]: if set as True, visualization of the imagination will be activated
- [-m]: if a directory is given, the video of the imagination will be saved thereof. Note that this needs to used with the [-v] option. The video name of the containabiliy imagination is object_name_contain.mp4 the video name of the pouring imagination is object_name_pour.mp4

An example argument is given as follows:
```
python main_imagination.py <root_dir> <root_dir>/data Amazon_Accessory_Tray_pour_pca Amazon_Accessory_Tray_pour_pca_mesh_0 -p True -v True -m <root_dir>/data/Amazon_Accessory_Tray_pour_pca
```
The directory of the data should be structured as follows:
```bash
├── data_root_dir
│   ├── data_name_0
│   │   ├── object_name_0.obj
│   │   ├── object_name_0_vhacd.obj
│   │   ├── object_name_0.urdf
...
```
### V-HACD convex decomposition
------
V-HACD is used to decompose the mesh reconstructed from TSDF fusion for physical simulation in Pybullet.
Please follow the [Setup instruction](Setup.md) to install V-HACD.

## Containability Imagination Benchmark
First, download the [dataset](https://www.dropbox.com/s/fpnxhigttq06w1w/contain_imagine_data_RAL2021.zip?dl=0).
To run the containability imagination benchmark, first generate the imagiantion result
  ```
  python containability_imagination_benchmark.py <root_dir> <data_root_dir> <result_dir>
  ```
  - root_dir: root directory of the code
  - data_root_dir: root directory of the data
  - result_dir: directory to save the result
The imagination result (txt) for each object will be saved in the <result directory>. The format of the result is:
  ```
  container <sphere_in_percentage> 0 1 2 3
  ```
The "0 1 2 3" does not have any meaning in specific.
Then, run the benchmark code to get the classification accuracy and AUC
  ```
  python benchmark_map.py <result_dir> <gt_dir>
  ```
  - result_dir: directory to save the result
  - gt_dir: directory of the ground truth

We use the <sphere_in_percentage> from the containability imagination as the confidence to calculate the classificaiton accuracy and AUC.
If <sphere_in_percentage> > 0, we classify the object as an open container.
The ground truths are saved in a similar format:
  ```
  container/noncontainer 0 1 2 3
  ```
They are obtained from human annotation. 
The "0 1 2 3" does not have any meaning in specific.

## Related Work
These are the related papers on the robot imagination project our group is working on. Please take a look!

* Is That a Chair? Imagining Affordances Using Simulations of an Articulated Human Body [[arxiv](https://arxiv.org/abs/1909.07572)] [[project page](https://chirikjianlab.github.io/chairimagination/)]

For more information about our group, please visit our website at: [https://chirikjianlab.github.io/](https://chirikjianlab.github.io/)

# TODO
- [ ] python 3 version
