import string
main=string.ascii_lowercase
def conversion(cipher_text,key):
index=0
plain_text=&quot;&quot;
cipher_text=cipher_text.lower()
key=key.lower()
for c in cipher_text:
if c in main:
off=ord(key[index])-ord(&#39;a&#39;)

positive_off=26-off
decrypt=chr((ord(c)-
ord(&#39;a&#39;)+positive_off)%26+ord(&#39;a&#39;))
plain_text+=decrypt
index=(index+1)%len(key)
else:
plain_text+=c
print(&quot;cipher text: &quot;,cipher_text)
print(&quot;plain text (message): &quot;,plain_text)
cipher_text=input(&quot;Enter the message to be decrypted:
&quot;)
key=input(&quot;Enter the key for decryption: &quot;)
conversion(cipher_text,key)
