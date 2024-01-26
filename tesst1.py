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

# User input for model selection
model = st.selectbox("Choose a ChatGPT Model", df["Model"])

# User input for token count
token_count = st.number_input("Enter the number of tokens (in thousands)", min_value=1.0, step=1.0)

# Calculation
selected_model_data = df[df["Model"] == model].iloc[0]
total_cost = (selected_model_data["Input Price per 1K Tokens"] + selected_model_data["Output Price per 1K Tokens"]) * token_count

# Display result
st.write(f"The total cost for using {model} with {token_count}K tokens is: ${total_cost:.2f}")
