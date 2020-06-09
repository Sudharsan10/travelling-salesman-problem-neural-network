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
TilePuzzleSolver/
├── controller/
|   ├── __init__.py
|   └── gui_controller.py   
├── data/
|   ├── __init__.py
|   └── ui_data.py 
├── docs/ ...
├── img/ ...
├── solver/
|   ├── __init__.py
|   ├── test_tile_puzzle_solver.py 
|   └── tile_puzzle_solver.py
├── ui/
|   ├── __init__.py  
|   ├── gui.py
|   └── TilePuzzleSolverGUI.ui
├── Readme.md
├── styles.css
└── setup.py
```


## Pre-requisites
This app depends on ```numpy``` and ```PyQt5``` libraries. We can setup this up using pip installer or conda virtual environment tool.

- setting up using pip installer
    > ```shell script
    > pip install numpy
    >```
    
    > ```shell script
    > pip install PyQt5 
    Note: If you have both python2 and python3 installed replace ```pip``` with ```pip3``` when using python3. In case you need to install
    ```pip``` follow this [link](#https://pip.pypa.io/en/stable/installing/) to get ```pip``` setup before running the above commands.
    
- setting up using conda environment for ```python3```     
    > ```shell script
    > conda install -c anaconda numpy
    >```
    
    > ```shell script
    > conda install -c anaconda pyqt
    > ```
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

If every requirement is fulfilled a window should open as follow,

<p align="center;">
    <a href="https://github.com/Sudharsan10/travelling-salesman-problem-neural-network">
    <img src=".\img\ui\start_screen.png" width="100%" alt="start-screen">
    </a>
</p>


## Documentation
### Contents:
1. [How to use](#howtouse)
2. [Architecture](#architecture)
3. [Solver.py](#solver_py)
4. [Node obj Data structure](#node)
    
### 1 How to use <a id ='howtouse'></a>
Navigate to the project folder containing setup.py and run it. If using command line to run it, you can follow the command given below,
```shell script
python  setup.py
```
Enter the initial state of the puzzle and goal state of the puzzle as shown in the fig below.

Now you have three actions to perform in the form of three different button in the options section in the right side of the app.
They are,
1. [Find solution](#find-solution)
2. [Is solvable?](#is-solvable)
3. [Reset](#reset)

##### 1.2.1 Is solvable? <a id ='is-solvable'></a>
If you wish only to check for the solution feasibility for given state then you can use this button just to check the solution feasibility.

##### 1.2.2 Find solution <a id ='find-solution'></a>
This button triggers the autoSolve() function, which in checks for the solution feasibility if solution is feasible then 
it calls the method solve() from the TilePuzzleSolver class, upon completion of solve() method, backtrack() method is called.
Which returns the solution to the given puzzle states as a list of numpy array. This can be seen well in the flowchart below.

##### 1.2.3 Reset <a id ='reset'></a>
This button resets all the fields in the GUI by triggering the ClearAll() method.

If the Find Solution action is performed and upon success, a new button simulation will be visible in the options section 
and simulation section also becomes visible with four more action buttons and a simulation output area.

**Auto/Manual toggle Button:** Toggles visibility between start, stop button with manual navigation buttons - next, previous.

**Start/Pause buttons:** Starts and stops the simulation sates

**Next/Previous buttons:** use it to manually switch to the next/previous state in solution

**Reset button:** it reset the simulation output and toggles back to start/pause button.

<p align="center">
    <img src=".\img\htu01.png" width="100%" alt="how-to-use-01">
    .
    <img src=".\img\htu02.png" width="100%" alt="how-to-use-02">
    .
    <img src=".\img\htu03.png" width="100%" alt="how-to-use-03">
    .
    <img src=".\img\htu04.png" width="100%" alt="how-to-use-04">
    .
    <img src=".\img\htu05.png" width="100%" alt="how-to-use-05">
  </a>  
</p>

### 2 Architecture<a id='architecture'></a>
<img src=".\img\architecture.png" width="100%" />

### 3 solver.py<a id='sovler'></a>
<img src=".\img\solver.png" width="100%" />

### 4 Node obj Data Structure<a id='node'></a>
<img src=".\img\node.png" width="100%" />


## Bugs and feature requests
Have a bug or a feature request? Search for existing and closed issues, if your problem or idea is not addressed yet, 
[please open a new issue](https://github.com/Sudharsan10/travelling-salesman-problem-neural-network/issues/new).

## Creators
**@Sudharsan** : <https://www.iamsudharsan.com>

<p align='center'>
    <a id='thanks'></a>
    Thank you for visiting our Repo!
</p>