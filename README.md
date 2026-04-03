# 🎓 Face Recognition Attendance System

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Face%20Recognition-green?logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🧭 Project Overview

A Python-based **Face Recognition Attendance System** that automates student attendance using a webcam. The system captures student face images, trains an LBPH (Local Binary Pattern Histogram) face recognition model, and marks attendance automatically with date and time — saving everything to a CSV file.

No manual roll calls. No proxy attendance. Just real-time face recognition.

---

## 📌 Features

- 📷 Capture student face images using webcam
- 🧠 Train a face recognition model using the LBPH algorithm
- 👤 Recognize registered students in real time
- ✅ Automatically mark attendance with date and time
- 🎨 Color-coded confidence display (green / yellow / red)
- 📝 Save attendance to a timestamped CSV file
- 🎥 Camera test utility included

---

## 🗂️ Project Structure

```
Attendance-project/
│
├── main.py                              # Main menu — run this to start
├── Capture_Image.py                     # Step 1: Capture student face images
├── Train_Image.py                       # Step 2: Train the recognition model
├── Recognize.py                         # Step 3: Recognize faces & mark attendance
├── check_camera.py                      # Utility: test if webcam is working
├── haarcascade_frontalface_default.xml  # Pre-trained face detection model (Haar Cascade)
├── Trainner.yml                         # Saved LBPH trained model
├── StudentDetails/
│   └── StudentDetails.csv               # Registered student ID & name records
├── Attendance/
│   └── Attendance_YYYY-MM-DD_HH-MM-SS.csv  # Auto-generated attendance files
└── TrainingImageLabel/
    └── Trainner.yml                     # Model weights (generated after training)
```

---

## 🔧 Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| OpenCV | Face detection (Haar Cascade) + LBPH recognition |
| NumPy | Image array processing |
| Pandas | CSV read/write for student & attendance data |
| Pillow (PIL) | Image capture and preprocessing |

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Manojkumar1910/Attendence--project.git
cd Attendence--project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create required folders
```bash
mkdir StudentDetails TrainingImageLabel Attendance TrainingImage
```

---

## ▶️ How to Run

Launch the main menu:
```bash
python main.py
```

### Menu Options

| Option | Action |
|--------|--------|
| 1 | Check camera |
| 2 | Capture student face images |
| 3 | Train the recognition model |
| 4 | Start face recognition & mark attendance |
| 5 | Exit |

---

## 📸 Step-by-Step Usage

**Step 1 — Capture Images**
Select option 2, enter the student's ID and name. The system captures 100 face images and saves them to the `TrainingImage/` folder.

**Step 2 — Train the Model**
Select option 3. The system trains an LBPH model on all captured images and saves it as `Trainner.yml`.

**Step 3 — Recognize & Mark Attendance**
Select option 4. The webcam opens and starts recognizing faces. Confidence is shown as a percentage:
- 🟢 Green (>67%) — recognized and attendance marked
- 🟡 Yellow (50–67%) — low confidence
- 🔴 Red (<50%) — not recognized

**Output** — Attendance saved as:
```
Attendance/Attendance_2025-01-15_09-30-00.csv
```
```
Id | Name | Date       | Time
1  | John | 2025-01-15 | 09:30:01
```

---

## 📊 How it Works

```
Webcam feed
    ↓
Haar Cascade face detection
    ↓
LBPH model prediction
    ↓
Confidence check (threshold: 67%)
    ↓
Match found → Log ID, Name, Date, Time to CSV
```

---

## 🚀 Future Improvements

- [ ] GUI using Tkinter or Streamlit
- [ ] Database integration (MySQL / Firebase)
- [ ] Email/SMS notification when attendance is marked
- [ ] Face mask detection support
- [ ] Multi-camera support
- [ ] Cloud attendance storage and dashboard

---

## 📋 Output Preview

> 📌 *Add a screenshot or GIF of the webcam recognizing a face here:*
> ```markdown
> ![Demo](images/demo.gif)
> ```

---

## 👤 Author

**V. Manoj Kumar**
- GitHub: [@Manojkumar1910](https://github.com/Manojkumar1910)
- Domain: AI & Data Science

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## ⭐ If you found this useful, give it a star!, give it a star!
