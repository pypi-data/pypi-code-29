from ide import models


def visit_record(func):
    def wrapper(*args, **kwargs):
        request = args[0]
        visit_record = models.VisitCounts.today_add_one()
        print(args[0].META)
        visitor = models.Visitors(
            ip=args[0].META.get("REMOTE_ADDR"), url=args[0].path)
        visitor.save()
        return func(*args, **kwargs)

    return wrapper
