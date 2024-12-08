import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset(file_path):
    """
    Load a dataset from the given file path.
    Supports CSV files for simplicity.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV file.")

def analyze_dataset(df):
    """
    Perform basic analysis on the dataset.
    """
    print("----- Dataset Summary -----")
    print(df.info())  # Dataset structure and non-null counts
    print("\n----- First 5 Rows of the Dataset -----")
    print(df.head())  # Preview of the dataset
    
    print("\n----- Summary Statistics -----")
    print(df.describe())  # Numeric column statistics
    
    print("\n----- Missing Values -----")
    print(df.isnull().sum())  # Missing values per column
    
    print("\n----- Column Data Types -----")
    print(df.dtypes)

def visualize_dataset(df):
    """
    Generate visualizations for the dataset.
    """
    # Numeric column distributions
    numeric_columns = df.select_dtypes(include='number')
    if not numeric_columns.empty:
        numeric_columns.hist(figsize=(10, 8), bins=20)
        plt.suptitle("Numeric Column Distributions")
        plt.show()

    # Correlation heatmap for numeric data
    if len(numeric_columns.columns) > 1:
        plt.figure(figsize=(10, 6))
        sns.heatmap(numeric_columns.corr(), annot=True, fmt='.2f', cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()

    # Count plots for categorical columns
    categorical_columns = df.select_dtypes(include='object')
    for column in categorical_columns.columns:
        plt.figure(figsize=(8, 4))
        sns.countplot(data=df, x=column)
        plt.title(f"Count Plot for {column}")
        plt.xticks(rotation=45)
        plt.show()

if __name__ == "__main__":
    print("C://Users//Hasan//Desktop//my-project//benin-malanville.cs\n")
    file_path = input("C://Users//Hasan//Desktop//my-project//benin-malanville.csv ")
    
    try:
        # Load the dataset
        dataset = load_dataset(file_path)
        
        # Analyze the dataset
        analyze_dataset(dataset)
        
        # Visualize the dataset
        visualize_dataset(dataset)
    except Exception as e:
        print(f"An error occurred: {e}")
