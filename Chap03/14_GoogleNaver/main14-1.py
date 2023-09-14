import smtplib
from email.mime.text import MIMEText

send_email = "0306jh@naver.com"
send_pwd = "@victory5637"

recv_email = "definejae234@gmail.com"

smtp_name = "smtp.naver.com"
smtp_port = 587

text = """
네이버에서 구글로 보내는 메일입니다.
내용 숙지 바랍니다.
"""
msg = MIMEText(text)

msg['Subject'] = "메일제목은 여기에 넣습니다."
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s=smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()

#네이버 메일을 보내는 코드 만들기