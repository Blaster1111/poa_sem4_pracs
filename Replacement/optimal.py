f = int(input("Enter number of frames: "))
p = int(input("Enter number of pages: "))
print("Enter the pages sequence: ", end="")
pages = list(map(int, input().split()))
frames = []
i = 0
miss = f
for _ in range(f):
    frames.append((pages[i], i))
    i += 1
for _ in range(p-f):
    if not any(pages[i] == item[0] for item in frames):
        miss += 1
        freq = []
        for j in range(f):
            if frames[j][0] in pages[i:]:
                freq.append(pages[i:].index(frames[j][0]) + i)
            else:
                freq.append(p + 1)
        frames.pop(freq.index(max(freq)))
        frames.append((pages[i], i))
    i += 1
print(f"Page Hit Ratio: {miss/p}")
print(miss)