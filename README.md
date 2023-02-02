# Attendance-Management-System-using-Face-Recognition

# Project Summary :
This Attendance management system is a complete GUI
based application which can act as a virtual assistant for taking attendance
(Using Python package - Tkinter).
1) This Application consist of a Login facility for current users and even a Signup facility
for new users. Login and Signup facility uses MySQL database for managing and
verifying usernames and corresponding passwords. (python package- mysql.connector)
2) “Take Attendance” allows the user to upload a video from a local camera system to the
computer with the date on which it was captured. This video will be converted into a
series of frames from which faces will be recognized and accordingly attendance will be
marked. (Python package- face_recognition)
S. No. Name of Students Roll No.
1 Bhumik Hemant Patil BT21ECE034
2 Abhishek Paithankar BT21ECE036
3 Meshram Pratik Bandu BT21ECE039
4 Ashay Anand Atkar BT21ECE060
2
3) “Image Register” allows the user to register an image of new student (Preferably of high
quality) with which faces in the uploaded video will be compared and attendance will be
marked only if face is present in the video for a considerable time.
(Python package – Pillow, OpenCV)
4) “Get Attendance Data” is a user-friendly function of AMS which displays Absentees and
Presentees on a specific entered date using a date picker calendar in a systematic way.
(Python package - datetime)
