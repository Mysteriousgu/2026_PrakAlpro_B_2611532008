# Program Jam Pasir Kristal Palindromik
print ("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK ===")
n_2008 = int(input("Masukkan tinggi jam pasir (N): "))

# 1. Bingkai Pembatas Horizontal Atas
lebar_tengah_2008 = 4 * n_2008 + 5
print("#" + "=" * lebar_tengah_2008 + "#")

# 2. Fase 1: Jam Pasir Atas (N s.d. 1)
for baris_2008 in range(n_2008, 0, -1):
    print("| " + " " * (2 * (n_2008 - baris_2008)), end="")
    
    for k_2008 in range(baris_2008, 0, -1):
        print(f"{k_2008} ", end="")
        
    print("<*>", end="")
    
    for k_2008 in range(1, baris_2008 + 1):
        print(f" {k_2008}", end="")
        
    print(" " * (2 * (n_2008 - baris_2008)) + " |")

# 3. Fase 2: Poros Titik Pusat Jam Pasir (Singularity)
spasi_2008 = 2 * n_2008 + 1
print("|" + " " * spasi_2008 + "<*>" + " " * spasi_2008 + "|")

# 4. Fase 3: Jam Pasir Bawah (1 s.d. N)
for baris_2008 in range(1, n_2008 + 1):
    print("| " + " " * (2 * (n_2008 - baris_2008)), end="")
    
    for k_2008 in range(baris_2008, 0, -1):
        print(f"{k_2008} ", end="")
        
    print("<*>", end="")
    
    for k_2008 in range(1, baris_2008 + 1):
        print(f" {k_2008}", end="")
        
    print(" " * (2 * (n_2008 - baris_2008)) + " |")

# 5. Bingkai Pembatas Horizontal Bawah
print("#" + "=" * lebar_tengah_2008 + "#")