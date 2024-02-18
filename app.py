import streamlit as st
import simulate

def main():
    st.title("Random vs Random")
    num_sims = st.slider('Select how many simulations to run...', 1, 100, 50)
    simulate.simulate_mancala(num_sims)


if __name__ == "__main__":
    main()
