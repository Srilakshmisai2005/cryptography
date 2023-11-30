import string
import numpy
def greatest_common_divisor(a: int, b: int) -&gt; int:
&quot;&quot;&quot;
&gt;&gt;&gt; greatest_common_divisor(4, 8)

4
&gt;&gt;&gt; greatest_common_divisor(8, 4)
4
&gt;&gt;&gt; greatest_common_divisor(4, 7)
1
&gt;&gt;&gt; greatest_common_divisor(0, 10)
10
&quot;&quot;&quot;
return b if a == 0 else greatest_common_divisor(b %
a, a)
class HillCipher:
key_string = string.ascii_uppercase + string.digits
# This cipher takes alphanumerics into account
# i.e. a total of 36 characters
# take x and return x % len(key_string)
modulus = numpy.vectorize(lambda x: x % 36)
to_int = numpy.vectorize(lambda x: round(x))
def __init__(self, encrypt_key):
&quot;&quot;&quot;
encrypt_key is an NxN numpy array
&quot;&quot;&quot;

self.encrypt_key = self.modulus(encrypt_key) #
mod36 calc&#39;s on the encrypt key
self.check_determinant() # validate the
determinant of the encryption key
self.decrypt_key = None
self.break_key = encrypt_key.shape[0]
def replace_letters(self, letter: str) -&gt; int:
&quot;&quot;&quot;
&gt;&gt;&gt; hill_cipher = HillCipher(numpy.array([[2, 5],
[1, 6]]))
&gt;&gt;&gt; hill_cipher.replace_letters(&#39;T&#39;)
19
&gt;&gt;&gt; hill_cipher.replace_letters(&#39;0&#39;)
26
&quot;&quot;&quot;
return self.key_string.index(letter)

def replace_digits(self, num: int) -&gt; str:
&quot;&quot;&quot;
&gt;&gt;&gt; hill_cipher = HillCipher(numpy.array([[2, 5],
[1, 6]]))
&gt;&gt;&gt; hill_cipher.replace_digits(19)

&#39;T&#39;
&gt;&gt;&gt; hill_cipher.replace_digits(26)
&#39;0&#39;
&quot;&quot;&quot;
return self.key_string[round(num)]

def check_determinant(self) -&gt; None:
&quot;&quot;&quot;
&gt;&gt;&gt; hill_cipher = HillCipher(numpy.array([[2, 5],
[1, 6]]))
&gt;&gt;&gt; hill_cipher.check_determinant()
&quot;&quot;&quot;
det = round(numpy.linalg.det(self.encrypt_key))
if det &lt; 0:
det = det % len(self.key_string)
req_l = len(self.key_string)
if greatest_common_divisor(det,
len(self.key_string)) != 1:
raise ValueError(
f&quot;determinant modular {req_l} of encryption
key({det}) is not co prime w.r.t {req_l}.\nTry another
key.&quot;

)
def process_text(self, text: str) -&gt; str:
&quot;&quot;&quot;
&gt;&gt;&gt; hill_cipher = HillCipher(numpy.array([[2, 5],
[1, 6]]))
&gt;&gt;&gt; hill_cipher.process_text(&#39;Testing Hill Cipher&#39;)
&#39;TESTINGHILLCIPHERR&#39;
&gt;&gt;&gt; hill_cipher.process_text(&#39;hello&#39;)
&#39;HELLOO&#39;
&quot;&quot;&quot;
chars = [char for char in text.upper() if char in
self.key_string]
last = chars[-1]
while len(chars) % self.break_key != 0:
chars.append(last)
return &quot;&quot;.join(chars)
def encrypt(self, text: str) -&gt; str:
&quot;&quot;&quot;
&gt;&gt;&gt; hill_cipher = HillCipher(numpy.array([[2, 5], [1,
6]]))
&gt;&gt;&gt; hill_cipher.encrypt(&#39;testing hill cipher&#39;)
&#39;WHXYJOLM9C6XT085LL&#39;

&gt;&gt;&gt; hill_cipher.encrypt(&#39;hello&#39;)
&#39;85FF00&#39;
&quot;&quot;&quot;
text = self.process_text(text.upper())
encrypted = &quot;&quot;
for i in range(0, len(text) - self.break_key + 1,
self.break_key):
batch = text[i : i + self.break_key]
batch_vec = [self.replace_letters(char) for char
in batch]
batch_vec = numpy.array([batch_vec]).T
batch_encrypted =
self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()
[
0
]
encrypted_batch = &quot;&quot;.join(
self.replace_digits(num) for num in
batch_encrypted
)
encrypted += encrypted_batch
return encrypted

def make_decrypt_key(self):
&quot;&quot;&quot;
&gt;&gt;&gt; hill_cipher = HillCipher(numpy.array([[2, 5],
[1, 6]]))
&gt;&gt;&gt; hill_cipher.make_decrypt_key()
array([[ 6., 25.],
[ 5., 26.]])
&quot;&quot;&quot;
det = round(numpy.linalg.det(self.encrypt_key))
if det &lt; 0:
det = det % len(self.key_string)
det_inv = None
for i in range(len(self.key_string)):
if (det * i) % len(self.key_string) == 1:
det_inv = i
break
inv_key = (
det_inv
* numpy.linalg.det(self.encrypt_key)
* numpy.linalg.inv(self.encrypt_key)
)

return self.to_int(self.modulus(inv_key))
def decrypt(self, text: str) -&gt; str:
&quot;&quot;&quot;
&gt;&gt;&gt; hill_cipher = HillCipher(numpy.array([[2, 5],
[1, 6]]))
&gt;&gt;&gt;
hill_cipher.decrypt(&#39;WHXYJOLM9C6XT085LL&#39;)
&#39;TESTINGHILLCIPHERR&#39;
&gt;&gt;&gt; hill_cipher.decrypt(&#39;85FF00&#39;)
&#39;HELLOO&#39;
&quot;&quot;&quot;
self.decrypt_key = self.make_decrypt_key()
text = self.process_text(text.upper())
decrypted = &quot;&quot;
for i in range(0, len(text) - self.break_key + 1,
self.break_key):
batch = text[i : i + self.break_key]
batch_vec = [self.replace_letters(char) for char
in batch]
batch_vec = numpy.array([batch_vec]).T
batch_decrypted =
self.modulus(self.decrypt_key.dot(batch_vec)).T.tolist()
[

0
]
decrypted_batch = &quot;&quot;.join(
self.replace_digits(num) for num in
batch_decrypted
)
decrypted += decrypted_batch
return decrypted

def main():
N = int(input(&quot;Enter the order of the encryption key:
&quot;))
hill_matrix = []
print(&quot;Enter each row of the encryption key with
space separated integers&quot;)
for i in range(N):
row = [int(x) for x in input().split()]
hill_matrix.append(row)
hc = HillCipher(numpy.array(hill_matrix))
print(&quot;Would you like to encrypt or decrypt some
text? (1 or 2)&quot;)
option = input(&quot;\n1. Encrypt\n2. Decrypt\n&quot;)

if option == &quot;1&quot;:
text_e = input(&quot;What text would you like to
encrypt?: &quot;)
print(&quot;Your encrypted text is:&quot;)
print(hc.encrypt(text_e))
elif option == &quot;2&quot;:
text_d = input(&quot;What text would you like to
decrypt?: &quot;)
print(&quot;Your decrypted text is:&quot;)
print(hc.decrypt(text_d))
if __name__ == &quot;__main__&quot;:
import doctest
doctest.testmod()
main()
