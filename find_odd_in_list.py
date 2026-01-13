def find_it(seq):
    for i in seq:
        times_appears = seq.count(i)
        if times_appears % 2 == 1:
            return(i)
    
find_it([0, 1, 1])