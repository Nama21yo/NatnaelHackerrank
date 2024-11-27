def meeting_rooms(intervals):
    conference_room = [0] * 10001
    for start, end in intervals:
        conference_room[start] += 1
        conference_room[end] -= 1
    
    running_sum = conference_room[0]
    min_conference = 0
    for i in range(1, len(conference_room)):
        running_sum += conference_room[i]
        min_conference = max(min_conference, running_sum)
    return min_conference
        
        
    
print(meeting_rooms([
  [7, 10],
  [2, 4]
]))