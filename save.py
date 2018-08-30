
    vdir = bomb_dir[0]
    if vdir == "U":
        vmax = y
        y -= int((vmax-vmin)/div)
    elif vdir == "D":
        vmin = y
        y += int((h-(y-vmax))/div)

    hdir = bomb_dir[-1]
    if hdir == "R":
        hmin = x
        x += int((w-(x-hmax))/div)
    elif hdir == "L":
        hmax = x
        x -= int((x-hmin)/div)
