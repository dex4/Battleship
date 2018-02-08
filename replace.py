import random

def getIndex(dim, matrix, colour):
    valid = False
    orientation = random.choice(["v", "h"])
    if(orientation == "v"):
        half = random.choice(["up", "down"])
    else:
        half = random.choice(["left", "right"])
    for i in range(0, 8):
        for j in range(0, 8):
            matrix[i].append(0)
    i = -1
    j = -1
    if(orientation == "v"):
        j = random.randint(0, 7)
        if(half == "up"):
            i = random.randint(0, 7-dim+1)
            while(valid == False):
                valid = True
                for x in range(i, i+dim):
                    if(matrix[x][j]["fg"] != "black"):
                        valid = False
                if(valid == True):
                    for x in range(i, i+dim):
                        matrix[x][j]["fg"] = colour
                else:
                    i = random.randint(0, 7-dim+1)
        else:
            i = random.randint(dim-1, 7)
            while(valid == False):
                valid = True
                for x in range(i-dim+1, i+1):
                    if(matrix[x][j]["fg"] != "black"):
                        valid = False
                if(valid == True):
                    for x in range(i-dim+1, i+1):
                        matrix[x][j]["fg"] = colour
                else:
                    i = random.randint(dim-1, 7)
    else:
        i = random.randint(0, 7)
        if(half == "left"):
            j = random.randint(0, 7-dim+1)
            while(valid == False):
                valid = True
                for x in range(j, j+dim):
                    if(matrix[i][x]["fg"] != "black"):
                        valid = False
                if(valid == True):
                    for x in range(j, j+dim):
                        matrix[i][x]["fg"] = colour
                else:
                    j = random.randint(0, 7-dim+1)
        else:
            j = random.randint(dim, 7)
            while(valid == False):
                valid = True
                for x in range(j-dim+1, j+1):
                    if(matrix[i][x]["fg"] != "black"):
                        valid = False
                if(valid == True):
                    for x in range(j-dim+1, j+1):
                        matrix[i][x]["fg"] = colour
                else:
                    j = random.randint(dim, 7)
    return matrix
