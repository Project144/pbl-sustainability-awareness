import streamlit as st

st.set_page_config(page_title="Sustainability Quiz", page_icon="🌱")

st.title("🌿 Reflect on your habits and find your Sustainability Awareness Level!")

score = 0

# Question 1
q1 = st.radio("1. How often do you carry a reusable bottle on campus?",
              ["Never", "Sometimes", "Always"])
if q1 == "Sometimes":
    score += 1
elif q1 == "Always":
    score += 2

# Question 2
q2 = st.radio("2. What do you usually do with used notebooks/papers at semester end?",
              ["Throw them away", "Store them", "Recycle or donate them"])
if q2 == "Store them":
    score += 1
elif q2 == "Recycle or donate them":
    score += 2

# Question 3
q3 = st.radio("3. Have you participated in any environmental clubs or green events in college?",
              ["Yes", "No"])
if q3 == "Yes":
    score += 2

# Question 4
q4 = st.radio("4. How aware are you about the SDGs (Sustainable Development Goals)?",
              ["Not aware", "Somewhat aware", "Very aware"])
if q4 == "Somewhat aware":
    score += 1
elif q4 == "Very aware":
    score += 2

# Question 5
q5 = st.radio("5. What would you do if you saw someone littering on campus?",
              ["Ignore it", "Pick it up silently", "Confront or suggest politely"])
if q5 == "Pick it up silently":
    score += 1
elif q5 == "Confront or suggest politely":
    score += 2

# Question 6
q6 = st.radio("6. Which of these is an example of sustainable food habits in college?",
              ["Packaged snacks", "Locally sourced meals", "Canned drinks"])
if q6 == "Locally sourced meals":
    score += 2

# Question 7
q7 = st.radio("7. Do you turn off fans/lights before leaving classrooms or hostels?",
              ["Always", "Sometimes", "Rarely"])
if q7 == "Sometimes":
    score += 1
elif q7 == "Always":
    score += 2

# Question 8
q8 = st.radio("8. Are you aware of any eco-friendly stores or canteens on/near campus?",
              ["Yes", "No"])
if q8 == "Yes":
    score += 2

# Question 9
q9 = st.radio("9. How do you usually commute to college?",
              ["Private vehicle", "Carpool/Public transport", "Cycle or walk"])
if q9 == "Carpool/Public transport":
    score += 1
elif q9 == "Cycle or walk":
    score += 2

# Question 10
q10 = st.radio("10. Would you be willing to join or support a student-led green initiative?",
               ["Yes", "No"])
if q10 == "Yes":
    score += 2

# Show score
st.write(f"### Your Score: {score}/20")

# Redirection based on score
if score < 12:
    st.warning("You’re on your sustainability journey! Start here:")
    st.page_link(
        "https://project144.github.io/pbl-sustainability-awareness/awareness",
        label="Explore Sustainability 🌱",
        icon="🌱"
    )
else:
    st.success("You’re doing great! Let’s take it further:")
    st.page_link(
        "https://project144.github.io/pbl-sustainability-awareness/practices",
        label="Take Sustainable Action 🚀",
        icon="🚀"
    )
