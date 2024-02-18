import streamlit as st
from simulations import random_simulate


def main():
    st.title("Random vs Random")
    num_sims = st.slider('Select how many simulations to run...', 1, 100, 50)
    random_simulate.simulate_mancala_random(num_sims)


if __name__ == "__main__":
    main()
