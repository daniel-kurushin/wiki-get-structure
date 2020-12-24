from utilites import dump, load

sentences = load('intuit_sents.json')
terms = load('intuit_terms.json')

candidates = []
for tokens_a in ( set(x[0]) for x in terms ):
    for tokens_b, n in ( (set(sentences[x]['tokens']), x) for x in sentences):
        if tokens_a & tokens_b: 
            candidates += [(int(n), len(tokens_a & tokens_b) / len(tokens_a), tokens_a & tokens_b)]
            
candidates = sorted(candidates, key=lambda x: x[1], reverse=1)

text = []
used = []
for candidate in candidates:
    if candidate[1] > 0.6:
        i = candidate[0]
        s = sentences[str(i)]
        if i not in used:
            text += [(s['sentence'].replace('\n',' '), i)]
        used += [i]

text = sorted(text, key=lambda x: x[1])

print(" ".join([ x[0] for x in text]))