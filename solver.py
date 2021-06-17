#!/usr/bin/python

sudoku1 = [
   [7,0,9,0,0,0,3,1,5], 
   [0,4,6,3,0,1,0,0,9], 
   [3,0,1,5,0,2,4,0,0],
   [8,0,0,0,4,5,9,0,2],
   [0,0,7,6,2,3,1,0,0],
   [4,0,2,9,8,0,0,0,3],
   [0,0,5,8,0,6,7,0,4],
   [1,0,0,2,0,9,5,8,0],
   [6,3,8,0,0,0,2,0,1]
] # solved
sudoku2 = [
   [3,0,0,9,0,8,5,0,0], 
   [2,1,0,4,0,7,0,0,6], 
   [9,8,0,0,0,0,0,0,0],
   [7,0,0,0,0,0,6,4,3],
   [4,3,0,0,7,6,0,5,0],
   [6,9,8,0,0,0,0,0,1],
   [0,0,0,0,0,9,1,0,5],
   [0,0,0,0,0,5,3,2,4],
   [0,0,6,2,0,3,0,0,8]
] # solved
#medium
sudoku3 = [
   [3,0,2,0,0,0,0,0,0],
   [4,7,5,9,0,0,2,0,0],
   [0,1,0,8,0,4,0,5,0],
   [0,0,3,0,5,0,0,0,7],
   [0,2,7,0,0,1,0,0,9],
   [8,0,4,0,0,2,0,3,0],
   [0,0,0,0,0,0,0,6,0],
   [2,0,9,0,7,3,0,8,5],
   [0,0,0,0,9,0,0,0,0],
] # solved
#hard
sudoku4 = [
   [0,0,0,0,0,1,6,0,0],
   [0,0,5,0,0,0,0,0,3],
   [0,0,0,0,0,0,5,9,4],
   [0,8,0,0,6,0,0,0,1],
   [0,1,0,0,0,4,9,0,2],
   [4,9,0,1,8,0,0,0,0],
   [0,2,0,4,0,6,1,0,0],
   [0,0,0,0,5,3,2,0,0],
   [7,0,0,0,0,8,0,6,0],
] # solved
#hard
sudoku5 = [
   [0,0,0,7,0,6,0,0,0],
   [0,0,9,0,3,0,0,0,2],
   [0,6,0,9,0,0,0,0,1],
   [0,0,5,0,1,0,4,0,0],
   [0,0,6,0,0,0,7,0,0],
   [0,3,0,0,7,4,8,0,0],
   [8,0,0,0,9,0,1,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,3,0,4,0,0,0,5],
] # solved
sudoku6 = [
   [0,0,0,7,0,6,0,0,0],
   [0,0,9,0,3,0,0,0,2],
   [0,6,0,9,0,0,0,0,1],
   [0,0,5,0,1,0,4,0,0],
   [0,0,6,0,0,0,7,0,0],
   [0,3,0,0,7,4,8,0,0],
   [8,0,0,0,9,0,1,0,0],
   [0,0,0,0,6,0,0,0,0],
   [6,0,3,0,4,0,0,0,5],
] # solved

