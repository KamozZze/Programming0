# lyulin_city.py

def solution(blocks):
    if len(blocks) == 0:
        return 0

    seen_blocks = 1
    current_max = blocks[0]

    for block in blocks:
        if block > current_max:
            seen_blocks += 1
            current_max = block

    return seen_blocks

n = input("Number of blocks: ")
n = int(n)

blocks = []
start = 1

while start <= n:
    height = input("Enter block's height: ")
    height = int(height)

    blocks += [height]

    start += 1

print("Ivancho will see " + str(solution(blocks)) + " blocks!")
