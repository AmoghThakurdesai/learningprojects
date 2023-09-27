#English to pig Latin
print('Enter the English message you want to translate into Pig Latin.')
message=input()

Vowels=('a','e','i','o','u','y')

pigLatin=[]#a list of words in pig latin
for word in message.split():
    #separate the nonletters at the start of the word
    prefixNonLetters=''
    while len(word)>0 and not word[0].isalpha():
        prefixNonLetters+=word[0]
        word=word[1:]

    if len(word)==0:
        pigLatin.append(prefixNonLetters)
        continue

    #separate non letters at end
    suffixNonLetters=''
    while not word[-1].isalpha():
        suffixNonLetters+=word[-1]
        word=word[:-1]
    #remember if the word was upper or title case
    wasUpper=word.isupper()
    wasTitle=word.istitle()

    word=word.lower()#make the word lowercase for translation

    #separate the consonants at the start of this word
    prefixConsonants=''
    while len(word)>0 and not word[0] in Vowels:
        prefixConsonants+=word[0]
        word=word[1:]

    #add the piglatin ending to the word
    if prefixConsonants!='':
        word+=prefixConsonants +'ay '
    else:
        word+='yay '
    #set the word back to uppercase or title case:
    if wasUpper:
        word=word.upper()
    if wasTitle:
        word=word.title()

    #Add the nonletters back to the start or end of the word
    pigLatin.append(prefixNonLetters+word+suffixNonLetters)

print(''.join(pigLatin))
