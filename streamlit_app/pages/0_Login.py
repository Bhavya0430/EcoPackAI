import streamlit as st

st.set_page_config(page_title="EcoPackAI | Login", page_icon="🔐", layout="centered")

# ================= MODERN UI =================
st.markdown("""
<style>
body{
    background: linear-gradient(135deg,#e6f9f2,#eef5ff);
}

.login-card{
    background:white;
    padding:40px;
    border-radius:22px;
    box-shadow:0 12px 30px rgba(0,0,0,.12);
    max-width:420px;
    margin:auto;
    margin-top:80px;
}

h1{
    color:#114b5f;
    text-align:center;
    margin-bottom:20px;
}

button{
    background:#1f7a5b !important;
    color:white !important;
    border-radius:14px !important;
}
</style>
""", unsafe_allow_html=True)

# ================= LOGIN CARD =================
st.markdown("""
<div class="login-card">
<h1>🔐 EcoPackAI Login</h1>
</div>
""", unsafe_allow_html=True)

with st.form("login_form"):
    email = st.text_input("📧 Email Address")
    password = st.text_input("🔑 Password", type="password")
    login = st.form_submit_button("Login")

if login:
    if email and password:
        st.session_state["authenticated"] = True
        st.success("✅ Login successful!")
        st.info("➡ Select a page from the sidebar to continue")
    else:
        st.error("❌ Please enter valid credentials")
