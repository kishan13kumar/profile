import streamlit as st

def main():
    st.title("KISHAN KUMAR SURESH KUMAR's Resume")
    st.markdown(
        """
        <style>
            /* Add custom CSS styles */
            .info-section {
                background-color: #f0f8ff; /* AliceBlue */
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 20px;
                color: black; /* Adjust text color */
            }
            .success-section {
                background-color: #f0fff0; /* Honeydew */
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 20px;
                color: black; /* Adjust text color */
            }
            .warning-section {
                background-color: #fff0f5; /* LavenderBlush */
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 20px;
                color: black; /* Adjust text color */
            }
            .contact-section {
                background-color: #e6e6e6; /* LightGray */
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 20px;
                color: black; /* Adjust text color */
            }
            .link {
                color: #007bff;
                text-decoration: none;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.image("./profile_photo.jpg", width=150)
    st.markdown("**Location:** Salem, Tamil Nadu, India")
    st.markdown("**Email:** krss132005@gmail.com")
    st.markdown("**Phone:** +91 6380383183")
    st.markdown("**LinkedIn:** [linkedin.com/in/kishan-kumar-037175259](https://www.linkedin.com/in/kishan-kumar-037175259/)")
    st.markdown("**GitHub:** [github.com/kishankumar1328](https://github.com/kishankumar1328)")
    st.markdown("---")

    st.markdown("### Objective")
    st.markdown(
        """
        <div class="info-section">
            A dedicated and motivated individual with a strong foundation in data science principles, seeking to leverage skills in Python, machine learning, and data analysis to contribute effectively to cutting-edge projects in artificial intelligence.
        </div>
        """
    )

    st.markdown("---")

    st.markdown("### Education")
    st.markdown(
        """
        <div class="info-section">
            Bachelor of Technology - BTech, Artificial Intelligence & Data Science<br>
            M.KUMARASAMY COLLEGE OF ENGINEERING, KARUR<br>
            Sep 2022 - May 2026
        </div>
        """
    )

    st.markdown("---")

    st.markdown("### Certifications")
    certifications = [
        "Python for Data Science - IBM",
        "Data Analysis Using Python - IBM",
        "Data Science Foundations - Level 1 - IBM",
        "Predictions: Regression for Car Mileage and Diamond Price - IBM",
        "Customer Clustering With KMeans to Boost Business Strategy - IBM",
        "Data Visualization Using Python - IBM",
        "Applied Data Science with Python - Level 2 - IBM",
        "Prompt Engineering for Everyone - IBM",
        "Machine Learning with Python - IBM",
        "Data Privacy Fundamentals - IBM",
        "Data Science Methodologies - IBM",
        "Python (Basic) - HackerRank"
    ]
    for cert in certifications:
        st.markdown(f"<div class='success-section'>{cert}</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Skills")
    skills = [
        "Data Analysis",
        "Data Visualization",
        "Data Privacy",
        "Prompt Engineering",
        "Machine Learning",
        "Data Science",
        "Python (Programming Language)"
    ]
    for skill in skills:
        st.markdown(f"<div class='success-section'>{skill}</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Projects")
    projects = {
        "Emotion Detection": "https://github.com/Kishankumar1328/Emotion-detection",
        "Sentiment Analysis": "https://github.com/Kishankumar1328/Stock-Dashboard-with-GPT",
        "Lung Cancer Analysis": "https://github.com/Kishankumar1328/lung_cancer_analysis",
        "Semiconductor Stock Dashboard": "https://github.com/Kishankumar1328/SEMICONDUCTOR-STOCK-DASHBOARD"
    }
    for i, (project, link) in enumerate(projects.items(), start=1):
        st.markdown(f"{i}. [{project}]({link})", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Contact")
    st.markdown(
        """
        <div class="contact-section">
            Feel free to reach out via email at [krss132005@gmail.com](mailto:krss132005@gmail.com) or connect with me on [LinkedIn](https://www.linkedin.com/in/kishan-kumar-037175259/).
        </div>
        """
    )

if __name__ == "__main__":
    main()
