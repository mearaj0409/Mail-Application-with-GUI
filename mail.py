import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = sender_entry.get()
    password = password_entry.get()
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        success_label.config(text="Email sent successfully!", fg="green")
        error_label.config(text="")
    except Exception as e:
        error_label.config(text="Error sending email: " + str(e), fg="red")
        success_label.config(text="")

root = tk.Tk()
root.title("Mail Application")

sender_label = tk.Label(root, text="Sender Email:", fg="blue")
sender_label.grid(row=0, column=0, pady=5)
sender_entry = tk.Entry(root, width=30)
sender_entry.grid(row=0, column=1, pady=5)

password_label = tk.Label(root, text="Password:", fg="blue")
password_label.grid(row=1, column=0, pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=1, column=1, pady=5)

recipient_label = tk.Label(root, text="Recipient Email:", fg="blue")
recipient_label.grid(row=2, column=0, pady=5)
recipient_entry = tk.Entry(root, width=30)
recipient_entry.grid(row=2, column=1, pady=5)

subject_label = tk.Label(root, text="Subject:", fg="blue")
subject_label.grid(row=3, column=0, pady=5)
subject_entry = tk.Entry(root, width=30)
subject_entry.grid(row=3, column=1, pady=5)

body_label = tk.Label(root, text="Email Body:", fg="blue")
body_label.grid(row=4, column=0, pady=5)
body_text = tk.Text(root, height=5, width=30)
body_text.grid(row=5, column=0, columnspan=2, pady=5)

send_button = tk.Button(root, text="Send Email", command=send_email, bg="green", fg="white")
send_button.grid(row=6, column=0, pady=10)

success_label = tk.Label(root, text="", fg="green")
success_label.grid(row=7, column=0, pady=5)
error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=8, column=0, pady=5)

root.mainloop()
