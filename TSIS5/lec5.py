# разделить текст по буквам
import re
txt = "I went to school at 8:45 o`clock"
x = re.findall("\w",txt)
# print(x)

#Найти цифры
# y = re.findall("\d",txt)
# if y:
#     print("YES")
# else:
#     print("NO")