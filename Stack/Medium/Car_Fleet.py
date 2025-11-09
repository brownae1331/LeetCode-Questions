def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    pairs = [(p, s) for p, s in zip(position, speed)]
    pairs.sort(reverse=True)

    stack = []
    for p, s in pairs:
        time = (target - p) / s
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)

if __name__ == "__main__":
    print(carFleet(target=10, position=[1,4], speed=[3,2]))