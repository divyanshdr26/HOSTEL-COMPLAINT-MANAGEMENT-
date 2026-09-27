def valid_category(choice, categories):
    return choice in categories


def valid_status(status):
    return status in {"Pending", "In Progress", "Resolved"}
