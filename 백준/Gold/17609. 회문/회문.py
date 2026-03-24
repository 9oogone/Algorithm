import sys
input=sys.stdin.readline
tc=int(input())

def semipal(w,l,r):
    while l < r:
        if w[l]==w[r]:
            l+=1
            r-=1
        else:
            return False
    return True


def pal(word):
    left = 0
    right = len(word)-1 
    
    while left < right:
        if word[left]==word[right]:
            left += 1
            right -= 1
        else:
            check_l = semipal(word,left+1,right)
            check_r = semipal(word,left,right-1)
            
            if check_l or check_r:
                return 1
            else:
                return 2
    return 0    

for _ in range(tc):
    palindrome = input().strip()
    print(pal(palindrome))