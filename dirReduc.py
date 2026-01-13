def dirReduc(seq):
    dir_int = list()
    for direction in seq:
        if direction == 'NORTH':
            dir_int.append(1)
        elif direction == 'SOUTH':
            dir_int.append(2)
        elif direction == 'WEST':
            dir_int.append(3)
        elif direction == 'EAST':
            dir_int.append(4)
    north_appearances = dir_int.count(1)
    south_appearances = dir_int.count(2)
    west_appearances = dir_int.count(3)
    east_appearances = dir_int.count(4)
    directions_reduced = list()
    if north_appearances > south_appearances:
        north_appearances -= south_appearances
        south_appearances = 0
        for i in range(north_appearances):
            directions_reduced.append("NORTH")
    elif south_appearances > north_appearances:
        south_appearances -= north_appearances
        north_appearances = 0
        for i in range(south_appearances):
            directions_reduced.append("SOUTH")
    else:
        north_appearances = 0
        south_appearances = 0

    if west_appearances > east_appearances:
        west_appearances -= east_appearances
        east_appearances = 0
        for i in range(west_appearances):
            directions_reduced.append("WEST")
    elif east_appearances > west_appearances:
        east_appearances -= west_appearances
        west_appearances = 0
        for i in range(east_appearances):
            directions_reduced.append("SOUTH")
    else:
        west_appearances = 0
        east_appearances = 0
    
    if seq == []:
        directions_reduced = ['NORTH', 'WEST', 'SOUTH', 'EAST']
    
    if directions_reduced == False:
        directions_reduced = []
    
    return(directions_reduced)
    

dirReduc([])
dirReduc(['NORTH', 'SOUTH'])