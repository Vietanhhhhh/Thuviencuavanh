from django.shortcuts import render
#from django.http import HttpResponse
from pyngrok import ngrok
# Create your views here.
http_url = ngrok.connect(8000)
#def index(response):
#    return HttpResponse("<h1> text view </h1><p>xin chao</p>")
from tkinter import *
from tkinter import messagebox

Num_time = 0

def game(request):
    window = Tk()
    window.title("Beautiful Check")
    window.geometry("600x420")
    Name = Label(window,
                 text="Code check : ",
                 font=("Arial", 20))
    Name.place(x=50, y=50)

    entry_name = Entry(window,
                       font=("Arial", 20), )
    entry_name.place(x=200, y=50)


    def Check():
        Correct_name = entry_name.get().lower()
        if Correct_name == "hằng xinh gái nhất hệ mặt trời":
            print("Welcome " + Correct_name)
            window.destroy()

            A = Tk()
            A.geometry("600x600")
            Photo = PhotoImage(file="C:/Users/anhle/OneDrive/Pictures/Screenshots/Screenshot 2023-07-18 181521.png")
            B = Label(A,
                      image=Photo)
            B.pack()
            A.mainloop()
        else:
            global Num_time
            wrong_name = Label(window, text="Không phải đâu tiếp tục đi",
                               font=("Arial", 10), fg="red")
            wrong_name.place(x=300, y=100)
            entry_name.delete(0, END)
            Num_time += 1
            if Num_time == 2:
                wrong_name.config(text="Có tên của ai đó á                    ")
            if Num_time == 3:
                wrong_name.config(text="Rồi nhưng mà ai đó làm sao cơ          ")
            if Num_time == 4:
                wrong_name.config(text="À còn trong dải ngân hà nữa á          ")
            if Num_time == 5:
                wrong_name.config(text="Còn cơ hội cuối nè                            ")
            if Num_time > 5:
                wrong_name.config(text="                                                       ")
                messagebox.showinfo(title='Loi nhan', message="Hằng không hiểu b ồi")
                window.destroy()


    button_check = Button(window, text="Check",
                          command=Check)

    button_check.pack()
    window.mainloop()
    return render(request)


