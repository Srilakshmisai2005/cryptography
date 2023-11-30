pt=str(input(&quot;ENTER THE PLAIN TEXT : &quot;))
cipher=&quot;&quot;
letter=&quot;abcdefghijklmnopqrstuvwxyz&quot;
common=max(set(pt),key=pt.count)
print(&quot;COMMON LETTER : &quot;+common)
if common in letter:
com=letter.find(common)
key=com-6

if (key&lt;0):
key=26-key
for i in pt:
if i in letter:
pos=letter.find(i)
new_pos=(pos+key)%26
new_char=letter[new_pos]
cipher+=new_char
print(&quot;CIPHER TEXT : &quot;+cipher)
