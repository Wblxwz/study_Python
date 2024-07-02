#结合unittest的结果发送邮件到邮箱中

import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MAIL = {"from":"111@qq.com",
        "pwd":"111",
        "smtp":"smtp.qq.com"
        }
reciveList = ["222@qq.com"]

if __name__ == "__main__":
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header('cs', 'utf-8')  # 标题
    msg['From'] = MAIL['from']  # 发件人
    msg['To'] = reciveList[0]  # 收件人

    # 内容
    content = "你好，感谢你的观看"
    # 此正文消息，参数为内容、编码格式（plain纯文本）、编码方式
    html_message = MIMEText(content, 'plain ', 'utf-8')  # 正文
    html_message["Accept-Language"] = "zh-CN"
    html_message["Accept-Charset"] = "ISO-8859-1,utf-8"

    msg.attach(html_message)
    try:
        # 非SSL，如果为SSL则看下面
        server = smtplib.SMTP(MAIL['smtp'])

        # 如果是ssl，需要加多一个端口号映射
        # server = smtplib.SMTP_SSL()
        # server.connect(MAIL['smtp'],MAIL['port'])

        # 登陆邮箱发送邮件
        server.login(MAIL['from'], MAIL['pwd'])
        server.sendmail(MAIL['from'], reciveList, msg.as_string())
        print('发送成功')

    except Exception as e:
        print('error', e)