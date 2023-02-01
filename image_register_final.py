# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:38:10 2022

@author: Yogita Hemant Patil
"""

from tkinter import *
from PIL import Image, ImageTk
import PIL
import os
from tkinter import filedialog
import cv2 as cv
import time
import Attendance_GUI


class Image_register:
    def main_menu(self):
        self.root.destroy()
        self.home_root = Tk()
        self.obj = Attendance_GUI.home_page(self.home_root)
        self.home_root.mainloop()

    def __init__(self, root):
        self.root = root
        self.root.title("Image registration")
        self.root.geometry("1000x500+0+0")

    def fileopenimage(self):
        self.filepath = filedialog.askopenfilename()
        self.file = os.path.splitext(self.filepath)
        self.file_extension = self.file[1]
        self.student_photo = Image.open(self.filepath)
        self.student_photo1 = self.student_photo.resize(
            (400, 500), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(self.student_photo1)
        self.lblimage = Label(
            self.frame2, image=self.photoimage1, bd=4, relief=RAISED)
        self.lblimage.pack(side=RIGHT, fill=Y)
        self.imagepathdir = r"D:\BHUMIK\VNIT NAGPUR BTECH\3rd_Sem\OOPS\PROJECT\images"
        os.chdir(self.imagepathdir)
        imagepath = f"{self.name.get()}.png"
        self.student_photo.save(imagepath)

    def take_photo(self):
        cv.waitKey(1)
        self.cap = cv.VideoCapture(0)
        self.start = time.time()
        while True:
            self.success, self.img = self.cap.read()
            self.imgS = cv.resize(self.img, (0, 0), None, 1, 1)
            self.imgS = cv.cvtColor(self.imgS, cv.COLOR_BGR2RGB)
            cv.imshow('t', self.imgS)
            self.intermediate = time.time()
            if (self.intermediate - self.start > 5):
                cv.destroyAllWindows()
                break

            cv.waitKey(1)
        self.imagepathdir = r"D:\BHUMIK\VNIT NAGPUR BTECH\3rd_Sem\OOPS\PROJECT\images"
        os.chdir(self.imagepathdir)
        self.imagepath = f"{self.roll_no.get()}_{self.name.get()}.png"
        cv.imwrite(self.imagepath, self.imgS)
        self.cap.release()
        self.student_photo_2 = Image.open(self.imagepath)
        self.student_photo2 = self.student_photo_2.resize(
            (400, 500), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(self.student_photo2)
        self.lblimage = Label(
            self.frame2, image=self.photoimage2, bd=4, relief=RAISED)
        self.lblimage.pack(side=RIGHT, fill=Y)

    def gui(self):

        # ============Image==============
        blankdp = r"D:\BHUMIK\VNIT NAGPUR BTECH\3rd_Sem\OOPS\PROJECT\blankdp.jpg"
        self.frame2 = Frame(self.root, width=410,
                            height=500, relief=SUNKEN, bg='blue')
        self.frame2.place(x=590, y=0)
        self.image1 = Image.open(blankdp)
        self.image1 = self.image1.resize((400, 500), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(self.image1)
        self.lblimage = Label(
            self.frame2, image=self.photoimage1, bd=4, relief=RAISED)
        self.lblimage.pack(side=RIGHT, fill=Y)

        # ===================Blue frame ================
        self.main_frame = Frame(self.root, width=590,
                                height=500, relief=SUNKEN, bg='blue')
        self.main_frame.place(x=0, y=0)

        self.roll_no = StringVar()
        self.name = StringVar()

        self.lroll_no = Label(self.main_frame, text="Roll_no",
                              font="comicsans 15 bold", bg='blue', fg='white', width=17)
        self.lroll_no.place(x=85, y=200)
        self.lname = Label(self.main_frame, text="Name",
                           font="comicsans 15 bold", bg='blue', fg='white', width=17)
        self.lname.place(x=85, y=250)

        self.ename = Entry(
            self.main_frame, textvariable=self.roll_no, width=25)
        self.ename.place(x=362, y=205)
        self.ename = Entry(self.main_frame, textvariable=self.name, width=25)
        self.ename.place(x=362, y=255)

        self.button_from_file = Button(text="Take photo from system", font="comicsans 10 bold",
                                       bg='white', fg='black', width=20, height=1, command=self.fileopenimage)
        self.button_from_file.place(x=147, y=300)

        self.button_from_camera = Button(text="Take photo from Camera", font="comicsans 10 bold",
                                         bg='white', fg='black', width=20, height=1, command=self.take_photo)
        self.button_from_camera.place(x=354, y=300)

        self.button_main_menu = Button(text="Main Menu", font="comicsans 10 bold",
                                       bg='white', fg='black', width=20, height=1, command=self.main_menu)
        self.button_main_menu.place(x=250, y=370)
