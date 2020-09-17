def hashOctree(pts, sz):
    octr = dict()
    for p in pts:
        x = p[0]
        y = p[1]
        z = p[2]
        a = 2
        b = 2
        c = 2
        if x>sz/2:
            a+=1
        if y>sz/2:
            b+=1
        if z>sz/2:
            c+=1
        if octr.get((a, b, c), None)==None:
            octr[(a, b, c)]=[p, 0]
        else:
            x-=(x>sz/2)*sz/2
            y-=(y>sz/2)*sz/2
            z-=(z>sz/2)*sz/2
            ct=2
            while octr.get((a, b, c), None)!=None and octr[(a, b, c)][1]:
                a=a<<1
                if x>(sz/(1<<ct)):
                    a+=1
                    x-=sz/(1<<ct)
                b=b<<1
                if y>(sz/(1<<ct)):
                    b+=1
                    y-=sz/(1<<ct)
                c=c<<1
                if z>(sz/(1<<ct)):
                    c+=1
                    z-=sz/(1<<ct)
                ct+=1
            if octr.get((a, b, c), None)==None:
                octr[(a, b, c)]=[p, 0]
            else:
                p2 = octr[(a, b, c)][0]
                x2 = octr[(a, b, c)][0][0]
                y2 = octr[(a, b, c)][0][1]
                z2 = octr[(a, b, c)][0][2]
                a2 = a
                b2 = b
                c2 = c
                while a2==a and b2==b and c2==c:
                    octr[(a, b, c)]=[p2, 1]
                    a=a<<1
                    L = sz/(1<<ct)
                    if x>L:
                        a+=1
                        x-=L
                    b=b<<1
                    if y>L:
                        b+=1
                        y-=L
                    c=c<<1
                    if z>L:
                        c+=1
                        z-=sz/L
                    a2=a2<<1
                    if x2>L:
                        a2+=1
                        x2-=L
                    b2=b2<<1
                    if y2>L:
                        b2+=1
                        y2-=L
                    c2=c2<<1
                    if z2>L:
                        c2+=1
                        z2-=L
                    ct+=1
                octr[(a2, b2, c2)]=[p2, 0]
                octr[(a, b, c)]=[p, 0]
    return octr
