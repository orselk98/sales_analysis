import pandas as pd

def analyze_data (file_path):
    #Load the CSV into a DataFrame
    df=pd.read_csv(file_path)

    #How big is the dataset?
    print("Shape:", df.shape)
    #shape returns (rows,columns) as a tuple
    #Example :(1000,12) means 1000 trn,12 columns 

    #2 What coulmns do we have?
    print("\nCoumn Names:")
    print(df.columns.tolist())
    #.columns gives the coulumn labels
    #..tolist() converts it to a regular Python list (easier to read)

    #3.What datatype is each column?
    print("\nData Types:")
    print(df.dtypes)
    #This tells ypu if pandas sees a column as numbers (int64,float64),
    #text (object), dates (datetime64), etc.
    #It is important because wrong types cause bugs later 

    #4.Full summary -combines shape, types and null counts 
    print("\nDataset Info:")
    print(df.info())
    #This shows non-null counts -if a column has fever non-null values 
    #than total rows , you have missing data

    #5.Actually look at the data
    print("\nFirst 5 Rows:")
    print(df.head())
    #ALWAYS eyeball your data. Numbers and summaries don't catch 
    #everything - sometimes you spot weird values just by looking 

    #6. Statistical summary of numeric columns 
    print("\nSummary Statistics :")
    print(df.describe())
    #Shows count, mean,std, min, max, percentiles
    #Quick way to spot outliers -if max is 10x the mean, investigate

if __name__ == "__main__":
    analyze_data("Data/raw/ecommerce_sales_data.csv")