from graphics import *
from random import *
from time import sleep

screen_width = 800
screen_height = 600
buff_width = 50
buff_height = 200
# bar_width = 40
bar_height = 500
max_range = 1000
nbs_count = 200
bar_width = screen_width / nbs_count

def swap(i, j, nbs, bars):
    aux = nbs[i]
    nbs[i] = nbs[j]
    nbs[j] = aux

    bars[i].p1 = Point(i * bar_width, screen_height)
    bars[i].p2 = Point((i + 1) * bar_width, screen_height - bar_height * nbs[i] / max_range)
    bars[j].p1 = Point(j * bar_width, screen_height)
    bars[j].p2 = Point((j + 1) * bar_width, screen_height - bar_height * nbs[j] / max_range)


def selection_sort(win, bars, nbs):
    for i in range(len(nbs) - 1):
        for j in range(i + 1, len(nbs)):
            bars[j].setFill('red')
            sleep(0.01)
            if nbs[i] > nbs[j]:
                bars[i].undraw()
                bars[j].undraw()
                swap(i, j, nbs, bars)
                bars[i].draw(win)
                bars[j].draw(win)
            bars[j].setFill('blue')


def merge(win, bars, nbs, st, mid, end):
    st2 = mid + 1
    if nbs[mid] < nbs[mid + 1]:
        return

    while st <= mid and st2 <= end:
        sleep(0.01)
        if nbs[st] < nbs[st2]:
            st += 1
        else:
            value = nbs[st2]
            index = st2

            while index != st:
                bars[index].undraw()
                bars[index - 1].undraw()

                swap(index, index - 1, nbs, bars)

                bars[index].draw(win)
                bars[index - 1].draw(win)
                index -= 1

            bars[st].undraw()
            bars[st2].undraw()
            bars[st].draw(win)
            bars[st2].draw(win)

            st += 1
            mid += 1
            st2 += 1


def merge_sort(win, bars, nbs, st, end):
    if st < end:
        mid = st + (end - st) // 2
        merge_sort(win, bars, nbs, st, mid)
        merge_sort(win, bars, nbs, mid + 1, end)
        merge(win, bars, nbs, st, mid, end)


def bubble_sort(win, bars, nbs):
    flag = False
    while not flag:
        flag = True
        for i in range(nbs_count - 1):
            if nbs[i] > nbs[i + 1]:
                bars[i].undraw()
                bars[i + 1].undraw()
                swap(i, i + 1, nbs, bars)
                bars[i].draw(win)
                bars[i + 1].draw(win)
                flag = False


def insertion_sort(win, bars, nbs):
    for k in range(nbs_count):
        i = k - 1
        while i >= 0 and nbs[i] > nbs[i + 1]:
            bars[i].undraw()
            bars[i + 1].undraw()
            swap(i, i + 1, nbs, bars)
            bars[i].draw(win)
            bars[i + 1].draw(win)
            i = i - 1


def main():
    win = GraphWin("Sorting Visualizer", screen_width, screen_height)

    nbs = []
    for i in range(nbs_count):
        nbs.append(randint(0, max_range))

    bars = []
    for i in range(nbs_count):
        bars.append(Rectangle(Point(i * bar_width, screen_height), Point((i + 1) * bar_width,
                screen_height - bar_height * nbs[i] / max_range)))

    for bar in bars:
        bar.setOutline('gray')
        bar.setFill('blue')
        bar.draw(win)

    merge_sort(win, bars, nbs, 0, nbs_count - 1)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()