import streamlit as st

st.set_page_config(page_title="Gossip Girl Quiz", page_icon="🗽")

st.title("Which *Gossip Girl* Character Are You?")
st.caption("You know you love me...xoxo...**Gossip Girl**")

# --- IMAGES (remote placeholders so there are no path errors) ---
c1, c2, c3, c4, c5 = st.columns(5)
with c1: st.image("Images/serena.jpg", caption="Serena")
with c2: st.image("Images/blair.jpg", caption="Blair")
with c3: st.image("Images/dan.jpg", caption="Dan")
with c4: st.image("Images/chuck.jpg", caption="Chuck")
with c5: st.image("Images/jenny.jpg", caption="Jenny")

st.write("---")

st.subheader("Question 1: Aesthetics")

# --- 5+ QUESTIONS using 3+ different widget types ---
q1_aesthetic = st.selectbox(                     # NEW
    "1) Pick the aesthetic that best describes you:",
    [
        "Model off Duty",
        "Country Club/Preppy",
        "Minimalist",
        "Finance, trust fund, 6'5, blue eyes",
        "Edgy/Thrift",
    ],
)



st.write("---")

st.subheader("Question 2: Weekend Plans")
q2_weekend = st.radio(                       # NEW
    "2) Your ideal weekend involves:",
    [
        "Party/Club in the city",
        "Planning a charity brunch",
        "Writing in a local cafe",
        "Business dinners with clients",
        "Fashion shoot",
    ],
)

st.write("---")

st.subheader("Question 3: Accessories")

q3_accessories = st.multiselect(             # NEW
    "3) When getting ready, I never leave without:",
    [
        "Balenciaga clutch",
        "Headband",
        "Notebook",
        "Silk pocket square",
        "Black eyeliner",
    ],
)

st.write("---")

st.subheader("Question 4: Drama")
q4_drama = st.slider(                        # NEW
    "4) How often are you involved in drama? (0 = avoid it at all costs, 10 = I am the drama):",
    min_value=0,
    max_value=10,
    value=5,
)

st.write("---")

st.subheader("Question 5: Secrets")

q5_secrets = st.number_input(                # NEW
    "5) How many secrets are you keeping right now?",
    min_value=0,
    max_value=20,
    value=1,
    step=1,
)

# --- PROGRESS: show completion ---
answered = 5  # all have defaults, so assume answered
st.progress(int(answered / 5 * 100), text="100% of questions answered")  # NEW

# --- SCORE MAPPING ---
chars = ["Serena", "Blair", "Dan", "Chuck", "Jenny"]
score = {c: 0 for c in chars}

# Q1 style
if q1_aesthetic == "Model off Duty":
    score["Serena"] += 1
elif q1_aesthetic == "Country Club/Preppy":
    score["Blair"] += 1
elif q1_aesthetic == "Minimalist":
    score["Dan"] += 1
elif q1_aesthetic == "Finance, trust fund, 6'5, blue eyes":
    score["Chuck"] += 1
elif q1_aesthetic == "Edgy/Thrift":
    score["Jenny"] += 1

# Q2 weekend
if q2_weekend == "Party/Club in the city":
    score["Serena"] += 1
elif q2_weekend == "Planning a charity brunch":
    score["Blair"] += 1
elif q2_weekend == "Writing in a local cafe":
    score["Dan"] += 1
elif q2_weekend == "Business dinners with clients":
    score["Chuck"] += 1
elif q2_weekend == "Fashion shoot":
    score["Jenny"] += 1

# Q3 accessories (can add multiple)
for item in q3_accessories:
    if item == "Balenciaga clutch":
        score["Serena"] += 1
    elif item == "Headband":
        score["Blair"] += 1
    elif item == "Notebook":
        score["Dan"] += 1
    elif item == "Silk pocket square":
        score["Chuck"] += 1
    elif item == "Black eyeliner":
        score["Jenny"] += 1


# Q4 drama tolerance
if q4_drama >= 8:
    score["Chuck"] += 1
    score["Blair"] += 1
elif q4_drama > 5:
    score["Serena"] += 1
else:
    score["Dan"] += 1
    score["Jenny"] += 1

# Q5 secrets
if q5_secrets >= 10:
    score["Chuck"] += 1
    score["Blair"] += 1
elif q5_secrets >= 5:
    score["Serena"] += 1
elif q5_secrets >= 2:
    score["Jenny"] += 1
else:
    score["Dan"] += 1

descriptions = {
    "Serena": "Charming, spontaneous, big-heart energy. People naturally orbit you.",
    "Blair":  "Ambitious planner with iconic style—and a secret soft side.",
    "Dan":    "Observant, bookish, principled… with a flair for narration.",
    "Chuck":  "Bold, strategic, thrives in the spotlight (and the drama).",
    "Jenny":  "Creative, determined, not afraid to reinvent the rules.",
}


if st.button("Show my result"):
    # find the highest score; handle ties in a very simple way
    top_score = max(score.values())
    winners = [name for name, pts in score.items() if pts == top_score]

    if len(winners) == 1:
        winner = winners[0]
        st.subheader("You got: " + winner)
        st.write(descriptions[winner])
    else:
        # tie case: display all winners
        st.subheader("It's a tie! You’re a mix of: " + ", ".join(winners))
        for w in winners:
            st.markdown(f"- **{w}** — {descriptions[w]}")

