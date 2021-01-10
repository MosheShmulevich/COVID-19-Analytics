from tkinter import *
import smtplib
import ssl


def send():
    sender_email = textentry.get()
    password = textentry_pas.get()
    receiver_email = textentry1.get()
    message = textentry2.get()
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


window = Tk()
window.configure(width=500, height=500, background="gray4")
Label(window, text="To send a message enter your email:", bg="gray4", fg="white", font="none 12 bold").grid(row=0, column=0)
textentry = Entry(window, width=15, bg="white")
textentry.grid(row=1, column=0)
Label(window, text="email password:", bg="gray4", fg="white", font="none 12 bold").grid(row=2, column=0)
textentry_pas = Entry(window, width=15, bg="white")
textentry_pas.grid(row=3, column=0)
Label(window, text="Enter receiver email:", bg="gray4", fg="white", font="none 12 bold").grid(row=4, column=0)
textentry1 = Entry(window, width=15, bg="white")
textentry1.grid(row=5, column=0)
Label(window, text="message:", bg="gray4", fg="white", font="none 12 bold").grid(row=6, column=0)
textentry2 = Entry(window, width=30, bg="white")
textentry2.grid(row=7, column=0)


Button(window, text="SEND", width=4, command=send).grid(row=8, column=0)
window.mainloop()
