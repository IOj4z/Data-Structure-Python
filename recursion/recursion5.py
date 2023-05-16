def pretty_print_numbers(numbers):
    if numbers < 10:
        print(numbers)
    else:
        print(numbers)
        pretty_print_numbers(numbers // 10)
        print(numbers)


pretty_print_numbers(4003)