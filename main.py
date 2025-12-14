import streamlit as st
from enrollment_and_verification import enrollment, verification

st.set_page_config(page_title="Biometric System", layout="centered")

st.title("🔐 Biometric Authentication System")

option = st.radio(
    "Select Mode",
    ["Enrollment", "Verification"]
)

username = st.text_input("Enter Username")

if option == "Enrollment":
    st.info("📷 Capture your face to enroll.")
    img_file = st.camera_input("Take a picture")
    
    if img_file is not None:
        if st.button("Complete Enrollment"):
            if not username:
                st.warning("Please enter a username first")
            else:
                success, message = enrollment(username, img_file)
                if success:
                    st.success(message)
                else:
                    st.error(message)

elif option == "Verification":
    st.info("📷 Capture your face to verify.")
    img_file = st.camera_input("Take a picture")

    if img_file is not None:
        if st.button("Verify Identity"):
            if not username:
                st.warning("Please enter a username first")
            else:
                success, message = verification(username, img_file)
                if success:
                    st.success(message)
                else:
                    st.error(message)
