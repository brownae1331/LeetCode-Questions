def dailyTemperatures(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []
    
    for i in range(len(temperatures)):
        while stack and temperatures[i] > stack[-1][1]:
            res[stack[-1][0]] = i - stack[-1][0]
            stack.pop()
        stack.append((i, temperatures[i]))
    return res
        

if __name__ == "__main__":
    print(dailyTemperatures(temperatures=[73,74,75,71,69,72,76,73]))