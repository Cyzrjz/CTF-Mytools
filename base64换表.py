import base64
code = str(input("请输入映射表："))
# code = 'gJ1BRjQie/FIWhEslq7GxbnL26M4+HXUtcpmVTKaydOP38of5v90ZSwrkYzCAuND'
str_flag = str(input("请输入要解码的字符串："))
# str_flag = 'GQTZlSqQXZ/ghxxwhju3hbuZ4wufWjujWrhYe7Rce7ju'
coder = str_flag.maketrans(code,'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
flag_encode = str_flag.translate(coder)
flag = base64.b64decode(flag_encode).decode()
print(flag)
input("Press Enter to exit...")