if __name__ == '__main__':
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name, score])
    score_set = sorted(set([score for name, score in score_list]))
    second_lowest_score = score_set[1]
    second_lowest_name = [name for name, score in score_list if score == second_lowest_score]
    print("\n".join(sorted(second_lowest_name)))