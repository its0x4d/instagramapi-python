class SentryBlockException(Exception):
    pass

class AccountTypeException(Exception):
    pass

class UserNotFoundException(Exception):
    pass

class InvalidCredentialsException(Exception):
    pass

class RateLimitException(Exception):
    pass

class AccessDeniedException(Exception):
    pass

class ChallengeRequiredException(Exception):
    pass

class LogedOutException(Exception):
    pass

class InternalException(Exception):
    pass