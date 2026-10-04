class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if not body.get("constraint"): failed.append("constraint")\n    if not body.get("metric"): failed.append("metric")
    return {"passed": not failed, "failed": failed, "applied": False}
