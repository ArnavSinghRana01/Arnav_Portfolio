import streamlit as st 
import base64


#Main Page
def home():
    #set page config 
    st.set_page_config(
        page_title="Arnav Singh Rana's Portfolio",
        page_icon="🍕"
    )
    
    #CSS style file 
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
    
    # Profile image file
    with open("assets/arnav_photo.jpeg", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()
        
    # PDF CV file
    with open("assets/Arnav Resume.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        
        # Top title
    st.write(f"""<div class="title"><strong>Hi! My name is</strong> Arnav Singh Rana👋</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Enric Domingo">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True)
    
        # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Enthusiast Data Scientist</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "Kaggle": ["https://www.kaggle.com/arnavsinghrana", "https://www.kaggle.com/static/images/site-logo.svg"],
        "LinkedIn": ["https://www.linkedin.com/in/arnav-singh-rana-a76508263/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/ArnavSinghRana01", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
       
      
    }
    
    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
     unsafe_allow_html=True)
    st.markdown("---")
    st.write("##")
    
        # About me section
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 I am a **System Operations Associate** @ [WellsFargo](https://www.wellsfargo.com/).

    - ❤️ I am passionate about **Machine Learning, Data,Artificial Intelligence, LLM, Automation**, and more!
    
    - 🤖 I enjoy developing projects, and one of my notable creations is my digital CV, accessible at [My Digital Resume](https://arnav-digital-cv.onrender.com/). I love to enhance my skills, am passionate about learning new things, and constantly explore and challenge myself.

    
    - 🏂 Enjoys practicing sports such as cricket, badminton, and climbing. Passionate about photography and editing.

    
    - 📫 How to reach me: arnavsinghrana74@gmail.com
    
    - 🏠 Rishikesh , Uttarakhand , India
    """)
    
    st.markdown("---")
    st.write("##")
    # Projects Section
    st.subheader("Projects")
    # Project 1: Sales Dashboard
    st.write("""
    ### Sales Dashboard 📊
    - **Project Link:** [Sales Dashboard](https://supermarket-sales-dashboard-qnan.onrender.com/)
    - **Description:** Explore the Sales Dashboard created with Streamlit and Plotly, providing insights into sales trends by product line and hourly patterns. Gain valuable data-driven perspectives for strategic decision-making.
""")
    
    # Project 2: Portfolio (This Streamlit App)
    st.write("""
    ### Portfolio Streamlit App 🚀
    - **Project Link:** [Portfolio](https://arnav-portfolio-sgu3.onrender.com/)
    - **Description:** This Streamlit app showcases my personal portfolio, highlighting my skills, projects, and experience. Feel free to explore!
    """)
    # Project 3: PBL Metrics Dashboard
    st.write("""
    ### PBL Metrics Dashboard📊
    "The 'PBL Metrics Graphical Visualization in Wells' project focused on implementing graphical visualization for PBL metrics at Wells Fargo. It leveraged Python for scripting and data processing, Streamlit for creating interactive web applications, and Pyplotly for crafting engaging charts. Excel served as the primary data source for PBL metrics."
    """)
    
    st.markdown("---")
    # Download CV button
    st.write("##")
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Arnav Resume.pdf",
        mime="application/pdf",
    )
 

    
    
if __name__=="__main__":
    
    home()