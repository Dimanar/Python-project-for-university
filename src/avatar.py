import pyganim

def create_direct():
    main_direct = '../image/image_part_0'
    result = []
    for x in range(1,81):
        temp = '0'+str(x) if x < 10 else str(x)
        result.append(main_direct+temp+'.png')
    return result

def create_different_moving(direct_image):
    step = 0.1
    cort = []
    result = []
    for x in range(1,81):
        cort.append((direct_image[x-1], step))
        if x % 8 == 0:
            result.append(cort)
            cort = list()
    return [ pyganim.PygAnimation(corteg) for corteg in result ]

direct_image = create_direct()
move = create_different_moving(direct_image)