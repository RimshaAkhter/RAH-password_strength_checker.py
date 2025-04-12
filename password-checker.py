import streamlit as st
import re

# --- Page configuration ---
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

# --- Light/Dark Theme Toggle ---
theme = st.radio("🎨 Choose Theme:", ["Light", "Dark"], horizontal=True)

# --- Custom CSS ---
light_theme = """
<style>
body {
    background-color: #ecf0f1;
}
.container {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', sans-serif;
}
.title {
    font-size: 36px;
    font-weight: bold;
    color: #2c3e50;
    text-align: center;
}
.subtitle {
    font-size: 18px;
    color: #34495e;
    text-align: center;
    margin-bottom: 30px;
}
.suggestions {
    color: #e74c3c;
    font-weight: 500;
}
</style>
"""

dark_theme = """
<style>
body {
    background-color: #1c1c1e;
}
.container {
    background-color: #2c2c2e;
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 4px 15px rgba(255,255,255,0.05);
    font-family: 'Segoe UI', sans-serif;
}
.title {
    font-size: 36px;
    font-weight: bold;
    color: #ecf0f1;
    text-align: center;
}
.subtitle {
    font-size: 18px;
    color: #bdc3c7;
    text-align: center;
    margin-bottom: 30px;
}
.suggestions {
    color: #ff6b6b;
    font-weight: 500;
}
</style>
"""

# Apply theme
st.markdown(light_theme if theme == "Light" else dark_theme, unsafe_allow_html=True)

# --- UI Content ---
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("<div class='title'>🔐 Password Strength Checker</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Check how strong your password is and get suggestions to improve it.</div>", unsafe_allow_html=True)

# --- Password Input ---
password = st.text_input("🔑 Enter your password:", type="password", help="Your password will be checked securely.")

# --- Check Button ---
check = st.button("✅ Check Password Strength")

# --- Logic ---
feedback = []
score = 0

if check and password:
    st.markdown("### 🛡️ Password Analysis")
    st.markdown("---")

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?>]", password):
        score += 1
    else:
        feedback.append("❌ Use at least one special character (!@#$%^&*(),.?>).")

    # --- Results ---
    if score == 4:
        st.success("✅ Your password is **Strong**. Well done! 🔥")
        st.progress(100)
    elif score == 3:
        st.warning("⚠️ Your password is **Medium**. Almost strong!")
        st.progress(75)
    else:
        st.error("❌ Your password is **Weak**. Improve it for better security.")
        st.progress(40)

    # --- Suggestions ---
    if feedback:
        st.markdown("### 🔧 Suggestions to Improve:")
        for msg in feedback:
            st.markdown(f"<div class='suggestions'>• {msg}</div>", unsafe_allow_html=True)
elif check and not password:
    st.info("⚠️ Please enter a password to check.")

# --- End container ---
st.markdown("</div>", unsafe_allow_html=True)


