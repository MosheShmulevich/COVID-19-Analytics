from tkinter import *


def city_map():
    city = clicked.get()
    if city == "Beer Sheva":
        window1 = Tk()
        window1.title("Beer Sheva")
        window1.configure(width=500, height=500, background="gray4")
        Label(window1,text="Matnas Neve Zeev",bg="gray4",fg="gold",font=" none 14 bold").grid(row=0, column=0,sticky = W)
        Label(window1, text="Dov Ronel 6", bg="gray4", fg="gold", font=" none 12").grid(row=1, column=0,sticky = W)
        Label(window1, text="08-6226909", bg="gray4", fg="gold", font=" none 12").grid(row=2, column=0,sticky =W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=3, column=0)
        Label(window1, text="9:00 - 21:00", bg="gray4", fg="gold", font=" none 12").grid(row=3,column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=0,sticky = E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=1)
        Label(window1, text="Clalit Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=5, column=0,sticky=W)
        Label(window1, text="Henrieta Szold 1", bg="gray4", fg="gold", font=" none 12").grid(row=6, column=0,sticky=W)
        Label(window1, text="086283777", bg="gray4", fg="gold", font=" none 12").grid(row=7, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=8, column=0, sticky=W)
        Label(window1, text="9:00 - 18:00", bg="gray4", fg="gold", font=" none 12").grid(row=8, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=1)
        Label(window1, text="Macabi Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=10, column=0,
                                                                                               sticky=W)
        Label(window1, text="Ben Gurion University", bg="gray4", fg="gold", font=" none 12").grid(row=11, column=0, sticky=W)
        Label(window1, text="08-6261457", bg="gray4", fg="gold", font=" none 12").grid(row=12, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=13,
                                                                                                             column=0,
                                                                                                             sticky=W)
        Label(window1, text="9:00 - 18:00", bg="gray4", fg="gold", font=" none 12").grid(row=13, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=14, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=14, column=1)

    if city == "Tel Aviv":
        window1 = Tk()
        window1.title("Tel Aviv")
        window1.configure(width=500, height=500, background="gray4")
        Label(window1, text="Macabi Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=0, column=0,
                                                                                                  sticky=W)
        Label(window1, text="Hatkuma 36", bg="gray4", fg="gold", font=" none 12").grid(row=1, column=0, sticky=W)
        Label(window1, text="03-512-2122", bg="gray4", fg="gold", font=" none 12").grid(row=2, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=3,
                                                                                                             column=0)
        Label(window1, text="9:00 - 21:00", bg="gray4", fg="gold", font=" none 12").grid(row=3, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=1)
        Label(window1, text="Clalit Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=5, column=0,
                                                                                               sticky=W)
        Label(window1, text="Even Gvirol 124", bg="gray4", fg="gold", font=" none 12").grid(row=6, column=0, sticky=W)
        Label(window1, text="03-512-2122", bg="gray4", fg="gold", font=" none 12").grid(row=7, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=8,
                                                                                                             column=0)
        Label(window1, text="9:00 - 21:00", bg="gray4", fg="gold", font=" none 12").grid(row=8, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=1)

    if city == "Heifa":
        window1 = Tk()
        window1.title("Heifa")
        window1.configure(width=500, height=500, background="gray4")
        Label(window1, text="Macabi Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=0, column=0,
                                                                                               sticky=W)
        Label(window1, text="Herzel 73", bg="gray4", fg="gold", font=" none 12").grid(row=1, column=0, sticky=W)
        Label(window1, text="048351111", bg="gray4", fg="gold", font=" none 12").grid(row=2, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=3,
                                                                                                             column=0)
        Label(window1, text="9:00 - 21:00", bg="gray4", fg="gold", font=" none 12").grid(row=3, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=1)

        Label(window1, text="Clalit Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=5, column=0,
                                                                                               sticky=W)
        Label(window1, text="Zahal 52", bg="gray4", fg="gold", font=" none 12").grid(row=6, column=0, sticky=W)
        Label(window1, text="048590222", bg="gray4", fg="gold", font=" none 12").grid(row=7, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=8,
                                                                                                             column=0)
        Label(window1, text="9:00 - 21:00", bg="gray4", fg="gold", font=" none 12").grid(row=8, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=1)

    if city == "Tveria":
        window1 = Tk()
        window1.title("Tveria")
        window1.configure(width=500, height=500, background="gray4")
        Label(window1, text="Macabi Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=0, column=0,
                                                                                               sticky=W)
        Label(window1, text="Eilat 1", bg="gray4", fg="gold", font=" none 12").grid(row=1, column=0, sticky=W)
        Label(window1, text="04-6725343", bg="gray4", fg="gold", font=" none 12").grid(row=2, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=3,
                                                                                                             column=0)
        Label(window1, text="9:00 - 21:00", bg="gray4", fg="gold", font=" none 12").grid(row=3, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=1)
        Label(window1, text="Clalit Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=5, column=0,
                                                                                               sticky=W)
        Label(window1, text="Hayarden 1", bg="gray4", fg="gold", font=" none 12").grid(row=6, column=0, sticky=W)
        Label(window1, text="046728200", bg="gray4", fg="gold", font=" none 12").grid(row=7, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=8,
                                                                                                             column=0)
        Label(window1, text="9:00 - 21:00", bg="gray4", fg="gold", font=" none 12").grid(row=8, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=1)

    if city == "Jerusalem":
        window1 = Tk()
        window1.title("Jerusalem")
        window1.configure(width=500, height=500, background="gray4")
        Label(window1, text="Meuheted Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=0, column=0,
                                                                                               sticky=W)
        Label(window1, text="Irmiyahu 19", bg="gray4", fg="gold", font=" none 12").grid(row=1, column=0, sticky=W)
        Label(window1, text="025444222", bg="gray4", fg="gold", font=" none 12").grid(row=2, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=3,
                                                                                                             column=0)
        Label(window1, text="9:00 - 21:00", bg="gray4", fg="gold", font=" none 12").grid(row=3, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=1)

        Label(window1, text="Clalit Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=5, column=0,
                                                                                               sticky=W)
        Label(window1, text="Ben Yehuda 26", bg="gray4", fg="gold", font=" none 12").grid(row=6, column=0, sticky=W)
        Label(window1, text="026292333", bg="gray4", fg="gold", font=" none 12").grid(row=7, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=8,
                                                                                                             column=0)
        Label(window1, text="9:00 - 21:00", bg="gray4", fg="gold", font=" none 12").grid(row=8, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=1)

    if city == "Eilat":
        window1 = Tk()
        window1.title("Eilat")
        window1.configure(width=500, height=500, background="gray4")
        Label(window1, text="Clalit Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=0, column=0,
                                                                                                 sticky=W)
        Label(window1, text="Yerushalaim Hashlema 2", bg="gray4", fg="gold", font=" none 12").grid(row=1, column=0, sticky=W)
        Label(window1, text="086381111", bg="gray4", fg="gold", font=" none 12").grid(row=2, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=3,
                                                                                                             column=0)
        Label(window1, text="9:00 - 21:00", bg="gray4", fg="gold", font=" none 12").grid(row=3, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=4, column=1)
        Label(window1, text="Macabi Clinic", bg="gray4", fg="gold", font=" none 14 bold").grid(row=5, column=0,
                                                                                               sticky=W)
        Label(window1, text="Bney Israel 6", bg="gray4", fg="gold", font=" none 12").grid(row=6, column=0, sticky=W)
        Label(window1, text="086574983", bg="gray4", fg="gold", font=" none 12").grid(row=7, column=0, sticky=W)
        Label(window1, text="testing hours: Sunday - Thursday", bg="gray4", fg="gold", font=" none 12").grid(row=8,
                                                                                                             column=0)
        Label(window1, text="9:00 - 21:00", bg="gray4", fg="gold", font=" none 12").grid(row=8, column=1)
        Label(window1, text="Friday", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=0, sticky=E)
        Label(window1, text="8:00 - 14:00", bg="gray4", fg="gold", font=" none 12").grid(row=9, column=1)


window = Tk()
window.title("Test Stations")
window.configure(width=500, height=500, background="gray4")
Label(window, text="Cities with a star have test stations ",bg="gray4",fg="gold",font=" none 14 bold").grid(row=0, column=0)
photo_map = PhotoImage(file="map1.png")
Label(window, image=photo_map, bg="gray4").grid(row=0, column=1, sticky=W)
Label(window, text="Select a city:",bg="gray4",fg="gold",font=" none 12").grid(row=1, column=0)
cities = ["Beer Sheva", "Tel Aviv", "Heifa","Tveria","Jerusalem","Eilat"]
clicked = StringVar()
clicked.set(cities[0])
drop = OptionMenu(window,clicked,*cities)
drop.grid(row=2,column=0)
Button(window, text="CHECK",width=6,command = city_map).grid(row=3, column=0)


window.mainloop()