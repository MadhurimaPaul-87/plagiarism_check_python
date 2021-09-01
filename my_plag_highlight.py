from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
Str_url = "A Hello, World! program generally is a computer program that outputs or displays the message Hello, World!. Such a program is very simple in most programming languages, and is often used to illustrate the basic syntax of a programming language. It is often the first program written by people learning to code.[1][2] It can also be used as a sanity test to make sure that computer software intended to compile or run source code is correctly installed, and that the operator understands how to use it."
Str_user = "Hello World dispays"
lst_url=word_tokenize(Str_url)
lst_user=word_tokenize(Str_user)
c=0
for i in range(len(lst_url)):
  for j in range(len(lst_user)):
    if lst_user[j]==lst_url[i]:
      print(f"\033[44;33m{lst_url[i]}\033[49m",end=" ")
      c=c+1
    else:
      print("",end="") 
  if c==1:
    c=0
    continue
  else:
    print(f"\033[30m{lst_url[i]}",end=" ") 
