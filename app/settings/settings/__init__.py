try: # NOQA 403
    from .local import * # NOQA 401
except ImportError: # NOQA 403
    from .base import * # NOQA