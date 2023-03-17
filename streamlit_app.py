import streamlit as st
import os
import urllib.request

# Set page title
st.set_page_config(page_title="Arizona Small Business Resources", page_icon=":guardsman:")

# URL of the Arizona flag image
url = "https://upload.wikimedia.org/wikipedia/commons/9/9d/Flag_of_Arizona.svg"

# Path to save the image
filename = "arizona_flag.svg"

# Download and save the image
urllib.request.urlretrieve(url, filename)

# Set up background
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url("{os.getcwd()}/{filename}")
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Define the page options in the drop-down box
nav_selection = st.sidebar.selectbox("Select a page:", ["Home", "Financial Assistance", "Legal Assistance", "Marketing and Advertising"])

# Set up home page
if nav_selection == "Home":
    st.title("Welcome to Arizona Small Business Resources")
    st.write("Please select a page from the drop-down box to learn about available resources for small businesses in Arizona.")

# set up financial assistance page
if nav_selection == "Financial Assistance":
    st.title("Financial Assistance for Small Businesses in Arizona")
    st.write("- Arizona Community Foundation: [https://www.azfoundation.org/GrantsLoans/LoanPrograms/SmallBusinessReliefFund.aspx](https://www.azfoundation.org/GrantsLoans/LoanPrograms/SmallBusinessReliefFund.aspx)")
    st.write("- Arizona Small Business Association: [https://www.asba.com/page/financialresources](https://www.asba.com/page/financialresources)")
    st.write("- Arizona Commerce Authority: [https://www.azcommerce.com/small-business-assistance/](https://www.azcommerce.com/small-business-assistance/)")

# set up legal assistance page
if nav_selection == "Legal Assistance":
    st.title("Legal Assistance for Small Businesses in Arizona")
    st.write("- Small Business Administration Legal Assistance: [https://www.sba.gov/business-guide/manage-your-business/running-business/finding-and-managing-resources/small-business-legal-assistance](https://www.sba.gov/business-guide/manage-your-business/running-business/finding-and-managing-resources/small-business-legal-assistance)")
    st.write("- Arizona Commerce Authority: [https://www.azcommerce.com/small-business-assistance/legal-assistance/](https://www.azcommerce.com/small-business-assistance/legal-assistance/)")
    st.write("- Arizona Small Business Development Center: [https://www.azsbdc.net/legal.html](https://www.azsbdc.net/legal.html)")

# set up marketing and advertising page
if nav_selection == "Marketing and Advertising":
    st.title("Marketing and Advertising for Small Businesses in Arizona")
    st.write("- Arizona Small Business Association: [https://www.asba.com/page/marketingresources](https://www.asba.com/page/marketingresources)")
    st.write("- Arizona Commerce Authority: [https://www.azcommerce.com/small-business-assistance/marketing/](https://www.azcommerce.com/small-business-assistance/marketing/)")

