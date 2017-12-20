# python 远程控制电脑关机

* [关机和重启](#关机和重启)
* [邮件发送](#邮件发送)
* [邮件获取](#邮件获取)
* [py2exe打包](#py2exe打包)

## 关机和重启
python的关机和重启的操作  
关机
```
os.system('shutdown -s -t 50')
```
重启
```
os.system('shutdown -r')
```

## 邮件发送
用新浪邮箱为例，需要引用smtplib包
```
    to = ['bai_dawn@sina.com']
    sent = smtplib.SMTP('smtp.sina.com')
    sent.login('bai_dawn@sina.com', 'bai910214')
    content = MIMEText('content')
    content['Subject'] = 'title'
    content['From'] = 'bai_dawn@sina.com'
    content['To'] = ','.join(to)
    sent.sendmail('bai_dawn@sina.com', to, content.as_string())
    sent.close()
```
出现错误smtplib.SMTPAuthenticationError，一般是SMTP没有开启，在邮箱设置中开启 

## 邮件获取
邮件获取需要引用poplib包
```
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
``` 

## py2exe打包
py2exe下载路径  
[http://prdownloads.sourceforge.net/py2exe](http://prdownloads.sourceforge.net/py2exe)
``` 
import py2exe
from distutils.core import setup

setup(console=['main.py'])

``` 
需要注意的是py2exe包必须导入。然后将setup.py和main.py放在同一目录下  
cmd进入到当前目录，出入
``` 
python setup.py py2exe
```
最后dist文件夹下的main.exe即为可执行文件。