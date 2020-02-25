import pandas as pd

# read the csv file and asign it to the variable dataset
dataset =pd.read_csv('AllCountries.csv')
#Show the shape  of the dataset, how many rows and columns
print(dataset.shape)
#Prints the datatypes in the dataset
print(dataset.dtypes)
# lets look at the 5 first columns just to get the feeling and understanding of the rest of the info given
print(dataset.head())
# describes statistical summary of the entire dataset
print(dataset.describe())
# select only the specified columns from the dataset in this case is Country and LandArea
# the loc[:,['Country,'LandArea] the firs :, is to jump over the rows, only look at the columns
selected_data =dataset.loc[:,['Country','LandArea']]
# iterate trhough the countries i, by using the itertuples function
for i in selected_data.itertuples():
    # look if in the country i at index 2 , that would be 'LandArea'
    if i[2]>2000:
        print(i)