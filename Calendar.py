
from tkinter import *
import tkinter.ttk as ttk
import calendar
import datetime
import webbrowser

months_names = ['-', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
months_names_shortcut = ['-', 'янв.', 'февр.', 'марта', 'апр.', 'мая', 'июня', 'июля', 'авг.', 'сент.', 'окт.', 'нояб.', 'дек.']
week_day_name = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

days = []

January = []
February = []
March = []
April = []

May = []
June = []
July = []
August = []

September = []
October = []
November = []
December = []

url = 'https://www.calend.ru/holidays/'

open_web_event = lambda x : (lambda p : webbrowser.open_new_tab(x))

def App():
    root.title("Календарь")
    notebook = ttk.Notebook(root, width = 800, height = 700)
    mode = ['Месяц', 'Год']
    for cur_mode in mode:
        #Вкладка Месяц
        if cur_mode == 'Месяц':
            month_frame = Frame(notebook)
            notebook.add(month_frame, text = cur_mode, sticky = NE + SW)
            #Разметка 
            row = 0
            column = 0
            while row < 8:
                month_frame.rowconfigure(row, weight=1, minsize=100)
                while column < 7:
                    month_frame.columnconfigure(column, weight=1, minsize=100)
                    column += 1
                row += 1
            #Дни в месяце
            for i in range(2, 8):
                for j in range(7):
                    #Дни в месяце
                    lbl = Label(month_frame, borderwidth=2, relief="groove", font = 'Ariel 20', cursor = 'hand2')
                    lbl.grid(row = i, column = j, sticky=NSEW)
                    days.append(lbl)
            #Вперед 
            forward_button = Button(month_frame, text = '>', command = lambda : forward_month(month_frame, year_frame))
            forward_button.grid(row = 0, column = 6, sticky = W)
            #Сегодня
            now_button = Button(month_frame, text = 'Сегодня', command = lambda : cur_month(month_frame, year_frame))
            now_button.grid(row = 0, column = 5, sticky = EW)
            #Назад 
            backward_button = Button(month_frame, text = '<', command = lambda : back_month(month_frame, year_frame))
            backward_button.grid(row = 0, column = 4, sticky = E)
            for j in range(7):
                #Дни недели 
                week_day = Label(month_frame, text = week_day_name[j], borderwidth=2, relief="groove", font = 'Arial 25 bold', bg = '#323232')
                week_day.grid(row = 1, column = j, sticky=NSEW)
            fill_month(month_frame)
        #Вкладка Год
        if cur_mode == 'Год':
            year_frame = Frame(notebook, width = 800, height = 700)
            notebook.add(year_frame, text = 'Год', sticky = NE + SW)
            #Разметка
            row = 0
            column = 0
            while row < 25:
                year_frame.rowconfigure(row, weight = 1)
                while column < 28:
                    year_frame.columnconfigure(column, weight = 1)
                    column += 1
                row += 1
            #Вперед
            pixelVirtual = PhotoImage(width=1, height=1)
            forward_button = Button(year_frame, text = '>', command = lambda : forward_year(year_frame, month_frame))
            forward_button.grid(row = 0, column = 26, columnspan = 2, sticky = W)
            #Сегодня
            now_button = Button(year_frame, text = 'Сегодня', command = lambda : cur_year(year_frame, month_frame))
            now_button.grid(row = 0, column = 23, columnspan = 3, sticky = EW)
            #Назад
            backward_button = Button(year_frame, text = '<', command = lambda : back_year(year_frame, month_frame))
            backward_button.grid(row = 0, column = 21, columnspan = 2, sticky = E)
            #Месяцы
            lbl = Label(year_frame, text = months_names[1], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 1, column = 0, columnspan = 7, sticky = NSEW)
            lbl = Label(year_frame, text = months_names[2], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 1, column = 7, columnspan = 7, sticky = NSEW)
            lbl = Label(year_frame, text = months_names[3], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 1, column = 14, columnspan = 7, sticky = NSEW)
            lbl = Label(year_frame, text = months_names[4], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 1, column = 21, columnspan = 7, sticky = NSEW)

            lbl = Label(year_frame, text = months_names[5], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 9, column = 0, columnspan = 7, sticky = NSEW)
            lbl = Label(year_frame, text = months_names[6], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 9, column = 7, columnspan = 7, sticky = NSEW)
            lbl = Label(year_frame, text = months_names[7], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 9, column = 14, columnspan = 7, sticky = NSEW)
            lbl = Label(year_frame, text = months_names[8], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 9, column = 21, columnspan = 7, sticky = NSEW)

            lbl = Label(year_frame, text = months_names[9], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 17, column = 0, columnspan = 7, sticky = NSEW)
            lbl = Label(year_frame, text = months_names[10], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 17, column = 7, columnspan = 7, sticky = NSEW)
            lbl = Label(year_frame, text = months_names[11], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 17, column = 14, columnspan = 7, sticky = NSEW)
            lbl = Label(year_frame, text = months_names[12], font = 'Ariel 20 bold', borderwidth=2, relief="groove", bg = '#323232', fg = '#f24038')
            lbl.grid(row = 17, column = 21, columnspan = 7, sticky = NSEW)

            #Дни недели
            week_day_row = [2, 10, 18]
            for i in week_day_row:
                for j in range(0, 28):
                    lbl = Label(year_frame, text = week_day_name[j % 7], borderwidth=2, relief="groove", bg = '#323232')
                    lbl.grid(row = i, column = j, sticky = NSEW)
            #Дни в месяцах 
            for i in range(3, 25):
                if i != 9 and i != 10 and i != 17 and i != 18:
                    for j in range(0, 28):
                        lbl = Label(year_frame, borderwidth=2, relief="groove", cursor = 'hand2')
                        lbl.grid(row = i, column = j, sticky=NSEW)
                        if i < 9 and j < 7:
                            January.append(lbl)
                        if i < 9 and j > 6 and j < 14:
                            February.append(lbl)
                        elif i < 9 and j > 13 and j < 21:
                            March.append(lbl)
                        elif i < 9 and j > 20:
                            April.append(lbl)
                        elif i > 10 and i < 17 and j < 7:
                            May.append(lbl)
                        elif i > 10 and i < 17 and j > 6 and j < 14:
                            June.append(lbl)
                        elif i > 10 and i < 17 and j > 13 and j < 21:
                            July.append(lbl)
                        elif i > 10 and i < 17 and j > 20:
                            August.append(lbl)
                        elif i > 18 and j < 7:
                            September.append(lbl)
                        elif i > 18 and j > 6 and j < 14:
                            October.append(lbl)
                        elif i > 18 and j > 13 and j < 21:
                            November.append(lbl)
                        elif i > 18 and j > 20:
                            December.append(lbl)
            fill_year(year_frame)
        
    label = Label(root)
    notebook.pack()
    label.pack(anchor = W)
    notebook.enable_traversal()

def select_tab(id):
    text = "Ваш текущий выбор: " + str(id) + '\n'
    print(text)

def back_year(frame1, frame2):
    global year
    year -= 1
    fill_year(frame1)
    fill_month(frame2)

def forward_year(frame1, frame2):
    global year
    year += 1
    fill_year(frame1)
    fill_month(frame2)

def cur_year(frame1, frame2):
    global year, month
    year = now.year
    month = now.month
    fill_year(frame1)
    fill_month(frame2)

def back_month(frame, frame2):
    global month
    global year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
        fill_year(frame2)
    fill_month(frame)

def forward_month(frame1, frame2):
    global month
    global year
    month += 1
    if month == 13:
        month = 1
        year += 1
        fill_year(frame2)
    fill_month(frame1)

def cur_month(frame1, frame2):
    global month
    global year
    now = datetime.datetime.now()
    month = now.month 
    year = now.year
    fill_month(frame1)
    fill_year(frame2)

def fill_month(frame):
    #Месяц + Год
    lbl = Label(frame, text = months_names[month] + ' ' + str(year) + ' г.', font = 'Ariel 25 bold')
    lbl.grid(row = 0, column = 0, columnspan=3, sticky=NSEW)
    #Заполнение
    month_days = calendar.monthrange(year, month)[1] #кол-во дней в месяце 
    if month == 1:
        back_month_days=calendar.monthrange(year - 1,12)[1]
        back_month = 12
    else: 
        back_month_days=calendar.monthrange(year,month - 1)[1]
        back_month = month - 1
    week_day=calendar.monthrange(year,month)[0] #первый день месяца
    #Заполнение текущего месяца  
    for n in range(month_days):
        days[n + week_day]['text'] = str(n + 1)
        days[n + week_day].bind('<Button-1>', open_web_event(url + '/' + str(month) + '-' + days[n + week_day]['text'] + '/'))
        if n + 1 == 1:
            days[n + week_day]['text'] = str(n + 1) + ' ' + months_names_shortcut[month]
            days[n + week_day]['bg'] = '#323232'
            days[n + week_day]['fg'] = 'white'
        elif n + 1 == now.day and month == now.month and year == now.year:
            days[n + week_day]['fg'] = 'black'
            days[n + week_day]['bg'] = '#f24038'
        else:
            days[n + week_day]['bg'] = '#323232'
            days[n + week_day]['fg'] = 'white'
        
    #Заполнение предыдущего месяца 
    for n in range (week_day):
        days[week_day - n - 1]['text'] = str(back_month_days - n)
        days[week_day - n - 1]['bg'] = '#323232'
        days[week_day - n - 1]['fg'] = '#A8A8A8'
        days[week_day - n - 1].bind('<Button-1>', open_web_event(url + '/' + str(back_month) + '-' + days[week_day - n - 1]['text'] + '/'))
    #Заполнение следующего месяца 
    for n in range (6 * 7 - month_days - week_day):
        if n + 1 == 1:
            if month + 1 == 13:
                days[week_day + month_days + n]['text'] = str(n + 1) + ' ' + months_names_shortcut[1]
                days[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '1-' + str(n + 1) + '/'))
            else: 
                days[week_day + month_days + n]['text'] = str(n + 1) + ' ' + months_names_shortcut[month + 1]
                days[week_day + month_days + n].bind('<Button-1>', open_web_event(url + str(month + 1) + '-' + str(n + 1) + '/'))
            days[week_day + month_days + n]['bg'] = '#323232'
            days[week_day + month_days + n]['fg'] = '#A8A8A8'
        else:
            days[week_day + month_days + n]['text'] = str(n + 1)
            days[week_day + month_days + n]['bg'] = '#323232'
            days[week_day + month_days + n]['fg'] = '#A8A8A8'
            if month + 1 == 13:
                days[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '1-' + days[week_day + month_days + n]['text'] + '/'))
            else:
                days[week_day + month_days + n].bind('<Button-1>', open_web_event(url + str(month + 1) + '-' + days[week_day + month_days + n]['text'] + '/'))

