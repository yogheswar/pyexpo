import streamlit as st
import random

# Initialize session state variables
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

st.title("Guess the Number Game")

st.write("I'm thinking of a number between 1 and 100.")
st.write("Can you guess what it is?")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
button_clicked = st.button("Submit Guess")

if button_clicked:
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.write("Too low! Try again.")
    elif guess > st.session_state.number:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0

# Run the Streamlit app
# To run the app, use the command: streamlit run guessing_game.pystreamlit run guessing_game.py