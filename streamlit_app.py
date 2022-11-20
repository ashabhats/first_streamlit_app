import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title(' 🍌🍊🥭🍓🍒 Build your own Fruit Smoothie🍑🍏🍐🍎 ' )
streamlit.dataframe(my_fruit_list)
streamlit.title('💖 I Love Eeshan & Pranav 💖' )

streamlit.header('Both are very good boys! 👌')
streamlit.text('Both are bigtime foodies!! 😊')
streamlit.text('E & P !!!')
