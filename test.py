f = open('counter.txt','r')
test = f.read(1)
if test == '':
    print(float(test))
else:
    print(type(int(test)))