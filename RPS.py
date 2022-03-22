history_table = {}

def player(prev_play, opponent_history=[]):

  # number of plays saved in memory
  n = 3

  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  guess = "R"

  if len(opponent_history)>n:
    inp = "".join(opponent_history[-n:])

    if "".join(opponent_history[-(n+1):]) in history_table.keys():
      history_table["".join(opponent_history[-(n+1):])]+=1
    else:
      history_table["".join(opponent_history[-(n+1):])]=1

    possible =[inp+"R", inp+"P", inp+"S"]

    for i in possible:
      if not i in history_table.keys():
        history_table[i] = 0

    predict = max(possible, key=lambda key: history_table[key])

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    guess = ideal_response[predict[-1]]


  return guess