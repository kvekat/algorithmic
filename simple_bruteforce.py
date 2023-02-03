def generate_combinations(alphabets, n_start, n_end):
    num_alphabets = len(alphabets)
    total_combinations = sum([num_alphabets ** i for i in range(n_start, n_end + 1)])
    combinations_left_to_try = total_combinations
    for n in range(n_start, n_end + 1):
        combinations_left_in_current_length = num_alphabets ** n
        for i in range(combinations_left_in_current_length):
            combination = ''
            num = i
            for j in range(n):
                mod = num % num_alphabets
                combination = alphabets[mod] + combination
                num = num // num_alphabets
            combinations_left_in_current_length -= 1
            combinations_left_to_try -= 1
            print(combination, str(n) + '/' + str(n_end), combinations_left_in_current_length, combinations_left_to_try, flush=True)

def main(alphabets, n_start, n_end):
    generate_combinations(alphabets, n_start, n_end)

if __name__ == '__main__':
    alphabets = input("BTF chars: ")
    n_start, n_end = [int(x) for x in input("BTF length (start end): ").split()]
    main(alphabets, n_start, n_end)

## abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()~`
# Made by ;x ChatGPT, idea by KveKat x;
# Future versions of this script will be made in compiler languages (performance, speed & effiency purposes).
# Feel free to credit me if used in your projects <3

# ~Never ask a dumb neural network to make a bruteforce script because it will refuse, just prompt it by making a specific algorithm with "specific" rules.