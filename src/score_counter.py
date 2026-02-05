from src.constants import STRIKE, OPEN_FRAME, FRAMES_KEYS, FRAMES_KEYS_UNTIL_NINE, FIRST_BOWLING, SECOND_BOWLING, THIRD_BOWLING, ONE_BOWLING, TWO_BOWLINGS, THREE_BOWLINGS, SPARE, BOWLING_VALUES_DICT, NINTH_FRAME

def frame_dict_creator(pins_knocked):
    
    bowling_count = 0
    frames_count = 0
    pins_knocked_per_frame = []


    while bowling_count < len(pins_knocked):
        
        current_bowling = pins_knocked[bowling_count]
        next_bowling = pins_knocked[bowling_count + 1]

        # STRIKE
        if pins_knocked[bowling_count] == STRIKE:
            pins_knocked_per_frame.append(tuple(current_bowling))
            bowling_count += 1
            frames_count += 1

        # OPEN FRAME O SPARE
        elif pins_knocked[bowling_count] in OPEN_FRAME:
            pins_knocked_per_frame.append((current_bowling, next_bowling))
            bowling_count += 2
            frames_count += 1
    
        # Los lanzamientgos del strike 10 son los que quedan.
        if frames_count == NINTH_FRAME:
            last_frame_bowlings = pins_knocked[bowling_count:]

            pins_knocked_per_frame.append(tuple(last_frame_bowlings)) # tuple() crea la tupla separando los caracteres del string.
            frames_dict = dict(zip(FRAMES_KEYS, pins_knocked_per_frame))
            return frames_dict



def score_counter(frames_dict):
    
    score_counter = 0
    
    for frame_key, frame_bowlings in frames_dict.items():

          frame_first_bowling_value = BOWLING_VALUES_DICT[frame_bowlings[FIRST_BOWLING]]
          number_bowlings_frame = len(frame_bowlings)
          second_bowling_value = BOWLING_VALUES_DICT[frame_bowlings[SECOND_BOWLING]] if number_bowlings_frame  >= 2 else None
          third_bowling_value = BOWLING_VALUES_DICT[frame_bowlings[THIRD_BOWLING]] if number_bowlings_frame  == 3 else None


          if frame_key in FRAMES_KEYS_UNTIL_NINE:
               
                next_frame = frames_dict[frame_key + 1]
                number_bowlings_next_frame = len(next_frame)
                next_bowling_value = BOWLING_VALUES_DICT[next_frame[FIRST_BOWLING]]
                second_next_bowling_value = BOWLING_VALUES_DICT[next_frame[SECOND_BOWLING]] if number_bowlings_next_frame >= TWO_BOWLINGS else None
                second_next_frame_first_bowling = BOWLING_VALUES_DICT[frames_dict[frame_key + 2][FIRST_BOWLING]] if number_bowlings_next_frame == ONE_BOWLING else None
                

                if frame_bowlings[FIRST_BOWLING] == STRIKE:
                    
                    score_counter += frame_first_bowling_value

                    if number_bowlings_next_frame == ONE_BOWLING:   
                            score_counter += next_bowling_value + second_next_frame_first_bowling

                    elif number_bowlings_next_frame == TWO_BOWLINGS:

                        if next_frame[SECOND_BOWLING] == SPARE:
                              score_counter += second_next_bowling_value
                        else:
                              score_counter += next_bowling_value + second_next_bowling_value

                    elif number_bowlings_next_frame == THREE_BOWLINGS:
                            score_counter += next_bowling_value + second_next_bowling_value
                
                elif frame_bowlings[SECOND_BOWLING] == SPARE:
                      score_counter += second_bowling_value + next_bowling_value
                
                elif frame_bowlings[FIRST_BOWLING] in OPEN_FRAME:
                      score_counter += frame_first_bowling_value + second_bowling_value

          
          else:
                if frame_bowlings[FIRST_BOWLING] == STRIKE:
                      score_counter += frame_first_bowling_value
                      if frame_bowlings[THIRD_BOWLING] == SPARE:
                            score_counter += third_bowling_value
                      else:
                            score_counter += second_bowling_value + third_bowling_value

                
                elif frame_bowlings[SECOND_BOWLING] == SPARE:
                      score_counter += second_bowling_value + third_bowling_value

                      
                elif frame_bowlings[FIRST_BOWLING] in OPEN_FRAME:
                      score_counter += frame_first_bowling_value + second_bowling_value
    
    
    
    return score_counter
