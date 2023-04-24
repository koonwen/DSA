from collections import Counter

# This problem is simple in intuition but a little bit complex to implement
# because we want to take care of the time complexity. The brute force method
# would be to have one counter to maintain a count of the number of values
# added and deleted. However, the problem with this is that during the search
# you would need to iterate over the hashtable's values to find if we have a
# correct frequency.To be able to solve this problem in one pass and prevent
# incurring O(N^2) number of operations to check the table, the proposed
# solution is to add an additional counter, this time, the second counter
# uses the frequency as the key and it's value corresponds to the number of
# values in the first hashtable with the same frequency

# e.g. [(1,5), (1,6), (3, 2), (1,10), (1, 10), (1,6), (2, 5), (3, 2)]
# itr1 (1): freq {1->1},       count {1->5}
# itr2 (1): freq {1->2},       count{5->1, 6->1}
# itr3 (3):        ---- no change ---                           found: 0
# itr4 (1): freq {1->3},       count{5->1, 6->1, 10->1}
# itr5 (1): freq {1->2, 2->1}, count{5->1, 6->1, 10->2}
# itr6 (1): freq {1->1, 2->2}, count{5->1, 6->2, 10->2}
# itr7 (2): freq {1->0, 2->2}, count{6->2, 10->2}
# itr8 (3):        ---- no change ---                           found: 1

def freq_query(queries):
    """
    return a list of results of queries about frequencies with opcode 3
    :param queries:
    :return: list of results
    """
    freq = Counter()
    count = Counter()
    arr = []

    for opcode, v in queries:
        if opcode == 1:
            freq[count[v]] -= 1
            count[v] += 1
            freq[count[v]] += 1
        if opcode == 2:
            if count[v] > 0:
                freq[count[v]] -= 1
                count[v] -= 1
                freq[count[v]] += 1
        if opcode == 3:
            if freq[v] > 0:
                arr.append(1)
            else:
                arr.append(0)

    return arr