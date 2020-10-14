class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (360/(12*60)) * (hour*60+minutes)
        m = 360/60 * minutes
        angle = abs(h - m)
        return min(angle, 360-angle)
