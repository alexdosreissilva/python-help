# coding=UTF-8

import collections

#def conta_ocorrencias(s):
#    ocorrencias = {}
#    for c in s:
#        if c in ocorrencias:
#            ocorrencias[c] += 1
#        else:
#            ocorrencias[c] = 1
#    return ocorrencias

def conta_ocorrencias(s):
    ocorrencias = collections.defaultdict(int)
    for c in s:
        ocorrencias[c] += 1
    return ocorrencias
 
s = "               "
c = collections.Counter(s)
print(c.most_common(5))
