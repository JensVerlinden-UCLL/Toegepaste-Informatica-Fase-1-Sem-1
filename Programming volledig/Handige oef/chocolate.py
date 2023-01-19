def make_chocolate(small, big, goal):
  if big * 5 + small >= goal and goal % 5 <= small: 
    if big*5 > goal:
      big = goal // 5
    return goal - (big*5)
  return -1
