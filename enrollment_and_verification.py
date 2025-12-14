from deepface import DeepFace
import cv2 as cv
import os

# Ensure database directory exists
if not os.path.exists("database"):
    os.makedirs("database")

def enrollment(username, image_buffer):
    """
    Saves the user's face image to the database.
    """
    if not username:
        return False, "❌ Username cannot be empty"

    # Sanitize username to prevent path issues
    safe_username = "".join([c for c in username if c.isalpha() or c.isdigit() or c in (' ', '_', '-')]).strip()
    if not safe_username:
         return False, "❌ Invalid username"

    file_path = f'database/{safe_username}.jpg'
    
    if os.path.exists(file_path):
        return False, f"❌ Username '{safe_username}' already exists"
    
    try:
        # image_buffer is a BytesIO object from streamlit
        with open(file_path, "wb") as f:
            f.write(image_buffer.getvalue())
        return True, f"✅ Enrollment successful for {safe_username}"
    except Exception as e:
        return False, f"❌ Enrollment failed: {str(e)}"


def verification(username, image_buffer):
    """
    Verifies the captured image against the stored user image.
    """
    if not username:
        return False, "❌ Username cannot be empty"

    safe_username = "".join([c for c in username if c.isalpha() or c.isdigit() or c in (' ', '_', '-')]).strip()
    registered_img = f"database/{safe_username}.jpg"

    # Check if user exists
    if not os.path.exists(registered_img):
        return False, "❌ User not found in database"

    temp_img = "temp_verify.jpg"
    try:
        # Save temp image for DeepFace
        with open(temp_img, "wb") as f:
            f.write(image_buffer.getvalue())

        # Perform verification
        result = DeepFace.verify(
            img1_path=registered_img,
            img2_path=temp_img,
            enforce_detection=True
        )
        
        if result["verified"]:
            return True, "✅ Verification successful"
        else:
            return False, "❌ Face does not match"

    except Exception as e:
        return False, f"❌ Verification error: {str(e)}"
    finally:
        # Cleanup temp file
        if os.path.exists(temp_img):
            os.remove(temp_img)

