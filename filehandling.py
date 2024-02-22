'''file=open('vidya1.txt','r')
print(file.readline())
file.close()


file=open('vidya1.txt','r')
print(file.readline(),file.readline())
file.close()


file=open('vidya1.txt','r')
print(file.readline())
print(file.readline())
print(file.readlines())
file.close()'''

file=open('vidya1.txt','r')
print(file.readlines()[-6:])
file.close()
