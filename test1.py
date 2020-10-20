# %%
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # write your code in Python 3.6
    data = S.split('\n')

    # case of no values/header
    if len(data) < 2:
        return -1

    # normal case
    header = data[0]
    values = data[1:]

    # find the column of C in the header
    pos = header.split(',').index(C)

    # collect all the values of the column C, and convert the value from string to int
    l = [int(x.split(',')[pos]) for x in values]

    # abnormal case
    if len(l) < 1:
        return -1

    val_max_C = max(l)

    return val_max_C

# %%
# print("this is a debug message")


def solution(S):
    # write your code in Python 3.6

    data = S.split('\n')

    # case of no values/header
    if len(data) < 2:
        return -1

    # normal case
    header = data[0]
    values = data[1:]

    # only consider the non-defective rows, remove the rows with "NULL"
    l = [item + '\n' for item in values if 'NULL' not in item.split(',')]

    # case of all rows are defective
    if len(l) == 0:
        res = header
    else:
        # concatenate the header and all the rows to a string and remove the last '\n'
        res = header + '\n' + ''.join(l)[:-1]
    return res


# %%
-- write your code in PostgreSQL 9.4
SELECT MAX(temp.min_required_rooms) AS rooms
FROM(SELECT COUNT(*) AS min_required_rooms
     FROM meetings AS m1
     LEFT JOIN meetings AS m2
     ON(m1.start_time < m2.end_time) AND(m1.start_time >= m2.start_time)
     GROUP BY m1.id) AS temp
