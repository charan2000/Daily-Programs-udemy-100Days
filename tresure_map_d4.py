lst = [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
n = int(input())
row = int(n/10)
col = (n-row*10)
print(row, col, n)
lst[row-1][col-1] = 'X'
print(lst)