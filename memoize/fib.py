from memoized import *

@memoized
def mfib(n):
	if n==1:
		print n, "cache miss"
		return 1
	if n==2:
		print n, "cache miss"
		return 1
	if n>2:
		print n, "cache miss"
		return mfib(n-2) + mfib(n-1)
		

def mfib2(n):
	if n==1:
		print n, "no cache"
		return 1
	if n==2:
		print  n, "no cache"
		return 1
	if n>2:
		print n, "no cache"
		return mfib2(n-2) + mfib2(n-1)
		
if __name__ == "__main__":
	print "memo: ", mfib(5)
	print "memo: ", mfib2(5)
	
