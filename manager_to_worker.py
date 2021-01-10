from tkinter import *
import smtplib
import ssl


def send():
    test_number = textentry_test_number.get()
    patient_id = textentry_id.get()
    message1 = textentry_feedback.get()
    receiver_email = textentry_workers_email.get()
    sender_email = textentry_manager_email.get()
    password = textentry_password.get()
    test_number1 = "test number: ".join(test_number)
    patient_id1 = "patient's id: ".join(patient_id)
    message2 = "feedback: ".join(message1)
    message = " ".join((test_number1,patient_id1,message2))
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    exit()


window = Tk()
window.title("Manager's feedback")
window.configure(width=500, height=500, background="gray4")
Label(window, text="Test feedback to worker", bg="gray4", fg="white", font="none 14 bold").grid(row=0, column=0)
Label(window, text="test number:", bg="gray4", fg="white", font="none 12").grid(row=1, column=0)
textentry_test_number = Entry(window, width=15, bg="white")
textentry_test_number.grid(row=2, column=0)
Label(window, text="patients ID:", bg="gray4", fg="white", font="none 12").grid(row=3, column=0)
textentry_id = Entry(window, width=15, bg="white")
textentry_id.grid(row=4, column=0)
Label(window, text="feedback:", bg="gray4", fg="white", font="none 12").grid(row=5, column=0)
textentry_feedback = Entry(window, width=30, bg="white")
textentry_feedback.grid(row=6,column=0)
Label(window, text="workers email:", bg="gray4", fg="white", font="none 12").grid(row=7, column=0)
textentry_workers_email = Entry(window, width=15, bg="white")
textentry_workers_email.grid(row=8, column=0)
Label(window, text="your email:", bg="gray4", fg="white", font="none 12").grid(row=9, column=0)
textentry_manager_email = Entry(window, width=15, bg="white")
textentry_manager_email.grid(row=10, column=0)
Label(window, text="your email password:", bg="gray4", fg="white", font="none 12").grid(row=11, column=0)
textentry_password = Entry(window, width=15, bg="white")
textentry_password.grid(row=12, column=0)
Button(window, text="SEND", width=4, command=send).grid(row=13, column=0)


window.mainloop()