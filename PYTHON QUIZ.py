from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Quiz")
window.geometry("500x500")

easy = StringVar()
name = StringVar()

def show():
    easy1 = easy.get()
    name1 = name.get()
    if easy1 == "easy":
        neweasy = Toplevel()
        neweasy.title("Question Bank")
        neweasy.geometry("1000x100")

        s = StringVar()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()
        f = StringVar()
        g = StringVar()
        h = StringVar()
        i = StringVar()

        def score():
            s1 = s.get()
            a1 = a.get()
            b1 = b.get()
            c1 = c.get()
            d1 = d.get()
            e1 = e.get()
            f1 = f.get()
            g1 = g.get()
            h1 = h.get()
            i1 = i.get()

            count = 0


            if  s1== "b":
                count+=1
            if  a1== "c":
                count+=1
            if b1 == "d":
                count += 1
            if c1 == "c":
                count += 1
            if d1 == "c":
                count += 1
            if e1 == "d":
                count += 1
            if f1 == "c":
                count += 1
            if g1 == "b":
                count += 1
            if h1 == "c":
                count += 1
            if i1 == "a":
                count += 1

            messagebox.showinfo("Result",count)


        label0 = Label(neweasy, text="Welcome " + name1, font=(15)).place(x=50, y=30)


        label1 = Label(neweasy, text="Question1  Suppose t = (1, 2, 4, 3), which of the following is incorrect? ", font=(12)).place(x=40, y=80)

        radio0 = Radiobutton(neweasy, text=" print(t[3])", value="a",variable=s, font =(9)).place(x=120, y=120)
        radio1 = Radiobutton(neweasy, text="t[3]=45",value="b", variable=s, font=(9)).place(x=120, y=150)
        radio2 = Radiobutton(neweasy, text="print(max(t))",value="c",variable=s, font=(9)).place(x=290, y=125)
        radio3 = Radiobutton(neweasy, text="print(len(t))",value="d", variable=s,font=(9)).place(x=290, y=155)

        label1 = Label(neweasy, text="Question2  which of the following is the tuple ", font=(12)).place(x=40,y=190)

        radio4 = Radiobutton(neweasy, text=" [1, 2, 3]", value="a", variable=a, font=(9)).place(x=120, y=230)
        radio5 = Radiobutton(neweasy, text="(1, 2, 3)", value="b", variable=a, font=(9)).place(x=120, y=260)
        radio6 = Radiobutton(neweasy, text="{1, 2, 3}", value="c", variable=a, font=(9)).place(x=290, y=235)
        radio7 = Radiobutton(neweasy, text="{}", value="d", variable=a, font=(9)).place(x=290, y=265)

        label8 = Label(neweasy, text="Question3 What will be the output of the following Python code? ", font=(12)).place(x=40,y=300)


        radio9 = Radiobutton(neweasy, text=" (1,2)", value="a", variable=b, font=(9)).place(x=120, y=330)
        radio11 = Radiobutton(neweasy, text="(1, 2, 4)", value="b", variable=b, font=(9)).place(x=120, y=360)
        radio12= Radiobutton(neweasy, text="(2,4)", value="c", variable=b, font=(9)).place(x=290, y=335)
        radio13 = Radiobutton(neweasy, text="(2,4,3)", value="d", variable=b, font=(9)).place(x=290, y=365)

        label14 = Label(neweasy, text="Question4  Which of these about a dictionary is false?", font=(12)).place(x=40,y=400)

        radio15 = Radiobutton(neweasy, text="keys", value="a", variable=c, font=(9)).place(x=120, y=430)
        radio16 = Radiobutton(neweasy, text="values", value="b", variable=c, font=(9)).place(x=120, y=460)
        radio17 = Radiobutton(neweasy, text="ordered", value="c", variable=c, font=(9)).place(x=290, y=435)
        radio18 = Radiobutton(neweasy, text="mutable", value="d", variable=c, font=(9)).place(x=290, y=465)

        label19 = Label(neweasy, text="Question 5  The function removes the first element.", font=(12)).place(x=40,y=500)

        radio20 = Radiobutton(neweasy, text=" remove", value="a", variable=d, font=(9)).place(x=120, y=530)
        radio21 = Radiobutton(neweasy, text=" discard", value="b", variable=d, font=(9)).place(x=120, y=560)
        radio22 = Radiobutton(neweasy, text="pop", value="c", variable=d, font=(9)).place(x=290, y=535)
        radio23 = Radiobutton(neweasy, text=" delete", value="d", variable=d, font=(9)).place(x=290, y=565)

        label19 = Label(neweasy, text="Question6 If a={5,6,7,8}, which of the following statements is false? ", font=(12)).place(x=850,y=80)

        radio20 = Radiobutton(neweasy, text=" print(len(a))", value="a", variable=e, font=(9)).place(x=930, y=120)
        radio21 = Radiobutton(neweasy, text=" print(min(a)", value="b", variable=e, font=(9)).place(x=930, y=150)
        radio22 = Radiobutton(neweasy, text="a.remove(5)", value="c", variable=e, font=(9)).place(x=1100, y=125)
        radio23 = Radiobutton(neweasy, text="a[2]=45", value="d", variable=e, font=(9)).place(x=1100, y=155)


        label19 = Label(neweasy, text="Question7  Only problems that recursively defined be solved using recursion. ", font=(12)).place(x=850,y=190)


        radio20 = Radiobutton(neweasy, text=" true", value="a", variable=f, font=(9)).place(x=930, y=230)
        radio21 = Radiobutton(neweasy, text="false", value="b", variable=f, font=(9)).place(x=930, y=260)
        radio22 = Radiobutton(neweasy, text=" both of the above", value="c", variable=f, font=(9)).place(x=1100, y=235)
        radio23 = Radiobutton(neweasy, text=" none of the above", value="d", variable=f, font=(9)).place(x=1100, y=265)

        label19 = Label(neweasy, text="Question8  Recursion and iteration are the same programming approach.", font=(12)).place(x=850,y=300)

        radio20 = Radiobutton(neweasy, text=" true ", value="a", variable=g, font=(9)).place(x=930, y=330)
        radio21 = Radiobutton(neweasy, text=" false", value="b", variable=g, font=(9)).place(x=930, y=360)
        radio22 = Radiobutton(neweasy, text=" both", value="c", variable=g, font=(9)).place(x=1100, y=335)
        radio23 = Radiobutton(neweasy, text=" none of the above", value="d", variable=g, font=(9)).place(x=1100, y=365)

        label19 = Label(neweasy, text = "Question9  Which keyword is used for function ", font=(12)).place(x=850,
                                                                                                                y=400)

        radio20 = Radiobutton(neweasy, text=" fun", value="a", variable=h, font=(9)).place(x=930, y=430)
        radio21 = Radiobutton(neweasy, text=" define ", value="b", variable=h, font=(9)).place(x=930, y=460)
        radio22 = Radiobutton(neweasy, text=" function", value="c", variable=h, font=(9)).place(x=1100, y=435)
        radio23 = Radiobutton(neweasy, text="definition", value="d", variable=h, font=(9)).place(x=1100, y=465)

        label19 = Label(neweasy, text= "Question10  Which of the following functions is a built-in function in python? ", font=(12)).place(x=850,y=500)

        radio20 = Radiobutton(neweasy, text=" sqrt()", value="a", variable=i, font=(9)).place(x=930, y=530)
        radio21 = Radiobutton(neweasy, text=" seed() ", value="b", variable=i, font=(9)).place(x=930, y=560)
        radio22 = Radiobutton(neweasy, text=" factorial()", value="c", variable=i, font=(9)).place(x=1100, y=535)
        radio23 = Radiobutton(neweasy, text=" print()", value="d", variable=i, font=(9)).place(x=1100, y=565)

        button2 = Button(neweasy, text="SUBMIT", font=(15), bg="skyblue", fg="black", command=score).place(x=1150, y=700)


    elif easy1 == "medium":
        neweasy = Toplevel()
        neweasy.title("Question Bank")
        neweasy.geometry("1000x100")

        s = StringVar()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()
        f = StringVar()
        g = StringVar()
        h = StringVar()
        i = StringVar()

        def score():
            s1 = s.get()
            a1 = a.get()
            b1 = b.get()
            c1 = c.get()
            d1 = d.get()
            e1 = e.get()
            f1 = f.get()
            g1 = g.get()
            h1 = h.get()
            i1 = i.get()

            count = 0

            if s1 == "b":
                count += 1
            if a1 == "c":
                count += 1
            if b1 == "d":
                count += 1
            if c1 == "c":
                count += 1
            if d1 == "c":
                count += 1
            if e1 == "d":
                count += 1
            if f1 == "c":
                count += 1
            if g1 == "b":
                count += 1
            if h1 == "c":
                count += 1
            if i1 == "a":
                count += 1

            messagebox.showinfo("Result", count)

        label0 = Label(neweasy, text="Welcome " + name1, font=(15)).place(x=50, y=30)

        label1 = Label(neweasy, text="Question1  Which of the following commands will create a list? ",
                       font=(12)).place(x=40, y=80)

        radio0 = Radiobutton(neweasy, text=" list1 = list()", value="a", variable=s, font=(9)).place(x=120, y=120)
        radio1 = Radiobutton(neweasy, text="list[]", value="b", variable=s, font=(9)).place(x=120, y=150)
        radio2 = Radiobutton(neweasy, text="list1 = list([1, 2, 3])", value="c", variable=s, font=(9)).place(x=290, y=125)
        radio3 = Radiobutton(neweasy, text=" all of the mentioned", value="d", variable=s, font=(9)).place(x=290, y=155)

        label1 = Label(neweasy, text="Question2 What is the output when we execute list(???hello???)? ", font=(12)).place(x=40, y=190)

        radio4 = Radiobutton(neweasy, text=" [???h???, ???e???, ???l???, ???l???, ???o???]", value="a", variable=a, font=(9)).place(x=120, y=230)
        radio5 = Radiobutton(neweasy, text="[???hello???]", value="b", variable=a, font=(9)).place(x=120, y=260)
        radio6 = Radiobutton(neweasy, text=" [???llo???]", value="c", variable=a, font=(9)).place(x=290, y=235)
        radio7 = Radiobutton(neweasy, text=" [???olleh???]", value="d", variable=a, font=(9)).place(x=290, y=265)

        label8 = Label(neweasy, text="Question3  Suppose listExample is [???h???,???e???,???l???,???l???,???o???], what is len(listExample)? ",font=(12)).place(x=40, y=300)

        radio9 = Radiobutton(neweasy, text=" 5 ", value="a", variable=b, font=(9)).place(x=120, y=330)
        radio11 = Radiobutton(neweasy, text=" 4 " , value="b", variable=b, font=(9)).place(x=120, y=360)
        radio12 = Radiobutton(neweasy, text=" none", value="c", variable=b, font=(9)).place(x=290, y=335)
        radio13 = Radiobutton(neweasy, text=" error", value="d", variable=b, font=(9)).place(x=290, y=365)

        label14 = Label(neweasy, text="Question4  Suppose list1 is [2445,133,12454,123], what is max(list1)?", font=(12)).place(x=40,
                                                                                                                 y=400)

        radio15 = Radiobutton(neweasy, text=" 2445", value="a", variable=c, font=(9)).place(x=120, y=430)
        radio16 = Radiobutton(neweasy, text=" 133", value="b", variable=c, font=(9)).place(x=120, y=460)
        radio17 = Radiobutton(neweasy, text=" 12454", value="c", variable=c, font=(9)).place(x=290, y=435)
        radio18 = Radiobutton(neweasy, text="123", value="d", variable=c, font=(9)).place(x=290, y=465)

        label19 = Label(neweasy, text="Question 5 Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?",  font=(12)).place(x=40,y=500)

        radio20 = Radiobutton(neweasy, text=" 3 ", value="a", variable=d, font=(9)).place(x=120, y=530)
        radio21 = Radiobutton(neweasy, text=" 5 ", value="b", variable=d, font=(9)).place(x=120, y=560)
        radio22 = Radiobutton(neweasy, text=" 25", value="c", variable=d, font=(9)).place(x=290, y=535)
        radio23 = Radiobutton(neweasy, text=" 1 ", value="d", variable=d, font=(9)).place(x=290, y=565)

        label19 = Label(neweasy, text="Question6  Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)? ",font=(12)).place(x=850, y=80)

        radio20 = Radiobutton(neweasy, text=" 1 ", value="a", variable=e, font=(9)).place(x=930, y=120)
        radio21 = Radiobutton(neweasy, text="  5", value="b", variable=e, font=(9)).place(x=930, y=150)
        radio22 = Radiobutton(neweasy, text=" 19 ", value="c", variable=e, font=(9)).place(x=1100, y=125)
        radio23 = Radiobutton(neweasy, text=" error " , value="d", variable=e, font=(9)).place(x=1100, y=155)

        label19 = Label(neweasy, text="Question7 To shuffle the list(say list1) what function do we use?", font=(12)).place(x=850, y=190)

        radio20 = Radiobutton(neweasy, text=" list1.shuffle()", value="a", variable=f, font=(9)).place(x=930, y=230)
        radio21 = Radiobutton(neweasy, text=" shuffle(list1)", value="b", variable=f, font=(9)).place(x=930, y=260)
        radio22 = Radiobutton(neweasy, text=" random.shuffle(list)", value="c", variable=f, font=(9)).place(x=1100, y=235)
        radio23 = Radiobutton(neweasy, text=" random.shufflelist(list)", value="d", variable=f, font=(9)).place(x=1100, y=265)

        label19 = Label(neweasy, text="Question8  What is the data type of (1)?", font=(12)).place(x=850, y=300)

        radio20 = Radiobutton(neweasy, text=" tuple ", value="a", variable=g, font=(9)).place(x=930, y=330)
        radio21 = Radiobutton(neweasy, text=" integer", value="b", variable=g, font=(9)).place(x=930, y=360)
        radio22 = Radiobutton(neweasy, text="  dictionary", value="c", variable=g, font=(9)).place(x=1100, y=335)
        radio23 = Radiobutton(neweasy, text="sets ", value="d", variable=g, font=(9)).place(x=1100, y=365)

        label19 = Label(neweasy, text="Question9   If a=(1,2,3,4), a[1:-1] is", font=(12)).place(x=850,
                                                                                                         y=400)

        radio20 = Radiobutton(neweasy, text=" Error, tuple slicing doesn???t exist", value="a", variable=h, font=(9)).place(x=930, y=430)
        radio21 = Radiobutton(neweasy, text=" (2,3)", value="b", variable=h, font=(9)).place(x=930, y=460)
        radio22 = Radiobutton(neweasy, text=" (2,3,4)", value="c", variable=h, font=(9)).place(x=1100, y=435)
        radio23 = Radiobutton(neweasy, text="[2,3]", value="d", variable=h, font=(9)).place(x=1100, y=465)

        label19 = Label(neweasy, text="Question10  What type of data is: a=[(1,1),(2,4),(3,9)]?", font=(12)).place(x=850, y=500)

        radio20 = Radiobutton(neweasy, text=" array of tuples", value="a", variable=i, font=(9)).place(x=930, y=530)
        radio21 = Radiobutton(neweasy, text=" list of tuples ", value="b", variable=i, font=(9)).place(x=930, y=560)
        radio22 = Radiobutton(neweasy, text=" tuples of lists", value="c", variable=i, font=(9)).place(x=1100, y=535)
        radio23 = Radiobutton(neweasy, text=" invalid data ", value="d", variable=i, font=(9)).place(x=1100, y=565)

        button2 = Button(neweasy, text="SUBMIT", font=(15), bg="skyblue", fg="black", command=score).place(x=1150,
                                                                                                           y=700)

    else:
        neweasy = Toplevel()
        neweasy.title("Question Bank")
        neweasy.geometry("1000x100")

        s = StringVar()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()
        f = StringVar()
        g = StringVar()
        h = StringVar()
        i = StringVar()

        def score():
            s1 = s.get()
            a1 = a.get()
            b1 = b.get()
            c1 = c.get()
            d1 = d.get()
            e1 = e.get()
            f1 = f.get()
            g1 = g.get()
            h1 = h.get()
            i1 = i.get()

            count = 0

            if s1 == "b":
                count += 1
            if a1 == "c":
                count += 1
            if b1 == "d":
                count += 1
            if c1 == "c":
                count += 1
            if d1 == "c":
                count += 1
            if e1 == "d":
                count += 1
            if f1 == "c":
                count += 1
            if g1 == "b":
                count += 1
            if h1 == "c":
                count += 1
            if i1 == "a":
                count += 1

            messagebox.showinfo("Result", count)

        label0 = Label(neweasy, text="Welcome " + name1, font=(15)).place(x=50, y=30)

        label1 = Label(neweasy, text="Question1  Which of the following statements create a dictionary?",font=(12)).place(x=40, y=80)

        radio0 = Radiobutton(neweasy, text=" d={}", value="a", variable=s, font=(9)).place(x=120, y=120)
        radio1 = Radiobutton(neweasy, text="  d = {???john???:40, ???peter???:45}", value="b", variable=s, font=(9)).place(x=120, y=150)
        radio2 = Radiobutton(neweasy, text="d = {???john???:40, ???peter???:45}", value="c", variable=s, font=(9)).place(x=290, y=125)
        radio3 = Radiobutton(neweasy, text="all of the mentioned ", value="d", variable=s, font=(9)).place(x=290, y=155)

        label1 = Label(neweasy, text="Question2  Which of these about a set is not true? ", font=(12)).place(x=40, y=190)

        radio4 = Radiobutton(neweasy, text=" mutable data type", value="a", variable=a, font=(9)).place(x=120, y=230)
        radio5 = Radiobutton(neweasy, text="allows duplicate vaalues ", value="b", variable=a, font=(9)).place(x=120, y=260)
        radio6 = Radiobutton(neweasy, text=" Data type with unordered values", value="c", variable=a, font=(9)).place(x=290, y=235)
        radio7 = Radiobutton(neweasy, text=" immutable data type", value="d", variable=a, font=(9)).place(x=290, y=265)

        label8 = Label(neweasy, text="Question3 Which of the following is not the correct syntax for creating a set? ",
                       font=(12)).place(x=40, y=300)

        radio9 = Radiobutton(neweasy, text=" set([[1,2],[3,4]])", value="a", variable=b, font=(9)).place(x=120, y=330)
        radio11 = Radiobutton(neweasy, text=" set([1,2,2,3,4])", value="b", variable=b, font=(9)).place(x=120, y=360)
        radio12 = Radiobutton(neweasy, text="set((1,2,3,4)) ", value="c", variable=b, font=(9)).place(x=290, y=335)
        radio13 = Radiobutton(neweasy, text=" {1,2,3,4}", value="d", variable=b, font=(9)).place(x=290, y=365)

        label14 = Label(neweasy, text="Question4  What will be the output of the following Python code?", font=(12)).place(x=40,
                                                                                                                 y=400)

        radio15 = Radiobutton(neweasy, text=" 7 ", value="a", variable=c, font=(9)).place(x=120, y=430)
        radio16 = Radiobutton(neweasy, text=" error ", value="b", variable=c, font=(9)).place(x=120, y=460)
        radio17 = Radiobutton(neweasy, text=" 4 ", value="c", variable=c, font=(9)).place(x=290, y=435)
        radio18 = Radiobutton(neweasy, text=" 8 ", value="d", variable=c, font=(9)).place(x=290, y=465)

        label19 = Label(neweasy, text="Question 5  Which of the following statements is used to create an empty set?", font=(12)).place(x=40,
                                                                                                              y=500)

        radio20 = Radiobutton(neweasy, text=" {} ", value="a", variable=d, font=(9)).place(x=120, y=530)
        radio21 = Radiobutton(neweasy, text=" set() ", value="b", variable=d, font=(9)).place(x=120, y=560)
        radio22 = Radiobutton(neweasy, text=" [ ]", value="c", variable=d, font=(9)).place(x=290, y=535)
        radio23 = Radiobutton(neweasy, text=" () ", value="d", variable=d, font=(9)).place(x=290, y=565)

        label19 = Label(neweasy, text="Question6 Which of the following statements is used to create an empty set?",
                        font=(12)).place(x=850, y=80)

        radio20 = Radiobutton(neweasy, text=" print(len(a))", value="a", variable=e, font=(9)).place(x=930, y=120)
        radio21 = Radiobutton(neweasy, text=" print(min(a)", value="b", variable=e, font=(9)).place(x=930, y=150)
        radio22 = Radiobutton(neweasy, text="a.remove(5)", value="c", variable=e, font=(9)).place(x=1100, y=125)
        radio23 = Radiobutton(neweasy, text="a[2]=45", value="d", variable=e, font=(9)).place(x=1100, y=155)

        label19 = Label(neweasy, text="Question7  What are the two main types of functions? ",
                        font=(12)).place(x=850, y=190)

        radio20 = Radiobutton(neweasy, text=" built in function", value="a", variable=f, font=(9)).place(x=930, y=230)
        radio21 = Radiobutton(neweasy, text="system function ", value="b", variable=f, font=(9)).place(x=930, y=260)
        radio22 = Radiobutton(neweasy, text=" user function ", value="c", variable=f, font=(9)).place(x=1100, y=235)
        radio23 = Radiobutton(neweasy, text="  custom function", value="d", variable=f, font=(9)).place(x=1100, y=265)

        label19 = Label(neweasy, text="Question8  Where is function defined?",
                        font=(12)).place(x=850, y=300)

        radio20 = Radiobutton(neweasy, text=" module ", value="a", variable=g, font=(9)).place(x=930, y=330)
        radio21 = Radiobutton(neweasy, text=" class", value="b", variable=g, font=(9)).place(x=930, y=360)
        radio22 = Radiobutton(neweasy, text=" another function", value="c", variable=g, font=(9)).place(x=1100, y=335)
        radio23 = Radiobutton(neweasy, text=" all of the mentioned", value="d", variable=g, font=(9)).place(x=1100, y=365)

        label19 = Label(neweasy, text="Question9  What is called when a function is defined inside a class? ", font=(12)).place(x=850,
                                                                                                         y=400)

        radio20 = Radiobutton(neweasy, text=" module", value="a", variable=h, font=(9)).place(x=930, y=430)
        radio21 = Radiobutton(neweasy, text="  class ", value="b", variable=h, font=(9)).place(x=930, y=460)
        radio22 = Radiobutton(neweasy, text=" function", value="c", variable=h, font=(9)).place(x=1100, y=435)
        radio23 = Radiobutton(neweasy, text=" method", value="d", variable=h, font=(9)).place(x=1100, y=465)

        label19 = Label(neweasy, text="Question10  Which of the following refers to mathematical function?",
                        font=(12)).place(x=850, y=500)

        radio20 = Radiobutton(neweasy, text=" sqrt()", value="a", variable=i, font=(9)).place(x=930, y=530)
        radio21 = Radiobutton(neweasy, text=" seed() ", value="b", variable=i, font=(9)).place(x=930, y=560)
        radio22 = Radiobutton(neweasy, text=" factorial()", value="c", variable=i, font=(9)).place(x=1100, y=535)
        radio23 = Radiobutton(neweasy, text=" print()", value="d", variable=i, font=(9)).place(x=1100, y=565)

        button2 = Button(neweasy, text="SUBMIT", font=(15), bg="skyblue", fg="black", command=score).place(x=1150,
                                                                                                           y=700)



label0 = Label(window, text="QUIZ", font=(50), justify=CENTER, width=20, fg="white", bg="black")
label0.place(x=120, y=40)

label1 = Label(window, text="Name: ",font=(15), justify=LEFT).place(x=120, y=100)
entry1 = Entry(window, textvariable=name).place(x=210, y=105)
label2 = Label(window, text="Reg No: ",font=(15), justify=LEFT).place(x=120, y=140)
entry2 = Entry(window).place(x=210, y=145)
label3 = Label(window, text="Section: ",font=(15), justify=LEFT).place(x=120, y=180)
entry3 = Entry(window).place(x=210, y=185)

label4 = Label(window, text = "Level:", font=(15), justify=LEFT).place(x=120, y=220)
radio = Radiobutton(window,text = "Easy",variable = easy, value ="easy", font=(2)).place(x=210,y=220)
radio1 = Radiobutton(window,text = "Moderate",variable = easy, value ="medium", font=(2)).place(x=210,y=250)
radio2 = Radiobutton(window,text = "Tough",variable = easy, value ="hard", font=(2)).place(x=210,y=280)

button1 = Button(window, text="SUBMIT", font=(15), bg="skyblue", fg="black", command = show).place(x=180, y=330)

window.mainloop()