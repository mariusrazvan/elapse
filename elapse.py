
cifre = {
        "un":"un",
        "unu":"unu",
        "0":"zero",
        "1":"o",
	"2":"doua",
	"3":"trei",
	"4":"patru",
	"5":"cinci",
	"6":"sase",
	"7":"sapte",
	"8":"opt",
	"9":"noua",
	"10":"zece",
	"11":"unsprezece",
	"12":"doisprezece",
	"13":"treisprezece",
	"14":"paisprezece",
	"15":"cincisprezece",
        "16":"saisprezece",
        "17":"saptesprezece",
        "18":"optsprezece",
        "19":"nouasprezece",
	
}

def cifratolitera(x):
    x=str(x)
    if x in cifre:
        return cifre.get(x)
    else:
        deca = cifre.get(x[0])+"zeci"
        unit = cifre.get(x[1:])
        if x[1] == '1':
            return deca+'siuna'
        elif x[1] == '0':
            return deca
        elif x[1] == 'unu':
            return deca+"siunu"
        else:
            return deca+'si'+unit

def spunelitere(x):
    zi = int(x/86400)
    ora = (x-zi*86400)/3600
    minut = (x-(zi*86400)-(ora*3600))/60
    secunda = x-(zi*86400)-(ora*3600)-(minut*60)

    if zi == 1:
        zile = "zi"
    elif zi > 1 and zi < 20:
        zile = "zile"
    elif zi == 0:
        zile = ""
    else:
        zile = "de zile"

    if ora == 1:
        ore = "ora"
    elif ora > 1 and ora < 20:
        ore = "ore"
    elif ora == 0:
        ore = ""
    else:
        ore = "de ore"

    if minut == 1:
        minut = 'un'
        minute = "minut"
    elif minut > 1 and minut < 20:
        minute = "minute"
    elif  minut == 0:
        minute = ""
    else:
        if str(minut)[1] == '1':
            minut=str(minut)
            minut = minut[0]+'unu'
        minute = "de minute"

    if secunda == 1:
        secunde = "secunda"
    elif secunda > 1 and secunda < 20:
        secunde = "secunde"
    elif  secunda == 0:
        secunde = ""
    else:
        secunde = "de secunde"
        
    days    = "%s %s" %(cifratolitera(str(zi)),zile)
    hours   = "%s %s" %(cifratolitera(str(ora)),ore)
    minutes = "%s %s" %(cifratolitera(str(minut)),minute)
    seconds = "%s %s" %(cifratolitera(str(secunda)),secunde)

    if zi != 0:
        if ora != 0:
            if minut != 0:
                if secunda != 0:
                    return  days+" "+hours+" "+minutes+" si "+seconds      #all != 0
                else:
                    return  days+" "+hours+" si "+minutes                  #zi,ora,minut != 0
            else:
                if secunda != 0:
                    return  days+" "+hours+" si "+seconds                  #zi,ora,secunda != 0
                else:
                    return  days+" si "+hours                              #zi,ora != 0
        else:
            if minut != 0:
                if secunda != 0:
                    return  days+" "+minutes+" si "+seconds                #zi,minut,secunda != 0
                else:
                    return  days+" si "+minutes                            #zi, minut != 0
            else:
                if secunda != 0:
                    return  days+" si "+seconds                  #
                else:
                    return  days
    else:
        if ora != 0:
            if minut != 0:
                if secunda != 0:
                    return  hours+" "+minutes+" si "+seconds      #ora,minut,secunda != 0
                else:
                    return  hours+" si "+minutes                  #ora,minut != 0
            else:
                if secunda != 0:
                    return  hours+" si "+seconds                  #ora,secunda != 0
                else:
                    return  hours                              #ora != 0
        else:
            if minut != 0:
                if secunda != 0:
                    return  minutes+" si "+seconds                #minut,secunda != 0
                else:
                    return  minutes                            #minut != 0
            else:
                if secunda != 0:
                    return  seconds                             #
                else:
                    return  "ZERO!"
