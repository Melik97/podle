from apis.exceptions import HTTPNotFound


def int_or_notfound(id):
    try:
        return int(id)

    except (ValueError, TypeError):
        raise HTTPNotFound()

