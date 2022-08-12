from ast import While
from tkinter import W
import os 
import time

def a():
    print('W   WW   W    OOOOOOO       SSSSSSSSSSS')
    print('W   WW   W  OO       OO     SS')
    print('W   WW   W OOO       OOO    SSSSSSSSSSS')
    print('W   WW   W OOO       OOO             SS')
    print('WWWWWWWWWW   OOOOOOOO       SSSSSSSSSSS')
def about():
    print('=====ABOUT=====')
    a()
    print('BiliBili_MCWHG')
    print('V:22B01')
def welcome():
    a()
    print('[WOS]START')
    for i in range(101):
        i = str(i)
        print(i+'%')
        i = int(i)
        time.sleep(1)
    print('[WOS]WELCOME!')
welcome()
lsq = ['about','stop']
while True:
    hd = input('[WOS]')
    if hd == 'ls':
        print(lsq)
    if hd == 'stop':
        b = input('Do you want stop WOS?[Y/N]')
        if b == 'Y':
            break
        else:
            continue
    if hd == 'about':
        about()
    if hd == 'ls new file':
        wjm = input('what is the new file name ')
        lsq.append(wjm)
    if hd == 'ERROR':
        print('WOS is stopping')
        break