from  html import unescape
import smtplib

# Airplane Emoji (U+2708, U+FE0F) - iEmoji.com


# a=b'U+2708'
# print(a.decode('utf-8'))

server=smtplib.SMTP("smtp.gmail.com",587)
message=f"Hey , how are you{unescape('&#128512')}"	
server.starttls()
server.login("csfun100@gmail.com", "jaymikeejosh")
server.sendmail("csfun100@gmail.com","boyijoshua72@gmail.com",msg=f"Subject: {'Hello'}\n\n{message}")
server.close()

# from users import Users

# user=Users("sir manny","boyijoshua0@gmail.com","boyijoshua0@gmail.com")

# print(user.create_new_user())
# # print(Users().get_all_users())
# # print(user.user_exists())



 