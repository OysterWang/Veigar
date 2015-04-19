#!/usr/bin/python
# -*- coding: utf-8 -*-
#需要先安装
#pyHook-1.5.1.win-amd64-py2.7.exe
#pywin32-219.win-amd64-py2.7.exe
#文件在360yunpan:\Software\Program

import pythoncom
import pyHook
import win32api
import time

def onMouseEvent(event):
    # 监听鼠标事件
    print "MessageName:", event.MessageName
    print "Message:", event.Message
    print "Event Time:", event.Time 
    print "Time:", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print "Window:", event.Window
    print "WindowName:", event.WindowName
    print "Position:", event.Position
    print "Wheel:", event.Wheel
    print "Injected:", event.Injected
    print "---"
    
    # 返回 True 以便将事件传给其它处理程序
    # 如果返回 False ，则鼠标事件将被全部拦截
    # 你的鼠标看起来会僵在那儿，似乎失去响应了
    return True

def onKeyboardEvent(event):
    print "MessageName:", event.MessageName
    print "Message:", event.Message
    print "Event Time:", event.Time
    print "Time:", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print "Window:", event.Window
    print "WindowName:", event.WindowName
    print "Ascii:", event.Ascii, chr(event.Ascii)
    print "Key:", event.Key
    print "KeyID:", event.KeyID
    print "ScanCode:", event.ScanCode
    print "Extended:", event.Extended
    print "Injected:", event.Injected
    print "Alt", event.Alt
    print "Transition", event.Transition
    print "---"
    # 同鼠标事件监听函数的返回值

    if str(event.Key)=='F12':   #按下F12终止
        win32api.PostQuitMessage()
    return True

if __name__ == "__main__":
    hm = pyHook.HookManager()   # 创建一个“钩子”管理对象

    hm.KeyDown = onKeyboardEvent    # 监听键盘事件
    hm.HookKeyboard()   # 设置键盘“钩子”

    hm.MouseAll = onMouseEvent  # 监听鼠标事件
    hm.HookMouse()   # 设置鼠标“钩子”

    pythoncom.PumpMessages()    # 循环获取消息