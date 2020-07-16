def do_cache(maxsize):
    def decorator(func):
        cache = dict()
        def wrapper(*args,**kwargs):
            if args in cache:
                return cache[args]
            else:
                if len(cache) == maxsize:
                    items = list(cache)
                    cache.pop(items[0])
                result = func(args, kwargs)
                cache[args] = result
            return result
        return wrapper
    return decorator


@do_cache(maxsize=3)
def get_value(a, b):
  return a ** b