def fill_year(year_frame):
    #Год
    lbl = Label(year_frame, text = str(year) + 'г.', font = 'Ariel 25 bold')
    lbl.grid(row = 0, column = 0, columnspan = 7, sticky = NSEW)
    #Заполнение Январь
    jan_month = 1
    month_days = calendar.monthrange(year, jan_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year - 1,12)[1] 
    week_day=calendar.monthrange(year,jan_month)[0]
    for n in range(month_days):
        January[n + week_day]['text'] = str(n + 1)
        January[n + week_day].bind('<Button-1>', open_web_event(url + '1-' + January[n + week_day]['text'] + '/'))
        if n + 1 == now.day and jan_month == now.month and year == now.year:
            January[n + week_day]['fg'] = 'black'
            January[n + week_day]['bg'] = '#f24038'
        else: 
            January[n + week_day]['bg'] = '#323232'
            January[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        January[week_day - n - 1]['text'] = str(back_month_days - n)
        January[week_day - n - 1]['bg'] = '#323232'
        January[week_day - n - 1]['fg'] = '#A8A8A8'
        January[week_day - n - 1].bind('<Button-1>', open_web_event(url + '12-' + January[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        January[week_day + month_days + n]['text'] = str(n + 1)
        January[week_day + month_days + n]['bg'] = '#323232'
        January[week_day + month_days + n]['fg'] = '#A8A8A8'
        January[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '2-' + January[week_day + month_days + n]['text'] + '/'))
    #Заполнение Февраль 
    feb_month = 2
    month_days = calendar.monthrange(year, feb_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year,feb_month - 1)[1]
    week_day=calendar.monthrange(year,feb_month)[0]
    for n in range(month_days):
        February[n + week_day]['text'] = str(n + 1)
        February[n + week_day].bind('<Button-1>', open_web_event(url + '2-' + February[n + week_day]['text'] + '/'))
        if n + 1 == now.day and feb_month == now.month and year == now.year:
            February[n + week_day]['fg'] = 'black'
            February[n + week_day]['bg'] = '#f24038'
        else: 
            February[n + week_day]['bg'] = '#323232'
            February[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        February[week_day - n - 1]['text'] = str(back_month_days - n)
        February[week_day - n - 1]['bg'] = '#323232'
        February[week_day - n - 1]['fg'] = '#A8A8A8'
        February[week_day - n - 1].bind('<Button-1>', open_web_event(url + '1-' + February[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        February[week_day + month_days + n]['text'] = str(n + 1)
        February[week_day + month_days + n]['bg'] = '#323232'
        February[week_day + month_days + n]['fg'] = '#A8A8A8'
        February[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '3-' + February[week_day + month_days + n]['text'] + '/'))
    #Заполнение Март
    march_month = 3
    month_days = calendar.monthrange(year, march_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year,march_month - 1)[1]
    week_day=calendar.monthrange(year,march_month)[0]
    for n in range(month_days):
        March[n + week_day]['text'] = str(n + 1)
        March[n + week_day].bind('<Button-1>', open_web_event(url + '3-' + March[n + week_day]['text'] + '/'))
        if n + 1 == now.day and march_month == now.month and year == now.year:
            March[n + week_day]['fg'] = 'black'
            March[n + week_day]['bg'] = '#f24038'
        else: 
            March[n + week_day]['bg'] = '#323232'
            March[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        March[week_day - n - 1]['text'] = str(back_month_days - n)
        March[week_day - n - 1]['bg'] = '#323232'
        March[week_day - n - 1]['fg'] = '#A8A8A8'
        March[week_day - n - 1].bind('<Button-1>', open_web_event(url + '2-' + March[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        March[week_day + month_days + n]['text'] = str(n + 1)
        March[week_day + month_days + n]['bg'] = '#323232'
        March[week_day + month_days + n]['fg'] = '#A8A8A8'
        March[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '4-' + March[week_day + month_days + n]['text'] + '/'))
    #Заполнение Апрель 
    march_month = 4
    month_days = calendar.monthrange(year, march_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year,march_month - 1)[1]
    week_day=calendar.monthrange(year,march_month)[0]
    for n in range(month_days):
        April[n + week_day]['text'] = str(n + 1)
        April[n + week_day].bind('<Button-1>', open_web_event(url + '4-' + April[n + week_day]['text'] + '/'))
        if n + 1 == now.day and march_month == now.month and year == now.year:
            April[n + week_day]['fg'] = 'black'
            April[n + week_day]['bg'] = '#f24038'
        else: 
            April[n + week_day]['bg'] = '#323232'
            April[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        April[week_day - n - 1]['text'] = str(back_month_days - n)
        April[week_day - n - 1]['bg'] = '#323232'
        April[week_day - n - 1]['fg'] = '#A8A8A8'
        April[week_day - n - 1].bind('<Button-1>', open_web_event(url + '3-' + April[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        April[week_day + month_days + n]['text'] = str(n + 1)
        April[week_day + month_days + n]['bg'] = '#323232'
        April[week_day + month_days + n]['fg'] = '#A8A8A8'
        April[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '5-' + April[week_day + month_days + n]['text'] + '/'))
    #Заполнение Май
    march_month = 5
    month_days = calendar.monthrange(year, march_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year,march_month - 1)[1]
    week_day=calendar.monthrange(year,march_month)[0]
    for n in range(month_days):
        May[n + week_day]['text'] = str(n + 1)
        May[n + week_day].bind('<Button-1>', open_web_event(url + '5-' + May[n + week_day]['text'] + '/'))
        if n + 1 == now.day and march_month == now.month and year == now.year:
            May[n + week_day]['fg'] = 'black'
            May[n + week_day]['bg'] = '#f24038'
        else: 
            May[n + week_day]['bg'] = '#323232'
            May[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        May[week_day - n - 1]['text'] = str(back_month_days - n)
        May[week_day - n - 1]['bg'] = '#323232'
        May[week_day - n - 1]['fg'] = '#A8A8A8'
        May[week_day - n - 1].bind('<Button-1>', open_web_event(url + '4-' + May[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        May[week_day + month_days + n]['text'] = str(n + 1)
        May[week_day + month_days + n]['bg'] = '#323232'
        May[week_day + month_days + n]['fg'] = '#A8A8A8'
        May[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '6-' + May[week_day + month_days + n]['text'] + '/'))
    #Заполнение Июнь
    march_month = 6
    month_days = calendar.monthrange(year, march_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year,march_month - 1)[1]
    week_day=calendar.monthrange(year,march_month)[0]
    for n in range(month_days):
        June[n + week_day]['text'] = str(n + 1)
        June[n + week_day].bind('<Button-1>', open_web_event(url + '6-' + June[n + week_day]['text'] + '/'))
        if n + 1 == now.day and march_month == now.month and year == now.year:
            June[n + week_day]['fg'] = 'black'
            June[n + week_day]['bg'] = '#f24038'
        else: 
            June[n + week_day]['bg'] = '#323232'
            June[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        June[week_day - n - 1]['text'] = str(back_month_days - n)
        June[week_day - n - 1]['bg'] = '#323232'
        June[week_day - n - 1]['fg'] = '#A8A8A8'
        June[week_day - n - 1].bind('<Button-1>', open_web_event(url + '5-' + June[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        June[week_day + month_days + n]['text'] = str(n + 1)
        June[week_day + month_days + n]['bg'] = '#323232'
        June[week_day + month_days + n]['fg'] = '#A8A8A8'
        June[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '7-' + June[week_day + month_days + n]['text'] + '/'))
    #Заполнение Июль 
    march_month = 7
    month_days = calendar.monthrange(year, march_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year,march_month - 1)[1]
    week_day=calendar.monthrange(year,march_month)[0]
    for n in range(month_days):
        July[n + week_day]['text'] = str(n + 1)
        July[n + week_day].bind('<Button-1>', open_web_event(url + '7-' + July[n + week_day]['text'] + '/'))
        if n + 1 == now.day and march_month == now.month and year == now.year:
            July[n + week_day]['fg'] = 'black'
            July[n + week_day]['bg'] = '#f24038'
        else: 
            July[n + week_day]['bg'] = '#323232'
            July[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        July[week_day - n - 1]['text'] = str(back_month_days - n)
        July[week_day - n - 1]['bg'] = '#323232'
        July[week_day - n - 1]['fg'] = '#A8A8A8'
        July[week_day - n - 1].bind('<Button-1>', open_web_event(url + '6-' + July[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        July[week_day + month_days + n]['text'] = str(n + 1)
        July[week_day + month_days + n]['bg'] = '#323232'
        July[week_day + month_days + n]['fg'] = '#A8A8A8'
        July[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '8-' + July[week_day + month_days + n]['text'] + '/'))
    #Заполнение Август 
    march_month = 8
    month_days = calendar.monthrange(year, march_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year,march_month - 1)[1]
    week_day=calendar.monthrange(year,march_month)[0]
    for n in range(month_days):
        August[n + week_day]['text'] = str(n + 1)
        August[n + week_day].bind('<Button-1>', open_web_event(url + '8-' + August[n + week_day]['text'] + '/'))
        if n + 1 == now.day and march_month == now.month and year == now.year:
            August[n + week_day]['fg'] = 'black'
            August[n + week_day]['bg'] = '#f24038'
        else: 
            August[n + week_day]['bg'] = '#323232'
            August[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        August[week_day - n - 1]['text'] = str(back_month_days - n)
        August[week_day - n - 1]['bg'] = '#323232'
        August[week_day - n - 1]['fg'] = '#A8A8A8'
        August[week_day - n - 1].bind('<Button-1>', open_web_event(url + '7-' + August[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        August[week_day + month_days + n]['text'] = str(n + 1)
        August[week_day + month_days + n]['bg'] = '#323232'
        August[week_day + month_days + n]['fg'] = '#A8A8A8'
        August[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '9-' + August[week_day + month_days + n]['text'] + '/'))
    #Заполнение Сентябрь 
    sept_month = 9
    month_days = calendar.monthrange(year, sept_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year,sept_month - 1)[1]
    week_day=calendar.monthrange(year,sept_month)[0]
    for n in range(month_days):
        September[n + week_day]['text'] = str(n + 1)
        September[n + week_day].bind('<Button-1>', open_web_event(url + '9-' + September[n + week_day]['text'] + '/'))
        if n + 1 == now.day and sept_month == now.month and year == now.year:
            September[n + week_day]['fg'] = 'black'
            September[n + week_day]['bg'] = '#f24038'
        else: 
            September[n + week_day]['bg'] = '#323232'
            September[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        September[week_day - n - 1]['text'] = str(back_month_days - n)
        September[week_day - n - 1]['bg'] = '#323232'
        September[week_day - n - 1]['fg'] = '#A8A8A8'
        September[week_day - n - 1].bind('<Button-1>', open_web_event(url + '8-' + September[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        September[week_day + month_days + n]['text'] = str(n + 1)
        September[week_day + month_days + n]['bg'] = '#323232'
        September[week_day + month_days + n]['fg'] = '#A8A8A8'
        September[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '10-' + September[week_day + month_days + n]['text'] + '/'))
    #Заполнение Октябрь
    oct_month = 10
    month_days = calendar.monthrange(year, oct_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year,oct_month - 1)[1]
    week_day=calendar.monthrange(year,oct_month)[0]
    for n in range(month_days):
        October[n + week_day]['text'] = str(n + 1)
        October[n + week_day].bind('<Button-1>', open_web_event(url + '10-' + October[n + week_day]['text'] + '/'))
        if n + 1 == now.day and oct_month == now.month and year == now.year:
            October[n + week_day]['fg'] = 'black'
            October[n + week_day]['bg'] = '#f24038'
        else: 
            October[n + week_day]['bg'] = '#323232'
            October[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        October[week_day - n - 1]['text'] = str(back_month_days - n)
        October[week_day - n - 1]['bg'] = '#323232'
        October[week_day - n - 1]['fg'] = '#A8A8A8'
        October[week_day - n - 1].bind('<Button-1>', open_web_event(url + '9-' + October[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        October[week_day + month_days + n]['text'] = str(n + 1)
        October[week_day + month_days + n]['bg'] = '#323232'
        October[week_day + month_days + n]['fg'] = '#A8A8A8'
        October[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '11-' + October[week_day + month_days + n]['text'] + '/'))
    #Заполнение Ноябрь 
    nov_month = 11
    month_days = calendar.monthrange(year, nov_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year,nov_month - 1)[1]
    week_day=calendar.monthrange(year,nov_month)[0]
    for n in range(month_days):
        November[n + week_day]['text'] = str(n + 1)
        November[n + week_day].bind('<Button-1>', open_web_event(url + '11-' + November[n + week_day]['text'] + '/'))
        if n + 1 == now.day and nov_month == now.month and year == now.year:
            November[n + week_day]['fg'] = 'black'
            November[n + week_day]['bg'] = '#f24038'
        else: 
            November[n + week_day]['bg'] = '#323232'
            November[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        November[week_day - n - 1]['text'] = str(back_month_days - n)
        November[week_day - n - 1]['bg'] = '#323232'
        November[week_day - n - 1]['fg'] = '#A8A8A8'
        November[week_day - n - 1].bind('<Button-1>', open_web_event(url + '10-' + November[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        November[week_day + month_days + n]['text'] = str(n + 1)
        November[week_day + month_days + n]['bg'] = '#323232'
        November[week_day + month_days + n]['fg'] = '#A8A8A8'
        November[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '12-' + November[week_day + month_days + n]['text'] + '/'))
    #Заполнение Январь
    dec_month = 12
    month_days = calendar.monthrange(year, dec_month)[1] #кол-во дней в месяце 
    back_month_days=calendar.monthrange(year,dec_month - 1)[1]
    week_day=calendar.monthrange(year,dec_month)[0]
    for n in range(month_days):
        December[n + week_day]['text'] = str(n + 1)
        December[n + week_day].bind('<Button-1>', open_web_event(url + '12-' + December[n + week_day]['text'] + '/'))
        if n + 1 == now.day and jan_month == now.month and year == now.year:
            December[n + week_day]['fg'] = 'black'
            December[n + week_day]['bg'] = '#f24038'
        else: 
            December[n + week_day]['bg'] = '#323232'
            December[n + week_day]['fg'] = 'white'
    for n in range(week_day):
        December[week_day - n - 1]['text'] = str(back_month_days - n)
        December[week_day - n - 1]['bg'] = '#323232'
        December[week_day - n - 1]['fg'] = '#A8A8A8'
        December[week_day - n - 1].bind('<Button-1>', open_web_event(url + '11-' + December[week_day - n - 1]['text'] + '/'))
    for n in range (6 * 7 - month_days - week_day):
        December[week_day + month_days + n]['text'] = str(n + 1)
        December[week_day + month_days + n]['bg'] = '#323232'
        December[week_day + month_days + n]['fg'] = '#A8A8A8'
        December[week_day + month_days + n].bind('<Button-1>', open_web_event(url + '01-' + December[week_day + month_days + n]['text'] + '/'))

if __name__ == "__main__":
    root = Tk()
    App()
    root.mainloop()