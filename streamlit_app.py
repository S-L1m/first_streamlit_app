import streamlit
import pandas as pd
import requests

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 & Bluebery Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg") 
streamlit.text("🥑🍞 Avocado Toast") 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit") 

# Let's put a pick lish here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show) 

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
streamlit.header("Fruityvice Fruit Advice!") 

# Normalize the json request
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# Output as a dataframe
streamlit.dataframe(fruityvice_normalized)
