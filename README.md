## Description 

This repository contains the project of the Ceng489 INTRO.TO COMP.SECURITY class of METU.

The aim is to train different ML models on a provided network traffic dump dataset to measure their performances and report them. 
The dataset consists of 10 feature columns and a label for classification. 
End aim is to have a ML based solution for network intrusion detection system.

## Usage

1. Place `snd_dataset` under `sdn` folder.
2. Setup python 3.7 and install `requirements.txt` by
```
pip install -r requirements.txt
```
3. To execute, simply run
```
python python driver.py 
```
to run the driver program. Driver will load the data and train the selected ML model with the data. 
It will then report the performance of the ML model.

Model selection can be done from `driver.py`
