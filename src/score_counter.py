def frame_dict_creator(pins_knocked):
    
    tries_bowling = 0
    frames_count = 0
    pins_knocked_list = []
    while tries_bowling < len(pins_knocked):

        # STRIKE
        if pins_knocked[tries_bowling] == "X":
                pins_knocked_list.append(tuple(pins_knocked[tries_bowling]))
                tries_bowling += 1
                frames_count += 1

        # OPEN FRAME O SPARE
        elif pins_knocked[tries_bowling] in "123456789-":
                pins_knocked_list.append((pins_knocked[tries_bowling], pins_knocked[tries_bowling + 1]))
                tries_bowling += 2
                frames_count += 1
    
        # Los lanzamientgos del strike 10 son los que quedan.
        if frames_count == 9:
                pins_knocked_list.append(tuple(pins_knocked[tries_bowling:])) # tuple() crea la tupla separando los caracteres del string.
                pins_knocked_dict = dict(zip((1,2,3,4,5,6,7,8,9,10), pins_knocked_list))
                return pins_knocked_dict



def score_counter(frames_dict):
    score_counter = 0

    dict_values = {'-':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'X':10, '/':10}

    for frame_number, frame_tries in frames_dict.items():
          if frame_number in (1,2,3,4,5,6,7,8,9):
                
                if frame_tries[0] == 'X':
                      score_counter += dict_values[frame_tries[0]]
                      if len(frames_dict[frame_number + 1]) == 2:
                            score_counter += dict_values[frames_dict[frame_number + 1][0]] + dict_values[frames_dict[frame_number + 1][1]]
                      elif len(frames_dict[frame_number + 1]) == 1:
                            score_counter += dict_values[frames_dict[frame_number + 1][0]] + dict_values[frames_dict[frame_number + 2][0]]
                      elif len(frames_dict[frame_number + 1]) == 3:
                            score_counter += dict_values[frames_dict[frame_number + 1][0]] + dict_values[frames_dict[frame_number + 1][1]]
                
                elif frame_tries[1] == '/':
                      score_counter += dict_values[frame_tries[1]] + dict_values[frames_dict[frame_number + 1][0]]
                
                elif frame_tries[0] in ('123456789-'):
                      score_counter += dict_values[frame_tries[0]] + dict_values[frame_tries[1]]

          
          else:
                if frame_tries[0] == 'X':
                      score_counter += dict_values[frame_tries[0]] + dict_values[frame_tries[1]] + dict_values[frame_tries[2]]

                
                elif frame_tries[1] == '/':
                      score_counter += dict_values[frame_tries[1]] + dict_values[frame_tries[2]]

                      
                elif frame_tries[0] in ('123456789-'):
                      score_counter += dict_values[frame_tries[0]] + dict_values[frame_tries[1]]
    
    
    
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
