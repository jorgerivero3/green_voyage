def formatter_helper(time):
    time_as_str = ""
    if time < 60:
        time_as_str = "less than a minute"
    elif time == 60:
        time_as_str = "1 min"
    elif time < 3600:
        time_as_str = str(int(time // 60)) + " mins"
    elif time == 3600:
        time_as_str = "1 hour"
    else:
        time_as_str = str(int(time // 3600)) + " hours"
        
    return time_as_str

def time_formatter(time):
     if time >= 3600:
          remainder = time % 3600
          h_str = formatter_helper(time)
          r_str = formatter_helper(remainder)
          new_str = h_str + " " + r_str
          return new_str
     else:
          return formatter_helper(time)