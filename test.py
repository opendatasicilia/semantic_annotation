from annotator import annotate_act

file = open('prova.txt', 'r')
text = file.read()

output = []

for annotation in annotate_act(text):
    print(annotation)
