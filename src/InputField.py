from tkinter import*

windows=Tk()
windows.geometry("500x500")
windows.title("Input Field")
windows.config(bg='#A6E1FA')

sos = IntVar()
alphabat = StringVar()
transition = StringVar()
start_state = IntVar()
final_state = IntVar()

def test_type():
    answer.config(text='This FA is ' +sos.get()+ ' type')

sos = Label(text = "Set of State", width="15" ,height="1", bg= '#0E6BA8', font=('Ariel',10), fg='#fff')
sos.place(x=10, y = 50)
alphabat = Label(text= "Alphabat", width="15" ,height="1", bg= '#0E6BA8', font=('Ariel',10), fg='#fff')
alphabat.place(x=10, y = 100)
transition = Label(text= "Transition", width="15" ,height="1", bg= '#0E6BA8', font=('Ariel',10), fg='#fff')
transition.place(x=10, y = 150)
start_state = Label(text= "Start State", width="15" ,height="1", bg= '#0E6BA8', font=('Ariel',10), fg='#fff')
start_state.place(x=10, y = 200)
final_state = Label(text= "Set of Finnal State", width="15" ,height="1", bg= '#0E6BA8', font=('Ariel',10), fg='#fff')
final_state.place(x=10, y = 250)


sos = Entry(textvariable= sos, width="25")
sos.place(x=150, y=50)
alphabat = Entry(textvariable= alphabat, width="25")
alphabat.place(x=150, y=100)
transition = Entry(textvariable= transition, width="25")
transition.place(x=150, y=150)
start_state = Entry(textvariable= start_state, width="25")
start_state.place(x=150, y=200)
final_state = Entry(textvariable= final_state, width="25")
final_state.place(x=150, y=250)

answer= Label(windows,fg='black' , bg='#A6E1FA',font=('Ariel',13))
answer.place(x= 30, y = 380 )

check = Button(windows,text="Check type of FA", width="15", height="2",bg='#0E6BA8',command=test_type ,fg='#fff')
check.place(x=170, y= 300)

windows.mainloop()
