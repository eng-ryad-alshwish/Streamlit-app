import streamlit as st

st.title("🏠 الصفحة الرئيسية")
st.markdown("### 👋 أهلاً بك في **اللوحة الاحترافية**")
st.write("هذه مجرد واجهة رئيسية تجريبية (UI).")

# ✅ Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("عدد المستخدمين", "1500", "+50 اليوم")
with col2:
    st.metric("المعاملات", "230", "+12")
with col3:
    st.metric("الملاحظات", "89", "-5")
