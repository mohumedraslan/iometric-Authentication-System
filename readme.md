# 🔐 Biometric Authentication System

This project is a **Face-Based Biometric Authentication System** built using **Python**, **Streamlit**, and **DeepFace**. It allows users to **enroll** their facial data and later **verify** their identity using a webcam.

---

## 📁 Project Structure

```
.
├── database/                     # Stores enrolled user face images
├── video/                        # (Optional) video resources
├── enrollment_and_verification.py# Core enrollment & verification logic
├── main.py                       # Streamlit application entry point
├── .gitignore
└── README.md
```

---

## 🚀 Features

- 👤 User Enrollment using face capture
- 🔍 Face Verification against stored data
- 🧠 DeepFace-powered facial recognition
- 🌐 Simple and interactive Streamlit UI

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit** – for the web interface
- **DeepFace** – for face recognition
- **OpenCV** – image handling

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohumedraslan/Biometric-Authentication-System
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit deepface opencv-python
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

---

## 🧪 How It Works

### Enrollment
- Enter a username
- Capture a face image using the webcam
- Image is saved in the `database/` directory

### Verification
- Enter the same username
- Capture a new face image
- DeepFace compares it with the stored image

---

## ⚠️ Notes

- Ensure good lighting for accurate face detection
- Each username must be unique
- Images are stored locally (no cloud storage)

---

## 👥 Contributors

- [@mohumedraslan](https://github.com/mohumedraslan)
- [@HamdyHegazy](https://github.com/HamdyHegazy)
- [@eyadeltabal](https://github.com/eyadeltabal1)


