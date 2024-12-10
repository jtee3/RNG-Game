import random
import streamlit as st

"""
Hello, My name is Jaytee Okonkwo and this is my Random Number Generator Guessing Game"
"""
# Initialization for session state
if "correct_number" not in st.session_state:
    st.session_state.correct_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.feedback = ""


def inspect_user_guess():
    """
    function for checking the user input for a guess and its validity
    """
    if not st.session_state.user_guess.isdigit():
        st.session_state.feedback = "Please enter a valid numerical number from 1 to 100!"
        return

    guess = int(st.session_state.user_guess)
    st.session_state.attempts += 1

    if guess < st.session_state.correct_number:
        st.session_state.feedback = "Hmm that was too low. Try guessing again."
    elif guess > st.session_state.correct_number:
        st.session_state.feedback = "Hmm that was too high. Try guessing again."
    else:
        st.session_state.feedback = f"That's Correct! It took you {st.session_state.attempts} attempts."


def reset_game():
    """
    resets the game
    """
    st.session_state.correct_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.feedback = ""
    st.session_state.user_guess = ""

# Streamlit user interface
st.title("Number Guessing Game")
st.write("Guess the number I'm thinking of between 1 and 100!")

# Inputs and buttons for submitting ang guessing
user_guess = st.text_input(
    "Enter your guess:", key="user_guess", on_change=inspect_user_guess
)

st.button("Reset Game", on_click=reset_game)

# Feedback display
if st.session_state.feedback:
    st.write(st.session_state.feedback)
