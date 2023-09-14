import smtplib
from email.mime.text import MIMEText

send_email = "definejae234@gmail.com"
send_pwd = "euwy iirb kgqy hirx"    #구글앱 비밀번호 이므로 계정비밀번호로 햇갈리지 말아야 함

recv_email = "0306jh@naver.com"

smtp_name = "smtp.gmail.com"
smtp_port = 587

text = """
이 메일은 구글에서 네이버로 보내지는 메일입니다.
내용을 반드시 숙지하십시오
"""

msg = MIMEText(text)

msg['Subject'] = "메일제목은 구글이 네이버에게 입니다."
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()