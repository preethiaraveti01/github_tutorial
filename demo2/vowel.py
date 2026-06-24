s=input("Enter a sentence")
vowel='aeiouAEIOU'
res=""
for i in vowel:
    if i in s:
        res+="*"
    else:
        res+=i
print(res)