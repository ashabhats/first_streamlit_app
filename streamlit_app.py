import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title(' 🍌🍊🥭🍓🍒 Build your own Fruit Smoothie🍑🍏🍐🍎 ' )
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.title('💖 I Love Eeshan & Pranav 💖' )
streamlit.header('Both are very good boys! 👌')
streamlit.text('Both are bigtime foodies!! 😊')
streamlit.text('E & P !!!')

def get_fruit_data(fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please enter the fruit name.")
  else:
    get_data = get_fruit_data(fruit_choice)
    streamlit.dataframe(get_data)
except URLError as e:
  streamlit.error()
  
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 

# write your own comment - what does this do?

#streamlit.stop()

streamlit.header("Fruit List contains")
def get_fruit_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
    return my_cur.fetchall()

if streamlit.button('Get fruit list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_list()
  streamlit.dataframe(my_data_rows)


# add new fruit
def insert_row(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
      return('Thanks fro adding '+new_fruit)
    
my_choice = streamlit.text_input('Which fruit would you like to add?')   
    
if streamlit.button('Add Fruit of your choice'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  added_fruit = insert_row(my_choice)
  streamlit.text(added_fruit)
  
#
#streamlit.write('The user added ', my_choice)

#
