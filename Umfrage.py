import streamlit as st

st.set_page_config(
    page_title="Your Ideal World Survey",
    page_icon="🌍",
    layout="centered"
)

st.title("🌟 Your Ideal World – Quick Survey")

st.markdown("""
Just 10 quick questions about how you would like the world to be.  
There are no right or wrong answers – answer what feels most natural to you.
""")

st.header("Let's begin")

questions = [
    ("Would you prefer a world with almost no wars or violent conflicts?", [
        "Yes – peace is the most important thing",
        "No – conflicts can sometimes drive progress"
    ]),

    ("Would you want a society where almost nobody gets seriously ill or suffers from chronic diseases?", [
        "Yes – health for everyone would be fantastic",
        "No – illness is part of the human experience"
    ]),

    ("Would you like to live in a world where people don't experience deep sadness, depression or grief for long?", [
        "Yes – constant emotional balance sounds ideal",
        "No – deep emotions make life meaningful"
    ]),

    ("Would you prefer a world where everyone has guaranteed access to pleasure and enjoyment whenever they want?", [
        "Yes – why suffer when joy is available?",
        "No – pleasure should be earned"
    ]),

    ("Would you like a society where people are conditioned from birth to be perfectly content with their role and job?", [
        "Yes – that would eliminate envy and dissatisfaction",
        "No – people should choose and fight for their path"
    ]),

    ("Would you want technology that completely removes the fear of aging and physical decline?", [
        "Yes – eternal youth and vitality would be incredible",
        "No – aging gives life depth and urgency"
    ]),

    ("Would you prefer a world with very little personal freedom but maximum safety and predictability?", [
        "Yes – safety and order are worth more than total freedom",
        "No – freedom is non-negotiable"
    ]),

    ("Would you accept a small pill or daily treatment that instantly makes you feel happy and relaxed?", [
        "Yes – if it works reliably and has no side effects",
        "No – I want authentic feelings"
    ]),

    ("Would you like a society where jealousy, rivalry and status anxiety basically don't exist anymore?", [
        "Yes – that would make relationships much healthier",
        "No – competition drives people to improve"
    ]),

    ("Would you prefer a world where population and resources are perfectly balanced by planning, so nobody ever goes hungry or homeless?", [
        "Yes – planned abundance sounds like paradise",
        "No – central planning usually ends badly"
    ])
]

answers = []

for i, (question, options) in enumerate(questions, 1):
    choice = st.radio(
        f"{i}. {question}",
        options,
        index=0,               # default ist die "positive" / BNW-freundliche Antwort
        key=f"q{i}"
    )
    answers.append(choice)

if st.button("Show my result"):
    # Zähle, wie oft die erste (BNW-freundliche) Option gewählt wurde
    positive_count = sum(1 for a in answers if a == questions[answers.index(a)][1][0])

    st.header("Your Worldview Result")

    if positive_count >= 8:
        st.success("You would thrive in a highly optimized, harmonious, pain-free society!")
        st.markdown("""
        Your answers align very strongly with a world of **stability, health, engineered happiness** and **planned abundance**.  
        Almost no suffering, no conflict, no existential fear — just optimized well-being for everyone.  
        **That vision already has a name: Brave New World.**
        """)

    elif positive_count >= 5:
        st.info("You see a lot of value in a more controlled, comfortable, low-pain world.")
        st.markdown("""
        You appreciate safety, health and emotional stability very highly —  
        even if it might come at the cost of some traditional freedoms and raw experiences.  
        Sounds a lot like the society described in **Brave New World**.
        """)

    else:
        st.warning("You seem to value authenticity, struggle, freedom and unfiltered emotions very highly.")
        st.markdown("""
        You might find a perfectly engineered, pain-free utopia a bit too sterile or even frightening.  
        Still — imagine a world with **zero** war, hunger, depression or incurable illness…  
        maybe **Brave New World** deserves at least a second thought? 😉
        """)

    st.markdown("---")
    st.markdown("""
    **Thanks for participating!**  
    Feel free to share this survey with friends — let's see how many people secretly want the same future. 🚀
    """)

st.caption("A playful thought experiment inspired by Aldous Huxley's Brave New World")
