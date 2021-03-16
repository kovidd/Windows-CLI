# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:10:56 2021

@author: Kovid
"""

import pandas as pd
from time import time
import sys
import json
import re


def sys_check(input_text):
    print('Platform:',sys.platform)
    if "win" in sys.platform:
        input_string = re.compile("([a-zA-Z]+)")
        input_string = input_string.sub(r'"\1"', input_text)
        input_string = input_string.replace('"null"', 'null')
        input_string = input_string.strip('\'')
    else:
        input_string = input_text        
        
    return input_string


def create_csv(df):
    if 0 in list(df.columns.values):
        df.to_csv('mapped_df.csv', index=False, header=None)  # save csv
    else:
        df.to_csv('mapped_df.csv', index=False)  # save csv
    print('File created')
    

def main():
    # command-line arguments
    input_text = (sys.argv[1:])
    # print('Text from args:', input_text)
    input_text = "".join(input_text)
    # print(input_text)
    input_string = sys_check(input_text)
    # print('String for JSON:', input_string)
    
    data = json.loads(input_string)  # convert string to json
    df = pd.DataFrame(data)  # make a dataframe
    # print(df.head())
    create_csv(df)


if __name__ == "__main__":
    start_main = time()
    main()
    print("Run time:", "{:.2f}".format((time()-start_main)/60), "mins")
