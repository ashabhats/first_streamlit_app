import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title(' 🍌🍊🥭🍓🍒 Build your own Fruit Smoothie🍑🍏🍐🍎 ' )
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)


streamlit.title('💖 I Love Eeshan & Pranav 💖' )

streamlit.header('Both are very good boys! 👌')
streamlit.text('Both are bigtime foodies!! 😊')
streamlit.text('E & P !!!')
