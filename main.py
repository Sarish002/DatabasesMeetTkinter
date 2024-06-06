from PIL import Image
Image.CUBIC = Image.BICUBIC
from ttkbootstrap import *
import tkinter as t
from tkinter import messagebox
from sqlite3 import *

#Creating a Database
Time = connect('Time.db')
Timmy = Time.cursor()

#Creating Window
root = Window(themename = 'minty')
root.geometry('2000x1200')

#Creating Heading
Frame_1 = Frame(master = root)
Label_1 = Label(text = 'Student Details . . . . . . . . . . . .',
                master = Frame_1, font = ('Comic Sans MS', 30, 'bold italic'),
                foreground = '#000000')
Label_1.pack()


Frame_1.pack(anchor = 'w',
             pady = 20,
             padx = 20)

Separator(bootstyle = 'danger').pack(fill = 'x',
                                     padx = 50)
Separator(bootstyle = 'danger').pack(fill = 'x',
                                     padx = 50)
Separator(bootstyle = 'danger').pack(fill = 'x',
                                     padx = 50)

#Code and Details (Scrolled Text)
Frame_2 = t.Frame(master = root,
                  highlightbackground='#e59dfa',
                  highlightthickness=10)
Scroll = ScrolledText(master = Frame_2,
                      font = ('Comic Sans MS', 15, 'bold italic'),
                      width = 40, height = 21.48)
Scroll.pack(pady = 20,
            padx = 20)
Frame_2.pack(anchor = 'w',
             padx = 20,
             pady = 10)

#Name Box
Frame_3 = t.Frame(master = root,
                  highlightbackground = '#e59dfa',
                  highlightthickness = 7)
Label_2 = Label(text = 'Name: ',
                font = ('Comic Sans MS', 18, 'bold italic'),
                master = Frame_3)
Entry_1 = Entry(font = ('Comic Sans MS', 15, 'bold italic'),
                master = Frame_3,
                width = 12,
                bootstyle = 'info')
Label_2.pack(padx = 20,
             pady = 20)
Entry_1.pack(side = 'left',
             padx = 20,
             pady = 20)
Frame_3.place(relx = 0.46875,
              rely = 0.125,
              anchor = 'n')

#DOB Box
Frame_4 = t.Frame(master = root,
                  highlightbackground = '#e59dfa',
                  highlightthickness = 7)
Label_3 = Label(text = 'DOB: ',
                font = ('Comic Sans MS', 18,
                        'bold italic'),
                master = Frame_4)

#Date Entry
Entry_2 = DateEntry(master = Frame_4,
                    bootstyle = 'info',
                    dateformat='%B %d, %Y',
                    width = 11)

#Variable for Current Year
a = list(Entry_2.entry.get().split())[2]

#Packing the DOB Frame
Label_3.pack(padx = 20,
             pady = 20)
Entry_2.pack(side = 'left',
             padx = 48,
             pady = 27)
Frame_4.place(relx = 0.622,
              rely = 0.125,
              anchor = 'n')

#Gender Box
mystyle = Style()
mystyle.configure('info.TMenubutton',
                  font = ('Comic Sans MS', 18, 'bold italic'))
Frame_5 = t.Frame(master = root,
                  highlightbackground = '#e59dfa',
                  highlightthickness = 7)
Label_4 = Label(text = 'Gender: ',
                font = ('Comic Sans MS', 18, 'bold italic'),
                master = Frame_5)
Entry_3 = Menubutton(master = Frame_5,
                     text = 'Gender: ',
                     bootstyle = 'info',
                     style = 'info.TMenubutton',
                     width = 7)

#Defining the "genders()" function
def genders(str):
    Entry_3.configure(text = str)
    query = StringVar()
    query.set(value = gender)

#Entering radiobuttons into the menubutton
Menu = Menu(Entry_3)
Gender = ['Male', 'Female', 'Transgender']
for gender in Gender:
    Menu.add_radiobutton(label = gender,
                         font = ('Comic Sans MS', 15, 'bold'),
                         command = lambda gender=gender: genders(gender))
