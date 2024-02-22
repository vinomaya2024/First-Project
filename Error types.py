# Type of Error
'''a=5
b=0
try:
    print(a/b)
except:
    print('your input is wrong')
'''

'''try:
    file2=open('no.txt','r')
    print(file2.read())
except Exception as e:
    print(' an error is occured',e)'''

try:
    file2=open('no.txt','r')
    file2.write('i am vidya')
    file2.close()
except Exception as e:
    print(' an error is occured',e)
