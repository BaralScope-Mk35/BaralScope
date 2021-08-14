#https://qiita.com/kotai2003/items/3d31528d56059c848458

import tkinter as tk
from tkinter import ttk
import cv2
import PIL.Image,PIL.ImageTk
from tkinter import font
from tkinter import messagebox
import serial
import LCD1602
import RPi.GPIO as GPIO
import time
import datetime
import os
import sys

now=str(datetime.date.today())
print(now)
x_pos=0
y_pos=0
z_pos=0

#Led_pin=18
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(Led_pin,GPIO.OUT)
#Led=GPIO.PWM(Led_pin,50)
#Led.start(0)

print("Open Port")
ser=serial.Serial('/dev/ttyUSB0',9600)
time.sleep(2)

def message():
    LCD1602.init(0x27, 1)   # init(slave address, background light)
    LCD1602.write(0, 0, '>')
    time.sleep(0.05)
    LCD1602.write(0, 0, '>>>')
    time.sleep(0.05)
    LCD1602.write(0, 0, '>>>>>')
    time.sleep(0.05)
    LCD1602.write(0, 0, '>>>>>>>')
    time.sleep(0.05)
    LCD1602.write(0, 0, '>>>>>>>>>')
    time.sleep(0.05)
    LCD1602.write(0, 0, '>>>>>>>>>>')
    time.sleep(0.05)
    LCD1602.write(0, 1, '         <')
    time.sleep(0.05)
    LCD1602.write(0, 1, '       <<<')
    time.sleep(0.05)
    LCD1602.write(0, 1, '     <<<<<')
    time.sleep(0.05)
    LCD1602.write(0, 1, '   <<<<<<<')
    time.sleep(0.05)
    LCD1602.write(0, 1, '<<<<<<<<<<')
    time.sleep(0.5)
    LCD1602.clear()
    LCD1602.write(0, 0, '++++ Hello! ++++')
    LCD1602.write(0, 1, '%r'%now)
    time.sleep(3)
    LCD1602.clear()
    LCD1602.write(0, 0, 'This is')
    LCD1602.write(0, 1, '\'ScopeScan\'')
    time.sleep(3)
    LCD1602.clear()
    LCD1602.write(0, 0, 'created by')
    LCD1602.write(0, 1, 'Tk Inc.')
    time.sleep(4)
    LCD1602.clear()
    #LCD1602.write(0, 0, 'Initializing')
    #LCD1602.write(0, 1, '.')
    #time.sleep(1)
    #LCD1602.write(0, 1, '...')
    #time.sleep(1)
    #LCD1602.write(0, 1, '.....')
    #time.sleep(1)
    #LCD1602.write(0, 1, '.......')
    #time.sleep(1)
    #LCD1602.write(0, 1, '.........')
    #time.sleep(1)
    #LCD1602.write(0, 1, '...........')
    #time.sleep(1)
    #LCD1602.write(0, 1, '.............')
    #time.sleep(1)
    LCD1602.clear()
    #LCD1602.write(0, 0, '<< Complete!! >>')
    #LCD1602.write(0, 1, ' Enjoy Scope!! ')
    time.sleep(3)
    LCD1602.clear()
    LCD1602.write(0, 0, 'x;  0 , y; 0 ')
    LCD1602.write(0, 1, 'z;  0 ')

