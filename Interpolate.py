def get_sample(data, target_index):
    index1 = int(target_index)

    if index1 >= target_index:
        return data[index1]

    index2 = index1 + 1
    fractional_index = target_index - index1
    value1 = data[index1]
    value2 = data[index2]
    return value1 + fractional_index * (value2 - value1)


def interpolate_wave_table(index, data):
    # Find the length the and the fractional part of the index
    N = len(data) - 1
    int_index = int(index)
    frac = index - int_index

    # Find the indices that we want to interpolate between
    index_2 = int_index + 2
    index_1 = int_index + 1
    index_0 = int_index
    index_sub_1 = int_index - 1

    # Find the edge cases on the wave table
    if index_sub_1 == -1:
        index_sub_1 = 0

    if index_sub_1 >= N:
        index_sub_1 = N

    if index_0 >= N:
        index_0 = N
        index_1 = N
        index_2 = N

    if index_1 >= N:
        index_1 = N
        index_2 = N

    if index_2 >= N:
        index_2 = N

    if type(data[0]) == list:
        out = []
        channels = len(data[0])
        for channel in range(channels):
            # Calculate Coefficients
            a0 = data[index_2][channel] - data[index_1][channel] - data[index_sub_1][channel] + data[index_0][channel]
            a1 = data[index_sub_1][channel] - data[index_0][channel] - a0
            a2 = data[index_1][channel] - data[index_sub_1][channel]
            a3 = data[index_0][channel]

            # Calculate the Sample at the index
            out.append(float(a0 * pow(frac, 3.0) + a1 * pow(frac, 2.0) + a2 * frac + a3))
    else:
        # Calculate Coefficients
        a0 = data[index_2] - data[index_1] - data[index_sub_1] + data[index_0]
        a1 = data[index_sub_1] - data[index_0] - a0
        a2 = data[index_1] - data[index_sub_1]
        a3 = data[index_0]

        # Calculate the Sample at the index
        out = a0 * pow(frac, 3.0) + a1 * pow(frac, 2.0) + a2 * frac + a3
    return out
