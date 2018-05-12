import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

N = 2000

maxX = 2*np.pi
phi = random.random() / 10
A = 1

def init_sequence():
    result = []
    for x in np.arange(0.0, maxX, maxX / N):
        result.append(A*np.sin(x + phi) + A*np.sin(x + phi)*random.uniform(-0.03, 0.03))
    return result

def sin_sequence():
    result = []
    for x in np.arange(0.0, maxX, maxX / N):
        result.append(np.sin(x))
    return result

def mean_arithmetic(sequence):
    sum = 0
    result = []
    i = 1
    for x in sequence:
        sum += x
        i += 1
        result.append(sum / i)
    return result

def mean_geometric(sequence):
    sum = 1
    result = []
    i = 0
    for x in sequence:
        sum *= x
        result.append(np.power(np.abs(sum),(1/(i+1))))
        i += 1
    return result

def mean_harmonic(sequence):
    sum = 0;
    result_arr = [];
    i = 0
    for x in sequence:
        if np.abs(x) >= 0.05:
            sum += np.abs(1 / x)
            result_arr.append((i + 1) / sum)
        i+=1
    return result_arr;

def simple_moving_average(sequence, bars):
        result = []
        for i in range(len(sequence) - bars):
            sum = 0
            for j in range(bars + 1):
                sum += sequence[i + j]
            result.append(sum / bars)
        return result
        # for j in range(bars):
        #     result.append(0)
        # for i in range(bars-1,len(sequence)):
        #     sum = 0
        #     for j in range(bars):
        #         sum += sequence[i - j]
        #     result.append(sum / bars)
        # return result

def weighted_moving_averange(sequence, bars):
    result = []
    for i in range(bars-1, len(sequence)):
        sum = 0
        for j in range(bars):
            sum += sequence[i - j]*(bars - j)
        result.append(sum / ((bars*(bars + 1)) / 2))
    return result

def modified_moving_averange(sequence):
    result = []
    result.append(sequence[0])

    alpha = 1/ (len(sequence) + 1)

    for i in range(1, len(sequence)):
        result.append(sequence[i]*alpha + (1 - alpha)*sequence[i - 1])

    return result

def exponential_moving_average(sequence, bars):
    alpha = 2/(bars + 1)
    result = [sequence[0]]
    for i in range(1,len(sequence)):
        result.append(sequence[i] * alpha + result[i - 1] * (1 - alpha))
    return result


def smoothing_out(sequence, smoothing):
    result = []

    for i in range(len(sequence)):
        sum = 0

        for j in range(i - smoothing,i + smoothing + 1):
            if j < 0:
                index = j + len(sequence)
            else:
                index = j % len(sequence)
            sum += sequence[index]

        result.append(sum / ((smoothing*2) + 1))

    # for (i = 0; i < func.length; i++) {
    #     var sum = 0;
    #
    #     for (index = i - smoothing; index <= i + smoothing; index++) {
    #         var thisIndex = index < 0 ? index + func.length : index % func.length;
    #         sum += func[thisIndex];
    #     }
    #     newArray[i] = sum/((smoothing*2)+1);
    # }



sequence = init_sequence()

plt.plot(sin_sequence(), label = "sin")
plt.plot(init_sequence(), label = "changed sin")
plt.plot(mean_arithmetic(sequence), label = "mean arithmetic")
plt.plot(mean_geometric(sequence), label = "mean geometric")
plt.plot(mean_harmonic(sequence), label = "mean harmonic")
plt.plot(simple_moving_average(sequence, 9), label = "simple moving average")
plt.plot(weighted_moving_averange(sequence,9), label = "weighted moving averange")
plt.plot(modified_moving_averange(sequence), label = "modifined moving averange")
plt.plot(exponential_moving_average(sequence,9), label = "exponential moving average")

# plt.plot(smoothing_out(sequence,20), label = "smoothing out")
plt.legend()
plt.show()
