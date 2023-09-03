import streamlit as st
import pandas as pd
import pickle

# Load model
with open('./model/rf_tuned.pkl', 'rb') as file_1:
    model_load = pickle.load(file_1)

# Define the Streamlit app
def main():
    st.title("Car Information Input")

    # Input fields for additional car information
    car_brand_options = ['TOYOTA', 'HONDA', 'SUZUKI', 'DAIHATSU', 'NISSAN', 'MITSUBISHI', 'ISUZU']
    car_brand = st.selectbox("Car Brand", car_brand_options)
    car_type = st.text_input("Car Type")
    car_color = st.text_input("Car Color")
    car_transmission = st.selectbox("Car Transmission", ["AT", "MT"])
    inspection_score = st.number_input("Inspection Score", min_value=0, max_value=100)

    # Input fields for buy and sell dates
    buy_date = st.date_input("Buy Date")
    sell_date = st.date_input("Sell Date")

    st.header("Car Details")

    col1, col2 = st.columns(2)

    # Input fields in the first column
    with col1:
        car_year = st.number_input("Car Year", min_value=1900, max_value=9999, value=2013)
        car_engine_size = st.number_input("Car Engine Size", min_value=0.0, value=1.3)

    # Input fields in the second column
    with col2:
        buy_price = st.number_input("Buy Price", min_value=0.0, value=13750.0)
        admin_fee = st.number_input("Admin Fee", min_value=0.0, value=250.0)
        aging_fee = st.number_input("Aging Fee", min_value=0.0, value=438.0)

    # Calculate date_diff based on buy_date and sell_date
    date_diff = (sell_date - buy_date).days

    # Create a DataFrame from the input data
    df_inf = pd.DataFrame({
        'car_brand': [car_brand],
        'car_type': [car_type],
        'car_color': [car_color],
        'car_transmission': [car_transmission],
        'inspection_score': [inspection_score],
        'car_year': [car_year],
        'car_engine_size': [car_engine_size],
        'buy_price': [buy_price],
        'admin_fee': [admin_fee],
        'aging_fee': [aging_fee],
        'buy_date': [buy_date],
        'sell_date': [sell_date],
        'date_diff': [date_diff]
    })

    # Display the input data
    st.header("Input Data")
    st.write(df_inf)

    submit = st.button("Predict")

    if submit:
        predict_inf = model_load.predict(df_inf)
        target_price_inf = df_inf['buy_price'] + df_inf['admin_fee'] + df_inf['aging_fee']

        price_diff_inf = round(((target_price_inf[0] - predict_inf[0]) / target_price_inf[0]) * 100, 2)

        if price_diff_inf > 10:
            car_label = "<span style='color:red;'>Poor Quality Buy</span>"
            reasons = "**Difference between predicted and target sale price is more than 10%**"
        else:
            car_label = "<span style='color:green;'>Worth To Buy</span>"
            reasons = "**Difference between predicted and target sale price is below 10%**"

        st.header("Car Quality Buy Prediction")
        st.write("Car Target Price    : **{:.2f}**".format(target_price_inf[0]))
        st.write("Car Predicted Price : **{:.2f}**".format(predict_inf[0]))
        st.write("Price Diff Percentage : **{:.2f}%**".format(price_diff_inf))
        st.markdown(f"<b>Car Label: {car_label}</b>", unsafe_allow_html=True)
        st.write(reasons)

if __name__ == "__main__":
    main()
