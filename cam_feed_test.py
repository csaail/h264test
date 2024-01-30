#!/usr/bin/env python3

from Pluto import pluto
from ctypes import *
from ctypes import POINTER, Structure
from ctypes import c_void_p, c_int, c_char

import threading  
import h264decoder  
import numpy as np   
import cv2    
 
global lewei_video_framepyth
frame = b''

my_pluto = pluto()# This commands creates an object of pluto() where you can connect your hardware to. my_pluto is literally your plutodrone

#libc = CDLL("libLeweiLib.so")
libc = windll.LoadLibrary(r"C:\Users\giant\Desktop\new_cam\LwcxVideoPlayer\LwcxVideoPlayer\x64\Release\LwcxStream.dll")

decoder = h264decoder.H264Decoder()

class lewei_video_frame(Structure):
        _fields_ = [('timestamp',c_int64),
                ('iFrame',c_int32),
                ('size',c_int32),
                ('buf', POINTER(c_char))]

        def __repr__(self):
            return f'Lewei Video Frame Buf: {self.buf}'

CMPFUNC = CFUNCTYPE(None,POINTER(c_void_p),POINTER(lewei_video_frame))

take_pic = False
global frame_data, recording
frame_data = None
recording = False

def read_buffer(lpParam, pFrame):
        frame_event  = threading.Event()
        global count
        global frame_data, recording
        ret = 0
        got_picture = 0
        
        pFrame_size = pFrame[0].size

        if (pFrame_size <= 0):
            libc.video_free_frame_ram(pFrame)
            return

        else:
            print("pframe_size: ", pFrame[0].size)
            data_in = pFrame[0].buf[:pFrame[0].size]

            framedatas = decoder.decode(data_in)
            for framedata in framedatas:
                (frame, w, h, ls) = framedata
                if frame is not None:
                    frame = np.frombuffer(frame, dtype=np.ubyte, count=len(frame))
                    frame = frame.reshape((h, ls//3, 3))
                    frame = frame[:,:w,:]

                    #change color format from bgr to rgb
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    # frame = cv2.resize(frame, (640, 480))  # Resize frame to match video resolution
                    frame_data = frame
           
                    cv2.imshow('frame', frame_data)
                    cv2.waitKey(1)


        return


class pluto_cam():

    def __init__(self):
        self.cam_running = False
        self.taking_pic = False

    def show_cam(self):
        cmp_func = CMPFUNC(read_buffer)

        libc.lewei_initialize_stream()
        libc.lewei_set_HDflag(False)

        ret = libc.lewei_start_stream(None,cmp_func)
         
    def start_cam(self):
        self.cam_running = True
        threading.Thread(target=self.show_cam).start()
    
    def stop_cam(self):
        cv2.destroyAllWindows()
        libc.lewei_stop_stream()

my_pluto_cam = pluto_cam()
my_pluto_cam.start_cam() # Start Camera Stream


     
