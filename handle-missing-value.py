import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title for the app
st.title("Dataset Analysis with Missing Value Handling")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Display basic dataset information
    st.subheader("Dataset Overview")
    st.write("**Shape of the dataset:**", df.shape)
    st.write("**First 5 rows:**")
    st.dataframe(df.head())

    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Show missing values
    st.subheader("Missing Values")
    missing_values = df.isnull().sum()
    st.write(missing_values)

    # Missing Value Handling Options
    st.subheader("Handle Missing Values")
    missing_columns = df.columns[df.isnull().any()].tolist()

    if missing_columns:
        st.write("Columns with missing values:", missing_columns)

        fill_option = st.selectbox(
            "How would you like to handle missing values?",
            ("Do nothing", "Fill with mean", "Fill with median", "Fill with mode", "Drop rows with missing values", "Drop columns with missing values"),
        )

        if fill_option == "Fill with mean":
            for col in missing_columns:
                if df[col].dtype in ["float64", "int64"]:
                    df[col].fillna(df[col].mean(), inplace=True)
            st.write("Filled numeric columns with mean values.")

        elif fill_option == "Fill with median":
            for col in missing_columns:
                if df[col].dtype in ["float64", "int64"]:
                    df[col].fillna(df[col].median(), inplace=True)
            st.write("Filled numeric columns with median values.")

        elif fill_option == "Fill with mode":
            for col in missing_columns:
                df[col].fillna(df[col].mode()[0], inplace=True)
            st.write("Filled columns with mode values.")

        elif fill_option == "Drop rows with missing values":
            df.dropna(inplace=True)
            st.write("Dropped rows with missing values.")

        elif fill_option == "Drop columns with missing values":
            df.dropna(axis=1, inplace=True)
            st.write("Dropped columns with missing values.")

        st.write("Updated Dataset:")
        st.dataframe(df)
    else:
        st.write("No missing values found.")

    # Visualizations
    st.subheader("Visualizations")

    # Numeric column histograms
    st.write("**Numeric Column Distributions:**")
    numeric_columns = df.select_dtypes(include=["float", "int"]).columns
    if not numeric_columns.empty:
        st.bar_chart(df[numeric_columns].hist(figsize=(10, 8)))
        plt.show()
    else:
        st.write("No numeric columns available for visualization.")

    # Correlation heatmap
    if len(numeric_columns) > 1:
        st.write("**Correlation Heatmap:**")
        fig, ax = plt.subplots()
        sns.heatmap(df[numeric_columns].corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # Categorical column count plots
    categorical_columns = df.select_dtypes(include=["object", "category"]).columns
    for col in categorical_columns:
        st.write(f"**Count Plot for {col}:**")
        fig, ax = plt.subplots()
        sns.countplot(data=df, x=col, ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

else:
    st.write("Please upload a CSV file to start analysis.")

