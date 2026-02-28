import csv
def candidate_elimination(filename):
    with open(filename, 'r') as f:
        data = list(csv.reader(f))
    n = len(data[0]) - 1  
    S = ['0'] * n
    G = [['?'] * n]
    for row in data[1:]:
        x = row[:-1]
        label = row[-1]
        if label == "Yes":  
            for i in range(n):
                if S[i] == '0':
                    S[i] = x[i]
                elif S[i] != x[i]:
                    S[i] = '?'
            G = [g for g in G if all(g[i] == '?' or g[i] == x[i] for i in range(n))]
        
        else:                 
            newG = []
            for g in G:
                for i in range(n):
                    if g[i] == '?':
                        if S[i] != x[i]:
                            h = g.copy()
                            h[i] = S[i]
                            newG.append(h)
            G = newG
    return S, G
filename = input("Enter CSV file name:")
S, G = candidate_elimination(filename)
print("\nFinal Specific Boundary S:")
print(S)
print("\nFinal General Boundary G:")
for g in G:
    print(g)
