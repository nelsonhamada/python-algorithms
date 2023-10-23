def study_schedule(permanence_period, target_time):
    count = 0
    if not target_time:
        return None
    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None
        if target_time >= period[0] and target_time <= period[1]:
            count += 1
    return count
