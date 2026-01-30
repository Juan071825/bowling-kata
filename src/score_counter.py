def score_counter(pins_knocked):
    
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


        
if __name__ == '__main__':
      print(score_counter('XXXXXXXXXXXX'))
      print(score_counter('1/2/3/4/5/6/7/8/9/1/5'))
      print(score_counter('12121212121212121212'))
      