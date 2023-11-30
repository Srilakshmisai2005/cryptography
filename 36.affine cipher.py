ct=str(input(&quot;ENTER THE PLAIN TEXT : &quot;))
a=int(input(&quot;ENTER a : &quot;))
b=int(input(&quot;ENTER b : &quot;))
letter=&quot;abcdefghijklmnopqrstuvwxyz&quot;
dec=&quot;&quot;
for x in ct:
en=0
if x in letter:
pos=letter.find(x)

en=((a*pos)+b)%26
dec+=letter[en]
print(&quot;CIPHER TEXT : &quot;+dec)
