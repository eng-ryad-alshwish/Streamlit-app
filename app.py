import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Dashboard Template", layout="wide")

# ✅ شريط التنقل العلوي (Navbar)
selected = option_menu(
    menu_title=None,
    options=["الرئيسية", "رفع ملف", "التحليل"],
    icons=["house", "cloud-upload", "bar-chart"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

st.write("---")

# ✅ استدعاء الصفحات (UI فقط)
if selected == "الرئيسية":
    st.switch_page("pages/1_Home.py")
elif selected == "رفع ملف":
    st.switch_page("pages/2_Upload.py")
elif selected == "التحليل":
    st.switch_page("pages/3_Analysis.py")
