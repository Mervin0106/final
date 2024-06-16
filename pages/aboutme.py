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

# with st.expander("Who I am 10 years From now??"):
#     st.markdown("""
    
#     #
#                 Ten Years From Now: A Glimpse into the Future as an Information Student
# In the year 2034, I envision myself as an accomplished information professional, leveraging the skills 
#                 and knowledge acquired through a decade of rigorous study and practical experience. The journey from a 
#                 curious student to a seasoned expert has been transformative, marked by significant technological advancements, 
#                 evolving industry demands, and personal growth. This essay delves into the aspirations, milestones, and the envisioned
#                 role I will play in the realm of information science ten years from now.

#                 Personal Growth and Vision
# The journey to becoming a prominent information professional will be shaped by continuous learning and personal growth. I will embrace a mindset
#                  of curiosity and resilience, constantly seeking new knowledge and adapting to changing circumstances. My passion for information 
#                  science will be fueled by a desire to make a positive impact on the world, addressing societal challenges through innovative solutions.

# In 2034, I will be a testament to the transformative power of education, perseverance, and a forward-thinking vision. My career will be a blend of research 
#                 excellence, educational mentorship, industry leadership, and societal impact. As I reflect on the journey from an eager information student 
#                 to a trailblazing professional, I will take pride in the contributions I have made to the field and the legacy I continue to build.

# In conclusion, ten years from now, I will be an influential information scientist, educator, and leader, dedicated to advancing the field and harnessing the 
#                 power of data for the greater good. My story will be one of relentless pursuit of knowledge, innovative thinking, and unwavering commitment to 
#                 making a difference in the world.
#     """, unsafe_allow_html=True)
# Quotes


st.header("Favorite Quotes")
st.write("1. *\"Every day is a new opportunity to learn and grow.\"*")
st.write("2. *\"Embrace the challenges, for they are the stepping stones to success.\"*")
st.write("3. *\"Kindness is the language that the deaf can hear and the blind can see.\"*")
st.write("4. *\"Dream big, work hard, stay focused, and surround yourself with good people.\"*")
st.write("5. *\"In a world where you can be anything, be yourself.\"*")



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
