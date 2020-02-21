#pylint:disable=C0103
#pylint:disable=C0304
#pylint:disable=W0312
A = "Some text for example".upper().split(" ")
c = len(A)
for word in A:
	b = []
	for letter in word:
		if (letter in b) or (ord("A")>ord(letter)) or (ord("Z")<ord(letter)):
			c-=1
			break
		b.append(letter)
print(c)