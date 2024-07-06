import streamlit as st
import random
import time

# Define the books and scenes
books = {
    "Alice in Wonderland": [
        {"text": "Alice was beginning to get very _____ of sitting by her sister on the bank.", "blank": "tired"},
        {"text": "So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and _____).", "blank": "stupid"},
        {"text": "Whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the _____", "blank": "daisies"}
    ],
    "Moby Dick": [
        {"text": "Call me _____. Some years ago - never mind how long precisely - having little or no money in my purse.", "blank": "Ishmael"},
        {"text": "I thought I would sail about a little and see the watery part of the _____", "blank": "world"},
        {"text": "There is no folly of the beast of the earth which is not infinitely outdone by the madness of _____", "blank": "men"}
    ],
    "The Adventures of Tom Sawyer": [
        {"text": "Tom appeared on the sidewalk with a bucket of whitewash and a long-handled _____", "blank": "brush"},
        {"text": "He surveyed the fence, and all gladness left him and a deep _____ settled down upon his spirit.", "blank": "melancholy"},
        {"text": "Thirty yards of board fence nine feet _____", "blank": "high"}
    ]
}

# Select a book randomly
selected_book = random.choice(list(books.keys()))
scenes = books[selected_book]
random_scene = random.choice(scenes)

# Session state for game
if 'current_scene' not in st.session_state:
    st.session_state.current_scene = random_scene
    st.session_state.timer = time.time()

def check_answer():
    user_answer = st.session_state.user_answer.lower().strip()
    correct_answer = st.session_state.current_scene['blank'].lower().strip()
    if user_answer == correct_answer:
        st.success("Correct!")
        st.session_state.current_scene = random.choice(books[selected_book])
        st.session_state.timer = time.time()
    else:
        st.error("Incorrect! Try again.")

def skip_scene():
    st.session_state.current_scene = random.choice(books[selected_book])
    st.session_state.timer = time.time()

def pick_random_scene():
    selected_book = random.choice(list(books.keys()))
    st.session_state.current_scene = random.choice(books[selected_book])
    st.session_state.timer = time.time()

def change_book():
    new_book = st.selectbox("Choose a book", options=list(books.keys()))
    st.session_state.current_scene = random.choice(books[new_book])
    st.session_state.timer = time.time()

st.title("Classic Literature Fill-in-the-Blank Game")
st.write(f"Book: {selected_book}")
st.write("Fill in the blank:")

# Display the scene with the blank
scene_text = st.session_state.current_scene['text'].replace("_____", "__________")
st.write(scene_text)

# User input for answer
user_answer = st.text_input("Your answer:", key="user_answer")

# Buttons for submitting and managing the game
st.button("Check Answer", on_click=check_answer)
st.button("Skip Scene", on_click=skip_scene)
st.button("Random Scene", on_click=pick_random_scene)
st.button("Change Book", on_click=change_book)

# Display timer
elapsed_time = time.time() - st.session_state.timer
st.write(f"Time elapsed: {int(elapsed_time)} seconds")
