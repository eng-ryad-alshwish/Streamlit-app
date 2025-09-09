import streamlit as st

st.title("📂 واجهة رفع الملفات")
st.write("هذه مجرد صفحة شكلية (UI) لعرض التصميم فقط.")

with st.container():
    st.subheader("📤 منطقة رفع الملف")
    st.markdown(
        """
        <div style="border:2px dashed #aaa; border-radius:10px; padding:30px; text-align:center;">
        ✨ اسحب الملف هنا أو اضغط للاختيار  
        <br><br>
        <button style="padding:10px 20px; border:none; border-radius:8px; background:#4CAF50; color:white; font-size:16px;">
        رفع الملف
        </button>
        </div>
        """,
        unsafe_allow_html=True,
    )
