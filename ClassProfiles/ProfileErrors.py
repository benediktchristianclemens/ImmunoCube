from typing import Self, List, Dict, Set

class ProfileError(Exception):
    def __init__(self, message=None):
        super().__init__(message)
        self.message = message
        
class ProfileNotFoundError(ProfileError):
    def __init__(self, message="Profile not found"):
        super().__init__(message)
        
class ProfileNegativeDistanceError(ProfileError):
    def __init__(self, message="Negative distance is not allowed."):
        super().__init__(message)

class ProfileInvalidDistanceError(ProfileError):
    def __init__(self, message="Distance measurement is not implemented."):
        super().__init__(message)

class FractionZeroDivisionError(ProfileError):
    def __init__(self, Profile_sampleData: dict[str, float]): # passed along as FractionProfile.sampleData in code
        
        zero_fractions = [key for key, value in Profile_sampleData.items() if value == 0]
        message = f"For those fraction(s) the value is zero: {', '.join(zero_fractions)}."
        super().__init__(message)   

class UnequalFractionsError(ProfileError):
    def __init__(self, message="Fractions are not the same across profiles."):
        super().__init__(message)

class ZeroSumError(ProfileError):
    def __init__(self, message="Sum cannot be zero."):
        super().__init__(message)
        
class EmptyProfileListError(ProfileError):
    def __init__(self, message="The provided list of profiles is empty."):
        super().__init__(message)

class EmptyProfileError(ProfileError):
    def __init__(self, message="Invalid profile. The profile is empty."):
        super().__init__(message)
        
class ComponentErrorPCA(ProfileError):
    def __init__(self, message="Number of components bigger than number of fractions or the number of samples."):
        super().__init__(message)