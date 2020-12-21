def isPalindrome(s):
  alphas = ""
  for i in s:
    if i.isalpha():
      alphas += i
  if alphas.lower() == alphas[::-1].lower():
    return True
  else:
    return False

    """ Accepts string s
    Returns True if s is Palindrome or False otherwise"""


# main code
string1 = 'Able was I, ere I saw Elba'
if(isPalindrome(string1)):
    print("The string 'Able was I, ere I saw Elba' is palindrome." )
else:
    print("The string 'Able was I, ere I saw Elba' is not palindrome." )

string2 = 'Is this a palindrome'
if(isPalindrome(string2)):
    print("The string 'Is this a palindrome' is palindrome." )
else:
    print("The string 'Is this a palindrome' is not palindrome." )

# Order of growth of this code is:

s = "malayalam"
ans = isPalindrome(s)

print(ans)
