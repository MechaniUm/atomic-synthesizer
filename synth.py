from serial import Serial
import sqlite3 as sql
from time import sleep
from PIL import ImageTk
from PIL import Image as PilImage
from tkinter import *
import tkinter.font
from threading import Thread
import pygame
import json
import RPi.GPIO as GPIO
from config import *
import math
def insert_newlines(string, w_max=50):
    l = len(string)
    s = ""
    w = 0
    idx = 0
    i = 0
    while i < l:
        if string[i] == ' ':
            idx = i
        if w > w_max:
            if i == ' ':
                s+='\n'
                w=0
            else:
                if not idx == i:
                    s=s[:(idx - i)]
                s+='\n'
                i=idx
                w=0
        else:
            s+=string[i]
        w+=1
        i+=1
    return s

class Application(Frame):

    def set_volume(self, volume):
        self.sounds['ok'].set_volume(volume / 1000)
        self.sounds['info'].set_volume(volume / 1000)
        self.sounds['error'].set_volume(volume / 1000)

    def create_widgets(self):
        self.c = Canvas(self, height = 600, width = 1024)
        self.c.pack()
        #images
        self.background_img = self.c.create_image(0,0,image=self.background_filename,anchor=NW, tag='main')
        self.info_img = self.c.create_image(0,0,image=self.info_filename, tag='info', anchor=NW)
        self.question_img = self.c.create_image(0,0,image=self.question_filename, tag='question', anchor=NW)
        self.logo_img = self.c.create_image(0,0,image=self.logo_filename, tag='logo', anchor=NW)
        self.out_of_p_img = self.c.create_image(0,0,image=self.out_of_p_filename, tag='out_of_p', anchor=NW)
        self.error_img = self.c.create_image(0,0,image=self.error_filename, tag='error', anchor=NW)
        #labels
        self.element_name = self.c.create_text(248,73,font='FuturaPT 30', tag='main', fill="#1b3660")
        self.element_logo = self.c.create_text(245,278, font='FuturaPt 144', tag='main', fill="#1b3660")
        #self.element_sublogo = self.c.create_text(170,220, font='FuturaPt 20', anchor=E, tag='main', fill="#1b3660")
        self.element_subname = self.c.create_text(248,119, font='FuturaPt 20', tag='main')
        self.element_number = self.c.create_text(248,499, font='FuturaPt 20', tag='main', fill="#F25B25")
        self.element_charge = self.c.create_text(124,499, font='FuturaPt 20', tag='main', fill="#F25B25")
        self.element_weight = self.c.create_text(372,499, font='FuturaPt 20', tag='main', fill="#F25B25")
        self.about = self.c.create_text(500,110, anchor=NW, font='FuturaPt 16', tag='main')
        self.usage = self.c.create_text(500,345, anchor=NW, font='FuturaPt 16', tag='main')
        self.error_text = self.c.create_text(235,280, anchor=NW, font='FuturaPt 18', tag='error')
    def show_question(self):
        self.changed = True
        self.c.tag_raise('question')

    def show_out_of_p(self):
        self.c.tag_raise('out_of_p')
    
    def show_error(self, error, p=0, n1=0, n2=0):
        if error == 1:
            self.c.itemconfigure(self.error_text, text=insert_newlines("Для данного числа протонов существуют изотопы с числом нейтронов в диапазоне от " + str(n1) + " до " + str(n2) + "."))
        elif error == 0:
            self.c.itemconfigure(self.error_text, text=insert_newlines("Число электронов не должно отличаться от числа протонов более чем на 20"))
        self.c.tag_raise('error')
    
    def wake_up(self):
        self.c.tag_raise('info')
        self.sounds['info'].play()

    def go_to_sleep(self):
        self.c.tag_raise('logo')

    def error_signal(self):
        GPIO.output(18, GPIO.LOW)
        sleep(0.1)
        GPIO.output(15, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        self.sounds['error'].play()

    def ok_signal(self):
        GPIO.output(18, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(15, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        self.sounds['ok'].play()
    
    def split_text_to_array(self, string):
        tmp = [""]
        i = 0
        words = string.split()
        for w in words:
            tmp[i] = tmp[i] + w + " "
            if len(tmp[i]) > 250:
                tmp[i] = tmp[i][:-1] + '...'
                i+=1
                tmp.append("")
        if tmp[-1] == "":
            tmp.pop(-1)
            tmp[-1]=tmp[-1][:-2]
        return tmp
    
    def update_gui(self):
        self.show_question()
        if (self.data['p'] == 0):
            self.error_signal()
            return
        if (self.data['p'] > 118):
            self.error_signal()
            self.show_out_of_p()
            return
        #conn = sql.connect(folder_path + "synthesizer.db")
        conn = sql.connect(folder_path + "atom.db")
        cursor = conn.cursor()
        cursor.execute(query, {
            "count_n": self.data['n'],
            "count_p": self.data['p'],
        })
        tmp = cursor.fetchone()
        if (tmp == None):
            conn.close()
            conn = sql.connect(folder_path + "atom.db")
            cursor = conn.cursor()
            cursor.execute(error_query, {"count_p": self.data['p']})
            tmp = cursor.fetchall()
            if tmp:
                self.show_error(1, self.data['p'], tmp[0][0], tmp[-1][0])
            self.error_signal()
            conn.close()
            return
        self.ok_signal()
        sleep(7)
        self.description_text = self.split_text_to_array(tmp[3])
        self.usage_text = self.split_text_to_array(tmp[4])
        self.usage_idx = 0
        self.desc_idx = 0
        self.c.itemconfigure(self.element_logo, text=tmp[0])
        #self.c.itemconfigure(self.element_sublogo, text=str(self.data['n'] + self.data['p']))
        #self.text_scroll()
        self.c.itemconfigure(self.about, text=insert_newlines(self.description_text[0]))
        self.c.itemconfigure(self.usage, text=insert_newlines(self.usage_text[0]))
        self.c.itemconfigure(self.element_name, text=tmp[1].upper())
        self.c.itemconfigure(self.element_subname, text=tmp[2].upper())
        self.c.itemconfigure(self.element_charge, text=str(self.data['p'] - self.data['e']))
        self.c.itemconfigure(self.element_weight, text=str(self.data['n'] + self.data['p']))
        self.c.itemconfigure(self.element_number, text=str(self.data['p']))
        self.c.tag_raise('main')
        self.changed = False
        conn.close()
    def text_scroll(self):
        if self.desc_idx < len(self.description_text):
            self.desc_idx += 1
        if self.usage_idx < len(self.usage_text):
            self.usage_idx += 1
        if self.desc_idx == len(self.description_text) and \
             self.usage_idx == len(self.usage_text):
            self.usage_idx = 0
            self.desc_idx = 0
        elif self.desc_idx == len(self.description_text):
            self.desc_idx = len(self.description_text) - 1
        elif self.usage_idx == len(self.usage_text):
            self.usage_idx = len(self.usage_text) - 1
        self.c.itemconfigure(self.about, text=insert_newlines(self.description_text[self.desc_idx]))
        self.c.itemconfigure(self.usage, text=insert_newlines(self.usage_text[self.usage_idx]))
    
    def loop_serial(self):
        try:
            s = Serial("/dev/ttyACM1", 9600, timeout=1)
        except:
            try:
                s = Serial("/dev/ttyACM0", 9600, timeout=1)
            except:
                s = Serial("/dev/ttyUSB0", 9600, timeout=1) 
        while(1):
            try:
                inp = (s.readline())
                msg = str(inp).split("'")[1].split('\n')[0][:-2]
                if (len(msg) == 0):
                    continue
                msg_data = json.loads(msg)
                print(msg_data)
                if (msg_data['event'] == 'button_pressed') and (msg_data['options']['buttonID'] == 1):
                    if abs(int(msg_data['options']['e']) - int(msg_data['options']['p']) > 20):
                        self.show_error(0)
                        self.error_signal()
                    else:
                        self.data['e'] = msg_data['options']['e']
                        self.data['n'] = msg_data['options']['n']
                        self.data['p'] = msg_data['options']['p']
                        self.update_gui()
                if (msg_data['event'] == 'button_pressed') and (msg_data['options']['buttonID'] == 0):
                    self.text_scroll()
                elif (msg_data['event'] == 'wake_up'):
                    self.wake_up()
                elif (msg_data['event'] == 'sleep'):
                    self.go_to_sleep()
                elif (msg_data['event'] == 'new_object'):
                    self.show_question()
                    self.changed=True
                elif (msg_data['event'] == 'set_volume'):
                    self.set_volume(msg_data['options']['volume'])
                elif ((msg_data['event'] == 'stop_sounds') or (msg_data['event'] == 'stop_info')):
                    self.stop_sounds()
            except:
                pass
    
    def stop_sounds(self):
        self.sounds['info'].stop()
        self.sounds['ok'].stop()
        self.sounds['error'].stop()
    
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        pygame.init()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        self.sounds = {
            'ok': pygame.mixer.Sound(folder_path + "Sounds/ok.ogg"),
            'info': pygame.mixer.Sound(folder_path + "Sounds/info.ogg"),
            'error': pygame.mixer.Sound(folder_path + "Sounds/error.ogg"),
        }
        self.load_images()
        self.create_widgets()
        self.changed = False
        self.serial_thread = Thread(target = self.loop_serial)
        self.data = {'n': 0, 'p': 0, 'e': 0}
        self.set_volume(100)
        self.c.tag_raise('logo')
        self.serial_thread.start()
     
    def load_images(self):
        self.background_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/background.png"))
        self.logo_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/logo.png"))
        self.info_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/info.png"))
        self.question_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/question.png"))
        self.out_of_p_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/out_of_p.png"))
        self.error_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/error.png"))


if __name__ == "__main__":
    root = Tk()
    root.attributes("-fullscreen", True) 
    root.title("atomic synthesizer")
    app = Application(master=root)
    app.mainloop()
