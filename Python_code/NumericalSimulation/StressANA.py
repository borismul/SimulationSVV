import matplotlib.pyplot as plt
import math 

def shearstress(x,y):
    numbers = range(3001)
    ## Basic inputs
    c = 1
    ang = -32.2*2*math.pi/180.
    c_t = 1.69
    c_r = 6.27
    L_1 = 2.88
    L_2 = 27.22
    L_3 = 9.7
    h0 = 2.17
    m_e = 5765
    T_e = 64000
    m_f = 15000*0.81
    g = 9.81
    la = -8.739*10**3
    f = 20693
    q01lst = list()
    q12lst = list()
    q23lst = list()
    q34lst = list()
    q45lst = list()
    q50lst = list()
    ilst = list()
##Forces and Moments
    for i in numbers:
        i = i/100.
        ilst.append(-1*(i-30))
        if(i>=27.22):
            c_i = c_r
        else:
            c_i = c_t+i*(-c_t+c_r)/L_2
        y = y*c_i
        x = x*c_i
        t_front = 0.005*c_i
        t_rear =  0.003*c_i
        t_top = 0.002*c_i
        Ixx = 17/3.*10**(-6)*c_i**4
        Iyy = 61/672.*10**(-3)*c_i**4
        h = h0-0.05*c_i
        Mx3 = la*(-1/6.*c_t*L_2*L_2-1/3.*c_r*L_2*L_2+1/2.*(c_r+c_t)*L_2*L_2)-m_e*g*(L_3-L_1)
        Sy3 = la*(L_2/2.*(c_r-c_t)+c_t*L_2)-m_e*g-f*(i-L_2)
        Mx2 = la*(1/6.*i*i*i*(c_r-c_t)/L_2+1/2.*c_t*i*i)-m_e*g*(i+L_3-(L_1+L_2))
        Sy2 = la*(1/2.*i*i*(c_r-c_t)/L_2+c_t*i)-m_e*g
        Mx1 = la*(1/6.*i*i*i*(c_r-c_t)/L_2+1/2.*c_t*i*i)
        Sy1 = la*(1/2.*i*i*(c_r-c_t)/L_2+c_t*i)
        A = 0.1*0.5*c_i*c_i
## Calculations for section 1
        if(i<30-9.7):
            Sy = Sy1
            Mx = Mx1
            Sx = 0
    ##Qso 
            qs0 = (-1/(2*A)*(Mx1*math.tan(ang)+Sy1*3/17.*(10*t_top+t_rear)/16.*10**(3)))
    ## Basic shear flows
            s = y
            q01b = -Sy/Ixx*t_rear/2.*s*s+Sx/Iyy*t_rear/4.*c_i*s
            s = x
            q12b = -Sy/Ixx*t_rear/800.*c_i*c_i+Sx/Iyy*t_rear/80.*c_i*c_i-Sy/Ixx*t_top/20.*c_i*(s+1/4.*c_i)-Sx/Iyy*t_top*(1/2.*s*s-1/32.*c_i*c_i)
            s = y
            q23b = -Sy/Ixx*(t_rear/800.*c_i*c_i+t_top/40.*c_i*c_i)+Sx/Iyy*(t_rear/80.-t_top/16.)*c_i*c_i-Sx/Iyy*t_front/4.*c_i*(s-1/20.*c_i)-Sy/Ixx*t_front*(c_i*c_i*-1/800.+1/2.*s*s)
            q34b = -q23b
            q45b = -q12b
            q50b = -q01b

## Section 2
        elif(i<27.22):
            Sy = Sy2
            Mx = Mx2
            Sx = T_e
    ##Qso
            qs0 = (-1/(2*A)*(Mx2*math.tan(ang)+Sy2*3/17.*10**3*(t_rear+10*t_top)/16.-T_e*(2.295*(3*t_rear+5*t_top)+h))) ##Moments of inertia already included
    ## Basic shear flows
            s = y
            q01b = -Sy/Ixx*t_rear/2.*s*s+Sx/Iyy*t_rear/4.*c_i*s
            s = x
            q12b = -Sy/Ixx*t_rear/800.*c_i*c_i+Sx/Iyy*t_rear/80.*c_i*c_i-Sy/Ixx*t_top/20.*c_i*(s+1/4.*c_i)-Sx/Iyy*t_top*(1/2.*s*s-1/32.*c_i*c_i)
            s = y
            q23b = -Sy/Ixx*(t_rear/800.*c_i*c_i+t_top/40.*c_i*c_i)+Sx/Iyy*(t_rear/80.-t_top/16.)*c_i*c_i-Sx/Iyy*t_front/4.*c_i*(s-1/20.*c_i)-Sy/Ixx*t_front*(c_i*c_i*-1/800.+1/2.*s*s)
            q34b = -q23b
            q45b = -q12b
            q50b = -q01b
        
