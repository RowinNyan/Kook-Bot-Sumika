import random

def randlist(times: int, max: int) -> list[int]:
    output: list[int] = []
    for _ in range(times):
        output.append(random.randint(0, max-1))
    return output
