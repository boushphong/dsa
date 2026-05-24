# Design
Design problems require you to design a data structure or algorithm to solve a specific problem. 
These problems often involve implementing a class or a set of functions that meet certain requirements.

# Patterns
## Brute Force 
When solving design problems, it is often best to begin with a brute-force solution, try every possible logic branch without overcomplicating it.
### Implement a Calendar
```
Given a calendar, you can add 3 types of events
None -> Add an event from `start_hour` to `end_hour` into a day
Daily -> Add an event from `start_hour` to `end_hour` to every day from that day onwards
Weekly -> Add an event from `start_hour` to `end_hour` to every day of the week from that day onwards (eg. 1 8 15 ...)


Implement the class Calendar.
There are 2 main methods that need to be implemented:
- add_event(day, start_hour, end_hour, EventType)
    - Upon adding an event, if there is a conflict then return False, else add the event and return True. Eg: 
        - add 3 -> 5 into 5 -> 7 (NO CONFLICT)
        - add 3 -> 5 into 4 -> 6 (CONFLICT)
        - add 0 -> 23 into 4 -> 6 (CONFLICT)
    
- get_event(day)
    - return all the events in that day, if there are no events on that day, return [] 
    
Constraints:
- 0 <= start_hour <= end_hour <= 23
```

```python
class Calendar:
    def __init__(self):
        self.calendar = []

    def has_conflicts(self, start, end, cal_start, cal_end):
        return max(start, cal_start) < min(end, cal_end)

    def add_event(self, day, start, end, event_type):
        if not event_type:
            for cal_day, cal_start, cal_end, cal_event_type in self.calendar:
                if (
                    not cal_event_type
                    and cal_day == day
                    and self.has_conflicts(start, end, cal_start, cal_end)
                ):
                    return False
                if (
                    cal_event_type == "Daily"
                    and cal_day <= day
                    and self.has_conflicts(start, end, cal_start, cal_end)
                ):
                    return False
                if (
                    cal_event_type == "Weekly"
                    and cal_day <= day
                    and (day - cal_day) % 7 == 0
                    and self.has_conflicts(start, end, cal_start, cal_end)
                ):
                    return False
        elif event_type == "Daily":
            for cal_day, cal_start, cal_end, cal_event_type in self.calendar:
                if (
                    not cal_event_type
                    and cal_day >= day
                    and self.has_conflicts(start, end, cal_start, cal_end)
                ):
                    return False
                if cal_event_type in {"Daily", "Weekly"} and self.has_conflicts(
                    start, end, cal_start, cal_end
                ):
                    return False
        elif event_type == "Weekly":
            for cal_day, cal_start, cal_end, cal_event_type in self.calendar:
                if (
                    not cal_event_type
                    and cal_day >= day
                    and (cal_day - day) % 7 == 0
                    and self.has_conflicts(start, end, cal_start, cal_end)
                ):
                    return False
                if cal_event_type == "Daily" and self.has_conflicts(
                    start, end, cal_start, cal_end
                ):
                    return False
                if (
                    cal_event_type == "Weekly"
                    and (cal_day - day) % 7 == 0
                    and self.has_conflicts(start, end, cal_start, cal_end)
                ):
                    return False

        self.calendar.append((day, start, end, event_type))
        self.calendar.sort()
        return True

    def get_event(self, day):
        events_today = []
        for cal_day, cal_start, cal_end, cal_event_type in self.calendar:
            if cal_day > day:
                break
            if not cal_event_type and cal_day == day:
                events_today.append((cal_start, cal_end))
            elif cal_event_type == "Daily" and cal_day <= day:
                events_today.append((cal_start, cal_end))
            elif cal_event_type == "Weekly" and cal_day <= day and (day - cal_day) % 7 == 0:
                events_today.append((cal_start, cal_end))

        return events_today

cal = Calendar()
print(cal.add_event(10, 13, 18, "Weekly"))  # True
print(cal.add_event(9, 14, 17, "Daily"))  # False
print(cal.add_event(2, 9, 10, "Daily"))  # True
print(cal.add_event(100, 10, 10, None))  # True
print(cal.add_event(100, 20, 21, None))  # True
print(cal.get_event(9))  # [(9, 10)]
print(cal.get_event(10))  # [(9, 10), (13, 18)]
print(cal.get_event(17))  # [(9, 10), (13, 18)]
print(cal.get_event(100))  # [(9, 10), (10, 10), (20, 21)]
```