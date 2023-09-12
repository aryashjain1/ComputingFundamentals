import numpy as np

def median(data, axis="x"):
    if data.ndim == 1:
        data = np.sort(data)
        if data.size % 2 == 0:
            return (data[int(data.size / 2 - 1)] + data[int(data.size / 2)]) / 2
        return data[data.size // 2]
    if axis == 'y':
        data = data.T
    meds = np.zeros(data.shape[0])
    for i in range(meds.size):
        cur_vals = data[i]
        cur_vals = np.sort(cur_vals)
        if cur_vals.size % 2 == 0:
            meds[i] = (cur_vals[int(cur_vals.size / 2 - 1)] + cur_vals[int(cur_vals.size / 2)]) / 2
        else:
            meds[i] = cur_vals[int(cur_vals.size // 2)]
    return meds

def mode(data, axis="x"):
    if data.ndim == 1:
        data = np.sort(data)
        cur_mode = data[0]
        mode = cur_mode
        num_instances = 1
        max_num_instances = 1
        for i in range(1, data.size):
            if data[i] == data[i-1]:
                num_instances += 1
            else:
                if num_instances > max_num_instances:
                    mode = cur_mode
                    max_num_instances = num_instances
                cur_mode = data[i]
                num_instances = 1
        return mode
    if axis == "y":
        data = data.T
    modes = np.zeros(data.shape[0])
    for i in range(modes.size):
        cur_vals = data[i]
        cur_vals = np.sort(cur_vals)
        cur_mode = cur_vals[0]
        mode = cur_mode
        num_instances = 1
        max_num_instances = 1
        for j in range(1, cur_vals.size):
            if cur_vals[j] == cur_vals[j-1]:
                num_instances += 1
            else:
                if num_instances > max_num_instances:
                    mode = cur_mode
                    max_num_instances = num_instances
                cur_mode = cur_vals[j]
                num_instances = 1
        modes[i] = mode
    return modes

mat1 = np.random.randint(1, 10, 10)
print(f'Matrix 1: {mat1}')
print(f'Median of Matrix 1: {median(mat1)}')
print(f'Mode of Matrix 1: {mode(mat1)}')
mat2 = np.random.randint(1, 10, (3, 4))
print(f'Matrix 2: {mat2}')
print(f'Medians of each row in Matrix 2: {median(mat2)}')
print(f'Modes of each row of Matrix 3: {mode(mat2)}')
mat3 = np.random.randint(1, 10, (6, 2))
print(f'Matrix 3: {mat3}')
print(f'Medians of each column in Matrix 3: {median(mat3, axis="y")}')
print(f'Modes of each column in Matrix 3: {mode(mat3, axis="y")}')