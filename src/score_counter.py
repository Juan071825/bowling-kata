from constants import STRIKE, OPEN_FRAME, FRAMES_KEYS, FRAMES_KEYS_UNTIL_NINE, FIRST_BOWLING, SECOND_BOWLING, THIRD_BOWLING, ONE_BOWLING, TWO_BOWLINGS, THREE_BOWLINGS, SPARE, BOWLING_VALUES_DICT, NINTH_FRAME

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
          
          if frame_key in FRAMES_KEYS_UNTIL_NINE:
                
               
                next_frame = frames_dict[frame_key + 1]
                number_bowlings_next_frame = len(frames_dict[frame_key + 1])
                
                if frame_bowlings[FIRST_BOWLING] == STRIKE:
                    
                    first_frame_bowling_value = BOWLING_VALUES_DICT[frame_bowlings[FIRST_BOWLING]]
                    score_counter += first_frame_bowling_value

                    if number_bowlings_next_frame == ONE_BOWLING:
                            bowlings_next_next_frame = frames_dict[frame_key + 2]
                            score_counter += BOWLING_VALUES_DICT[next_frame[FIRST_BOWLING]] + BOWLING_VALUES_DICT[bowlings_next_next_frame[FIRST_BOWLING]]        

                    elif number_bowlings_next_frame == TWO_BOWLINGS:

                        if next_frame[SECOND_BOWLING] == SPARE:
                              score_counter += BOWLING_VALUES_DICT[next_frame[SECOND_BOWLING]]
                        else:
                              score_counter += BOWLING_VALUES_DICT[next_frame[FIRST_BOWLING]] + BOWLING_VALUES_DICT[next_frame[SECOND_BOWLING]]

                    elif number_bowlings_next_frame == THREE_BOWLINGS:
                            score_counter += BOWLING_VALUES_DICT[next_frame[FIRST_BOWLING]] + BOWLING_VALUES_DICT[next_frame[SECOND_BOWLING]]
                
                elif frame_bowlings[SECOND_BOWLING] == SPARE:
                      score_counter += BOWLING_VALUES_DICT[frame_bowlings[SECOND_BOWLING]] + BOWLING_VALUES_DICT[next_frame[FIRST_BOWLING]]
                
                elif frame_bowlings[FIRST_BOWLING] in OPEN_FRAME:
                      score_counter += BOWLING_VALUES_DICT[frame_bowlings[FIRST_BOWLING]] + BOWLING_VALUES_DICT[frame_bowlings[SECOND_BOWLING]]

          
          else:
                if frame_bowlings[FIRST_BOWLING] == STRIKE:
                      score_counter += BOWLING_VALUES_DICT[frame_bowlings[FIRST_BOWLING]]
                      if frame_bowlings[THIRD_BOWLING] == SPARE:
                            score_counter += BOWLING_VALUES_DICT[frame_bowlings[THIRD_BOWLING]]
                      else:
                            score_counter += BOWLING_VALUES_DICT[frame_bowlings[SECOND_BOWLING]] + BOWLING_VALUES_DICT[frame_bowlings[THIRD_BOWLING]]

                
                elif frame_bowlings[SECOND_BOWLING] == SPARE:
                      score_counter += BOWLING_VALUES_DICT[frame_bowlings[SECOND_BOWLING]] + BOWLING_VALUES_DICT[frame_bowlings[THIRD_BOWLING]]

                      
                elif frame_bowlings[FIRST_BOWLING] in OPEN_FRAME:
                      score_counter += BOWLING_VALUES_DICT[frame_bowlings[FIRST_BOWLING]] + BOWLING_VALUES_DICT[frame_bowlings[SECOND_BOWLING]]
    
    
    
    return score_counter
                      

                      


                   
                        
if __name__ == '__main__':

    assert score_counter(frame_dict_creator('XXXXXXXXXXXX')) == 300
    assert score_counter(frame_dict_creator('1/2/3/4/5/6/7/8/9/1/5')) == 150
    assert score_counter(frame_dict_creator('12121212121212121212')) == 30
    assert score_counter(frame_dict_creator('--------------------')) == 0
    assert score_counter(frame_dict_creator('XXX-----------------')) == 60
    assert score_counter(frame_dict_creator('----------------XXXX')) == 60
    assert score_counter(frame_dict_creator('12345123451234512345')) == 60
    assert score_counter(frame_dict_creator('9-9-9-9-9-9-9-9-9-9-')) == 90
    assert score_counter(frame_dict_creator('9-3561368153258-7181')) == 82
    assert score_counter(frame_dict_creator('9-3/613/815/-/8-7/8-')) == 121
    assert score_counter(frame_dict_creator('X9-9-9-9-9-9-9-9-9-')) == 100
    assert score_counter(frame_dict_creator('X9-X9-9-9-9-9-9-9-')) == 110
    assert score_counter(frame_dict_creator('XX9-9-9-9-9-9-9-9-')) == 120
    assert score_counter(frame_dict_creator('XXX9-9-9-9-9-9-9-')) == 141
    assert score_counter(frame_dict_creator('9-3/613/815/-/8-7/8/8')) == 131
    assert score_counter(frame_dict_creator('5/5/5/5/5/5/5/5/5/5/5')) == 150
    assert score_counter(frame_dict_creator('9-9-9-9-9-9-9-9-9-XXX')) == 111
    assert score_counter(frame_dict_creator('8/549-XX5/53639/9/X')) == 149
    assert score_counter(frame_dict_creator('X5/X5/XX5/--5/X5/')) == 175
