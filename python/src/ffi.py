from functools import wraps
import inspect


def eager(fn):
    @wraps(fn)
    async def wrapper(*args, **kwargs):
        args_computed = []
        kwargs_computed = {}
        for arg in args:
            args_computed.append(await arg.compute())
        for name, arg in kwargs.items():
            kwargs_computed[name] = await arg.compute()
        return await fn(*args_computed, **kwargs_computed)

    return wrapper


def lazy(fn):
    return fn


def foreign_function(eval_strategy=eager):
    def wrap(fn):
        @wraps(fn)
        @eval_strategy
        async def wrapper(*args, **kwargs):
            if inspect.iscoroutinefunction(fn):
                return await fn(*args, **kwargs)
            else:
                return fn(*args, **kwargs)

        return wrapper

    return wrap
