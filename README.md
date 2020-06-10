<p align="center">
  <a href="https://github.com/Sudharsan10/travelling-salesman-problem-neural-network">
    <img src=".\img\project_social_card01.png" alt="Social-header">
  </a>  
</p>

<p align="center">
  A solution to travelling salesman problem using 1D self-organizing maps.  
  <br>
    <a href=""><strong>Explore the docs »</strong></a>
    <br>
    <br>
    <a href="https://github.com/Sudharsan10/travelling-salesman-problem-neural-network/issues/new">Report bug</a>
    ·
    <a href="https://github.com/Sudharsan10/travelling-salesman-problem-neural-network/issues/new">Request feature</a>    
</p>

In this project we will try to solve a traveling salesman problem using unsupervised learning 
technique - self organizing maps (SOM).

## Table of contents
- [Quick start](#quick-start)
- [Pre-Requisites](#pre-requisites)
- [Run instructions](#run-instructions)
- [Status](#status)
- [What's included](#whats-included)
- [Documentation](#documentation)
- [Bugs and Feature requests](#bugs-and-feature-requests)
- [Creators](#creators)
- [Thanks](#thanks)

## Quick start
There are two ways to run this app: 
- [Download the latest Docker container.]() and run from the app in that container ( Note: No Docker container is available 
at the moment)
- Clone the repo: 
    > ```shell script
    > git clone https://github.com/Sudharsan10/travelling-salesman-problem-neural-network.git
    > ```
    
## Status
[![Documentation Status](https://img.shields.io/badge/Documentation-yes-e01563)](https://github.com/Sudharsan10/travelling-salesman-problem-neural-network/tree/master/img/logo)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-e01563.svg)](https://github.com/Sudharsan10/travelling-salesman-problem-neural-network/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Python%20Version-3.8.3-brightgreen)](https://www.python.org/)
[![pip-version](https://img.shields.io/badge/pip%20Version-20.0.2-brightgreen)](https://pip.pypa.io/en/stable/installing/)
[![pyqt-version](https://img.shields.io/badge/pandas%20Version-5.14.2-brightgreen)](https://pypi.org/project/PyQt5/)
[![numpy-version](https://img.shields.io/badge/numpy%20Version-1.18.1-brightgreen)](https://pypi.org/project/numpy/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-0366d6.svg)](http://commonmark.org)
[![contributors](https://img.shields.io/badge/Contributors-01-0366d6)](https://github.com/Sudharsan10/travelling-salesman-problem-neural-network/graphs/contributors)
[![Logo](https://img.shields.io/badge/Logo-Adobe%20Photoshop-20639B.svg)](https://github.com/Sudharsan10/travelling-salesman-problem-neural-network/graphs/commit-activity)
[![Flow-charts](https://img.shields.io/badge/Flowcharts-MS%20Power%20Point-20639B.svg)](https://github.com/Sudharsan10/travelling-salesman-problem-neural-network/graphs/commit-activity)


## What's included
Within the download you'll find the following directories and files, logically grouping the modules in its own packages. 
You'll see something like this:

```text
(root folder)/
├── docs/  
├── img/
├── models/ 
|   └── weights/
├── notebooks/ ...
├── src/
|   ├── handler/
|   |   ├── __init__.py
|   |   └── utility.py
|   ├── som/ 
|   |   ├── __init__.py
|   |   ├── som.py
|   |   └── som_1d.py
|   └── main.py
├── Readme.md
└── setup.py
```


## Pre-requisites
This app depends on ```numpy```, ```matplotlib```, ```OpenCV``` and ```pandas``` libraries. We can setup this up using pip installer or conda virtual environment tool.

- setting up using pip installer
    > ```shell script
    > pip install numpy
    >```
    
    > ```shell script
    > pip install pandas 
    > ```
    
    > ```shell script
    > pip install matplotlib 
    > ```
    Note: If you have both python2 and python3 installed replace ```pip``` with ```pip3``` when using python3. In case you need to install
    ```pip``` follow this [link](#https://pip.pypa.io/en/stable/installing/) to get ```pip``` setup before running the above commands.
    
- setting up using conda environment for ```python3```     
    > ```shell script
    > conda install -c anaconda numpy matplotlib pandas Opencv
    >```
    Note: To install and setup anaconda environment follow this [link](#https://docs.anaconda.com/anaconda/install/) first and visit this section again after successfully setting up the conda environment.

## Run instructions
To run the app, first finish the pre-requisites mentioned, then
1. Clone the repo in terminal using following command: 
    > ```shell script
    > git clone https://github.com/Sudharsan10/travelling-salesman-problem-neural-network.git
    > ```
    or download github repo as ```.zip``` and extract it in the desired location.
    
2. In terminal navigate to the root folder abd locate the ```setup.py``` file and run the following command:
    > ```shell script
    > python setup.py
    > ```

If every requirement is fulfilled a Pyplot window should open with the dotted line showing the solution for the Travelling 
salesman problem, example

<p align="center;">
    <a href="https://github.com/Sudharsan10/travelling-salesman-problem-neural-network">
    <img src=".\img\solution.png" width="100%" alt="start-screen">
    </a>
</p>


## Documentation
### Contents:
1. [Introduction](#howtouse)
2. [Architecture](#architecture)
3. [SOM Class Methods](#som)
4. [SOM_1D Class Methods](#som1d)
5. [Utility.py](#utility_py)
6. [Notebooks](#notebooks)
    
### 1 Introduction <a id ='howtouse'></a>


### 2 Architecture<a id='architecture'></a>
<img src=".\img\architecture.png" width="100%" />

### 3 SOM Class methods<a id='som'></a>

### 4 SOM 1D Class methods<a id='som1d'></a>

### 4 Utility.py<a id='utility_py'></a>

### 4 Notebooks<a id='notebooks'></a>
<img src=".\img\node.png" width="100%" />


## Bugs and feature requests
Have a bug or a feature request? Search for existing and closed issues, if your problem or idea is not addressed yet, 
[please open a new issue](https://github.com/Sudharsan10/travelling-salesman-problem-neural-network/issues/new).

## Creators
**@Sudharsan** : [www.iamsudharsan.com](https://www.iamsudharsan.com)

<p align='center'>
    <a id='thanks'></a>
    Thank you for visiting our Repo!
</p>