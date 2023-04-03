from collections import deque

MAX_LEN = 3

lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.appendleft(element)


def pop():
    return lifo.popleft()