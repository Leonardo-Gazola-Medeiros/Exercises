
def papagaio(falando, hora):

    if (falando == True) and (hora > 20 or hora < 7):
        return True
    else:
        return False