Entry_3['menu'] = Menu
Label_4.pack(padx = 20,
             pady = 20)
Entry_3.pack(side = 'left',
             padx = 23, pady = 18)
Frame_5.place(relx = 0.774125,
              rely = 0.125,
              anchor = 'n')


#Creating Notebook for marks scored in Exam 1
Notes = Notebook(master = root,
                 bootstyle = 'dark')
Notes.place(relx = 0.37885,
            rely = 0.475, anchor = 'w')

English = Frame(Notes)
Label1 = Label(English,
               text = 'Marks scored in English Test 1: ',
               font = ('Comic Sans MS', 18, 'bold'))
Enter1 = Entry(English,
               font = ('Comic Sans MS', 18, 'bold'))
Label1.pack()
Enter1.pack()
English.pack()
Maths = Frame(Notes)
Label2 = Label(Maths,
               text = 'Marks scored in Maths Test 1: ',
               font = ('Comic Sans MS', 18, 'bold'))
Enter2 = Entry(Maths,
               font = ('Comic Sans MS', 18, 'bold'))
Label2.pack()
Enter2.pack()
Maths.pack()
Science = Frame(Notes)
Label3 = Label(Science,
               text = 'Marks scored in Science Test 1: ',
               font = ('Comic Sans MS', 18, 'bold'))
Enter3 = Entry(Science,
               font = ('Comic Sans MS', 18, 'bold'))
Label3.pack()
Enter3.pack()
Science.pack()

#Creating Notebook for marks scored in Exam 2
Notes2 = Notebook(master = root)
Notes2.place(relx = 0.65,
             rely = 0.475,
             anchor = 'w')

English2 = Frame(Notes2)
Label12 = Label(English2,
                text = 'Marks scored in English Test 2: ',
                font = ('Comic Sans MS', 18, 'bold'))
Enter12 = Entry(English2,
                font = ('Comic Sans MS', 18, 'bold'))
Label12.pack()
Enter12.pack()
English2.pack()
Maths2 = Frame(Notes2)
Label22 = Label(Maths2,
                text = 'Marks scored in Maths Test 2: ',
                font = ('Comic Sans MS', 18, 'bold'))
Enter22 = Entry(Maths2,
                font = ('Comic Sans MS', 18, 'bold'))
Label22.pack()
Enter22.pack()
Maths2.pack()
Science2 = Frame(Notes2)
Label32 = Label(Science2,
                text = 'Marks scored in Science Test 2: ',
                font = ('Comic Sans MS', 18, 'bold'))
Enter32 = Entry(Science2,
                font = ('Comic Sans MS', 18, 'bold'))
Label32.pack()
Enter32.pack()
Science2.pack()


#Father's Name, Mother's name and Phone no. Frame
Frame_8 = Frame(master = root)
Frame_8_1 = Frame(master = Frame_8)
LabelA = Label(Frame_8_1,
               text = "Father's Name: ",
               font = ('Comic Sans MS', 18, 'bold italic'))
EntryA = Entry(master = Frame_8_1,
               bootstyle = 'info',
               font = ('Comic Sans MS', 15, 'bold italic'),
               width = 20)
Frame_8_2 = Frame(master = Frame_8)
Labelb = Label(Frame_8_2,
               text = "Mother's Name: ",
               font = ('Comic Sans MS', 18, 'bold italic'))
Entryb = Entry(master = Frame_8_2,
               bootstyle = 'info',
               font = ('Comic Sans MS', 18, 'bold italic'),
               width = 20)
Frame_9 = Frame(master = Frame_8)
LabelC = Label(Frame_9,
               text = "Phone no.: ",
               font = ('Comic Sans MS', 18, 'bold italic'))
EntryC = Entry(master = Frame_9,
               bootstyle = 'info',
               font = ('Comic Sans MS', 18, 'bold italic'),
               width = 20)
LabelA.pack(padx = 5)
EntryA.pack(padx = 5)
Frame_8_1.pack(side = 'left',
               padx = 5)
