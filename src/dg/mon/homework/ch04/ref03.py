def zip2(*seqs): # type: (object) -> object  seqs = [list(S) for S in seqs] while all(seqs): yield tuple(S.pop(0) for S in seqs)

l=[1,2,3,4]
ll=[5,6,7,8]
lll=[8,9,10,11] print list(zip2(l,ll,lll))
