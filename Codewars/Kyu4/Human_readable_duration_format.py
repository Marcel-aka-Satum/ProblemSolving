
def pluralize(n, string):
    if n == 1:
        return '%d %s' % (n, string)

    return '%d %ss' % (n, string)
        
def format_duration(seconds):
    if seconds == 0:
        return 'now'

    one_min = 60
    one_hour = one_min * 60
    one_day = one_hour * 24
    one_year = one_day * 365

    units = (
        (one_year, 'year'),
        (one_day, 'day'),
        (one_hour, 'hour'),
        (one_min, 'minute'),
        (1, 'second')
    )

    ol = []
    for i in units:
        time, string = i
        if seconds >= time:
            n = int(seconds / time)
            ol.append(pluralize(n, string))
            seconds -= n * time
    return ' and'.join(', '.join(ol).rsplit(',',1))
