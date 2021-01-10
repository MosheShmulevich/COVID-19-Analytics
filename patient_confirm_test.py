from tkinter import *
import smtplib
import ssl


def send():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "project35company@gmail.com"
    receiver_email = textentry.get()
    password = "python2021"  # company's email password
    message = """\
    Subject: Hi there
    Dear patient, you have positive result to covid 19 test.
    To avoid any mistakes, please reply to this email if you did not take the test.
    Tank you
    ."""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    exit()


window = Tk()
window.title("patients confirm testing")
window.configure(width=500, height=500, background="gray4")
Label(window, text="Enter patient's email:", bg="gray4", fg="white", font="none 12 bold").grid(row=1, column=0)
textentry = Entry(window, width=15, bg="white")
textentry.grid(row=2, column=0)
Button(window, text="SEND", width=4, command=send).grid(row=3, column=0)
window.mainloop()
