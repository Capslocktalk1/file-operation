f = open('text_afterclass.txt' , 'r')
print(f.read(10))
f.close

f = open('text_afterclass.txt' , 'a')
f.write("i love coding")
f.close