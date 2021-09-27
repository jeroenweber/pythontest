def board(rows,cols):
    table = (rows*cols-1)*[''] + ['B']
    print(table)

rows = eval(input('geef aantal rijen: '))
cols = eval(input('geef aantal kols: '))
board(rows,cols)
