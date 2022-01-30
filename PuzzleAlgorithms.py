## 1. 모두 똑같이 만들기 ##

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

pleaseConform(cap1)

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
s = 'abcabcdede'
# solution(s)