cogFunc = {
    'INTJ':['Ni', 'Te', 'Fi', 'Se'],
    'INTP':['Ti', 'Ne', 'Si', 'Fe'],
    'ENTJ':['Te', 'Ni', 'Se', 'Fi'],
    'ENTP':['Ne', 'Ti', 'Fe', 'Si'],

    'INFJ':['Ni', 'Fe', 'Ti', 'Se'],
    'INFP':['Fi', 'Ne', 'Si', 'Te'],
    'ENFJ':['Fe', 'Ni', 'Se', 'Ti'],
    'ENFP':['Ne', 'Fi', 'Te', 'Si'],

    'ISTJ':['Si', 'Te', 'Fi', 'Ne'],
    'ISFJ':['Si', 'Fe', 'Ti', 'Ne'],
    'ESTJ':['Te', 'Si', 'Ne', 'Fi'],
    'ESFJ':['Fe', 'Si', 'Ne', 'Ti'],

    'ISTP':['Ti', 'Se', 'Ni', 'Fe'],
    'ISFP':['Fi', 'Se', 'Ni', 'Ti'],
    'ESTP':['Se', 'Ti', 'Fe', 'Ni'],
    'ESFP':['Se', 'Fi', 'Te', 'Ni']
}

functions = ['Ne', 'Ni', 'Se', 'Si', 'Te', 'Ti', 'Fe', 'Fi']

axis = {
    'Ni':'Se',
    'Ne':'Si',
    'Se':'Ni',
    'Si':'Ne',

    'Fi':'Te',
    'Fe':'Ti',
    'Ti':'Fe',
    'Te':'Fi'
    }

func_multiplier = [0.5, 1, 2, 4]
precision = 0.9

def createPointMap(inp_score):
    a = inp_score
    points = [float(i) for i in a]

    pointMap = {}
    for i in range(8):
        pointMap[functions[i]] = points[i]

    return pointMap

def display(result):
    points = []
    result_dic = {}
    FinalType = []
    FinalMarks = []
    reply = ''

    for k,v in result.items():
        points.append(v)
    
    s_points = sorted(points)
    for i in s_points:
        for keys in result:
            if result[keys] == i:
                result_dic[i*(-1)] = keys

    for k, v in result_dic.items():
        MaxType = v
        MaxMark = k
        break

    for k, v in result_dic.items():
        if k/MaxMark >= precision:
            FinalType.append(v)
            FinalMarks.append(k)

    reply += '\nPredicted type      Score\n\n'

    for i in range(len(FinalType)):
        s = '     ' + str(FinalType[i]) + '      ' + str(FinalMarks[i]) + '\n'
        reply += s

    reply += '\nAll type with scores\n\n'
    for k, v in result_dic.items():
        s = '     ' + v + '      ' + str(k) +'\n'
        reply += s

    print(reply)
    return reply

def cog_main(inp_score):
        pointMap = createPointMap(inp_score)

        result = {}

        for Type, Func in cogFunc.items():
            marks = 0
            for i in range(4):
                x = (pointMap[Func[i]] - pointMap[axis[Func[i]]]) * func_multiplier[i]
                marks += x

            marks = round(marks, 2)
            result[Type] = marks
            
        reply = display(result)
        return reply

if __name__ == "__main__":
    cog_main()