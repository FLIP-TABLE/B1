from random import randint

infamy = ['Terrible', 'Peculiar', 'Eternal', 'Horrible', 'Inexperienced', 'Unworthy', 'Complacent', 'Immoral', 'Hideous', 'Inexpressible']
title= ['Miss', 'Mister', 'King', 'Queen', 'Prince', 'Princess', 'Count', 'Maid', 'Master', 'Madame']
first = ['Tabby', 'Caden', 'Kaarina', 'Xandra', 'Viktor', 'Eadric', 'Hades', 'Hadley', 'Jackie', 'Percy']
last = ['Smith', 'Brown', 'Almond', 'Pelletier', 'Upchurch', 'Xiong', 'Zamora', 'Ybarra', 'Finley', 'Franx']
origin = ['Mt. Doom', 'Hell', 'Helsinki', 'the Shire', 'River-Heights', 'R\'Lyeh', 'Santa Theresa', 'Yian', 'Trantor', 'Magrathea', 'Hogsmeade']


infamy_ = infamy[randint(0, len(infamy)-1)]
title_ = title[randint(0, len(title)-1)]
first_ = first[randint(0, len(first)-1)]
last_ = last[randint(0, len(last)-1)]
origin_ = origin[randint(0, len(origin)-1)]

print('The %s %s %s %s from %s' % (infamy_, title_, first_, last_, origin_))
