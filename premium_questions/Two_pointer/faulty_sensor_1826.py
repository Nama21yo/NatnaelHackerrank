def faulty_sensor(sensor1, sensor2):
    # n = len(sensor1)
    # m = len(sensor2)
    # i, j = 0, 0

    # while i < n-1 and j < m - 1:
    #     if sensor1[i] != sensor2[j]:
    #         if sensor1[i] > sensor2[j]:
    #             return sensor2[j]
    #         elif sensor1[i] < sensor2[j]:
    #             return sensor1[i]
    #     i += 1
    #     j += 1

    i = 0

    while i < len(sensor1)-1:
        
        if sensor1[i] != sensor2[i]:
            if sensor1[i+1] != sensor2[i]:
                return 1
            elif sensor1[i] != sensor2[i+1]:
                return 2
        i += 1
    return -1

    

# Test cases
print(faulty_sensor([2,3,4,5], [2,1,3,4])) 
print(faulty_sensor([2,2,2,2,2], [2,2,2,2,5])) 
print(faulty_sensor([2,3,2,2,3,2], [2,3,2,3,2,5])) 


from typing import List

class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        # Initialize index and get the length of the sensor arrays
        index, length = 0, len(sensor1)
      
        # Find the first mismatch in the sensor readings
        while index < length - 1:
            if sensor1[index] != sensor2[index]:
                break
            index += 1
      
        # Variables to track whether the mismatch pattern is consistent with one sensor failing
        mismatch_sensor1, mismatch_sensor2 = False, False
      
        # Continue checking for mismatches and determine which sensor, if any, is bad
        while index < length - 1:
            # Check if the rest of sensor1 matches with sensor2 shifted once
            if sensor1[index + 1] != sensor2[index]:
                mismatch_sensor1 = True
            # Check if the rest of sensor2 matches with sensor1 shifted once
            if sensor1[index] != sensor2[index + 1]:
                mismatch_sensor2 = True
            # If both sensors have mismatches after shifting, we can't determine the bad one
            if mismatch_sensor1 and mismatch_sensor2:
                return -1
          
            index += 1
      
        # If only sensor1 had mismatches, sensor2 is bad
        if mismatch_sensor1:
            return 2
        # If only sensor2 had mismatches, sensor1 is bad
        elif mismatch_sensor2:
            return 1
        # If there were no mismatches, we cannot determine the bad sensor
        else:
            return -1

# Note: The method name 'badSensor' remains unchanged as requested.
