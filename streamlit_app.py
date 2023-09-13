import streamlit
import requests

fruityvice_responce = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_responce)

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Manu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
