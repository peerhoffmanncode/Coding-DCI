def singleton(class_):
    # build cache dict for classes
    # cache is private
    __instances = {}

    # inner def for decorator
    def get_instance(*args, **kwargs):
        # check if instance is already existing
        if class_ not in __instances:
            # only add instance if not existing
            __instances[class_] = class_(*args, **kwargs)
        # return instance anyway
        return __instances[class_]

    # execute decorator
    return get_instance
