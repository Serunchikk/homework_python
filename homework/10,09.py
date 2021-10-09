def show(func):
    def new_func(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', kwargs)
        
    return new_func
@show
def initials_PRO(names):
    b = len(names)
    new_names = []
    for i in range(b):
        a,b,c= names[i].split(' ')
        a +=' ' + b[0]+ ' ' + c[0]
        new_names.append(a)
    return new_names


spisok=['Ковтун Степан Ильич ','Меняйло Екатерина Андреевна','Бухтиничева Ксения Геннадьвна','Яцына Леонид Сергеевич','Бабков Никита Алексеевич']

print(initials_PRO(spisok))