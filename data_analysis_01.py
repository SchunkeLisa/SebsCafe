# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pandas.io import json
import pandas as pd

def read_data():
   # read emp.json file in directory data01
    employe_data = pd.read_json('data01/emp.json')
   #convert json to csv
    employe_data.to_csv('data01/emp.csv', index=False)
    print(employe_data)
   #read survey.csv file
    survey_data = pd.read_csv('data01/survey.csv')
    print(survey_data)

   #combine



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
