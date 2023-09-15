import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

send_email = "definejae234@gmail.com"
send_pwd = "euwy iirb kgqy hirx"

recv_email = "0306jh@naver.com"

smtp_name = "smtp.gmail.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = "구글이 네이버에게 첨부파일을 보냈습니다."
msg['From'] = send_email
msg['To'] = recv_email

text = """
구글이 네이버로 부터 보내는 첨부파일입니다.
파일을 잘 확인해주세요.
첨부파일을 수정했습니다. html 형식으로 페이지를 나타낼 수 있는 사이트입니다.
"""

contentPart = MIMEText(text)
msg.attach(contentPart)

etc_file_path = r'.//비밀번호.txt'
with open(etc_file_path, 'rb') as f:
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition', 'attachment', filename='.//비밀번호.txt')

    msg.attach(etc_part)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()

#파일을 첨부하여 메일을 보내는 코드 만들기