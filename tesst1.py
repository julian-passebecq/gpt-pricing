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

# User input for token counts
input_token_count = st.number_input("Enter the number of input tokens (in thousands)", min_value=0.1, step=0.1, key="input_tokens")
output_token_count = st.number_input("Enter the number of output tokens (in thousands)", min_value=0.1, step=0.1, key="output_tokens")

# Multiselect for models
selected_models = st.multiselect("Select models to display costs", df["Model"].tolist(), default=df["Model"].tolist())

# Filter dataframe based on selected models
filtered_df = df[df["Model"].isin(selected_models)]

# Calculate and display prices for each selected model based on token count
filtered_df["Total Input Cost"] = filtered_df["Input Price per 1K Tokens"] * input_token_count
filtered_df["Total Output Cost"] = filtered_df["Output Price per 1K Tokens"] * output_token_count
st.subheader("Cost per Selected Model for Given Token Count")
st.table(filtered_df)

# Additional user input for activations per day
activations_per_day = st.number_input("Enter the number of activations per day", min_value=1, step=1)

# Calculating monthly cost
days_in_month = 30  # Assuming an average month
filtered_df["Monthly Total Cost"] = (filtered_df["Total Input Cost"] + filtered_df["Total Output Cost"]) * activations_per_day * days_in_month

# Display monthly cost table for selected models
st.subheader("Monthly Total Cost for Selected Models")
st.table(filtered_df[["Model", "Monthly Total Cost"]])
