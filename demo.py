my_file = open("num.txt", "r")
content = my_file.read()
A = list(map(int, content.split()))
my_file.close()