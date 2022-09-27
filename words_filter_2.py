

statement = str('The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.')

texto = str(statement)
texto = texto.replace('.',' ')
texto = texto.replace(',',' ')
texto = texto.replace(':',' ')
texto = texto.lower()
texto = texto.split()

palavras = []

for f in texto:
        if f[0] in 'python' or f[-1] in 'python':
            if len(f) > 5:
                palavras.append(f)

print(palavras)