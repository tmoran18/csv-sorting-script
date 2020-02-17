import pathlib
import os
import glob
import pandas as pd

path = r"C:\Users\Mandalorian\Desktop\python\sorted"
CSVfilesInDirectory = list(pathlib.Path(path).glob('*.csv'))


def showCsvFilesInDirectory():
    for index, filename in enumerate(CSVfilesInDirectory):
        print(f"{index} - {os.path.basename(filename)}")


def showColsOfCSVFile(dataframe):
    for index, col in enumerate(dataframe.columns):
        print(f"{index+1} - {col}")


def write_CSV(sortedDataframe, sortedDataframeFileName):
    sortedFileName = os.path.basename(sortedDataframeFileName)
    sortedDataframe.to_csv('Sorted_' + sortedFileName)


print('Enter a number to choose a .csv file to sort')
showCsvFilesInDirectory()
CSVFileChoice = int(input())
print("---------------\n")
dataframe = pd.read_csv(CSVfilesInDirectory[CSVFileChoice])
print('Choose a column to sort')
showColsOfCSVFile(dataframe)
CSVColChoice = int(input())
dataframe.sort_values(
    dataframe.columns[CSVColChoice], ascending=True)
write_CSV(dataframe, CSVfilesInDirectory[CSVFileChoice])

# name = str(input())
# print('Thank you ' + name)

# print('Please choose a CSV File to sort')


# os.chdir(path)
# for file in glob.glob("*.csv"):
#     print(file)
# def showCsvFilesInDirectory():
#     path = r"C:\Users\Mandalorian\Desktop\python\sorted"
#     CSVfiles = list(pathlib.Path(path).glob('*.csv'))
#     for(i, fileName) in enumerate(CSVfiles):
#         (f"{i+1} - {os.path.basename(fileName)}")
