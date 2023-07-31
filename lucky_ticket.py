def check_sum(n):
    count = 0
    for num in range(10**(n-1), 10**n):
        digits = [int(digit) for digit in str(num)]
        mid = n//2
        first_half_sum = sum(digits[:mid])
        second_half_sum = sum(digits[mid:])
        if first_half_sum == second_half_sum:
            count += 1
    return count/(10**n)

if __name__ == '__main__':
    while True:
        n = int(input("Enter an even number of digits: "))
        if n % 2 == 1:
            print("Please enter an even number of digits.")
        else:
            prob = check_sum(n)
            print(f"The probability that the sum of the first {n//2} digits equals the sum of the last {n//2} digits is: {prob:.6f}")
            break
