import streamlit as st

st.title("📊 واجهة التحليل")
st.write("هذه مجرد واجهة تجريبية (UI) لعرض تصميم Dashboard.")

# ✅ Layout for charts placeholders
col1, col2 = st.columns(2)
with col1:
    st.subheader("📈 مخطط بياني 1")
    st.empty()  # Placeholder

with col2:
    st.subheader("📉 مخطط بياني 2")
    st.empty()

st.subheader("📋 جدول بيانات")
st.table({
    "الاسم": ["أحمد", "منى", "يوسف"],
    "القيمة": [120, 95, 130],
    "الحالة": ["✅", "⚠️", "❌"]
})
