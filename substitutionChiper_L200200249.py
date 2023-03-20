import random
import string

def enkripsi(pesan):
    huruf = list(string.ascii_uppercase)
    random.shuffle(huruf)
    peta_subtitution = {}
    for i in range(26):
        peta_subtitution[huruf[i]] = string.ascii_uppercase[i]
    teks_chiper = ''
    for char in pesan:
        if char.isalpha(): 
            teks_chiper += peta_subtitution[char.upper()] 
        else: 
           teks_chiper += char
    return teks_chiper, peta_subtitution

def dekripsi(teks_chiper, peta_substitusi):
    pesan_dekripsi = ''
    for char in teks_chiper:
        if char.isalpha(): 
            for kunci, value in peta_substitusi.items(): 
                if char.upper() == value: 
                    pesan_dekripsi += kunci
        else: 
            pesan_dekripsi += char 
    return pesan_dekripsi

def main():
    print("-----------------------------------------------------")
    pesan = input('Masukkan Pesan      : ')
    print("-----------------------------------------------------")
    teks_chiper,peta_substitusi = enkripsi(pesan)
    print('Pesan : ', pesan)
    print('Hasil Pesan Enkripsi : ', teks_chiper)  
    print('Hasil Pesan Dekripsi : ', dekripsi(teks_chiper, peta_substitusi)) 
    print("======================================================")

if __name__ == '__main__':
    main()