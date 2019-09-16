from collections import Counter
import array

def most_common_element(filepath):
    with open(filepath) as file:
        arr = array.array('i', map(int, file.readlines()[1].split()))
        cnt_most_common = Counter(arr).most_common()
        max_value, max_count = cnt_most_common[0]
        for value, count in cnt_most_common:
            if count == max_count:
                max_value = max(value, max_value)
    return max_value







