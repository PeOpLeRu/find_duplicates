import os, time, numpy as np

# ---------------------- Код функций ----------------------

def find_duplicates(data : list[str], hash_func : callable) -> list[str]:
    res = []
    cache = {}

    for i in data:
        file_data = open(i).read()
        __hash = hash_func(file_data)
        if __hash not in cache:
            cache[__hash] = i
        else:
            res.append(i)

    return res

def generate_R() -> list[int]:
    res = np.random.permutation(256)
    return res

def CRC(data : str) -> int:
    h = 0

    for char in data:
        highorder = h & 0xf8000000
        h = h << 5
        h = h ^ (highorder >> 27)
        h = h ^ ord(char)

    return h

def PJW(data : str) -> int:
    h = 0

    for char in data:
        h = (h << 4) + ord(char)
        g = h & 0xf0000000
        if (g != 0):
            h = h ^ (g >> 24)
            h = h ^ g

    return h

def BUZ(data : str) -> int:
    h = 0

    for char in data:
        highorder = h & 0x80000000
        h = h << 1
        h = h ^ (highorder >> 31)
        h = h ^ R[ord(char)]

    return h

# ---------------------- Основной код ----------------------

files = []  # Считываем файлы с директории
for dirpath, dirnames, filenames in os.walk("out"):
    for filename in filenames:
        files.append(os.path.join(dirpath, filename))

print("Find: " + str(len(files)) + " files")

print("\n----------------------------------\n")

start = time.time()  # Дубликаты с помощью функции hash
print("Start with function: hash")
res = find_duplicates(files, hash)
print("Working time: " + str(time.time() - start))
print("Number of duplicates: " + str(len(res)))

print("\n----------------------------------\n")

start = time.time()  # Дубликаты с помощью функции CRC
print("Start with function: CRC")
res = find_duplicates(files, CRC)
print("Working time: " + str(time.time() - start))
print("Number of duplicates: " + str(len(res)))

print("\n----------------------------------\n")

start = time.time()  # Дубликаты с помощью функции PJW
print("Start with function: PJW")
res = find_duplicates(files, PJW)
print("Working time: " + str(time.time() - start))
print("Number of duplicates: " + str(len(res)))

print("\n----------------------------------\n")

start = time.time()  # Дубликаты с помощью функции BUZ
R = generate_R()
print("Start with function: BUZ")
res = find_duplicates(files, BUZ)
print("Working time: " + str(time.time() - start))
print("Number of duplicates: " + str(len(res)))