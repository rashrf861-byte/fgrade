import streamlit as st
st.set_page_config(page_title= "Total Grade Calcilator", page_icon="🎓", layout="centered")
st.sidebar.title("Choose your grade📌")
page = st.siderbar.radio("go to:"["university","secondary"])
if page =="secondary":
    st.title("The Grade Calculator🎓")
    st.write("Write your grade in each subject down here, and let the calc do the rest")



grade_map_school={
    "A+":(95,100),
    "A":(90,94),
    "B+":(85,89),
    "B":(80,84),
    "C+":(75,79),
    "C":(70,74),
    "D+":(65,69),
    "D":(61,64),
    "F":(1,60),
    "else/non mentioned":(0,0)

}

subjects_school = [
    "Arabic","English","Second language","Math","Physics","Geology",
    "Biology","Mechanics","Chenistry","Social Studies"
    
]
user_grades= {}
st.subheader("Enter the subject grade 📝")
col1, col2 = st.columns(2)
for i, subject in enumerate(subjects_school):
    with col1 if i % 2 == 0 else col2:
        choice = st.selectbox(
            f"{subject}:",
            options=list(grade_map_school.keys()),
            key=f"school_{subject}"
        )
        user_grades[subject] = grade_map_school[choice]

st.subheader("The Final Result 📊")

if st.button("calculate the total grade",type="primary", key="btn_school"):
    min_total=sum(grade[0]for grade in user_grades.values())    
    max_total=sum(grade[1]for grade in user_grades.values())
    max_possible=len(subjects_school)*100
    min_percentage=(min_total/max_possible)*100
    max_percentage=(max_total/max_possible)*100
    
    st.success(f"🎉 Your Grade: **{min_total}** و **{max_total}** from {max_possible})")
    st.metric(label="Approximate Precentage", value=f"{min_percentage:.1f}% _ {max_percentage:.1f}%")

    if max_percentage >=90:
        st.balloons()
        st.write("WHAT ARE YOU, AN ALIEN OR SOMETHING 🔥? ")
    elif max_percentage >=75:
        st.write("GREAT JOB, DUDE 👍, BUT YOU ARE BETTER THAN THAT")
    else:
        st.write("GOOD LUCK NEXT TIME, DON'T FORGET, FAKE IT TILL YOU MAKE IT💪")

else:
    st.title("Grade Calculator for university 🏛️")
    st.write("A special calculator for university")

    grade_map_uni={
        "A+ / ممتاز مرتفع": (95, 100),
        "A / ممتاز": (90, 94),
        "B+ / جيد جداً مرتفع": (85, 89),
        "B / جيد جداً": (80, 84),
        "C+ / جيد مرتفع": (75, 79),
        "C / جيد": (70, 74),
        "D+ / مقبول مرتفع": (65, 69),
        "D / مقبول": (60, 64),
        "F / راسب": (0, 59)
    }

    st.subheader("semester⚙️:")
    num_subjects= st.number_input("the number of subjects this semester:",min_value=1,max_value=10,value=5)
    user_grades_uni={}
    st.subheader("enter your subjects grades📝:")
    col1,col2= st.columns(2)
    for i in range(int(num_subjects)):
        with col1 if i % 2 == 0 else col2:
            choice = st.selectbox(f"number of subject {i+1}:", options=list(grade_map_uni.keys()), key=f"uni_sub_{i}")
            user_grades_uni[f"subject {i+1}"] = grade_map_uni[choice]
    st.subheader("Expected grade 📊")
    if st.button("Calculate the grade", type="primary", key="btn_uni"):
         min_total = sum(grade[0] for grade in user_grades_uni.values())
         max_total = sum(grade[1] for grade in user_grades_uni.values())       
         max_possible = num_subjects * 100
        
         min_percentage = (min_total / max_possible) * 100
         max_percentage = (max_total / max_possible) * 100 
         st.info(f"🎓 Your approximate grade:")
         st.metric(label="Semester precentage", value=f"{min_percentage:.1f}% _ {max_percentage:.1f}%")
         avg_percentage = (min_percentage + max_percentage) / 2
         if avg_percentage >= 90:
            st.success("🏆 (Excellent) 🔥")
         elif avg_percentage >= 80:
            st.success("👍   (Very Good)")
         elif avg_percentage >= 65:
            st.warning("👌   (Good)")
         else:
            st.error(" Study more and more and more 💪")
