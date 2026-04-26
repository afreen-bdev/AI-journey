def calculate_priority(urgency, time_required):
    score = urgency * 2 - time_required

    if score > 5:
        return "High"
    elif score > 2:
        return "Medium"
    else:
        return "Low"