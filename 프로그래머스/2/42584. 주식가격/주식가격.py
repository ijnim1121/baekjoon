def solution(prices):
    count = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            count[i] += 1
            if prices[i] > prices[j]:
                break
    return count