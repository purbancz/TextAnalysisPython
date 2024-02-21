from collections import Counter
from collections import deque


def generate_tokens(filename):
    with open(filename, encoding="utf-8") as infile:
        for line in infile:
            for token in line.split():
                yield token


def generate_n_grams(filename, n):
    tokens = deque(maxlen=n)
    token_generator = generate_tokens(filename)
    for _ in range(n):
        tokens.append(next(token_generator))
    yield ' '.join(tokens)
    for token in token_generator:
        tokens.append(token)
        yield ' '.join(tokens)


def count_tokens(generator):
    return Counter(generator)
    # token_counter = {}
    # for token in generator:
    #     if token in token_counter:
    #         token_counter[token] += 1
    #     else:
    #         token_counter[token] = 1
    # return dict


def sort_dictionary(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)


def get_top_n_with_ties(dictionary, n):
    sorted_tuples = sort_dictionary(dictionary)
    result = sorted_tuples[:n]
    for entry in sorted_tuples[n:]:
        if entry[1] == sorted_tuples[n - 1][1]:
            result.append(entry)
        else:
            break
    # i = n
    # while i < len(sorted_items) and sorted_items[i][1] == sorted_items[n - 1][1]:
    #     result.append(sorted_items[i])
    #     i += 1
    return result


def print_scoreboard(sorted_scoreboard):
    last_score = sorted_scoreboard[0][1]
    place = 1
    for i, entry in enumerate(sorted_scoreboard):
        if entry[1] != last_score:
            place = i + 1
            last_score = entry[1]
        print(f"{place}. {entry[0]} {entry[1]}")


def print_top_k_ex_aequo_most_frequent_tokens(filename, k):
    print_scoreboard(get_top_n_with_ties(count_tokens(generate_tokens(filename)), k))


def print_top_k_ex_aequo_most_frequent_n_grams(filename, n, k):
    print_scoreboard(get_top_n_with_ties(count_tokens(generate_n_grams(filename, n)), k))


if __name__ == "__main__":
    # print_top_n_ex_aequo_most_frequent_tokens("potop.txt", 1000)
    print_top_k_ex_aequo_most_frequent_n_grams("potop.txt", 2, 1000)
