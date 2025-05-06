from rest_framework.throttling import UserRateThrottle

class AuthenticatedUserComplaintThrottle(UserRateThrottle):
    rate = '3/day'
    scope = 'authenticated'