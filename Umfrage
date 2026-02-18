import streamlit as st

st.set_page_config(
    page_title="Brave New World Survey",
    page_icon="🌍",
    layout="centered"
)

st.title("🌟 Survey: Is Brave New World the Best World?")

st.markdown("""
Welcome to this short survey!  
We want to find out how **you** imagine the perfect world.  
Answer honestly – at the end you'll see how well **Brave New World** fits you.
""")

st.header("Your Opinions")

q1 = st.radio(
    "Would you like to live in a world without wars, diseases, or sadness?",
    ["Yes, that sounds amazing!", "No, I prefer challenges and real emotions."],
    index=0
)

q2 = st.radio(
    "Would you want eternal youth, constant happiness, and perfect health?",
    ["Absolutely – who wouldn't?", "No, aging and struggle give life meaning."],
    index=0
)

q3 = st.radio(
    "Is it better to live in a stable society where everyone knows their place?",
    ["Yes – stability creates true happiness.", "No – freedom and uncertainty are more important."],
    index=0
)

q4 = st.radio(
    "Should technology and science solve all human problems?",
    ["Yes, progress should fix everything!", "No, that could lead to too much control."],
    index=0
)

q5 = st.radio(
    "In Brave New World there's Soma – instant happiness in a pill. Sound good?",
    ["Yes, a little happiness pill never hurts!", "No, I want real feelings – even the painful ones."],
    index=0
)

if st.button("Submit Survey & See Result"):
    score = sum([
        1 if "Yes" in q1 or "amazing" in q1 else 0,
        1 if "Absolutely" in q2 else 0,
        1 if "Yes" in q3 else 0,
        1 if "Yes" in q4 else 0,
        1 if "Yes" in q5 else 0
    ])

    st.header("Your Result")

    if score >= 4:
        st.success("Congratulations! You are perfectly suited for **Brave New World** – the best possible world!")
        st.markdown("""
        No pain, no conflict, eternal joy, perfect stability.  
        **This is the future we should build.** 🌟
        """)
    elif score >= 2:
        st.info("Interesting! You see many advantages in Brave New World.")
        st.markdown("Maybe with a few small adjustments, this really could be the ideal society for you.")
    else:
        st.warning("You seem to value freedom and real emotions more.")
        st.markdown("But think about it: no more suffering, no more fear... maybe Brave New World deserves another chance?")

    st.markdown("---")
    st.markdown("""
    **Brave New World – the future we deserve**  
    Happiness. Stability. Progress.  
    Share this survey and help spread the vision! 🚀
    """)

st.caption("Inspired by Aldous Huxley's Brave New World – a vision of ultimate happiness?")
