def enkripsi(pesan, kunci):
    key_dict = {kunci[i]: i for i in range(len(kunci))}
    rows = len(pesan) // len(kunci)
    if len(pesan) % len(kunci) > 0:
        rows += 1

    matrix = [['' for _ in range(len(kunci))] for _ in range(rows)]
    row = 0
    col = 0
    for c in pesan:
        matrix[row][col] = c
        col += 1
        if col == len(kunci):
            col = 0
            row += 1

    chiper = ''
    for k in sorted(key_dict.keys()):
        col = key_dict[k]
        for row in range(rows):
            chiper += matrix[row][col]
    return chiper

def dekripsi(chiper, kunci):
    key_dict = {kunci[i]: i for i in range(len(kunci))}
    rows = len(chiper) // len(kunci)
    if len(chiper) % len(kunci) > 0:
        rows += 1

    matrix = [['' for _ in range(len(kunci))] for _ in range(rows)]
    col = 0
    row = 0
    for k in sorted(key_dict.keys()):
        j = key_dict[k]
        i = 0
        while i < rows and col < len(chiper):
            matrix[i][j] = chiper[col]
            i += 1
            col += 1
        row += 1

    plaintext = ''
    for row in matrix:
        plaintext += ''.join(row)
    return plaintext

def main():
    print("-----------------------------------------------------")
    pesan = input('Masukan Pesan      : ')
    kunci = input('Key                : ')
    print("-----------------------------------------------------") 
    chiper = enkripsi(pesan, kunci)
    print('Pesan : ', pesan)
    print('Kunci : ', kunci)
    print('Hasil Pesan Enkripsi : ', chiper)  
    print('Hasil Pesan Dekripsi : ', dekripsi(chiper, kunci))
    print("======================================================")
    
if __name__ == '__main__':
    main()
