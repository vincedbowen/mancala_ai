import streamlit as st
from simulations import ai_simulate as ai


def main():
    st.title("AI vs Random")
    num_sims = st.slider('Select how many simulations to run...', 1, 100, 50)
    ai.simulate_mancala_ai(num_sims)


if __name__ == "__main__":
    main()
