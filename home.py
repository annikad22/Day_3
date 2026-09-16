import streamlit as st
st.header("Day 3")

if "Bubble1" not in st.session_state:
    st.session_state.bubble1 = False

if "Bubble2" not in st.session_state:
    st.session_state.bubble2 = False

if "Bubble3" not in st.session_state:
    st.session_state.bubble3 = False

if st.session_state.bubble1 is False and st.session_state.bubble2 is False and st.session_state.bubble3 is False:
    st.write("All bubbles are False")

if st.session_state.bubble1 is False and st.session_state.bubble2 is False and st.session_state.bubble3 is False:
    st.write("Only bubble 3 is True")

if st.session_state.bubble1 is False:
    st.write("Bubble1 is False")
    if st.session_state.bubble2 is False:
        st.write("And bubble2 is False")
    else:
        st.write("Bubble 3 is True")
        