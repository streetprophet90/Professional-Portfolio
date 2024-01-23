# Digital root is the recursive sum of all the digits in a number.
#
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
#
# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    # Base case: if n is a single-digit number, return it
    if n < 10:
        return n

    # Convert the number to a list of its digits and calculate the sum
    digit_sum = sum(int(digit) for digit in str(n))

    # Recursively call digital_root on the sum
    return digital_root(digit_sum)

# Examples:
print(digital_root(16))      # Output: 7
print(digital_root(942))     # Output: 6
print(digital_root(132189))  # Output: 6
print(digital_root(493193))  # Output: 2
