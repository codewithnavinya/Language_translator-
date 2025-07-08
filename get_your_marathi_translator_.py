#the dictonary translating marathi into english
oxford={ 'lakod':'wood',
'kapde':'clothes',
'khurchi':'chair'}
print(oxford.keys())
print('enter which word do you want from the above')
# enter your.word
key=input('ENTER YOUR KEY\n')
#your key is here 
print('your key is',oxford.get(key))