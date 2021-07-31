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
from config import *
import math
from random import randrange

try:
    s = Serial("/dev/ttyACM0", 9600, timeout=1)
except:
    try:
        s = Serial("/dev/ttyACM1", 9600, timeout=1)
    except:
        s = Serial("/dev/ttyUSB0", 9600, timeout=1)

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
        # self.background_img = self.c.create_image(0,0,image=self.background_filename,anchor=NW, tag='main')
        self.background_1_img = self.c.create_image(0,0,image=self.background_1_filename,anchor=NW, tag='back-1')
        self.background_2_img = self.c.create_image(0,0,image=self.background_2_filename,anchor=NW, tag='back-2')
        self.background_3_img = self.c.create_image(0,0,image=self.background_3_filename,anchor=NW, tag='back-3')
        self.background_4_img = self.c.create_image(0,0,image=self.background_4_filename,anchor=NW, tag='back-4')
        self.info_img = self.c.create_image(0,0,image=self.info_filename, tag='info', anchor=NW)
        self.question_img = self.c.create_image(0,0,image=self.question_filename, tag='question', anchor=NW) 
        self.logo_img = self.c.create_image(0,0,image=self.logo_filename, tag='logo', anchor=NW)
        self.out_of_p_img = self.c.create_image(0,0,image=self.out_of_p_filename, tag='out_of_p', anchor=NW)
        self.error_img = self.c.create_image(0,0,image=self.error_filename, tag='error', anchor=NW)
        # easter images
        self.easter_img = []
        
        self.easter_1_1 = self.c.create_image(0, 0, image=self.easter_1_1_file, tag='1-1', anchor=NW)        
        self.easter_1_2 = self.c.create_image(0, 0, image=self.easter_1_2_file, tag='1-2', anchor=NW)        
        self.easter_1_3 = self.c.create_image(0, 0, image=self.easter_1_3_file, tag='1-3', anchor=NW)        
        self.easter_1_4 = self.c.create_image(0, 0, image=self.easter_1_4_file, tag='1-4', anchor=NW)        
        self.easter_1_5 = self.c.create_image(0, 0, image=self.easter_1_5_file, tag='1-5', anchor=NW)        
        self.easter_1_6 = self.c.create_image(0, 0, image=self.easter_1_6_file, tag='1-6', anchor=NW)

        
        self.easter_2_1 = self.c.create_image(0, 0, image=self.easter_2_1_file, tag='2-1', anchor=NW)        
        self.easter_2_2 = self.c.create_image(0, 0, image=self.easter_2_2_file, tag='2-2', anchor=NW)        
        self.easter_2_3 = self.c.create_image(0, 0, image=self.easter_2_3_file, tag='2-3', anchor=NW)        
        self.easter_2_4 = self.c.create_image(0, 0, image=self.easter_2_4_file, tag='2-4', anchor=NW)        
        self.easter_2_5 = self.c.create_image(0, 0, image=self.easter_2_5_file, tag='2-5', anchor=NW)        
        self.easter_2_6 = self.c.create_image(0, 0, image=self.easter_2_6_file, tag='2-6', anchor=NW)

        self.easter_3_1 = self.c.create_image(0, 0, image=self.easter_3_1_file, tag='3-1', anchor=NW)        
        self.easter_3_2 = self.c.create_image(0, 0, image=self.easter_3_2_file, tag='3-2', anchor=NW)        
        self.easter_3_3 = self.c.create_image(0, 0, image=self.easter_3_3_file, tag='3-3', anchor=NW)        
        self.easter_3_4 = self.c.create_image(0, 0, image=self.easter_3_4_file, tag='3-4', anchor=NW)        
        self.easter_3_5 = self.c.create_image(0, 0, image=self.easter_3_5_file, tag='3-5', anchor=NW)        
        self.easter_3_6 = self.c.create_image(0, 0, image=self.easter_3_6_file, tag='3-6', anchor=NW)
        
        self.easter_4_1 = self.c.create_image(0, 0, image=self.easter_4_1_file, tag='4-1', anchor=NW)        
        self.easter_4_2 = self.c.create_image(0, 0, image=self.easter_4_2_file, tag='4-2', anchor=NW)        
        self.easter_4_3 = self.c.create_image(0, 0, image=self.easter_4_3_file, tag='4-3', anchor=NW)        
        self.easter_4_4 = self.c.create_image(0, 0, image=self.easter_4_4_file, tag='4-4', anchor=NW)        
        self.easter_4_5 = self.c.create_image(0, 0, image=self.easter_4_5_file, tag='4-5', anchor=NW)        
        self.easter_4_6 = self.c.create_image(0, 0, image=self.easter_4_6_file, tag='4-6', anchor=NW)
        
        self.easter_5_1 = self.c.create_image(0, 0, image=self.easter_5_1_file, tag='5-1', anchor=NW)        
        self.easter_5_2 = self.c.create_image(0, 0, image=self.easter_5_2_file, tag='5-2', anchor=NW)        
        self.easter_5_3 = self.c.create_image(0, 0, image=self.easter_5_3_file, tag='5-3', anchor=NW)        
        self.easter_5_4 = self.c.create_image(0, 0, image=self.easter_5_4_file, tag='5-4', anchor=NW)        
        self.easter_5_5 = self.c.create_image(0, 0, image=self.easter_5_5_file, tag='5-5', anchor=NW)        
        self.easter_5_6 = self.c.create_image(0, 0, image=self.easter_5_6_file, tag='5-6', anchor=NW)
        
        self.easter_6_1 = self.c.create_image(0, 0, image=self.easter_6_1_file, tag='6-1', anchor=NW)        
        self.easter_6_2 = self.c.create_image(0, 0, image=self.easter_6_2_file, tag='6-2', anchor=NW)        
        self.easter_6_3 = self.c.create_image(0, 0, image=self.easter_6_3_file, tag='6-3', anchor=NW)        
        self.easter_6_4 = self.c.create_image(0, 0, image=self.easter_6_4_file, tag='6-4', anchor=NW)        
        self.easter_6_5 = self.c.create_image(0, 0, image=self.easter_6_5_file, tag='6-5', anchor=NW)        
        self.easter_6_6 = self.c.create_image(0, 0, image=self.easter_6_6_file, tag='6-6', anchor=NW)
        
        self.easter_7_1 = self.c.create_image(0, 0, image=self.easter_7_1_file, tag='7-1', anchor=NW)        
        self.easter_7_2 = self.c.create_image(0, 0, image=self.easter_7_2_file, tag='7-2', anchor=NW)        
        self.easter_7_3 = self.c.create_image(0, 0, image=self.easter_7_3_file, tag='7-3', anchor=NW)        
        self.easter_7_4 = self.c.create_image(0, 0, image=self.easter_7_4_file, tag='7-4', anchor=NW)        
        self.easter_7_5 = self.c.create_image(0, 0, image=self.easter_7_5_file, tag='7-5', anchor=NW)        
        self.easter_7_6 = self.c.create_image(0, 0, image=self.easter_7_6_file, tag='7-6', anchor=NW) 
        
        #labels
        self.element_name = self.c.create_text(295,80,font='FuturaPT 19', tag='main', fill="#1b3660")
        self.element_logo = self.c.create_text(295,180, font='FuturaPt 80', tag='main', fill="#1b3660")
        #self.element_sublogo = self.c.create_text(170,220, font='FuturaPt 20', anchor=E, tag='main', fill="#1b3660")
        self.element_subname = self.c.create_text(295,119, font='FuturaPt 16', tag='main')
        self.element_number = self.c.create_text(310,520, font='FuturaPt 20', tag='main', fill="#F25B25")
        self.element_charge = self.c.create_text(188,520, font='FuturaPt 20', tag='main', fill="#F25B25")
        self.element_weight = self.c.create_text(430,520, font='FuturaPt 20', tag='main', fill="#F25B25")
        self.about = self.c.create_text(510,80, anchor=NW, font='FuturaPt 16', tag='main')
        self.usage = self.c.create_text(510,355, anchor=NW, font='FuturaPt 16', tag='main')
        self.error_text = self.c.create_text(235,280, anchor=NW, font='FuturaPt 18', tag='error')
        
        
    def show_question(self):
        self.changed = True
        self.c.tag_raise('question')

    def show_out_of_p(self):
        self.c.tag_raise('out_of_p')
    
    def show_easter(self, is_good):
        if len(self.easter_not_used) == 0:
            self.easter_not_used = self.easter_used
            self.easter_used = []
        idx = randrange(len(self.easter_not_used))
        easter_idx = self.easter_not_used.pop(idx)
        self.easter_used.append(easter_idx)
        easter_text_idx = randrange(1, 4)
        if not is_good:
            easter_text_idx += 3
        easter_tag = f'{easter_idx}-{easter_text_idx}'
        print(self.c.find_withtag(easter_tag))
        self.c.tag_raise(easter_tag)
        
    
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
        self.easter_counter = 0
        self.c.tag_raise('logo')

    def error_signal(self):
        try:
            s.write("0\n".encode('utf-8'))
            if self.easter_counter > 0:
                self.easter_counter = -1
            else:
                self.easter_counter -= 1
            self.sounds['error'].play()
            
            if self.easter_counter < -2:
                a = 2
                b = 7
                c = self.easter_counter * (-1) - a
                if randrange(1,101) <= c * 100 / (b - a):
                    self.easter_counter = 0
                    self.show_easter(False)
        except Exception as e:
            print(e)

    def ok_signal(self):
        s.write("1\n".encode('utf-8'))
        if self.easter_counter < 0:
            self.easter_counter = 1
        else:
            self.easter_counter += 1
        self.sounds['ok'].play()
        
        if self.easter_counter > 2:
                a = 2
                b = 7
                c = self.easter_counter - a
                if randrange(1,101) <= c * 100 / (b - a):
                    self.easter_counter = 0
                    self.show_easter(True)
    
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
        hero_id = str(tmp[-1] % 4 + 1)
        self.c.tag_raise(f'back-{hero_id}')
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
        s.write("1\n".encode('utf-8'))
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
        self.easter_counter = 0
        self.easter_not_used = [1, 2, 3, 4, 5, 6, 7]
        self.easter_used = []
        self.set_volume(100)
        self.c.tag_raise('logo')
        self.serial_thread.start()
     
    def load_images(self):
        # self.background_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/background.png"))
        self.logo_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/logo.png"))
        self.info_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/info.png"))
        self.question_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/question.png"))
        self.out_of_p_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/out_of_p.png"))
        self.error_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/error.png"))
        
        # absolutelly cursed but in other case objects will be delete by GC
        self.background_1_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/backgrounds/1.png"))
        self.background_2_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/backgrounds/2.png"))
        self.background_3_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/backgrounds/3.png"))
        self.background_4_filename = ImageTk.PhotoImage(PilImage.open(folder_path + "Pictures/backgrounds/4.png"))
        
        self.easter_1_1_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/1-1.png'))        
        self.easter_1_2_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/1-2.png'))        
        self.easter_1_3_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/1-3.png'))        
        self.easter_1_4_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/1-4.png'))        
        self.easter_1_5_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/1-5.png'))        
        self.easter_1_6_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/1-6.png'))
                
        self.easter_2_1_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/2-1.png'))        
        self.easter_2_2_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/2-2.png'))        
        self.easter_2_3_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/2-3.png'))        
        self.easter_2_4_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/2-4.png'))        
        self.easter_2_5_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/2-5.png'))        
        self.easter_2_6_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/2-6.png'))

                
        self.easter_3_1_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/3-1.png'))        
        self.easter_3_2_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/3-2.png'))        
        self.easter_3_3_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/3-3.png'))        
        self.easter_3_4_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/3-4.png'))        
        self.easter_3_5_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/3-5.png'))        
        self.easter_3_6_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/3-6.png'))
        
                
        self.easter_4_1_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/4-1.png'))        
        self.easter_4_2_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/4-2.png'))        
        self.easter_4_3_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/4-3.png'))        
        self.easter_4_4_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/4-4.png'))        
        self.easter_4_5_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/4-5.png'))        
        self.easter_4_6_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/4-6.png'))
        
                
        self.easter_5_1_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/5-1.png'))        
        self.easter_5_2_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/5-2.png'))        
        self.easter_5_3_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/5-3.png'))        
        self.easter_5_4_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/5-4.png'))        
        self.easter_5_5_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/5-5.png'))        
        self.easter_5_6_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/5-6.png'))
        
                
        self.easter_6_1_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/6-1.png'))        
        self.easter_6_2_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/6-2.png'))        
        self.easter_6_3_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/6-3.png'))        
        self.easter_6_4_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/6-4.png'))        
        self.easter_6_5_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/6-5.png'))        
        self.easter_6_6_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/6-6.png'))
        
                
        self.easter_7_1_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/7-1.png'))        
        self.easter_7_2_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/7-2.png'))        
        self.easter_7_3_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/7-3.png'))        
        self.easter_7_4_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/7-4.png'))        
        self.easter_7_5_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/7-5.png'))        
        self.easter_7_6_file = ImageTk.PhotoImage(PilImage.open(f'{folder_path}Pictures/easter/7-6.png'))

if __name__ == "__main__":
    root = Tk()
    root.attributes("-fullscreen", True) 
    root.title("atomic synthesizer")
    app = Application(master=root)
    app.mainloop()
