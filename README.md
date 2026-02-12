# 🎓 Face Recognition Attendance System

A Python-based Face Recognition Attendance System that captures student
face images, trains a recognition model, and marks attendance
automatically using a webcam.

This project uses **OpenCV**, **Python**, and **LBPH Face Recognizer**
to detect and recognize faces in real time.

------------------------------------------------------------------------

## 📌 Features

-   📷 Capture student face images using webcam\
-   🧠 Train images using LBPH Face Recognition algorithm\
-   👤 Recognize students in real-time\
-   📝 Automatically mark attendance with date and time\
-   🎥 Camera testing feature\
-   🖥️ Simple command-line menu interface

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python\
-   OpenCV\
-   NumPy\
-   Pandas\
-   Pillow (PIL)

------------------------------------------------------------------------

## 📂 Project Structure

    Project-Attendance/
    │
    ├── Capture_Image.py        # Capture student images
    ├── Train_Image.py           # Train face recognition model
    ├── Recognize.py              # Recognize faces & mark attendance
    ├── check_camera.py           # Test webcam
    ├── homge.py                  # Main menu file
    ├── haarcascade_frontalface_default.xml  # Face detection model
    ├── Trainner.yml              # Trained model file

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/your-username/Face-Recognition-Attendance-System.git
cd Face-Recognition-Attendance-System
```

### 2️⃣ Install Required Libraries

``` bash
pip install opencv-python numpy pandas pillow
```

------------------------------------------------------------------------

## ▶️ How to Run the Project

Run the main file:

``` bash
python homge.py
```

### Menu Options:

  Option   Function
  -------- -----------------------------
  1        Check Camera
  2        Capture Student Faces
  3        Train Images
  4        Recognize & Mark Attendance
  5        Exit

------------------------------------------------------------------------

## 📸 Steps to Use

### 🔹 Step 1: Capture Images

Enter student ID and name. The system captures face images and saves
them.

### 🔹 Step 2: Train Images

Train the captured images to create a recognition model.

### 🔹 Step 3: Recognize & Attendance

The system recognizes faces and stores attendance with date and time.

------------------------------------------------------------------------

## 📊 Output

Attendance is saved in a CSV file with:

    Id | Name | Date | Time

------------------------------------------------------------------------

## 🚀 Future Improvements

-   GUI using Tkinter or Streamlit\
-   Database integration (MySQL/Firebase)\
-   Cloud attendance storage\
-   Face mask detection\
-   Multi-camera support

------------------------------------------------------------------------

## 👨‍💻 Author

**V. Manoj Kumar**\
AI & Data Science Student

------------------------------------------------------------------------

## ⭐ If you like this project, give it a star!