class Application(tk.Frame):
    def __init__(self,master, video_source=0):
        super().__init__(master)

        self.master.geometry("1000x580")
        self.master.title("Video Streaming and Snapshot")

        # ---------------------------------------------------------
        # Font
        # ---------------------------------------------------------
        self.font_frame = font.Font( family="Meiryo UI", size=15, weight="normal" )
        self.font_btn_big = font.Font( family="Meiryo UI", size=20, weight="bold" )
        self.font_btn_small = font.Font( family="Meiryo UI", size=15, weight="bold" )

        self.font_lbl_bigger = font.Font( family="Meiryo UI", size=45, weight="bold" )
        self.font_lbl_big = font.Font( family="Meiryo UI", size=30, weight="bold" )
        self.font_lbl_middle = font.Font( family="Meiryo UI", size=15, weight="bold" )
        self.font_lbl_small = font.Font( family="Meiryo UI", size=12, weight="normal" )

        # ---------------------------------------------------------
        # Open the video source
        # ---------------------------------------------------------

        self.vcap = cv2.VideoCapture( video_source )
        self.width = self.vcap.get( cv2.CAP_PROP_FRAME_WIDTH )
        self.height = self.vcap.get( cv2.CAP_PROP_FRAME_HEIGHT )

        # ---------------------------------------------------------
        # Widget and action
        # ---------------------------------------------------------

        self.create_widgets()

        # ---------------------------------------------------------
        # Canvas Update
        # ---------------------------------------------------------

        self.delay = 15 #[mili seconds]
        self.update()


    def create_widgets(self):
        global txt_0,txt_1,scale

        #Frame_Camera
        self.frame_cam = tk.LabelFrame(self.master, text = 'Camera', font=self.font_frame)
        self.frame_cam.place(x = 10, y = 10)
        self.frame_cam.configure(width = self.width+30, height = self.height+70)
        self.frame_cam.grid_propagate(0)

        #Canvas
        self.canvas1 = tk.Canvas(self.frame_cam)
        self.canvas1.configure( width= self.width, height=self.height)
        self.canvas1.place(x=10, y=10)
        
        # 3axis stage
        self.frame_axis = tk.LabelFrame(self.master, text = '3axis stages', font=self.font_frame)
        self.frame_axis.place(x = 700, y = 10)
        self.frame_axis.configure(width = 285, height = 335)
        self.frame_axis.grid_propagate(0)
        
        #self.frame_axis = tk.LabelFrame(self.master, text = 'brightness', font=self.font_frame)
        #self.frame_axis.place(x = 700, y = 325)
        #self.frame_axis.configure(width = 285, height = 80)
        #self.frame_axis.grid_propagate(0)
        
        # ラベル
        lbl_0 = tk.Label(text='x-stage',font=("MSゴシック", "10", "bold"))
        lbl_0.place(x=813, y=43)
        lbl_1 = tk.Label(text='y-stage',font=("MSゴシック", "10", "bold"))
        lbl_1.place(x=813, y=97)
        lbl_2 = tk.Label(text='z-stage',font=("MSゴシック", "10", "bold"))
        lbl_2.place(x=813, y=152)
        lbl_3 = tk.Label(text='HOME position',font=("MSゴシック", "10", "bold"))
        lbl_3.place(x=795, y=215)
        lbl_4 = tk.Label(text='Auto Focus',font=("MSゴシック", "10", "bold"))
        lbl_4.place(x=805, y=275)
        lbl_5 = tk.Label(text='save to',font=("MSゴシック", "10", "bold"))
        lbl_5.place(x=715, y=355)
        lbl_6 = tk.Label(text='name',font=("MSゴシック", "10", "bold"))
        lbl_6.place(x=715, y=395)
        
        # ボタン
        btn_x_h = tk.Button(self.master, text='HOME',bg='salmon')
        btn_x_h.bind('<Button-1>',self.event_test)
        btn_x_h.extra="c"
        btn_x_h.place(x=815, y=65)
        btn_x_r_s = tk.Button(self.master, text=' >  ',bg='coral')
        btn_x_r_s.bind('<Button-1>',self.event_test)
        btn_x_r_s.extra="d"
        btn_x_r_s.place(x=875, y=65)
        btn_x_r_l = tk.Button(self.master, text=' >> ',bg='tomato')
        btn_x_r_l.bind('<Button-1>',self.event_test)
        btn_x_r_l.extra="e"
        btn_x_r_l.place(x=915, y=65)
        btn_x_l_s = tk.Button(self.master, text=' <  ',bg='coral')
        btn_x_l_s.bind('<Button-1>',self.event_test)
        btn_x_l_s.extra="b"
        btn_x_l_s.place(x=775, y=65)
        btn_x_l_l = tk.Button(self.master, text=' <<  ',bg='tomato')
        btn_x_l_l.bind('<Button-1>',self.event_test) 
        btn_x_l_l.extra="a"
        btn_x_l_l.place(x=725, y=65)

        btn_y_h = tk.Button(self.master, text='HOME',bg='greenyellow')
        btn_y_h.bind('<Button-1>',self.event_test)
        btn_y_h.extra="h"
        btn_y_h.place(x=815, y=120)
        btn_y_r_s = tk.Button(self.master, text=' >  ', bg='chartreuse')
        btn_y_r_s.bind('<Button-1>',self.event_test)
        btn_y_r_s.extra="i"
        btn_y_r_s.place(x=875, y=120)
        btn_y_r_l = tk.Button(self.master, text=' >> ',bg='lawngreen')
        btn_y_r_l.bind('<Button-1>',self.event_test)
        btn_y_r_l.extra="j"
        btn_y_r_l.place(x=915, y=120)
        btn_y_l_s = tk.Button(self.master, text=' <  ',bg='chartreuse')
        btn_y_l_s.bind('<Button-1>',self.event_test)
        btn_y_l_s.extra="g"
        btn_y_l_s.place(x=775, y=120)
        btn_y_l_l = tk.Button(self.master, text=' <<  ',bg='lawngreen')
        btn_y_l_l.bind('<Button-1>',self.event_test)
        btn_y_l_l.extra="f"
        btn_y_l_l.place(x=725, y=120)

        btn_z_h = tk.Button(self.master, text='HOME',bg='skyblue')
        btn_z_h.bind('<Button-1>',self.event_test)
        btn_z_h.extra="m"
        btn_z_h.place(x=815, y=175)
        btn_z_r_s = tk.Button(self.master, text=' >  ',bg='lightskyblue')
        btn_z_r_s.bind('<Button-1>',self.event_test)
        btn_z_r_s.extra="n"
        btn_z_r_s.place(x=875, y=175)
        btn_z_r_l = tk.Button(self.master, text=' >> ',bg='deepskyblue')
        btn_z_r_l.bind('<Button-1>',self.event_test)
        btn_z_r_l.extra="o"
        btn_z_r_l.place(x=915, y=175)
        btn_z_l_s = tk.Button(self.master, text=' <  ',bg='lightskyblue')
        btn_z_l_s.bind('<Button-1>',self.event_test)
        btn_z_l_s.extra="l"
        btn_z_l_s.place(x=775, y=175)
        btn_z_l_l = tk.Button(self.master, text=' <<  ',bg='deepskyblue')
        btn_z_l_l.bind('<Button-1>',self.event_test)
        btn_z_l_l.extra="k"
        btn_z_l_l.place(x=725, y=175)

        btn_h = tk.Button(self.master, text='  HOME (all axis)  ', bg='gold')
        btn_h.bind('<Button-1>',self.event_test)
        btn_h.extra="p"
        btn_h.place(x=781, y=238)
        
        btn_af = tk.Button(self.master, text='      Auto Focus      ', bg='orange', command=self.press_af_button)
        btn_af.bind('<Button-1>',self.event_test)
        btn_af.extra="m"
        btn_af.place(x=781, y=298)

        btn_f = tk.Button(self.master, text=' register ', bg='darkgrey',command=self.btn_click_0)
        btn_f.place(x=900, y=370)
        btn_sam = tk.Button(self.master, text=' register ', bg='darkgrey',command=self.btn_click_1)
        btn_sam.place(x=900, y=418)

        snap = tk.Button(self.master, text='                              Snapshot                              ',bg='darkturquoise', command=self.press_snapshot_button)
        snap.configure(width=34,height=2)
        snap.place(x=710, y=465)
        
        # close btn
        close = tk.Button(self.master, text='                                  close                                  ',bg='darkgrey', command=self.press_close_button)
        close.bind('<Button-1>',self.event_test)
        close.extra="p"
        close.configure(width=34,height=1)
        close.place(x=710, y=525)

        # テキストボックス
        txt_0 = tk.Entry(width=25)
        txt_0.insert(tk.END,"/home/pi")
        txt_0.place(x=710, y=375)
        txt_1 = tk.Entry(width=25)
        txt_1.insert(tk.END,"hippocampus")
        txt_1.place(x=710, y=420)
        
        # scale (slider)
        #scale = tk.Scale(self.master,variable=0,orient=tk.HORIZONTAL,length=240,command=self.bright)
        #scale.place(x=720, y=353)
    
    #def bright(self,event):
    #    Led.ChangeDutyCycle(scale.get())
    
    def update(self):
        #Get a frame from the video source
        _, frame = self.vcap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))

        #self.photo -> Canvas
        self.canvas1.create_image(0,0, image= self.photo, anchor = tk.NW)
        self.master.after(self.delay, self.update)

    def press_snapshot_button(self):
        # Get a frame from the video source
        _, frame = self.vcap.read()
        directory = txt_0.get()
        os.chdir(directory)
        fn = txt_1.get()
        LCD1602.clear()
        LCD1602.write(0, 0, '|| SnapShot! ||')
        time.sleep(2)
        LCD1602.clear()
        LCD1602.write(0, 0, r'x; %d, y; %d'%(x_pos,y_pos))
        LCD1602.write(0, 1, 'z; %d '%z_pos)
        frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.imwrite( fn + "_" + time.strftime( "%Y-%d-%m-%H-%M-%S" ) + ".jpg",
                     cv2.cvtColor( frame1, cv2.COLOR_BGR2RGB ) )

    def press_af_button(self):
        _, frame = self.vcap.read()
        frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        lap=cv2.Laplacian(frame1,cv2.CV_64F)
        
        while lap.var()<15:
            command='q'
            ser.write(command.encode())
            time.sleep(0.5)
            _, frame = self.vcap.read()
            frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            lap=cv2.Laplacian(frame1,cv2.CV_64F)
            print(lap.var())
            
        while lap.var()<20:
            command='l'
            ser.write(command.encode())
            time.sleep(0.5)
            _, frame = self.vcap.read()
            frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            lap=cv2.Laplacian(frame1,cv2.CV_64F)
            print(lap.var())
        
        while lap.var()<25:
            command='r'
            ser.write(command.encode())
            time.sleep(0.5)
            _, frame = self.vcap.read()
            frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            lap=cv2.Laplacian(frame1,cv2.CV_64F)
            print(lap.var())

    
    def press_close_button(self):
        LCD1602.clear()
        LCD1602.write(0, 0, '|| Good Bye! ||')
        time.sleep(2)
        #Led.stop(0)
        LCD1602.clear()
        self.master.destroy()
        self.vcap.release()
        #GPIO.cleanup()
        sys.exit()
    
    def btn_click_0(self):
        global directory
        # テキスト取得
        directory = txt_0.get()
        messagebox.showinfo('確認', 'directory registered')
        print("directory; "+directory)
        os.chdir(directory)
        
    def btn_click_1(self):
        global fn
        # テキスト取得
        fn = txt_1.get()
        messagebox.showinfo('確認', 'filename registered')
        print("filename; "+fn)
        
    def event_test(self,event):
        global x_pos,y_pos,z_pos
        command=event.widget.extra
        ser.write(command.encode())
        if command == 'a':
            x_pos-=2.0
        elif command == 'b':
            x_pos-=1.0
        elif command == 'c':
            x_pos = 0
        elif command == 'd':
            x_pos+=1.0
        elif command == 'e':
            x_pos+=2.0
        elif command == 'f':
            y_pos-=2.0
        elif command == 'g':
            y_pos -=1.0 
        elif command == 'h':
            y_pos=0
        elif command == 'i':
            y_pos+=1.0
        elif command == 'j':
            y_pos+=2.0
        elif command == 'k':
            z_pos-=2.0
        elif command == 'l':
            z_pos -=1.0 
        elif command == 'm':
            z_pos=0
        elif command == 'n':
            z_pos+=1.0
        elif command == 'o':
            z_pos+=2.0
        elif command == 'p':
            x_pos=0
            y_pos=0
            z_pos=0
        time.sleep(0.5)
        _, frame = self.vcap.read()
        frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        lap=cv2.Laplacian(frame1,cv2.CV_64F)
        print("button; "+str(command))
        print("x position; "+str(event.x_root))
        print("y position; "+str(event.y_root))
        print("Laplacian; " +str(lap.var()))
        LCD1602.clear()
        LCD1602.write(0, 0, r'x; %d, y; %d'%(x_pos,y_pos))
        LCD1602.write(0, 1, 'z; %d '%z_pos)


def main():
    message()
    root = tk.Tk()
    # "window close button"  invalidation
    root.protocol('WM_DELETE_WINDOW',(lambda:'pass')())
    app = Application(master=root)#Inherit
    app.mainloop()

if __name__ == "__main__":
    main()

