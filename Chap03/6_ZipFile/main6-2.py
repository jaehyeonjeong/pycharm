import itertools
import zipfile

passwd_string = "01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r'.//Password1234.zip')
#비밀번호가 입력된 압축파일의 경로를 입력하여 불러옵니다.

for len in range(1, 6):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        #비밀번호를 입력해서 맞으면 try를 실행하고 틀리다면 except를 실행합니다.
        try:
            zFile.extractall(pwd = passwd.encode())
            #비밀번호를 입력합니다. 비밀번호가 맞다면 14~15줄을 실행합니다.
            #비밀번호가 틀리다면 오류가 발생하여 except를 실행합니다.
            print(f"비밀번호는 {passwd}입니다.")
            break#비밀번호를 찾으면 for문을 종료합니다.
        except:
            pass

        #이 코드는 정상적으로 작동하지 않음