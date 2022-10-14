import smtplib
from email.mime.text import MIMEText
from email.header import Header


def email():
    sender = 'XXXX@163.com'  # 填写发件人
    pwd = 'XXXX'  # 登录密码
    receivers = ['XXXX@qq.com']  # 填写收件人

    message = MIMEText("你好，网站有内容更新，请及时查看", "plain", 'utf-8')
    # 三个参数：第一个为文本内容，第二个为plain设置文本格式，第三个为utf-8设置编码
    message['From'] = "XXX <XXX@163.com>"
    message['To'] = "XXX <XXX@qq.com>"

    subject = "网站有内容更新"
    # 邮件主题
    message["Subject"] = subject

    try:
        # 使用非本地服务器，需要建立ssl连接
        smtpObj = smtplib.SMTP_SSL("smtp.163.com", 465)
        # 发件箱邮件服务器
        smtpObj.login(sender, pwd)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error：无法发送邮件.Case:%s" % e)
