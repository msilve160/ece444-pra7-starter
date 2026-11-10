def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


def is_missing(x):
    if x is None:
        return True
    return False
