original_gravity = 1.050  #input('Введите начальную плотность сусла \n')
time_hop = 60 #input('Введите время кипячения хмеля \n')
alfa_hop = 10 #input('Введите значение альфа-кислоты хмеля \n')
weight_hop = 100000 #input('Введите массу хмеля \n')
weight_malt = 10 #input('Введите массу солода, кг \n')
colour_malt = 7 #input('Введите цветность солода, ЕВС \n')
final_volume_mash = 50 #input('Введите объем сусла после охлаждения \n')


def alcohol(original_gravity, final_gravity):
    ABV = (original_gravity - final_gravity) * 131.25
    return (ABV)


def bitter():
    IBU = (1.65 * 0.000125 ** (original_gravity - 1)) * ((1 - 2.71828**(-0.04 * time_hop)) / 4.15) * (alfa_hop/100 * weight_hop) / final_volume_mash
    return (IBU)

def colour():
    EBC = 1.97 * 1.03 * (weight_malt * colour_malt / final_volume_mash) ** 0.6859
    return (EBC)
