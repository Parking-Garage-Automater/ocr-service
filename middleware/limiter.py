from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_ipaddr

limiter = Limiter(key_func=get_ipaddr, default_limits=["100/minute"])
