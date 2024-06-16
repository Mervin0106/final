
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "🔔"),
        Section("Main Page", "💡"),
        Page("pages/aboutme.py", "👦🏻 IT'S MERVIN", "1️⃣", in_section=True),
        Page("pages/description.py", "📋 PROJECT APP DESCRIPTION", "2️⃣", in_section=True),
        Page("pages/learnings.py", "📚 ITQMT INSIGHTS", "3️⃣", in_section=True),
     
  
        Section("Projects", "📂"),
        Page("pages/analyzer.py", "🔎 SENTIMENT ANALYZER", "1️⃣", in_section=True),
        Page("pages/classification.py", "🎯 IMAGE CLASSIFICATION", "2️⃣", in_section=True),
        Page("pages/prediction.py", " 🧐 PREDICTION", "3️⃣", in_section=True),

        Section("Project Source Code","💻"),
        Page("pages/analyze_src.py","♨️ SENTIMENT SRC", "1️⃣", in_section=True),
        Page("pages/classification_src.py","♨️ CLASSIFICATION SRC", "2️⃣", in_section=True),
        Page("pages/prediction_src.py","♨️ PREDICTION SRC", "3️⃣", in_section=True),
        
    ]
)

hide_pages(["Thank you"])

st.markdown("### FINAL REQUIREMENTS SUBMITTED BY: ")
st.header("MERVIN OPIALDA - BSIS 3B")
st.image("./pic/merv2.jpg")
st.markdown("""<a href="/photographer/thinkstock-83786">Thinkstock</a> on <a href="/">Freeimages.com</a>""",unsafe_allow_html=True,)

st.info("For more info. Contact [Mervin Opialda](https://www.facebook.com/mervin.opialda) on Fb")
st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")

with st.expander("Machine Learning"""):
    st.markdown("""
    
    
    #

                 Purpose of Machine Learning
Machine learning (ML) serves a wide array of purposes across various domains, enabling systems to learn from data and make intelligent decisions. Here are some key purposes of machine learning:

                 1. Automation of Tasks
Repetitive Processes: Automates routine tasks, reducing human intervention and increasing efficiency.

Complex Calculations: Performs complex calculations and processes large datasets quickly.

                 2. Data Analysis and Interpretation
Pattern Recognition: Identifies patterns and correlations in data that might be missed by human analysis.

Predictive Analytics: Predicts future trends and behaviors based on historical data.

                 3. Enhancement of Decision Making
Data-Driven Decisions: Provides insights and recommendations based on data analysis, leading to more informed decisions.

Real-Time Analysis: Offers real-time data processing and decision-making capabilities. 
                    
    """, unsafe_allow_html=True)

st.title('the Streamlit Application Project')

st.markdown("""


##### 👨‍🔧 Machine Learning

             Purpose of Machine Learning
The primary purpose of machine learning is to develop algorithms and statistical models that enable computers to perform specific tasks without explicit instructions, relying instead on patterns and inference.
                 Machine learning aims to automate and improve decision-making processes, enhance the accuracy of predictions, and uncover insights from large and complex datasets. Its objectives include:

* Automation: Automating repetitive and mundane tasks, improving efficiency and reducing human error.
* Prediction: Making accurate predictions based on historical data, such as stock market trends, weather forecasting, and disease outbreaks.
* Pattern Recognition: Identifying patterns and relationships in data that are not apparent to human analysts.
* Personalization: Tailoring services and products to individual users' preferences, such as recommendation systems in e-commerce and content platforms.
* Optimization: Enhancing processes and systems, such as supply chain management, through data-driven decision-making.
                
### 🔎 Overview""", unsafe_allow_html=True)


st.image("./pic/st.jfif")


st.markdown("""
The beauty of Streamlit lies in its simplicity and versatility, allowing you to bring your ideas to life quickly and efficiently.
             Whether you're a data scientist, developer, educator, or hobbyist, Streamlit empowers you to build impactful applications
             that engage and inspire your audience. With its growing community and ecosystem of plugins and integrations, the potential 
            for innovation is limitless. So go ahead, unleash your creativity, and see where Streamlit takes you!
* Streamlit offers a powerful and user-friendly way to create interactive web applications for data analysis and machine learning, with benefits 
            ranging from ease of use and rapid development to robust data visualization and seamless sharing capabilities.
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
