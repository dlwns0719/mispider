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
 
## Usage

Given a two target and source RNA sequece, obtain each sgRNA target sequence and one or two mismatchs via csv files.

 
    ```
    enzymatic_protospacers(
        '~/scaffolds_directory/',
        'chr6:136640001-136680000',
        'mm8.fasta'
        )
    ```
