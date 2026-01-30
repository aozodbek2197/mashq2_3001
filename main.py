# 8-masala
roy1 = [1, 2, 3, 4]
roy2 = [3, 4, 5, 6]

res = sorted(set(roy1 + roy2))
print(res)
# 9-masala
roy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

juft = []
toq = []

for i in range(len(roy)):
    if i % 2 == 0:
        juft.append(roy[i])
    else:
        toq.append(roy[i])

print(f"Juft indekslilar: {juft}")
print(f"Toq indekslilar: {toq}")
# 10-masala
roy = [1, 1, 2, 2, 2, 3, 3, 1]

natija = []
son = roy[0]
n = 1

for i in range(1, len(roy)):
    if roy[i] == son:
        n += 1
    else:
        natija.append((son, n))
        son = roy[i]
        n = 1

natija.append((son, n))
print(natija)
# 11-masala
roy = [4, 7, 21, 17, 9, 12]

max_son = max(roy)
min_son = min(roy)

farqi = max_son - min_son

roy.remove(max_son)
roy.remove(min_son)

print(f"Farqi: {farqi}")
print(f"Toza royhat: {roy}")
# 12-masala
roy = [1, -4, 7, -2, -8, 5]

new = []
for i in roy:
    new.append(-i)

print(new)
# 13-masala
roy = [1, 2, 3, 4, 5, 6, 7]
hajm = 3

result = []
for i in range(0, len(roy), hajm):
    result.append(roy[i:i+hajm])

print(result)
# 14-masala
roy = [1, 2, 2, 3, 3, 4]

hisob = {}

for i in roy:
    hisob[i] = hisob.get(i, 0) + 1

print(hisob)
