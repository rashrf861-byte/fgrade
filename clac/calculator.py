import streamlit as st
st.set_page_config(page_title= "Total Grade Calcilator", page_icon="🎓", layout="centered")
st.title("The Grade Calculator🎓")
st.write("Write your grade in each subject down here, and let the calc do the rest")
grade_map={
    "A+":100,
    "A":94,
    "B+":89,
    "B":84,
    "C+":79,
    "C":74,
    "D+":69,
    "D":64,
    "F":60,
    "else/non mentioned":0

}

subjects = [
    "Arabic","English","Second language","Math","Physics","Geology",
    "Biology","Mechanics","Chenistry","Social Studies","Computer Science",
    "Religion"
]
user_grades= {}
st.subheader("Enter the subject grade 📝")
col1, col2 = st.columns(2)
for i, subject in enumerate(subjects):
    with col1 if i % 2 == 0 else col2:
        choice = st.selectbox(
            f"{subject}:",
            options=list(grade_map.keys()),
            key=subject
        )
        user_grades[subject] = grade_map[choice]

st.subheader("The Final Result 📊")

if st.button("calculate the total grade",type="primary"):
    total_score = sum(user_grades.values())
    max_score = len(subjects) *100
    precentage = (total_score / max_score)* 100
    
    st.success(f"🎉 Your Grade: {total_score} from {max_score}")
    st.metric(label="Approximate Precentage", value=f"{precentage:.2f}%")

    if precentage >=90:
        st.balloons()
        st.write("WHAT ARE YOU, AN ALIEN OR SOMETHING 🔥? ")
    elif precentage >=75:
        st.write("GREAT JOB, DUDE 👍, BUT YOU ARE BETTER THAN THAT")
    else:
        st.write("GOOD LUCK NEXT TIME, DON'T FORGET, FAKE IT TILL YOU MAKE IT💪")