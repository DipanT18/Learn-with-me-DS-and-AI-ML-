import streamlit as st
import requests

# Replace with your actual API key
API_KEY = "YOUR_API_KEY"

def get_exchange_rates(base_currency):
    """Fetches exchange rates from the API."""
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["rates"]
        else:
            st.error(f"Error fetching exchange rates: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Network error: {e}")
        return None

def currency_converter_app():
    """Defines the Streamlit app layout."""
    st.title("Currency Converter")

    # Fetch rates with a default base currency to populate the dropdown
    default_base = "USD"
    rates = get_exchange_rates(default_base)

    if rates:
        currencies = sorted(rates.keys())

        # Create columns for the input fields
        col1, col2 = st.columns(2)

        with col1:
            amount = st.number_input("Amount", min_value=0.01, step=0.01, value=1.0)
            from_currency = st.selectbox("From", currencies, index=currencies.index(default_base))

        with col2:
            to_currency = st.selectbox("To", currencies, index=currencies.index("EUR"))

        if st.button("Convert"):
            # Fetch the specific conversion rate
            all_rates = get_exchange_rates(from_currency)
            if all_rates and to_currency in all_rates:
                conversion_rate = all_rates[to_currency]
                converted_amount = amount * conversion_rate
                st.success(f"{amount} {from_currency} = {converted_amount:,.2f} {to_currency}")
            else:
                st.warning("Could not find the conversion rate.")

if __name__ == "__main__":
    currency_converter_app()


