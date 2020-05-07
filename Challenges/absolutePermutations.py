

#time limit problem, try to add solution with dict

def absolutePermutation(n, k):
    integers = set(range(1, n + 1))

    positions = list(range(1, n + 1))

    def check_permutation(remaining_integers, k, positions):
        if len(positions) == 1:
            if abs(positions[0] - list(remaining_integers)[0]) == k:
                return list(remaining_integers)
            else:
                return False
        else:
            first_option = positions[0] - k
            resp_first_option = False
            if first_option in remaining_integers:
                resp_first_option = check_permutation(remaining_integers - {first_option}, k, positions[1:])
            if resp_first_option != False:
                return [first_option] + resp_first_option
            else:
                second_option = positions[0] + k
                resp_second_option = False
                if second_option in remaining_integers:
                    resp_second_option = check_permutation(remaining_integers - {second_option}, k, positions[1:])
                if resp_second_option != False:
                    return [second_option] + resp_second_option
                else:
                    return False

    complete_resp = check_permutation(integers, k, positions)

    if complete_resp == False:
        return [-1]
    else:
        return complete_resp


absolutePermutation(4,2)

