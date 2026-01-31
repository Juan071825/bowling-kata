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

    print(frame_dict_creator('XXXXXXXXXXXX'))
    print(frame_dict_creator('1/2/3/4/5/6/7/8/9/1/5'))
    print(frame_dict_creator('12121212121212121212'))
    print(frame_dict_creator('--------------------'))

    print('-'*60)

    print(score_counter(frame_dict_creator('XXXXXXXXXXXX')))
    print(score_counter(frame_dict_creator('1/2/3/4/5/6/7/8/9/1/5')))
    print(score_counter(frame_dict_creator('12121212121212121212')))
    print(score_counter(frame_dict_creator('--------------------')))
