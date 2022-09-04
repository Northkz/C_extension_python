import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import myModule


def Csort(data):
    list = myModule.selectSort(list)
    yield list


def sort(data, x_ax):
    datalen = len(data)
    for i in range(datalen):
        minpos = i
        for j in range(i + 1, datalen):
            if data[j] < data[minpos]:
                minpos = j
        data[minpos], data[i] = data[i], data[minpos]
        yield np.c_[x_ax, data]



def main():
    size = int(input("Input array size: "))
    while not 1 <= size <= 20000:
        print("Size must be within 1 to 20000.")
        size = int(input("Input array size: "))
    data = [random.randint(-1000000, 1000000) for x in range(size)]
    data2 = [random.randint(-1000000, 1000000) for x in range(size)]

    '''Domain'''
    x_ax = [i for i in range(len(data))]
    '''generator'''
    generator = sort(data, x_ax)
    second_generator = sort(data2, x_ax)
    # fig, ax = plt.subplots()
    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    ax1.title.set_text('Sort using Python')

    ax1.ticklabel_format(useOffset=False, style='plain')
    ax1.margins(x=0.0015, y=0.005)
    ax2.title.set_text('Sort using C')
    ax2.margins(y=0.005)
    ax2.ticklabel_format(useOffset=False, style='plain')

    x, y = next(generator).T
    python = ax1.scatter(x, y, s=1, c="blue")
    c = ax2.scatter(x, y, s=1, c="red")


    def updatePython(i):
        if (i % 4 == 0):
            data = next(generator)
            python.set_offsets(data[:, :2])
            return python,
        else:
            return python,


    def updateC(j):
        data2 = next(second_generator)
        c.set_offsets(data2[:, :2])
        return c,


    ani = []
    ani.append(animation.FuncAnimation(
        fig, updatePython, interval=0, blit=True, repeat=False))
    ani.append(animation.FuncAnimation(
        fig, updateC, interval=0, blit=True, repeat=False))

    plt.show()


if _name_ == "_main_":
    main()