# =============================================================
# Face Recognition Attendance System
# Author  : V. Manoj Kumar
# File    : main.py  (entry point — run this file to start)
# Description:
#   Main menu for the attendance system. Choose an option to
#   check the camera, capture images, train the model, or
#   start recognizing faces and marking attendance.
# =============================================================

from Capture_Image import capture_images
from Train_Image import train_images
from Recognize import recognize_attendence
from check_camera import check_camera


def main_menu():
    while True:
        print("\n" + "=" * 45)
        print("   Face Recognition Attendance System")
        print("=" * 45)
        print("  1. Check Camera")
        print("  2. Capture Student Face Images")
        print("  3. Train Recognition Model")
        print("  4. Recognize Faces & Mark Attendance")
        print("  5. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\n[INFO] Opening camera test...")
            check_camera()

        elif choice == "2":
            print("\n[INFO] Starting image capture...")
            capture_images()

        elif choice == "3":
            print("\n[INFO] Training face recognition model...")
            train_images()

        elif choice == "4":
            print("\n[INFO] Starting face recognition & attendance...")
            recognize_attendence()

        elif choice == "5":
            print("\n[INFO] Exiting. Goodbye!")
            break

        else:
            print("\n[WARNING] Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main_menu()
