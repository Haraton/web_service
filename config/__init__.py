try:
    from .settings import *
except ImportError:
    pass
try:
    from .localsettings import *
except ImportError:
    pass