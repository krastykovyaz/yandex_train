# На некоторых кросс-платформенных станциях метро (как, например, «Третьяковская») на разные стороны платформы приходят поезда разных направлений. Таня договорилась встретиться с подругой на такой станции, но поскольку подруга приехала из другого часового пояса, то из-за джетлага сильно проспала, и Тане пришлось долго её ждать. Поезда всегда ходят точно по расписанию, и Таня знает, что поезд стоит на платформе ровно одну минуту, а интервал между поездами (время, в течение которого поезда у платформы нет) составляет a минут для поездов на первом пути и b минут для поездов на втором пути. То есть на первый путь приезжает поезд и стоит одну минуту, затем в течение a минут поезда у платформы нет, затем в течение одной минуты у платформы стоит следующий поезд и т. д.
#
# Пока Таня стояла на платформе, она насчитала n поездов на первом пути и m поездов на втором пути. Определите минимальное и максимальное время, которое Таня могла провести на платформе, или сообщите, что она точно сбилась со счёта.
#
# Все поезда, которые видела Таня, она наблюдала в течение всей минуты, то есть Таня не приходит и не уходит с платформы посередине той минуты, когда поезд стоит на платформе.
# Формат ввода
# Первая строка входных данных содержит число a — интервал между поездами на первом пути. Вторая строка содержит число b — интервал между поездами на втором пути. Третья строка содержит число n — количество поездов на первом пути, которые увидела Таня. Четвёртая строка содержит число m — количество поездов на втором пути, которые увидела Таня. Все числа — целые, от 1 до 1000.

def get_time():
    a, b, n, m = 1, 5, 1, 2
    interval_a = n - 1
    interval_a_time = a * interval_a
    min_time_a = interval_a_time + n
    interval_b = m - 1
    interval_b_time = b * interval_b
    min_time_b = interval_b_time + m
    max_time_a = min_time_a + (2 * a)
    max_time_b = min_time_b + (2 * b)
    min_time_a_b = max(min_time_a, min_time_b)
    max_time_a_b = min(max_time_a, max_time_b)
    if min_time_a_b > max_time_a_b:
        return -1
    return min_time_a_b, max_time_a_b




if __name__=='__main__':
    print(get_time())