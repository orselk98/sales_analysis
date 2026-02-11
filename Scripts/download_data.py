import kagglehub
from pathlib import Path
import shutil


path = kagglehub.dataset_download("uzmaakhtar/ecommerce-sales-data")
print("Path to dataset files:", path)

# Move the downloaded files to a specific directory
source=Path(path)
file_path =source / "ecommerce_sales_data.csv"
shutil.copy(file_path, "Data/raw")