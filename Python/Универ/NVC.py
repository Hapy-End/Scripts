def NVC(n,p):
	q = 1 - p
	return n*p-q,'k',n*p+p
print(NVC(600,0.005))