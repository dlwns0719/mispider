# mispider
 *a tool for designing mispider libraries*

 [![Python 3.6 Status](https://img.shields.io/badge/Python-3.6-brightgreen.svg)](https://img.shields.io/badge/Python-3.6-blue.svg)
  
  
## Installation

install biopython (version 1.74)
    
    ```
    pip install biopython
    ```

install pandas (version 0.25.0)
    
    ```
    pip install pandas
    ```


mispyder runs on Python 3.6
 
## Usage (example running code on main.py)

Given a two target and source RNA sequece, obtain each sgRNA target sequence and one or two mismatchs via csv files.

ngg_list_up.py 
    ```
    CCR5 = target RNA sequence (type : string)
    CCR2 = souece RNA sequence (type : string)
    NGG_list_up(CCR5,'CCR5')
    NGG_list_up(CCR2,'CCR2')
    ```

mismatch.py
    '''
    CCR5_ngg_DataFrame = return from ngg_list_up.py (type : pandas DataFrame)
    CCR2_ngg_DataFrame = return from ngg_list_up.py (type : pandas DataFrame)
    mismatch(CCR5_ngg_DataFrame, CCR2_ngg_DataFrame, 'CCR5', 'CCR2')
    '''
