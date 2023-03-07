# read from input
f=open('input.txt','r')
text=f.read()
a,b=text.split()


# write to output
f=open('output.txt','w')
f.write(str(int(a)+int(b)**2))
f.close()