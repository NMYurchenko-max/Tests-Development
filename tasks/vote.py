
def vote(votes):
    """Выводит число, которое встречается чаще всего
    :param votes: список чисел
    :return: число, которое встречается чаще всего
    """
    return max(set(votes), key=votes.count)
