# for  multiline string use three double qoutes
hi = """Hey There!
This is me!
Shivam Yadav"""
print(len(hi))
print(hi[:5])
print(hi[0:5])
print(hi[0:])
print(hi.lower())
print(hi.upper())
print(hi.count('h'))
print(hi.count('H'))
print(hi.find('h'))#will find and return the index of first match
print(hi.find('Z'))#-1
print(hi.replace("Hey","Hello")) #this replace will not change the initail value of hi it will just create a new string replcing the given istructions
greeting = "hello"
name = "shivam"
message= greeting + ", " + name
print(message)
message= '{}, {}. Welcome!'.format(greeting,name)
print(message)
message= f'{greeting}, {name.upper()}. Welcome!' #by just adding that f in front we can use them directly in quote and even we can use properties here
print(message)
print(dir(name))
print(help(str))#will give all the mehods of string