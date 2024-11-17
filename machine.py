import streamlit as st
import time

def initialize_session_state():
    if 'low' not in st.session_state:
        st.session_state.low = 1
    if 'high' not in st.session_state:
        st.session_state.high = 100
    if 'guess_count' not in st.session_state:
        st.session_state.guess_count = 0
    if 'game_active' not in st.session_state:
        st.session_state.game_active = True
    if 'computer_guess' not in st.session_state:
        st.session_state.computer_guess = 50

def reset_game():
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess_count = 0
    st.session_state.game_active = True
    st.session_state.computer_guess = 50

def calculate_progress(low, high):
    # Calculate progress as a percentage of the reduced search space
    total_range = 100 - 1  # Initial range
    current_range = high - low
    progress = (total_range - current_range) / total_range
    # Ensure progress stays between 0 and 1
    return max(0.0, min(1.0, progress))

def main():
    st.title("🤖 Computer Number Guessing Game")
    st.write("""
    Think of a number between 1 and 100, and I'll try to guess it!
    Use the buttons below to tell me if my guess is too high, too low, or correct.
    """)
    
    initialize_session_state()
    
    if st.session_state.game_active:
        st.write(f"### Attempt #{st.session_state.guess_count + 1}")
        st.write(f"## Is your number {st.session_state.computer_guess}?")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("Too Low ⬆️"):
                st.session_state.low = st.session_state.computer_guess + 1
                st.session_state.guess_count += 1
                st.session_state.computer_guess = (st.session_state.low + st.session_state.high) // 2
                st.rerun()
                
        with col2:
            if st.button("Correct! 🎯"):
                st.session_state.game_active = False
                st.balloons()
                st.rerun()
                
        with col3:
            if st.button("Too High ⬇️"):
                st.session_state.high = st.session_state.computer_guess - 1
                st.session_state.guess_count += 1
                st.session_state.computer_guess = (st.session_state.low + st.session_state.high) // 2
                st.rerun()
        
        # Show the current range being considered
        st.write(f"I'm thinking of numbers between {st.session_state.low} and {st.session_state.high}")
        
        # Add a progress bar with properly clamped values
        progress = calculate_progress(st.session_state.low, st.session_state.high)
        st.progress(progress)
        
    else:
        st.success(f"🎉 I guessed your number ({st.session_state.computer_guess}) in {st.session_state.guess_count + 1} attempts!")
        if st.button("Play Again"):
            reset_game()
            st.rerun()

if __name__ == "__main__":
    main()