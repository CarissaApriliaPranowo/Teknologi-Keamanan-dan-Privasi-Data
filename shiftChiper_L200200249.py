def enkripsi(pesan, kunci):
    chiper = '' 
    for char in pesan:
        if char.isupper(): 
            chiper += chr((ord(char) - 65 + kunci) % 26 + 65)     
        elif char.islower():
            chiper += chr((ord(char) - 97 + kunci) % 26 + 97)  
        else:  
            chiper += char   
    return chiper

def dekripsi(chiper, kunci):
    pesan = '' 
    for char in chiper:
        if char.isupper():  
            pesan += chr((ord(char) - 65 - kunci) % 26 + 65) 
        elif char.islower(): 
            pesan += chr((ord(char) - 97 - kunci) % 26 + 97)  
        else:  
            pesan += char 
    return pesan

def main():
    print("------------------------------------------------------")
    pesan = input('Masukkan Pesan      : ')
    print("------------------------------------------------------")
    kunci = 49 #L200200249
    chiper = enkripsi(pesan, kunci)
    print('Pesan : ', pesan)
    print('Hasil Pesan Enkripsi :', chiper)
    print('Hasil Pesan Dekripsi :', dekripsi(chiper, kunci))
    print("======================================================")

if __name__ == '__main__': 
    main()
