import json

subj = {}
with open('subj.txt', 'r') as file:
    for line in file:
        sub, lec, pr, lab = line.split()
        subj[sub] = int(lec) + int(pr) + int(lab)
    print(f'Кол-во часов по предмету: \n {subj}')