

def score_counter(pins_knocked):
    total_frames = range(1,11)
    
    try_bowling_count = 0
    pins_knocked_list = []
    while try_bowling_count < len(pins_knocked):
        
        if pins_knocked[try_bowling_count] in range(1,10) or ("-", "/"):
                pins_knocked_list.append((pins_knocked[try_bowling_count], pins_knocked[try_bowling_count] + 1))
                try_bowling_count += 2

        elif pins_knocked[try_bowling_count] == "X":
                pins_knocked_list.append((pins_knocked[try_bowling_count]))
                try_bowling_count += 1
        
    
    
    frames_dict = {zip(total_frames, pins_knocked_list)}
