########################
## 1. 모두 똑같이 만들기 ##
########################
# 바꾸어야 할 배열의 순서 찾기

cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']

# F와 B 중 더 많은 수로 통일 시키기

def pleaseConform(caps):
  start = forward = backward = 0
  intervals = []
  # caps = caps + ['END']
  for i in range(1, len(caps)):
    if caps[start] != caps[i]:
      intervals.append([start, i - 1, caps[start]])
      if caps[start] == 'F':
        forward += 1
      else:
        backward += 1
      start = i
      print(i, intervals, forward, backward)
  # intervals.append((start, len(caps)-1, caps[start]))
  # if caps[start] == 'F':
  #   forward += 1
  # else:
  #   backward += 1
  if forward < backward:
    flip = 'F'
  else:
    flip = 'B'
  for t in intervals:
    if t[2] == flip:
      if t[0] == t[1]:
        print('Person at position', t[0], 'flip your cap!')
      else:
        print('People in positions', t[0], 'through', t[1], 'flip your caps!')
    print(t[0:])

# pleaseConform(cap1)

# 리스트에 + [] 배열로 추가하는 방법은 기존 리스트에 변화를 주지 않는다.
def listConcatenate(caps):
  caps = caps + ['END']
  print(caps)

capA = ['F', 'F', 'B']
# listConcatenate(capA)
# print(capA)

# 리스트에 append 함수를 사용하여 추가하는 방법은 기존 리스트에 변화를 준다.
def listAppend(caps):
  caps.append('END')
  print(caps)

# listAppend(capA)
# print(capA)

## 알고리즘 최적화하기 ##
## F가 F를 만나지 않았을 때 첫 번째 수를 얻고 다시 F를 만났을 때 i-1을 얻어 변경 ##

def pleasConformOnepass(caps):
  caps = caps + [caps[0]]
  for i in range(1, len(caps)):
    if caps[i] != caps[i-1]:
      if caps[i] != caps[0]:
        print('People in positions', i, end = '')
      else:
        print(' through', i-1, 'flip your caps!')

# pleasConformOnepass(cap1)

## 1-1. 압축 알고리즘 ##
data = 'WWWWWWWWWWWWWBBWWWWWWWWWWWWBBBBB'
encoded = ''

count = 1
for i in range(1, len(data)):
  if data[i] == data[i-1]:
    count += 1
  else:
    encoded += str(count) + data[i-1]
    count = 1

  if i == len(data) - 1:
    encoded += str(count) + data[i]

# print(encoded)

## 1-2. 압축 알고리즘 ##
## 몇 개씩 분리하여 압축하는 것이 가장 짧은지 ##
def solution(s):
  result = []
  if len(s) == 1:
    return 1
  for i in range(1, (len(s) // 2) + 1):
    b = ''
    cnt = 1
    tmp = s[:i]

    for j in range(i, len(s), i):
      if tmp == s[j:i+j]:
        cnt += 1
      else:
        if cnt != 1:
          b = b + str(cnt) + tmp
        else:
          b = b + tmp
        tmp = s[j:j+1]
        cnt = 1
    if cnt != 1:
      b = b + str(cnt) + tmp
    else:
      b = b + tmp

    result.append(len(b))
  return print(result)

# s = 'ababcdcdababcdcd'
# s = 'abcabcdede'
# solution(s)

##################################
## 2. 파티에 참석하기 가장 좋은 시간 ##
##################################
# 가장 중복이 많은 시간 찾기

sched =  [(6, 8), (6, 12), (6, 7), (7, 8),
          (7, 10), (8, 9), (8, 10), (9, 12),
          (9, 10), (10, 11), (10, 12), (11, 12)]

sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]

def bestTimeToParty(schedule):
  start = schedule[0][0]
  end = schedule[0][1]
  for c in schedule:
    start = min(c[0], start)
    end = max(c[1], end)
  count = celebrityDensity(schedule, start, end)
  # print(start, end, c[0:], count)
  # maxcount = 0
  # for i in range(start, end + 1):
  #   if count[i] > maxcount:
  #     maxcount = count[i]
  #     time = i
  # 위 주석부분 변경가능
  maxcount = max(count[start:end + 1])
  time = count.index(maxcount)
  # print(maxcount, time)
  print('Best time to attend the party is at',
    time, 'o\'clock', ':', maxcount, 'celebrities will be attending!')

def celebrityDensity(sched, start, end):
  count = [0] * (end + 1)
  for i in range(start, end + 1):
    count[i] = 0
    for c in sched:
      if c[0] <= i and c[1] > i:
        count[i] += 1
        # print(count[i], end = ' ')
        # print(count)
  return count

bestTimeToParty(sched)

def bestTimeToPartySmart(schedule):
  times = []
  for c in schedule:
    times.append((c[0], 'start'))
    times.append((c[1], 'end'))
  sortList(times)
  maxcount, time = chooseTime(times)
  print('Best time to attend the party is at',
    time, 'o\'clock', ':', maxcount, 'celebrities will be attending!')

def sortList(tlist):
  for ind in range(len(tlist)-1):
    iSm = ind
    for i in range(ind, len(tlist)):
      if tlist[iSm][0] > tlist[i][0]:
        iSm = i
    tlist[ind], tlist[iSm] = tlist[iSm], tlist[ind]
  return

def chooseTime(times):

  rcount = 0
  maxcount = 0
  time = 0

  for t in times:
    if t[1] == 'start':
      rcount = rcount + 1
    elif t[1] == 'end':
      rcount = rcount - 1
    if rcount > maxcount:
      maxcount = rcount
      time = t[0]

  return maxcount, time

bestTimeToPartySmart(sched2)