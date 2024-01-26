import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.title("ChatGPT Model Pricing Calculator")

# Pricing data
pricing_data = {
    "Model": ["gpt-4-0125-preview", "gpt-4-1106-preview", "gpt-4-1106-vision-preview", "gpt-4", "gpt-4-32k", "gpt-3.5-turbo-1106", "gpt-3.5-turbo-instruct"],
    "Input Price per 1K Tokens": [0.01, 0.01, 0.01, 0.03, 0.06, 0.0010, 0.0015],
    "Output Price per 1K Tokens": [0.03, 0.03, 0.03, 0.06, 0.12, 0.0020, 0.0020]
}
df = pd.DataFrame(pricing_data)

# Display pricing tables
st.subheader("GPT-4 Pricing Details")
st.table(df[df["Model"].str.contains("gpt-4")])

st.subheader("GPT-3 Pricing Details")
st.table(df[df["Model"].str.contains("gpt-3.5")])

# User input for token count
token_count = st.number_input("Enter the number of tokens (in thousands)", min_value=1.0, step=1.0)

# Calculate and display prices for each model based on token count
df["Total Input Cost"] = df["Input Price per 1K Tokens"] * token_count
df["Total Output Cost"] = df["Output Price per 1K Tokens"] * token_count
st.subheader("Cost per Model for Given Token Count")
st.table(df)

# Additional user input for activations per day
activations_per_day = st.number_input("Enter the number of activations per day", min_value=1, step=1)

# Calculating monthly cost
days_in_month = 30  # Assuming an average month
df["Monthly Total Cost"] = (df["Total Input Cost"] + df["Total Output Cost"]) * activations_per_day * days_in_month

# Display monthly cost tables
st.subheader("Monthly Total Cost for GPT-4 Models")
st.table(df[df["Model"].str.contains("gpt-4")][["Model", "Monthly Total Cost"]])

st.subheader("Monthly Total Cost for GPT-3 Models")
st.table(df[df["Model"].str.contains("gpt-3.5")][["Model", "Monthly Total Cost"]])
