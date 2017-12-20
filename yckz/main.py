import email
import os
import poplib
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText


def read():
    pass


def shutdown():
    os.system('shutdown -s -t 50')


def restart():
    os.system('shutdown -r')


def send():
    to = ['bai_dawn@sina.com']
    sent = smtplib.SMTP('smtp.sina.com')
    sent.login('bai_dawn@sina.com', 'bai910214')
    content = MIMEText('content')
    content['Subject'] = 'title'
    content['From'] = 'bai_dawn@sina.com'
    content['To'] = ','.join(to)
    sent.sendmail('bai_dawn@sina.com', to, content.as_string())
    sent.close()


def read():
    read = poplib.POP3('pop.sina.com')
    read.user('bai_dawn@sina.com')
    read.pass_('bai910214')
    tongji = read.stat()
    str = read.top(tongji[0], 0)
    str2 = []
    for x in str[1]:
        try:
            str2.append(x.decode())
        except:
            try:
                str2.append(x.decode('gbk'))
            except:
                str2.append(x.decode('big5'))
    msg = email.message_from_string('\n'.join(str2))
    title = decode_header(msg['subject'])
    if title[0][1]:
        title2 = title[0][0].decode(title[0][1])
    else:
        title2 = title[0][0]
    read.quit()
    return title2

if __name__ == '__main__':
    print read()