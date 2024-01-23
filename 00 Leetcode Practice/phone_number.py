# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers
# in the form of a phone number.
#
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
#
# Don't forget the space after the closing parentheses!


def create_phone_number(n):
    # Ensure the input list has exactly 10 integers
    if len(n) != 10 or not all(isinstance(i, int) and 0 <= i <= 9 for i in n):
        raise ValueError("Input must be a list of 10 integers between 0 and 9")

    # Format the phone number
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# Example usage:
phone_number = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(phone_number)
