"""
你现在是一场采用特殊赛制棒球比赛的记录员。这场比赛由若干回合组成，过去几回合的得分可能会影响以后几回合的得分。
比赛开始时，记录是空白的。你会得到一个记录操作的字符串列表 ops，其中 ops[i] 是你需要记录的第 i 项操作，ops 遵循下述规则：
1. 整数 x - 表示本回合新获得分数 x
2. "+" - 表示本回合新获得的得分是前两次得分的总和。题目数据保证记录此操作时前面总是存在两个有效的分数。
3. "D" - 表示本回合新获得的得分是前一次得分的两倍。题目数据保证记录此操作时前面总是存在一个有效的分数。
4. "C" - 表示前一次得分无效，将其从记录中移除。题目数据保证记录此操作时前面总是存在一个有效的分数。
请你返回记录中所有得分的总和。

Not a very difficult question if you know the syntax.
"""

ops = ['0', '1', '+', '+', '+', '+', '+', '+', '+']
record = []
for i in range(len(ops)):
  if ops[i] == 'C':
    record.pop()
  elif ops[i] == 'D':
    record.append(int(record[-1]) * 2)
  elif ops[i] == '+':
    record.append(int(record[-1]) + int(record[-2]))
  else:
    record.append(int(ops[i]))
print(record)
