# Import necessary libraries
import streamlit as st 
import pandas as pd 
import seaborn as sns 



# Title and Subheader
st.title("Data Analysis")
st.subheader("Data Analysis using Python & Streamlit")


# Upload Dataset
upload = st.file_uploader("Upload your dataset (in .csv format)")
if upload is not None:
    data = pd.read_csv(upload)
        
        
# Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            
            
# Check Datatype of each column
if upload is not None:
    if st.checkbox("DataType of each column"):
        st.text("DataTypes")
        st.write(data.dtypes)
        



# Find shape of dataset
if upload is not None:
    data_shape = st.radio("What dimension do you want to check?", ('Rows', 'Columns'))
    
    if data_shape == 'Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])
        
# find null values
if upload is not None:
    test= data.isnull().values.any()
    if test == True:
        if st.checkbox("Null values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulation!!! No Missing Values")
    

# Find duplicate values
if upload is not None:
    test = data.duplicated().any()
    if test==True:
        st.warning("This dataset contains some Duplicate Values")
        dup=st.selectbox("do you want to remove Duplicate Values?", \
            ("Select One", "Yes", "No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup == "No":
            st.text("Ok No Problem")



# Overall Statistics
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe(include='all'))
    

# About section

if st.button("About App"):
    st.text("Build with Streamlit")
    st.text("Thanks to Streamlit")
    

# By
if st.checkbox("By"):
    st.success("Aastha Kumari")


    


