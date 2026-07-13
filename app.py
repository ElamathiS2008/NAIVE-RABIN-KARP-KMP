import streamlit as st
from PROGRAM import naive_search, kmp_search, rabin_karp

st.title("Comparative Analysis of Naive, Rabin-Karp, and KMP Algorithms")
text = st.text_input("Enter Text")
pattern = st.text_input("Enter Pattern")
if st.button("Compare"):
    naive_result = naive_search(text, pattern)
    kmp_result = kmp_search(text, pattern)
    rk_result = rabin_karp(text, pattern)
    st.subheader("Results")
    st.write("Naive:", naive_result)
    st.write("KMP:", kmp_result)
    st.write("Rabin-Karp:", rk_result)
