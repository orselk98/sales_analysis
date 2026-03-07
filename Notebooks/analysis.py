import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def inspect_data(df):
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

    print("Years:",df["Order Date"].dt.year.unique())
    print("Date Range:",df["Order Date"].min(),"to",df['Order Date'].max())


def analyze_data(df):
    #Which category makes the most money?
    print(df.groupby('Category')['Sales'].sum())
    #Which category is most profitable?
    print(df.groupby('Category')['Profit'].sum())
    #Which category is more efficient at turning sales into profit?
    print(df.groupby('Category')[['Sales','Profit']].sum())

    category_summary=df.groupby('Category')[['Sales','Profit']].sum()
    category_summary['Margin']=category_summary['Profit']/category_summary['Sales']
    print(category_summary)

    region_summary=df.groupby('Region')[['Sales','Profit']].sum()
    region_summary['Margin']=region_summary['Profit']/region_summary['Sales']
    print(region_summary)

    product_summary=df.groupby('Product Name')[['Sales','Profit']].sum().sort_values(by='Sales', ascending=False)
    print(product_summary.head(10))

    date_summary=df.groupby(df['Order Date'].dt.year)[['Sales']].sum()
    print(date_summary)

    df['Year-Month']=df['Order Date'].dt.to_period('M')
    monthly_summary=df.groupby('Year-Month')[['Sales']].sum()
    print(monthly_summary)

    print("-"*40)
    filter_by_sales=df[df['Sales']>5000]
    print(filter_by_sales.head())
    print(filter_by_sales.shape)

    print("-"*40)

    filter_by_sales_category=df[(df['Sales']>5000) & (df['Category']=='Electronics')]
    print(filter_by_sales_category)
    print(filter_by_sales_category.shape)

    print("-"*40)

    filter_by_north_or_east=df[(df['Region']=='North') | (df['Region']=='West')]
    print(filter_by_north_or_east)
    print(filter_by_north_or_east.shape)

    print("-"*40)

    filter_camera_laptop_tablet=df[df['Product Name'].isin(['Camera','Laptop','Tablet'])]
    print(filter_camera_laptop_tablet.head())
    print(filter_camera_laptop_tablet.shape)
    print("-"*40)
    print(df.head())
    df['Margin Level']=np.where(df['Profit Margin']>0.2,'High','Low')
    print(df['Margin Level'].value_counts())

    print("-"*40)
    #Which categories have the most high-margin transactions? 
    filter_high_margin_trn=df[df['Margin Level']=='High'].groupby('Category').size()
    print(filter_high_margin_trn)
    print("-"*40)
    # What percentage of each category's transactions are high margin?
    total=df.groupby('Category').size()
    high=df[df['Margin Level']=='High'].groupby('Category').size()
    print(high/total)

    df.to_excel("Data/processed/ecommerce_summary.xlsx", sheet_name="Summary", index=True)

    return df


def plot_charts(df):
    df['Year-Month']=df['Order Date'].dt.to_period('M')
    monthly_summary=df.groupby('Year-Month')[['Sales']].sum()
    monthly_summary.plot(kind='line')
    plt.title("Monthly Sales Over Time")
    plt.ylabel("Total Sales")
    plt.xlabel("Month")
    plt.tight_layout()
    plt.savefig('Output/monthly_sales_trend.png')
    plt.show()

    category_sales = df.groupby('Category')['Sales'].sum()
    category_sales.plot(kind='bar', color=['steelblue', 'salmon', 'lightgreen'])
    plt.title("Total Sales by Category")
    plt.ylabel("Total Sales ($)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('Output/category_sales.png')
    plt.show()

    sales_by_region=df.groupby('Region')['Sales'].sum()
    sales_by_region.plot(kind='bar', color=['steelblue', 'salmon', 'lightgreen'])
    plt.title("Total Sales By Region")
    plt.ylabel("Total Sales ($)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('Output/region_sales.png')
    plt.show()

    fig, axes=plt.subplots(nrows=1,ncols=2, figsize=(14,5))

    category_data=df.groupby('Category')[['Sales','Profit']].sum()

    category_data['Sales'].plot(kind='bar',ax=axes[0]) 
    axes[0].set_title("Total Sales by Category")
    axes[0].tick_params(axis='x', rotation=0)

    category_data['Profit'].plot(kind='bar',ax=axes[1])
    axes[1].set_title('Profit by Category')
    axes[1].tick_params(axis='x', rotation=0)

    plt.tight_layout()
    plt.savefig('Output/category_sales_profit.png')
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("Data/raw/ecommerce_sales_data.csv")
    df['Order Date'] = pd.to_datetime(df["Order Date"])
    df['Profit Margin'] = df['Profit']/df['Sales']

    #inspect_data(df)
    #df = analyze_data(df)
    plot_charts(df)