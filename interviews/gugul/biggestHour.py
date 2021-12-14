def isValidHour(hour):
    secondHour = hour
    hour = hour[0:2]
    minute = secondHour[3:6]

    if int(hour) > 23:
        return False

    if int(minute) > 59:
        return False

    return True


# I don't think this function will be used, but I prefer to consider the case
def invalidHour(T):

    if T[0] != "?":
        if int(T[0]) > 2:
            return True

    if T[3] != "?":
        if int(T[3]) > 5:
            return True

    return False

    # print(T[0])
    # print(T[3])


def solution(T):

    # In case something like "9?:9:?" arrived
    if invalidHour(T):
        return T

    for i in reversed(range(10)):
        newHour = T.replace("?", str(i))

        if isValidHour(newHour):
            return newHour

    return newHour


print(solution("9?:9?"))
