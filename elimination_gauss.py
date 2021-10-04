import os
from fractions import Fraction

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def back_to_menu():
    try:
        input("\nTekan 'Enter' untuk kembali...")
        show_menu()
    except KeyboardInterrupt:
        show_menu()

def show_menu():
    clear_screen()
    print("=====================================")
    print("|      PROGRAM ELIMINASI GAUSS      |")
    print("=====================================")
    print("|                OLEH               |")
    print("=====================================")
    print("|  ANDI ALFIAN BAHTIAR (2009106002) |")
    print("|         INFORMATIKA A 2020        |")
    print("|          FAKULTAS TEKNIK          |")
    print("|       UNIVERSITAS MULAWARMAN      |")
    print("=====================================")
    print("| [1] Eliminasi Gauss               |")
    print("| [0] Exit                          |")
    print("=====================================")
    try:
        try:
            selected_menu = int(input("Pilih menu> "))
            if selected_menu == 1:
                eliminasi()
            elif selected_menu == 0:
                exit()
            else:
                print("Kamu memilih menu yang salah!")
                back_to_menu()
        except ValueError:
            print("Kamu memilih menu yang salah!")
            back_to_menu()
    except KeyboardInterrupt:
        exit()

def pprint(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")

def gauss(A):
    n = len(A)
    for i in range(0, n):
        maxE1 = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) < maxE1 or maxE1 == 0:
                maxE1 = abs(A[k][i])
                maxRow = k
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
    print("Matriks Eselon:\t")
    pprint(A)
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        if A[i][i] == 0:
            return [0 for i in range(n)]
        else:
            x[i] = A[i][n]/A[i][i]
            for k in range(i-1, -1, -1):
                A[k][n] -= A[k][i]*x[i]
    return x

def eliminasi():
    print("=====================================")
    n = int(input("Silakan masukkan jumlah variabel: "))
    A = [[0 for j in range(n+1)] for i in range(n)]
    print("Harap masukkan setiap baris yang dipisahkan oleh baris baru:")
    for i in range(0, n):
        line = map(Fraction, input().split(" "))
        for j, el in enumerate(line):
            A[i][j] = el
    print("Harap masukkan setiap baris yang dipisahkan oleh baris baru:")
    line = input().split(" ")
    lastLine = list(map(Fraction, line))
    for i in range(0, n):
        A[i][n] = lastLine[i]
    print("\nMatriks:")
    pprint(A)
    x = gauss(A)
    print("Hasil:")
    solution = False
    for i in range(n):
        if x[i] != 0:
            solution = True
    if solution:
        for i in range(len(x)):
            print("x", i+1, " = ", x[i])
    else:
        print("Tidak ada solusi")
    back_to_menu()

if __name__ == "__main__":
    show_menu()
