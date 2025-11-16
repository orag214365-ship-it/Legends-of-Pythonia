def addPercent(value, percent):
    return value + (value * percent // 100)


def add_percentage_to_stats(stats_dict, percent):
    updated_stats = {}
    for key, value in stats_dict.items():
        if isinstance(value, int):
            updated_stats[key] = value + (value * percent // 100)
        else:
            updated_stats[key] = value
    return updated_stats
