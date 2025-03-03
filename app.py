import streamlit as st
import time

def length_converter(value, from_unit, to_unit):
    length_units = {
        "km": 1000, "m": 1, "cm": 0.01, "mm": 0.001,
        "mile": 1609.34, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254,
        "nanometer": 1e-9, "light-year": 9.461e+15
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "kg": 1, "g": 0.001, "mg": 1e-6, "pound": 0.453592,
        "ounce": 0.0283495, "ton": 1000
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    return value

def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🌍")
    
    st.markdown(
        """
        <style>
        .globe {
            font-size: 50px;
            display: inline-block;
            transition: transform 0.5s ease-in-out;
        }
        .globe:hover {
            transform: rotate(360deg);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px;
        }
        .stSelectbox>div>div>select {
            background-color: #f0f0f5;
            font-size: 16px;
            padding: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h1 style='text-align: center;'>🌍 <span class='globe'>🔄</span> Unit Converter</h1>", unsafe_allow_html=True)
    
    category = st.selectbox("Select Conversion Category:", ["Length", "Weight", "Temperature"])
    
    if category == "Length":
        units = ["km", "m", "cm", "mm", "mile", "yard", "foot", "inch", "nanometer", "light-year"]
        converter = length_converter
    elif category == "Weight":
        units = ["kg", "g", "mg", "pound", "ounce", "ton"]
        converter = weight_converter
    else:
        units = ["Celsius", "Fahrenheit", "Kelvin"]
        converter = temperature_converter
    
    from_unit = st.selectbox("From Unit:", units)
    to_unit = st.selectbox("To Unit:", units)
    value = st.number_input("Enter Value:", min_value=0.0, step=0.01)
    
    if st.button("Convert"):
        with st.spinner("Converting..."):
            time.sleep(1)
            result = converter(value, from_unit, to_unit)
            st.success(f"✅ {value} {from_unit} = {result:.6f} {to_unit}")
    
    st.markdown("""
        <hr>
        <p style='text-align: center;'>🚀 From <b>Muhammad Umar</b> with ❤️</p>
        """, unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