Labelb.pack(padx = 5)
Entryb.pack(padx = 5)
Frame_8_2.pack(side = 'left',
               padx = 5)
LabelC.pack(padx = 5)
EntryC.pack(padx = 5)
Frame_9.pack(side = 'left',
             padx = 5)
Frame_8.place(relx = 0.38,
              rely = 0.75,
              anchor = 'w')

#Defining function for saving info into database
def showinfo():

    #Adjusting the Name, DOB, and Gender boxes
    Frame_3.place(relx = 0.44675)
    Frame_4.place(relx=0.578)
    Frame_5.place(relx=0.706125)

    #Creating variables for Father's name, Mother's name and Phone No.
    m = EntryA.get()
    n = Entryb.get()
    o = EntryC.get()

    #Destroying the Frame with Father's name, Mother's name and Phone No. boxes
    Frame_8.destroy()

    #Creating the Treeview
    s = Style()
    s.configure('Treeview',
                font = ('Comic Sans MS', 9, 'bold italic'))
    Tree = Treeview(master = root,
                    bootstyle = 'success',
                    height=8)

    #Treeview Columns
    Tree['columns'] = ("Detail",
                       "Student's Detail")
    Tree.column('#0',
                anchor = CENTER,
                width = 50)
    Tree.column("Detail",
                anchor=CENTER,
                width = 140)
    Tree.column("Student's Detail",
                anchor=CENTER,
                width = 150)
    Tree.heading("#0",
                 text = "S.no.",
                 anchor = CENTER)
    Tree.heading("Detail",
                 text = 'Detail',
                 anchor = CENTER)
    Tree.heading("Student's Detail",
                 text="Student's Detail",
                 anchor=CENTER)

    #Values to insert in Treeview
    Tree.insert('',
                'end',
                text = "1.",
                values = ('Name',
                          Entry_1.get()))
    Tree.insert('',
                'end',
                text="2.",
                values=('DOB',
                        Entry_2.entry.get()))
    Tree.insert('',
                'end',
                text="3.",
                values=('Gender: ',
                        Entry_3['text']))
    Tree.insert('',
                'end',
                text="4.",
                values=("Father's Name: ",
                        m))
    Tree.insert('',
                'end',
                text="5.",
                values=("Mother's Name: ",
                        n))
    Tree.insert('',
                'end',
                text="6.",
                values=('Phone no.:' ,
                        o))
    Tree.place(relx = 0.78,
               rely = 0.1312)

    #Frame with the Scales of Average marks scored in Exam 1 and 2
    Frame_6 = Frame(master = root)
    Label_5 = Label(master = Frame_6,
                    text = f'Average marks scored in Exam 1 ({int(int(Enter1.get()) + int(Enter2.get()) + int(Enter3.get())) / 3}%): ',
                    font = ('Comic Sans MS', 12, 'bold'))
    Label_6 = Label(master = Frame_6,
                    text = f'Average marks scored in Exam 2 ({(int(Enter12.get()) + int(Enter22.get()) + int(Enter32.get())) / 3}%): ',
                    font = ('Comic Sans MS', 12, 'bold'))
    Scale_1 = Scale(master = Frame_6,
                    from_ = 1,
                    to = 100,
                    value = (int(Enter1.get()) + int(Enter2.get()) + int(Enter3.get())) / 3,
                    bootstyle = 'danger')
    Scale_2 = Scale(master = Frame_6,
                    from_ = 1,
                    to = 100,
                    value = (int(Enter12.get()) + int(Enter22.get()) + int(Enter32.get())) / 3,
                    bootstyle = 'danger')
    Label_5.pack()
    Scale_1.pack()
    Label_6.pack()
    Scale_2.pack()
    Frame_6.place(relx = 0.45,
                  rely = 0.72)

    # Progressbar Value
    x = int(Scale_2.get()) - int(Scale_1.get())

    #Creating the Progressbar
    Frame_7 = Frame(master = root)
    Label_7 = Label(master = Frame_7,
                    text = f'Progress ({int(Scale_2.get()) - int(Scale_1.get())}): ',
                    font = ('Comic Sans MS', 12, 'bold'))
    Prog = Progressbar(master = Frame_7,
                       maximum=100, value=x,
                       bootstyle = 'danger striped',
                       length = 360)

    #Packing the Frame with Progressbar
    Label_7.pack()
    Prog.pack()
    Frame_7.place(relx = 0.4,
                  rely = 0.85)

    #Variables for age:
    x = (Entry_2.entry.get()) #DOB Entry
    y = list(x.split())[2] #Year of Birth
    t = int(a) - int(y) #Age --> Current Year - Birth Year

    #Meter displaying age
    Metre = Meter(master=root,
                  amounttotal=100,
                  metertype='full',
                  stepsize=1,
                  interactive=False,
                  subtext='Years Old',
                  subtextfont=('Comic Sans MS', 10),
                  stripethickness=1,
                  amountused=t)
    Metre.place(relx = 0.75,
                rely = 0.68)

    # Variable for Gender
    f = Entry_3['text']

    #Creating list of variables in a row
    timelist = [(Entry_1.get(),
                 Entry_2.entry.get(),
                 f, m, n, o,
                 Scale_1['value'],
                 Scale_2['value'],
                 str(Scroll.get('1.0',
                                '2.0')).replace('\n',
                                                ''))]

    #Insert the list of variables
    Timmy.executemany('insert into info values (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                      timelist)

    #Printing the database's info on the Terminal
    for row in Timmy.execute('select * from info'):
        print(row)

    #Commiting and Closing the Connection
    Time.commit()

#The Update Function
def updateinfo():

    #Making a Button Style
    mystyle = Style()
    mystyle.configure('warning.TButton',
                      font=('Comic Sans MS', 15, 'bold italic'))

    #Creating the actual update function
    def update():
        Timmy.execute('select * from info where name=:b and code=:c',
                      {'b': list(Entry_4.get().split(' | '))[0],
                           'c': list(Entry_4.get().split(' | '))[1]})
        recoall = Timmy.fetchall()
        if recoall == []:
            messagebox.showinfo('sqlite3.NotFoundError', 'Your person was not found. Please Try Again')

        else:
            #If The Combobox's value is Name,
            #Set the Name column to be the value of Entry No.5,
            #Where the first value of the two values in Entry No.4 is the Name value of the row
            #And the code is the second part
            if Setting.get() == 'Name':
                Timmy.execute('update info set name=:a where name=:b, code=:c',
                              {'a': Entry_5.get(),
                               'b': list(Entry_4.get().split(' | '))[0],
                               'c': list(Entry_4.get().split(' | '))[1]})

            # If The Combobox's value is DOB,
            # Set the dob column to be the value of Entry No.5,
            # Where the first value of the two values in Entry No.4 is the Name value of the row
            # And the code is the second part
            elif Setting.get() == 'DOB':
                Timmy.execute('update info set dob=:a where name=:b, code=:c',
                              {'a': Entry_5.get(),
                               'b': list(Entry_4.get().split(' | '))[0],
                               'c': list(Entry_4.get().split(' | '))[1]})

            # If The Combobox's value is Gender,
            # Set the Gender column to be the value of Entry No.5,
            # Where the first value of the two values in Entry No.4 is the Name value of the row
            # And the code is the second part
            elif Setting.get() == 'Gender':
                Timmy.execute('update info set gender=:a where name=:b, code=:c',
                              {'a': Entry_5.get(),
                               'b': list(Entry_4.get().split(' | '))[0],
                               'c': list(Entry_4.get().split(' | '))[1]})

            # If The Combobox's value is Father's name,
            # Set the fatnam column to be the value of Entry No.5,
            # Where the first value of the two values in Entry No.4 is the Name value of the row
            # And the code is the second part
            elif Setting.get() == "Father's name":
                Timmy.execute('update info set fatnam=:a where name=:b,'
                              ' code=:c',
                              {'a': Entry_5.get(),
                               'b': list(Entry_4.get().split(' | '))[0],
                               'c': list(Entry_4.get().split(' | '))[1]})

            # If The Combobox's value is Mother's name,
            # Set the motnam column to be the value of Entry No.5,
            # Where the first value of the two values in Entry No.4 is the Name value of the row
            # And the code is the second part
            elif Setting.get() == "Mother's name":
                Timmy.execute('update info set motnam=:a where name=:b and code=:c',
                              {'a': Entry_5.get(),
                               'b': list(Entry_4.get().split(' | '))[0],
                               'c': list(Entry_4.get().split(' | '))[1]})

            # If The Combobox's value is Phone no.,
            # Set the phone column to be the value of Entry No.5,
            # Where the first value of the two values in Entry No.4 is the Name value of the row
            # And the code is the second part
            elif Setting.get() == 'Phone no.':
                Timmy.execute('update info set phone=:a where name=:b, code=:c',
                              {'a': Entry_5.get(),
                               'b': list(Entry_4.get().split(' | '))[0],
                               'c': list(Entry_4.get().split(' | '))[1]})


            # If The Combobox's value is 'Exam 2 marks',
            # Set the examavg1 column to be the value of Entry No.5,
            # Where the first value of the two values in Entry No.4 is the Name value of the row
            # And the code is the second part
            elif Setting.get() == 'Exam 1 marks':
                Timmy.execute('update info set examavg1=:a where name=:b, code=:c',
                              {'a': Entry_5.get(),
                               'b': list(Entry_4.get().split(' | '))[0],
                               'c': list(Entry_4.get().split(' | '))[1]})

            # If The Combobox's value is 'Exam 2 marks',
            # Set the examavg2 column to be the value of Entry No.5,
            # Where the first value of the two values in Entry No.4 is the Name value of the row
            # And the code is the second part
            elif Setting.get() == 'Exam 2 marks':
                Timmy.execute('update info set examavg2=:a where name=:b, code=:c',
                              {'a': Entry_5.get(),
                               'b': list(Entry_4.get().split(' | '))[0],
                               'c': list(Entry_4.get().split(' | '))[1]})
            elif Setting.get() == 'Code':
                Timmy.execute('update info set code=:a where name=:b, code=:c',
                              {'a': Entry_5.get(),
                               'b': list(Entry_4.get().split(' | '))[0],
                               'c': list(Entry_4.get().split(' | '))[1]})

            Time.commit()
            messagebox.showinfo('sqlite3.UpdateSuccess', 'Updated Successfully!')
    #The GUI
    Label_5 = Label(master = root,
                    text = 'Name | Code : ',
                    font = ('Comic Sans MS', 12))

    Entry_4 = Entry(master = root,
                    font = ('Comic Sans MS', 12),
                    bootstyle = 'danger')

    #The Combobox mentioned above
    Setting = Combobox(master = root,
                       font = ('Comic Sans MS', 12))

    #The Combolist
    Setting['values'] = ['Name',
                         'DOB',
                         'Gender',
                         "Father's name",
                         "Mother's name",
                         'Phone no.',
                         'Exam 1 marks',
                         'Exam 2 marks',
                         'Code']

    #The Change Entry
    Entry_5 = Entry(master=root,
                    font=('Comic Sans MS', 12),
                    bootstyle='danger')
    Entry_5.insert(END,
                   'Change: ')

    #The ComboLabel
    Label_6 = Label(master=root,
                    text='Setting: ',
                    font=('Comic Sans MS', 12))

    #The updater
    Button_1 = Button(master = root,
                      text = 'Save',
                      style='warning.TButton',
                      command = update)

    #First Destroy, then 'Pack'! Wait...No, it's 'Place'
    Frame_2.destroy()
    Label_5.place(relx = 0.08,
                  rely = 0.4)
    Entry_4.place(relx = 0.18,
                  rely = 0.4)
    Label_6.place(relx = 0.08,
                  rely = 0.47)
    Setting.place(relx = 0.14,
                  rely = 0.47)
    Entry_5.place(relx = 0.08,
                  rely = 0.54)
    Button_1.place(relx = 0.08,
                   rely = 0.61)

#Die Suchfunktion
def findtheinfo():
    rec = ([])

    #The Display
    Label_8 = Label(root,
                    text='Your Find!',
                    font = ('Comic Sans MS', 18),
                    justify='left')

    Label_8.place(relx = 0.13,
                  rely = 0.25)

    #The Button Style
    mystyle = Style()
    mystyle.configure('warning.TButton',
                      font=('Comic Sans MS',
                            15,
                            'bold italic'))

    #Die Eigentliche Suchfunktion
    def Find():

        #If the Combobox says 'All'!
        if Entry_5.get() == 'All':
            Timmy.execute('select * from info where name=:A and code=:B',
                          {'A': list(Entry_4.get().split(' | '))[0],
                           'B': list(Entry_4.get().split(' | '))[1]})
            rec = Timmy.fetchall()
            printi = ''
            if rec == []:
                messagebox.showinfo('sqlite3.NotFoundError', 'We cannot find your person here. Please Try Again.')
            for i in range(len(rec)):
                reclist = ['Name',
                           'DOB',
                           'Gender',
                           "Father's name",
                           "Mother's name",
                           'Phone no.',
                           'Exam 1 marks',
                           'Exam 2 marks',
                           'Code']
                i2 = 0
                for j in rec[i]:
                    if reclist[i2] == 'Code':
                        if j == '':
                            printi += reclist[i2] + ': ' + 'None'
                        else:
                            printi += reclist[i2] + ': ' + str(j)
                    else:
                        printi += reclist[i2] + ': ' + str(j) + ',\n'
                    i2 += 1

            Label_8.place_configure(rely = 0.17)
            Label_8.configure(text=printi,
                              font=('Comic Sans MS',
                                    10,
                                    'bold'))


        # If the Combobox says 'DOB'!
        elif Entry_5.get() == 'DOB':
                Timmy.execute('select name, dob from info where name=:A and code=:B',
                              {'A': list(Entry_4.get().split(' | '))[0],
                               'B': list(Entry_4.get().split(' | '))[1]})
                rec = Timmy.fetchall()
                if rec == []:
                    messagebox.showinfo('sqlite3.NotFoundError', 'We cannot find your person here. Please Try Again.')
                printi = ''
                for i in range(len(rec)):
                    reclist = ['Name',
                               'DOB']
                    i2 = 0
                    for j in rec[i]:
                        if reclist[i2] == 'DOB':
                            printi += reclist[i2] + ': ' + str(j)
                        else:
                            printi += reclist[i2] + ': ' + str(j) + ',\n'
                        i2 += 1
                Label_8.configure(text=printi,
                                  font=('Comic Sans MS',
                                        15,
                                        'bold'))

        # If the Combobox says 'Father's name'!
        elif Entry_5.get() == "Father's name":
                Timmy.execute('select name, fatnam from info where name=:A and code=:B',
                              {'A': list(Entry_4.get().split(' | '))[0],
                               'B': list(Entry_4.get().split(' | '))[1]})
                rec = Timmy.fetchall()
                if rec == []:
                    messagebox.showinfo('sqlite3.NotFoundError', 'We cannot find your person here. Please Try Again.')
                printi = ''
                for i in range(len(rec)):
                    reclist = ['Name',
                               "Father's name"]
                    i2 = 0
                    for j in rec[i]:
                        if reclist[i2] == "Father's name":
                            printi += reclist[i2] + ': ' + str(j)
                        else:
                            printi += reclist[i2] + ': ' + str(j) + ',\n'
                        i2 += 1
                Label_8.configure(text=printi,
                                  font=('Comic Sans MS',
                                        15,
                                        'bold'))

        # If the Combobox says 'Mother's name'!
        elif Entry_5.get() == "Mother's name":
                Timmy.execute('select name, motnam from info where name=:A and code=:B',
                              {'A': list(Entry_4.get().split(' | '))[0],
                               'B': list(Entry_4.get().split(' | '))[1]})
                rec = Timmy.fetchall()
                if rec == []:
                    messagebox.showinfo('sqlite3.NotFoundError', 'We cannot find your person here. Please Try Again.')
                printi = ''
                for i in range(len(rec)):
                    reclist = ['Name',
                               "Mother's name"]
                    i2 = 0
                    for j in rec[i]:
                        if reclist[i2] == "Mother's name":
                            printi += reclist[i2] + ': ' + str(j)
                        else:
                            printi += reclist[i2] + ': ' + str(j) + ',\n'
                        i2 += 1
                Label_8.configure(text=printi, font=('Comic Sans MS', 15, 'bold'))

        # If the Combobox says 'phone'!
        elif Entry_5.get() == "Phone no.":
                Timmy.execute('select name, phone from info where name=:A and code=:B',
                              {'A': list(Entry_4.get().split(' | '))[0], 'B': list(Entry_4.get().split(' | '))[1]})
                rec = Timmy.fetchall()
                if rec == []:
                    messagebox.showinfo('sqlite3.NotFoundError', 'We cannot find your person here. Please Try Again.')
                printi = ''
                for i in range(len(rec)):
                    reclist = ['Name',
                               "Phone no."]
                    i2 = 0
                    for j in rec[i]:
                        if reclist[i2] == 'Phone no.':
                            printi += reclist[i2] + ': ' + str(j)
                        else:
                            printi += reclist[i2] + ': ' + str(j) + ',\n'
                        i2 += 1
                Label_8.configure(text=printi,
                                  font=('Comic Sans MS',
                                        15,
                                        'bold'))

        # If the Combobox says 'Exam 1 marks'!
        elif Entry_5.get() == "Exam 1 marks":
                Timmy.execute('select name, examavg1 from info where name=:A and code=:B',
                              {'A': list(Entry_4.get().split(' | '))[0],
                               'B': list(Entry_4.get().split(' | '))[1]})
                rec = Timmy.fetchall()
                if rec == []:
                    messagebox.showinfo('sqlite3.NotFoundError', 'We cannot find your person here. Please Try Again.')
                printi = ''
                for i in range(len(rec)):
                    reclist = ['Name',
                               "Marks scored in the First Exam"]
                    i2 = 0
                    for j in rec[i]:
                        if reclist[i2] == "Marks scored in the First Exam":
                            printi += reclist[i2] + ': ' + str(j)
                        else:
                            printi += reclist[i2] + ': ' + str(j) + ',\n'
                        i2 += 1
                Label_8.configure(text=printi,
                                  font=('Comic Sans MS',
                                        15,
                                        'bold'))

        # If the Combobox says 'Exam 2 marks'!
        else:
                Timmy.execute('select name, examavg2 from info where name=:A and code=:B',
                              {'A': list(Entry_4.get().split(' | '))[0],
                               'B': list(Entry_4.get().split(' | '))[1]})

                rec = Timmy.fetchall()
                if rec == []:
                    messagebox.showinfo('sqlite3.NotFoundError', 'We cannot find your person here. Please Try Again.')
                printi = ''
                for i in range(len(rec)):
                    reclist = ['Name',
                               "Marks scored in the Second Exam"]
                    i2 = 0
                    for j in rec[i]:
                        if reclist[i2] == "Marks scored in the Second Exam":
                            printi += reclist[i2] + ': ' + str(j)
                        else:
                            printi += reclist[i2] + ': ' + str(j) + ',\n'
                        i2 += 1

                Label_8.configure(text=printi, font=('Comic Sans MS',
                                                     15,
                                                     'bold'))

    #Die grafische Benutzeroberfläche
    Label_5 = Label(master = root,
                    text = 'Name | Code: ',
                    font = ('Comic Sans MS', 12))
    Entry_4 = Entry(master = root,
                    font = ('Comic Sans MS', 12),
                    bootstyle = 'danger')
    Label_6 = Label(master = root,
                    text = 'Optional Find: ',
                    font = ('Comic Sans MS', 12))

    #Wanna Have a COMBO?
    Entry_5 = Combobox(master = root,
                       bootstyle = 'danger',
                       font = ('Comic Sans MS', 12))

    #Oh Really! Here is the list
    Entry_5['values'] = ['All',
                         'DOB',
                         "Father's name",
                         "Mother's name",
                         'Phone no.',
                         'Exam 1 marks',
                         'Exam 2 marks']
    Entry_5.current(0)

    #Der Einzige ... Sucher!
    Button_1 = Button(master = root,
                      text = 'Name | Code: ',
                      style='warning.TButton',
                      command = Find)
    Frame_2.destroy()

    #Place Again!
    Label_5.place(relx = 0.06,
                  rely = 0.4)
    Entry_4.place(relx = 0.15,
                  rely = 0.4)
    Label_6.place(relx=0.06,
                  rely=0.45)
    Entry_5.place(relx=0.15,
                  rely=0.45)
    Button_1.place(relx=0.115,
                   rely = 0.525)

#Die Löschfunktion
def delinfo():


    # The Button Style
    mystyle = Style()
    mystyle.configure('warning.TButton',
                      font=('Comic Sans MS',
                            15,
                            'bold italic'))

    #Die Eigentliche Löschfunktion
    def Delete():
        Timmy.execute('select * from info where name=:b and code=:c',
                      {'b': list(Entry_4.get().split(' | '))[0],
                       'c': list(Entry_4.get().split(' | '))[1]})
        recoall = Timmy.fetchall()
        if recoall == []:
            messagebox.showinfo('sqlite3.NotFoundError', 'Your person was not found. Please Try Again')
        else:
            Timmy.execute('DELETE FROM info WHERE name=:a and code=:b', {'a': list(str(Entry_4.get()).split(' | '))[0], 'b': list(str(Entry_4.get()).split(' | '))[1],})
            Time.commit()
            messagebox.showinfo('sqlite3.DeleteSuccess', 'Deleted Successfully!')

    #Ich denke, wir sollten jetzt die Graphichalbenutzeroberfläche erstellen!
    Frame_2.destroy()
    Label_6 = Label(master = root,
                    text = 'Name | Code: ',
                    font = ('Comic Sans MS', 15, 'bold'))
    Entry_4 = Entry(font = ('Comic Sans MS', 15, 'bold'),
                    master = root)
    Entry_4.insert(END,
                   'Name | Code')
    Button_1 = Button(root,
                      text = 'Delete?',
                      command = Delete,
                     style = 'warning.TButton')
    Label_6.place(relx = 0.04,
                  rely = 0.4)
    Entry_4.place(relx = 0.17,
                  rely = 0.39555)
    Button_1.place(relx = 0.145,
                   rely = 0.5)


#Creating Button Style for "Add, Update, Find, and Delete" buttons
mystyle = Style()
mystyle.configure('warning.TButton',
                  font=('Comic Sans MS', 15, 'bold italic'))

#Add Button
Buttontype = Button(master = root,
                    text = 'Find Progress and Add?',
                    style = 'warning.TButton',
                    command = showinfo)
Buttontype.place(relx = 0.55,
                 rely = 0.65)

#Find button
Buttontypo = Button(master = root,
                    text = 'Find?',
                    style = 'warning.TButton',
                    command = findtheinfo)
Buttontypo.place(relx = 0.88,
                 rely = 0.14)

#Delete Button
Buttontyper = Button(master = root,
                     text = 'Delete?',
                     style = 'warning.TButton',
                     command = delinfo)
Buttontyper.place(relx = 0.8725,
                  rely = 0.205)

#Update Button
Buttontypetyper = Button(master = root,
                         text = 'Update?',
                         style = 'warning.TButton',
                         command = updateinfo)
Buttontypetyper.place(relx = 0.8725,
                      rely = 0.265)


#Opening the Window
root.mainloop()

#Vielleicht wird diese grafische Benutzeroberfläche zu benutzerfreundlich!