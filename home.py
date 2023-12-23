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
    with open("assets/nav_pic.jpeg", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()
        
    # PDF CV file
    with open("assets/Arnav_Resume.pdf", "rb") as pdf_file:
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
        "Instagram": ["https://www.instagram.com/uk.culture.in/", "https://img.icons8.com/ios/50/000000/instagram-new--v1.png"]
      
    }
    
    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
     unsafe_allow_html=True)
    
    st.write("##")
    
        # About me section
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 I am a **System Operations Associate** @ [WellsFargo](https://www.wellsfargo.com/).

    - ❤️ I am passionate about **Machine Learning/Deep Learning, Data,Artificial Intelligence, Computer Vision, Automation**, and more!
    
    - 🤖 I enjoy developing projects, and one of my notable creations is my digital CV, accessible at [My Digital Resume](https://arnav-resume.streamlit.app/). I love to enhance my skills, am passionate about learning new things, and constantly explore and challenge myself.

    
    - 🏂 Enjoys practicing sports such as cricket, badminton, and climbing. Passionate about photography and editing.

    
    - 📫 How to reach me: arnavsinghrana74@gmail.com
    
    - 🏠 Rishikesh , Uttarakhand , India
    """)
    
    
    st.write("##")
    # My Projects section
    st.header("My Projects")

    # Download CV button
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Arnav_Resume.pdf",
        mime="application/pdf",
    )

    
    
    
if __name__=="__main__":
    
    home()