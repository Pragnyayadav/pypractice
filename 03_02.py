yourName = input("Name:" )
letter = '''Dear <|NAME|>
\t You are selected!
\t\t Date:02-04-2021 '''
letter = letter.replace("<|NAME|>", yourName)
print(letter)