# expert
sudoku7 = [
   [2,1,0,0,6,0,0,0,0], # [2,1,0,0,6,4,0,0,0],
   [0,3,0,0,0,0,0,0,0],
   [6,0,0,0,0,0,4,9,7],
   [0,0,0,0,0,0,3,0,4],
   [0,0,0,0,0,9,0,6,0],
   [0,7,3,0,5,0,8,0,0],
   [5,0,0,4,0,7,9,0,1],
   [0,0,2,0,1,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
]
sudoku8 = [
   [0,0,0,0,7,2,9,0,4],
   [6,0,0,8,0,0,0,0,0],
   [0,2,0,5,0,0,0,0,3],
   [0,0,5,0,0,0,0,0,0],
   [0,0,0,0,1,0,0,0,0],
   [0,7,4,0,2,0,0,0,1],
   [0,0,3,0,8,4,0,0,0],
   [0,0,8,3,0,0,7,0,0],
   [0,0,6,0,0,0,0,0,2],
] # solved
sudoku9 = [
   [0,8,2,0,5,0,0,0,0],
   [0,0,3,2,0,0,0,0,4],
   [0,0,0,8,0,0,0,0,0],
   [9,0,0,0,1,6,0,0,0],
   [4,0,0,0,0,0,0,3,0],
   [0,5,0,0,0,0,0,0,1],
   [0,0,0,9,0,5,4,0,0],
   [0,0,0,0,0,0,2,8,3],
   [0,0,0,0,0,7,5,0,0],
] # solved
sudoku10 = [
   [0,0,8,0,0,0,4,0,5],
   [0,0,0,0,0,0,0,7,0],
   [6,0,2,0,3,0,9,0,0],
   [7,0,0,0,0,6,0,0,3],
   [0,1,0,0,0,0,0,0,0],
   [0,0,0,1,0,0,0,2,0],
   [0,3,0,0,5,0,7,4,0],
   [0,9,0,7,0,0,6,0,0],
   [0,0,0,0,9,1,0,0,0],
] # solved
sudoku11 = [
   [2,1,0,0,6,0,5,0,0],
   [0,3,0,0,0,0,0,0,0],
   [6,0,0,0,0,0,4,9,7],
   [0,0,0,0,0,0,3,0,4],
   [0,0,0,0,0,9,0,6,0],
   [0,7,3,0,5,0,8,0,9],
   [5,0,0,4,0,7,9,0,1],
   [0,0,2,0,1,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
]



sudoku_test = [
   [2,1,0,0,6,4,5,0,0], # [2,1,0,0,6,4,0,0,0],
   [0,3,0,0,0,0,0,0,0],
   [6,0,0,0,0,0,4,9,7],
   [0,0,0,0,0,0,3,0,4],
   [0,0,0,0,0,9,0,6,0],
   [0,7,3,0,5,0,8,0,9],
   [5,0,0,4,0,7,9,0,1],
   [0,0,2,0,1,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
]

anja1 = [
   [0,0,0,5,0,0,0,2,7],
   [0,0,0,1,9,7,0,8,3],
   [0,0,0,0,4,2,0,1,5],
   [0,0,0,0,0,0,1,3,2],
   [0,2,6,7,0,0,5,9,8],
   [0,8,3,2,0,0,7,6,4],
   [3,5,4,0,2,0,8,7,1],
   [0,6,0,8,5,1,3,4,9],
   [0,0,0,0,7,0,2,5,6],
]
anja2 = [
   [0,0,0,5,0,0,0,0,0],
   [0,0,0,0,9,0,0,8,3],
   [0,0,0,0,4,2,0,0,5],
   [0,0,0,0,0,0,1,3,0],
   [0,2,6,7,0,0,0,0,8],
   [0,8,0,2,0,0,7,0,0],
   [3,0,4,0,0,0,8,0,1],
   [0,6,0,8,5,0,0,4,0],
   [0,0,0,0,0,0,2,0,0],
]

sudoku_to_solve = sudoku_test

def sudokuNumbers():
   return [1, 2, 3, 4, 5, 6, 7, 8, 9]

def containedInColumn(sudoku, c, number):
   for x in range(0, 9):
      if sudoku[x][c] == number:
         return True
   return False

def containedInLine(sudoku, l, number):

   return number in sudoku[l]

def containedInGrid(sudoku, l, c, number):
   start_l = getStartOfGrid(l)
   start_c = getStartOfGrid(c)
   for ll in range(start_l, start_l+3):
      for cc in range(start_c, start_c+3):
         if sudoku[ll][cc] == number:
            return True
   return False

def getStartOfGrid(x):
   while x % 3 != 0:
      x -= 1
   return x

def getSolvedNumbersCount(sudoku):
   i = 0
   for l in sudoku:
      for c in l:
         if c != 0:
            i += 1
   return i

def isSolved(sudoku):
   for i in range(0, 9):
      if len(getMissingNumbersForLine(sudoku, i)) > 0 or len(getMissingNumbersForCol(sudoku, i)) > 0:
         return False

   return getSolvedNumbersCount(sudoku) == 81

def printSudoku(sudoku, withZero = False):
   print('-' * 23)
   i = 0
   for line in sudoku:
      j = 0
      l = '|'
      for col in line:
         l += ('.' if col == 0 and not withZero else str(col)) + '|'
         j += 1
         if j == 3 or j == 6:
            l += ' |'
      print(l)
      i += 1
      if i == 3:
         print('-' * 23)
         i = 0

def getMissingNumbersForLine(sudoku, l):
   numbers = sudokuNumbers()
   for c in sudoku[l]:
      if c in numbers:
         numbers.remove(c)
   return numbers

def getMissingNumbersForCol(sudoku, c):
   numbers = sudokuNumbers()
   for l in range(0, 9):
      if sudoku[l][c] in numbers:
         numbers.remove(sudoku[l][c])
   return numbers

def getMissingNumbersForGrid(sudoku, l, c):
   numbers = sudokuNumbers()
   l = getStartOfGrid(l)
   c = getStartOfGrid(c)
   for ll in range(l, l+3):
      for cc in range(c, c+3):
         if sudoku[ll][cc] in numbers:
            numbers.remove(sudoku[ll][cc])
   return numbers

def copySudoku(s):
   sudoku = []
   for i in range(0, 9):
      line = []
      for j in range(0, 9):
         line.append(s[i][j])
      sudoku.append(line)
   return sudoku

def minimize(s):
   sudoku = copySudoku(s)
   for l in range(0, 9):
      for c in range(0, 9):
         test = copySudoku(sudoku)
         test[l][c] = 0

         if getSolvedNumbersCount(solve(test)) == getSolvedNumbersCount(solve(sudoku)):
            sudoku = test

   return sudoku

def reservedInColumn(sudoku, c):
   # TODO
   return []


def reverseSudoku(sudoku):
   rev = copySudoku(sudoku)
   for l in range(0, 9):
      for c in range(0, 9):
         rev[l][c] = sudoku[c][l]
   return rev

def checkRelatedVerticalGrids(sudoku, lCheck, cCheck, numberCheck):
   '''returns wheter the number to check can be removed from this position'''

   for _l in range(0, 3):
      l = _l * 3

      c = getStartOfGrid(cCheck)
      if l != getStartOfGrid(lCheck):
         # l and c is start of grid to check
         missingNumbersInGrid = getMissingNumbersForGrid(sudoku, l, c)

         possibleMissingNumberPositions = {}
         for missingNumber in missingNumbersInGrid:
            possiblePositions = []
            for ll in range(l, l+3):
               for cc in range(c, c+3):
                  if sudoku[ll][cc] == 0 and not containedInLine(sudoku, ll, missingNumber) and not containedInColumn(sudoku, cc, missingNumber):
                     possiblePositions.append(str(ll) + str(cc))
            possibleMissingNumberPositions[missingNumber] = possiblePositions

         if len(possibleMissingNumberPositions) > 1:
            redo = True
            while redo:
               redo = False
               for k1 in possibleMissingNumberPositions:
                  for k2 in possibleMissingNumberPositions:
                     if k1 != k2 and len(possibleMissingNumberPositions[k1]) == 2 and possibleMissingNumberPositions[k1] == possibleMissingNumberPositions[k2]:
                        for k3 in possibleMissingNumberPositions:
                           if k3 != k1 and k3 != k2:
                              for reserved in possibleMissingNumberPositions[k1]:
                                 if reserved in possibleMissingNumberPositions[k3]:
                                    possibleMissingNumberPositions[k3].remove(reserved)
                                    redo = True
         
         if numberCheck in possibleMissingNumberPositions and len(possibleMissingNumberPositions[numberCheck]) > 1:
            tmp = [item[1] for item in possibleMissingNumberPositions[numberCheck]]
            allSameColumn = len(set(tmp)) == 1
            if allSameColumn and int(tmp[0]) == cCheck:
               return True

   return False

def doLines(sudoku):
   somethingChanged = True
   while not isSolved(sudoku) and somethingChanged:
      somethingChanged = False

      for l in range(0, 9):
         for missingNumber in getMissingNumbersForLine(sudoku, l):
            possiblePositions = []
            for c in range(0, 9):
               if sudoku[l][c] == 0 and not containedInColumn(sudoku, c, missingNumber) and not containedInGrid(sudoku, l, c, missingNumber):
                  possiblePositions.append(c)

            # remove reserved places
            positionsToRemove = []
            for possiblePositionC in possiblePositions:
               missingNumbersInC = getMissingNumbersForCol(sudoku, possiblePositionC)
               if checkRelatedVerticalGrids(sudoku, l, possiblePositionC, missingNumber):
                  positionsToRemove.append(possiblePositionC)
               
            for n in positionsToRemove:
               possiblePositions.remove(n)

            if len(possiblePositions) == 1:
               sudoku[l][possiblePositions[0]] = missingNumber
               somethingChanged = True
               print('change on line' + ('(#)' if len(positionsToRemove) > 0 else ''), '[' + str(l) + '|' + str(possiblePositions[0]) + '] =', missingNumber)

   return sudoku

def _doColumns(sudoku): 
   return reverseSudoku(doLines(reverseSudoku(sudoku)))

def doColumns(sudoku):
   somethingChanged = True
   while not isSolved(sudoku) and somethingChanged:
      somethingChanged = False

      for c in range(0, 9):
         for missingNumber in getMissingNumbersForCol(sudoku, c):
            possiblePositions = []
            for l in range(0, 9):
               if sudoku[l][c] == 0 and not containedInLine(sudoku, l, missingNumber) and not containedInGrid(sudoku, l, c, missingNumber):
                  possiblePositions.append(l)

            if len(possiblePositions) == 1:
               sudoku[possiblePositions[0]][c] = missingNumber
               somethingChanged = True
               print('change on col', '[' + str(possiblePositions[0]) + '|' + str(c) + '] =', missingNumber)

   return sudoku

def doGrid(sudoku):
   somethingChanged = True
   while not isSolved(sudoku) and somethingChanged:
      somethingChanged = False

      for _l in range(0, 3):
         l = _l * 3
         for _c in range(0, 3):
            c = _c * 3

            for missingNumber in getMissingNumbersForGrid(sudoku, l, c):
               possiblePositions = []
               for ll in range(l, l+3):
                  for cc in range(c, c+3):
                     if sudoku[ll][cc] == 0 and not containedInLine(sudoku, ll, missingNumber) and not containedInColumn(sudoku, cc, missingNumber):
                        possiblePositions.append([ll, cc])

               if len(possiblePositions) == 1:
                  sudoku[possiblePositions[0][0]][possiblePositions[0][1]] = missingNumber
                  somethingChanged = True
                  print('change on grid', '[' + str(possiblePositions[0][0]) + '|' + str(possiblePositions[0][1]) + '] =', missingNumber)

   return sudoku

def doReservedPlaces2Combo(sudoku):
   somethingChanged = True
   while not isSolved(sudoku) and somethingChanged:
      somethingChanged = False

      for _l in range(0, 3):
         l = _l * 3
         for _c in range(0, 3):
            c = _c * 3

            possibleMissingNumberPositions = {}
            for missingNumber in getMissingNumbersForGrid(sudoku, l, c):
               possiblePositions = []
               for ll in range(l, l+3):
                  for cc in range(c, c+3):
                     if ll < 9 and cc < 9 and sudoku[ll][cc] == 0 and not containedInLine(sudoku, ll, missingNumber) and not containedInColumn(sudoku, cc, missingNumber):
                        possiblePositions.append(str(ll) + str(cc))
               possibleMissingNumberPositions[missingNumber] = possiblePositions

            # print('before processing')
            # for key in possibleMissingNumberPositions:
            #    print(key, ':', possibleMissingNumberPositions[key])
            if len(possibleMissingNumberPositions) > 1:
               redo = True
               while redo:
                  redo = False
                  for k1 in possibleMissingNumberPositions:
                     for k2 in possibleMissingNumberPositions:
                        # if k1 != k2 and len(possibleMissingNumberPositions[k1]) > 2 and possibleMissingNumberPositions[k1] == possibleMissingNumberPositions[k2]:
                        # == 2 because only two keys (k1, k2) are compared
                        if k1 != k2 and len(possibleMissingNumberPositions[k1]) == 2 and possibleMissingNumberPositions[k1] == possibleMissingNumberPositions[k2]:
                           for k3 in possibleMissingNumberPositions:
                              if k3 != k1 and k3 != k2:
                                 for reserved in possibleMissingNumberPositions[k1]:
                                    if reserved in possibleMissingNumberPositions[k3]:
                                       possibleMissingNumberPositions[k3].remove(reserved)
                                       redo = True



               # print('after processing')
               # for key in possibleMissingNumberPositions:
               #    print(key, ':', possibleMissingNumberPositions[key])
               for possiblePositionKey in possibleMissingNumberPositions:
                  # print(possiblePositionKey, possibleMissingNumberPositions[possiblePositionKey])
                  if len(possibleMissingNumberPositions[possiblePositionKey]) == 1:
                     __l = int(possibleMissingNumberPositions[possiblePositionKey][0][0])
                     __c = int(possibleMissingNumberPositions[possiblePositionKey][0][1])

                     # if possiblePositionKey == 5:
                        # print('=========== overwriting')
                        # for key in possibleMissingNumberPositions:
                        #    print(key, ':', possibleMissingNumberPositions[key])

                     sudoku[__l][__c] = possiblePositionKey
                     somethingChanged = True
                     print('change on reserved', '[' + str(__l) + '|' + str(__c) + '] =', possiblePositionKey)

            # print ('-' * 20)

   return sudoku

def doRemainingPlacesOfGrid(sudoku):
   somethingChanged = True
   while not isSolved(sudoku) and somethingChanged:
      somethingChanged = False

      for _l in range(0, 3):
         l = _l * 3
         for _c in range(0, 3):
            c = _c * 3

            possibleMissingNumberPositions = {}
            for missingNumber in getMissingNumbersForGrid(sudoku, l, c):
               possiblePositions = []
               for ll in range(l, l+3):
                  for cc in range(c, c+3):
                     # TODO
                     if ll < 9 and cc < 9 and sudoku[ll][cc] == 0 and not containedInLine(sudoku, ll, missingNumber) and not containedInColumn(sudoku, cc, missingNumber):
                        possiblePositions.append(str(ll) + str(cc))
               possibleMissingNumberPositions[missingNumber] = possiblePositions


            allPositions = []
            for key in possibleMissingNumberPositions:
               for position in possibleMissingNumberPositions[key]:
                  allPositions.append(position)
            
            for position in allPositions:
               if allPositions.count(position) == 1:
                  for key in possibleMissingNumberPositions:
                     if position in possibleMissingNumberPositions[key]:
                        __l = int(position[0])
                        __c = int(position[1])
                        sudoku[__l][__c] = key
                        somethingChanged = True
                        print('change on remainingPlacesOfGrid', '[' + str(__l) + '|' + str(__c) + '] =', key)

   return sudoku

def bruteForce(sudoku):
   print('$$$ brute forcing')
   tries = 0
   for l in range(0, 9):
      for c in range(0, 9):
         if sudoku[l][c] == 0:
            for n in range(1, 10):
               tries += 1
               print('$$$ try', tries)
               test = copySudoku(sudoku)
               test[l][c] = n
               printSudoku(test)
               test = solve(test, False)
               if isSolved(test):
                  return test
   return sudoku

def solve(sudoku, withBruteForce=True):
   loopCount = 0
   previousSolvedCount = 0
   while previousSolvedCount != getSolvedNumbersCount(sudoku):
      previousSolvedCount = getSolvedNumbersCount(sudoku)

      sudoku, loopCount = _solve(sudoku, loopCount)
      if not isSolved(sudoku):
         print('### reversing')
         sudoku, loopCount = _solve(reverseSudoku(sudoku), loopCount)
         sudoku = reverseSudoku(sudoku)

   if withBruteForce and not isSolved(sudoku):
      sudoku = bruteForce(sudoku)

   return sudoku

def _solve(s, loopCount):
   sudoku = copySudoku(s)

   previousSolvedCount = 0
   while previousSolvedCount != getSolvedNumbersCount(sudoku):
      previousSolvedCount = getSolvedNumbersCount(sudoku)
      loopCount += 1
      print('### loop', loopCount)
      sudoku = doLines(sudoku)
      # sudoku = doColumns(sudoku)
      sudoku = doGrid(sudoku)
      sudoku = doReservedPlaces2Combo(sudoku)
      sudoku = doRemainingPlacesOfGrid(sudoku)

   return sudoku, loopCount

def main():
   # sudoku = sudoku4
   sudoku = sudoku_to_solve

   print('Original (' + str(getSolvedNumbersCount(sudoku)) + ')', ('Solved!' if isSolved(sudoku) else 'Not solved!'))
   printSudoku(sudoku)

   print('\n')

   # minimized = minimize(sudoku)
   # print('Minimized (' + str(getSolvedNumbersCount(minimized)) + ')')
   # if getSolvedNumbersCount(minimized) < getSolvedNumbersCount(sudoku):
   #    printSudoku(minimized)


   solved = solve(sudoku, True)
   print('')

   print('Result (' + str(getSolvedNumbersCount(solved)) + ')', ('Solved!' if isSolved(solved) else 'Not solved!'))
   printSudoku(solved)

if __name__ == '__main__':
   main()