## Section 3
        else:
            Sy = Sy3
            Mx = Mx3
            Sx = T_e
    #Qso
            qs0 = (-1/(2*A)*(Mx3*math.tan(ang)+Sy3*3/17.*10**3*(t_rear+10*t_top)/16.-T_e*(2.295*(3*t_rear+5*t_top)+h))-1/4.*f*(i-L_2)*c_i)##Moments of inertia already included
    ## Basic shear flows
            s = y
            q01b = -Sy/Ixx*t_rear/2.*s*s+Sx/Iyy*t_rear/4.*c_i*s
            s = x
            q12b = -Sy/Ixx*t_rear/800.*c_i*c_i+Sx/Iyy*t_rear/80.*c_i*c_i-Sy/Ixx*t_top/20.*c_i*(s+1/4.*c_i)-Sx/Iyy*t_top*(1/2.*s*s-1/32.*c_i*c_i)
            s = y
            q23b = -Sy/Ixx*(t_rear/800.*c_i*c_i+t_top/40.*c_i*c_i)+Sx/Iyy*(t_rear/80.-t_top/16.)*c_i*c_i-Sx/Iyy*t_front/4.*c_i*(s-1/20.*c_i)-Sy/Ixx*t_front*(c_i*c_i*-1/800.+1/2.*s*s)
            q34b = -q23b
            q45b = -q12b
            q50b = -q01b

        q01lst.append((qs0+q01b)*c/t_rear)
        q12lst.append((qs0+q12b)*c/t_top)
        q23lst.append((qs0+q23b)*c/t_front)
        q34lst.append((qs0+q34b)*c/t_front)
        q45lst.append((qs0+q45b)*c/t_top)
        q50lst.append((qs0+q50b)*c/t_rear)
    ##need to use right shear flow
    return ilst, q01lst, q12lst, q23lst, q34lst, q45lst, q01lst
##x,y here different then in shear stress
def Normstress(x1,y1):
    i = range(0,2030)
    j = range(2030,2722)
    k = range(2722,3001)
    lst = list()
    r = list()
    for w in i:
        w = w/100.
        y = (1.69+((6.27-1.69)/27.22*w))*y1
        x = (1.69+((6.27-1.69)/27.22*w))*x1
        s1 = 5.39574*10.**10*w**2*(w+30.1233)*y/((w+10.0441)**4)
        lst.append(s1)
        r.append((w-30)*-1.)
    for v in j:
        v = v/100.
        y = (1.69+((6.27-1.69)/27.22*v))*y1
        x = (1.69+((6.27-1.69)/27.22*v))*x1
        s2 = 5.39574*10**10*(v**3+30.1322*v**2-230.771*v+4684.640)*y/((v+10.0441)**4)+8.7965*10**11*(v-20.3)*x/((v+10.0441)**4)
        lst.append(s2)
        r.append((v-30)*-1)
    for u in k:
        u = u/100.
        y = y1*6.27
        x = x1*6.27
        s3 = -1.1814*10**6*(u**2-140.478*u+2114.19)*y+456194*(u-20.3)*x
        lst.append(s3)
        r.append((u-30)*-1)
    return r,lst

def vonMisesFront():
    a,b,c,d,e,f,g = shearstress(0.25,0)
    h,t = Normstress(0.25,0)

    mlst = list()
    for i in range(3001): 
        mlst.append((3*d[i]*d[i]+t[i]*t[i])**(0.5))

    return h,mlst

def vonMisesTop():
    a,b,c,d,e,f,g = shearstress(0,1/20.)
    h,t = Normstress(0,0.05)

    mlst = list()
    for i in range(3001): 
        mlst.append((3*c[i]*c[i]+t[i]*t[i])**(0.5))

    return h,mlst

a,b = vonMisesTop()
