n=int(input())
l=input().split()
s=[]
a=[]
def mul(n):
	k=1
	while n!=0:
		k=k*(n%10)
		n=n//10
	return k

for i in range(n):
	p=int(l[i])
	k=mul(p)
	s.append([p,k])

for i in range(len(s)):
	for j in range(i+1,len(s)):
		if s[i][1]>s[j][1]:
			temp=s[i]
			s[i]=s[j]
			s[j]=temp
		elif s[i][1]==s[j][1]:
			if s[i][0]>s[j][0]:
				temp=s[i]
				s[i]=s[j]
				s[j]=temp

ans=""
for i in range(len(s)):
	ans=ans+str(s[i][0])+" "
print(ans)
