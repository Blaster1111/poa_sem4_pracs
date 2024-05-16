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
        frames.pop(0)
        frames.append((pages[i], i))
        miss += 1
    i += 1
print(f"Page Hit Ratio: {1 - miss/p}")
print(miss)