import streamlit as st

st.title("ALL ABOUT MERVIN 👨‍💼")



st.title("🖼️Gallery")


image_paths = ["./pic/merv2.jpg", "./pic/merv1.jpg", "./pic/merv3.jpg"]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header("👨‍🎓 OPIALDA, MERVIN")


# Personal Information
st.header("INFORMATION ABOUT ME")
st.write("**Name:** OPIALDA, MERVIN")
st.write("**Age:** 21 years old")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student")
st.write("**Location:** Silay City Negros Occidental")




st.header("Hobbies")

st.subheader("Basketball")
st.write("""
Basketball is a popular sport where two teams, usually of five players each, compete to score points by throwing a ball through the opposing team's hoop. 
It improves physical fitness, teamwork skills, and is a fun way to stay active.
""")

st.subheader("Playing Online Games")
st.write("""
Playing online games involves interacting with others through various gaming platforms. 
It can be a great way to unwind, improve strategic thinking, and connect with friends. 
Popular genres include action, adventure, and role-playing games.
""")



import streamlit as st


images = [
    {"path": "./pic/ey1.jpg", "caption": "Friends are an essential part of life, providing not only companionship but also support and joy. The essence of a true friendship lies in mutual help and shared enjoyment."},
    {"path": "./pic/ey2.jpg", "caption": "This symbiotic relationship fosters a bond that can withstand the trials and tribulations of life, making it an indispensable aspect of human experience."},
   
]


st.title("Mervin's Photo")


for image in images:
    st.image(image["path"], caption=image["caption"])



st.markdown(
    """
    <style>
    .stApp {
        background-color: #80C4E9;
        padding: 2em;
    }
    h1, h2 {
        color: white;
    }
    .stText {
        font-size: 1.2em;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### Thank you for visiting my profile!")
st.write("Feel free to connect and reach out if you share similar interests or have any questions.")
