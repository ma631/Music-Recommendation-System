import mysql.connector
from tkinter import *
from tkinter import ttk
import re
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "pass",
    auth_plugin='mysql_native_password',
    database = 'MahakProject'
)
mycursor = db.cursor(buffered=True)
# mycursor.execute("CREATE DATABASE MahakProject")
# mycursor.execute("CREATE TABLE SongList (Serial_Number int, Song varchar(50), Artist varchar(50), Genre varchar(50), Language varchar(10))")
# mycursor.execute("INSERT INTO Songlist (Serial_Number, Song, Artist, Genre,Language) VALUES (1,'Afgan Jalebi','Asrar','Item Song','Hindi')") # Insert Statement
# mycursor.execute("INSERT INTO Songlist (Serial_Number, Song, Artist, Genre,Language) VALUES (2,'Khairiyat','Pritam','Love Song','Hindi')")
# mycursor.execute("INSERT INTO Songlist (Serial_Number, Song, Artist, Genre,Language) VALUES (3,'Any man of mine','Shania Twain','Country Song','English')")
# mycursor.execute("INSERT INTO Songlist (Serial_Number, Song, Artist, Genre,Language) VALUES (4,'Raataan Lambiyan','Jubin','Romantic Song','Hindi')")
# mycursor.execute("INSERT INTO Songlist (Serial_Number, Song, Artist, Genre,Language) VALUES (5,'Humnava','Jubin','Romantic Song','Hindi')")
# mycursor.execute("INSERT INTO Songlist (Serial_Number, Song, Artist, Genre,Language) VALUES (6,'Lut Gaye','Jubin','Romantic Song','Hindi')")
# mycursor.execute("INSERT INTO Songlist (Serial_Number, Song, Artist, Genre,Language) VALUES (7,'Jannat Ve','Darshan','Love Song','Hindi')")
def retrieve():
    a = clicked1.get()
    a = "".join(re.split("[^a-zA-Z]*", a))
    a = "'" + a + "'"
    query4 = ("SELECT * FROM Songlist where Artist = " + a + "ORDER BY RAND() LIMIT 1")
    mycursor.execute(query4)
    result4 = mycursor.fetchall()
    label5 = Label(my_frame1, text='                                                                 ', font ="times 30 bold")
    label5.place(x=50, y=300)
    label4 = Label(my_frame1, text=result4, font="times 20 bold")
    label4.place(x=50, y=300)
def addition():
    w = e20.get()
    x = e21.get()
    y = e22.get()
    z = e23.get()
    mycursor.execute("INSERT INTO Songlist (Serial_Number, Song, Artist, Genre,Language) VALUES (30,%s,%s,%s,%s)",(w,x,y,z))
    db.commit()

window=Tk()
window.title("Song Suggestion by Mahak")
window.geometry("1000x500")

my_notebook = ttk.Notebook(window)
my_notebook.pack()

my_frame1 = Frame(my_notebook, width=1000, height=500)
my_frame2 = Frame(my_notebook, width=1000, height=500)

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Get a Suggestion")
my_notebook.add(my_frame2, text="Add New Song")

label=Label(my_frame1,text="Song Suggestion",font="times 30 bold")
label.place(x=220,y=30)

label1=Label(my_frame1,text="Select Artist",font="times 15 bold")
label1.place(x=105,y=150)
query1 = "Select distinct Artist from SongList;"

mycursor.execute(query1)

result1 = mycursor.fetchall()

options1 = [list(i) for i in result1]
options1.append("All")

# datatype of menu text
clicked1 = StringVar()

# initial menu text
clicked1.set("All")

# Create Dropdown menu
drop1 = OptionMenu(my_frame1, clicked1, *options1)
drop1.place(x=105,y=200)


b21 = Button(my_frame1,text = "Find Me A Song", width = 20, command = retrieve)
b21.place(x=500,y=400)



label=Label(my_frame2,text="Song Addition",font="times 30 bold")
label.place(x=220,y=30)

label20=Label(my_frame2,text="Song Name",font="times 15 bold")
label20.place(x=55,y=150)
e20=Entry(my_frame2)
e20.place(x=55,y=175)

label21=Label(my_frame2,text="Artist Name",font="times 15 bold")
label21.place(x=200,y=150)
e21=Entry(my_frame2)
e21.place(x=200,y=175)


label22=Label(my_frame2,text="Genre",font="times 15 bold")
label22.place(x=345,y=150)
e22=Entry(my_frame2)
e22.place(x=345,y=175)


label3=Label(my_frame2,text="Language",font="times 15 bold")
label3.place(x=490,y=150)
e23=Entry(my_frame2)
e23.place(x=490,y=175)


b22 = Button(my_frame2,text = "Add My Song", width = 20, command = addition)
b22.place(x=500,y=400)

window.mainloop()