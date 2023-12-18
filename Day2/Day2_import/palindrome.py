# 회문
# 앞뒤가 똑같은 문자를 palindrome
# 다이쁜이쁜이쁜이다
# 여보게저기저게보여
# 여보안경안보여

word = 'abcdcbe' # X
word = 'abcdcba' # O

# 어떻게 판단할 수 있을까요??

word = 'abcde'
word = 'abcdcba' # O

reversed_word = word[::-1]
print(word == reversed_word)

n= len(word)

left = 0
right = n-1

is_palindrome = True
# 너를 우선 회문이라고 치자. 만약 하나라도 틀리잖아? 더이상 회문이 아니야.

# 싹다 맞아야 회문이야. 아니야? 그럼 회문이 아니야. <- 체크하기 귀찮음
# while문을 사용한 코드
while left < right:
    if word[left] != word[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

# for문을 사용한 코드
for left in range(len(word)//2):
    right = n - 1 - left
    # right = -(1 + left)
    if word[left] != word[right]:
        is_palindrome = False
        break