import streamlit as st


st.set_page_config(
    page_title="Research Profile | Adetiba Blessed EJ",
    page_icon="🎓",
    layout="centered"
)

st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to section:",
    ["Profile", "Research Interests", "Qualifications", "Contact"],
)


if menu == "Profile":
    st.title("Adetiba Blessed EJ")
    st.subheader("Honours Student | Data Science & Artificial Intelligence")

    st.markdown("""
    **Institution:** University of Fort Hare, Alice Campus, South Africa  
    **Academic Focus:** Data Science, Artificial Intelligence, and Cybersecurity

    I am a motivated and detail-oriented postgraduate (Honours) student with strong
    analytical and problem-solving skills. My academic interests lie at the
    intersection of artificial intelligence, data science, and real-world problem
    solving. I am passionate about research, innovation, and community development,
    and I continuously seek opportunities to apply technology for societal impact.
    """)

    st.image(
        "https://infrastructurenews.co.za/wp-content/uploads/2021/06/UFH-Alice-Campus-New-Student-Village-scaled.jpg",
        caption="University of Fort Hare – Alice Campus"
    )


elif menu == "Research Interests":
    st.title("Research Interests")

    st.markdown("""
    My primary research interest lies in the application of **artificial intelligence
    to cybersecurity**. As cyber threats grow increasingly complex, traditional
    security mechanisms struggle to adapt in real time. AI-driven systems offer the
    potential to detect, predict, and respond to cyber threats with greater accuracy
    and speed.

    During my undergraduate studies, I developed a strong interest in anomaly
    detection and predictive modelling, particularly in scenarios involving large
    and complex datasets. These experiences highlighted the value of intelligent
    systems in identifying malicious patterns before significant damage occurs.

    Looking ahead, I aim to focus on developing **robust and explainable AI-based
    security solutions**, with particular interest in adversarial machine learning
    and resilience against model manipulation. My long-term goal is to contribute
    to building safer, more trustworthy digital environments through rigorous
    research and innovation.
    """)


elif menu == "Qualifications":
    st.title("Qualifications")

    option = st.sidebar.selectbox(
        "Select category:",
        ["Education", "Work Experience", "Skills"]
    )

    if option == "Education":
        st.subheader("Educational Background")
        st.markdown("""
        **Bachelor of Science in Computer Science and Mathematics (2025)**  
        *University of Fort Hare*

        **Relevant Modules:**
        - Software Engineering
        - Data Structures
        - Database Systems and Management
        - Complex Analysis
        - Advanced Calculus
        - Abstract Algebra

        **Academic Achievement:**
        - Achieved a 76% average in Computer Applications Technology
        """)

    elif option == "Work Experience":
        st.subheader("Professional Experience")
        st.markdown("""
        **Tutor (Part-Time)**  
        *University of Fort Hare, Alice Campus*  
        *July 2025 – December 2025*

        **Key Responsibilities:**
        - Assisted first-year students with programming fundamentals (HTML, Java, C++)
        - Conducted weekly tutorial sessions
        - Provided one-on-one academic support

        **Key Achievements:**
        - Contributed to a 30% improvement in student pass rates
        - Developed strong communication, teamwork, and problem-solving skills
        """)

    elif option == "Skills":
        st.subheader("Technical Skills")
        st.markdown("""
        **Programming Languages:**
        - Python
        - Java
        - C++
        - HTML

        **Software & Tools:**
        - Microsoft Word
        - Microsoft Excel
        - Microsoft PowerPoint
        """)


elif menu == "Contact":
    st.title("Contact Information")

    st.markdown("""
    **Email:** adetibablessed17@gmail.com | 202100905@ufh.ac.za  
    **Phone:** +27 73 057 4138  
    **Location:** Panorama, Empangeni, KwaZulu-Natal, South Africa

    I welcome academic collaboration, research discussions, and professional
    opportunities. Please feel free to reach out using the contact details above.
    """)
