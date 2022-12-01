from math import *
from prettytable import PrettyTable
import ctypes, os

while True:
    table = PrettyTable()
    table2 = PrettyTable()

    def error():
        ctypes.windll.user32.MessageBoxW(0, "Keine Lösung", "Error!", 1)
        
    def clear():
        os.system('cls' if os.name=='nt' else 'clear')
    
    clear()
        
    table.field_names = ["S","S output", "W","W output"]
    table2.field_names = ["SS","SS output", "WW","WW output"]
    mode = input("Wähle den Modus:\nsss, ssw, sws, www, wws, wsw oder distanz?\n")

    if mode == "sss":
        s1 = float(input("s1: "))
        s2 = float(input("s2: "))
        s3 = float(input("s3: "))
        s1 = radians(s1)
        s2 = radians(s2)
        s3 = radians(s3)

        if s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
            ctypes.windll.user32.MessageBoxW(0, "Keine Lösung (Dreiecksungleichung)", "Error!", 1)
        else:
            w1_1 = sin(s1)*sin(s2)
            w1_2 = cos(s1)-cos(s2)*cos(s3)
            w1_3 = w1_2/w1_1
            w1 = acos(w1_3)
            w1 = degrees(w1)

            w2_1 = sin(s1)*sin(s3)
            w2_2 = cos(s2)-cos(s1)*cos(s3)
            w2_3 = w2_2/w2_1
            w2 = acos(w2_3)
            w2 = degrees(w2)

            w3_1 = sin(s1)*sin(s2)
            w3_2 = cos(s3)-cos(s1)*cos(s2)
            w3_3 = w3_2/w3_1
            w3 = acos(w3_3)
            w3 = degrees(w3)

            s1 = degrees(s1)
            s2 = degrees(s2)
            s3 = degrees(s3)
            
            table.add_row(["s1", s1, "w1", w1])
            table.add_row(["s2", s2, "w2", w2])
            table.add_row(["s3", s3, "w3", w3])

            print (table)

    elif mode == "ssw":
        sa = float(input("sa: "))
        sb = float(input("sb: "))
        wa = float(input("wa: "))
        sa = radians(sa)
        sb = radians(sb)
        wa = radians(wa)

        if sin(sb)*sin(wa)>sin(sa):
            error()
        else:
            delta = 0.0004
            a = ((cos(sb))**2)+((sin(sb))**2)*((cos(wa))**2)
            b = (cos(sa))*(cos(sb))*(-2)
            c = (cos(sa))**2-(sin(sb))**2*(cos(wa))**2
            d = (b**2)-4*a*c
            s1 = sa
            s2 = sb
            w1 = wa
            s3_1 = sqrt(d)
            s3_1 = s3_1-b
            s3_2 = 2*a
            s3 = s3_1/s3_2
            s3 = acos(s3)

            w2_1 = (cos(s2))-(cos(s1))*(cos(s3))
            w2_2 = (sin(s1))*(sin(s3))
            w2 = w2_1/w2_2
            w2 = acos(w2)

            w3_1 = (cos(s3))-(cos(s1))*(cos(s2))
            w3_2 = (sin(s1))*(sin(s2))
            w3 = w3_1/w3_2
            w3 = acos(w3)
            #2. Lösung
            ss1 = sa
            ss2 = sb
            ww1 = wa

            ss3 = acos((sqrt(d)-b)/(2*a))
            ww2_1 = cos(ss2)-cos(ss1)*cos(ss3)
            ww2_2 = sin(ss1)*sin(ss3)
            ww2 = ww2_1/ww2_2
            ww2 = acos(ww2)

            ww3_1 = cos(ss3)-cos(ss1)*cos(ss2)
            ww3_2 = sin(ss1)*sin(ss2)
            ww3 = ww3_1/ww3_2
            ww3 = acos(ww3)

            if degrees((cos(s1)-cos(s2)*cos(s3)-sin(s2)*sin(s3)*cos(w1)))>delta:
                s3=0;  w2=0;  w3=0 #Scheinlösung
            if degrees((cos(ss1)-cos(ss2)*cos(ss3)-sin(ss2)*sin(ss3)*cos(ww1)))>delta:
                ss3=0;  ww2=0;  ww3=0 #Scheinlösung

            s1 = degrees(s1)
            s2 = degrees(s2)
            s3 = degrees(s3)

            ss1 = degrees(ss1)
            ss2 = degrees(ss2)
            ss3 = degrees(ss3)

            w1 = degrees(w1)
            w2 = degrees(w2)
            w3 = degrees(w3)

            ww1 = degrees(ww1)
            ww2 = degrees(ww2)
            ww3 = degrees(ww3)

            table.add_row(["s1", s1, "w1", w1])
            table.add_row(["s2", s2, "w2", w2])
            table.add_row(["s3", s3, "w3", w3])

            table2.add_row(["ss1", ss1, "ww1", ww1])
            table2.add_row(["ss2", ss2, "ww2", ww2])
            table2.add_row(["ss3", ss3, "ww3", ww3])

            print (table)
            print (table2)

    elif mode == "sws":
        b = float(input("b: "))
        wa = float(input("wa: "))
        c = float(input("c: "))
        b = radians(b)
        wa = radians(wa)
        c = radians(c)
        s2 = b
        w1 = wa
        s3 = c
        s1 = acos(cos(b)*cos(c)+sin(b)*sin(c)*cos(wa))
        w2 = acos(((cos(s2)-cos(s1)*cos(s3))/(sin(s1)*sin(s3))))
        w3 = acos(((cos(s3)-cos(s1)*cos(s2))/(sin(s1)*sin(s2))))
        
        table.add_row(["s1", s1, "w1", w1])
        table.add_row(["s2", s2, "w2", w2])
        table.add_row(["s3", s3, "w3", w3])
        
        b = degrees(b)
        wa = degrees(wa)
        c = degrees(c)
        
        print (table)

    elif mode == "www":
        wa = float(input("wa: "))
        wb = float(input("wb: "))
        wc = float(input("wc: "))
        
        wa = radians(wa)
        wb = radians(wb)
        wc = radians(wc)
        
        s1 = 180-wa
        s2 = 180-wb
        s3 = 180-wc
        
        if s1+s2>=s3 or s1+s3<=s2 or s2+s3<=s1:
            error()
        
        else:    
            w1 = acos(((cos(s1)-cos(s2)*cos(s3))/(sin(s2)*sin(s3))))
            w2 = acos(((cos(s2)-cos(s1)*cos(s3))/(sin(s1)*sin(s3))))
            w3 = acos(((cos(s3)-cos(s1)*cos(s2))/(sin(s1)*sin(s2))))
            
            s1 = 180-w1
            s2 = 180-w2
            s3 = 180-w3
            
            w1 = wa
            w2 = wb
            w3 = wc
            
            wa = degrees(wa)
            wb = degrees(wb)
            wc = degrees(wc)
            
            table.add_row(["s1", s1, "w1", w1])
            table.add_row(["s2", s2, "w2", w2])
            table.add_row(["s3", s3, "w3", w3])
            
            print (table)
            
    elif mode == "wws":
        delta = 0.0001
        if sin(wb)*sin(sa) > sin(wa):
            error()
        else:
            wa = float(input("wa: "))
            wb = float(input("wb: "))
            sa = float(input("sa: "))
            
            wa = radians(wa)
            wb = radians(wb)
            sa = radians(sa)
            
            a = (cos(wb)**2)+(sin(wb)**2)*(cos(sa)**2)
            b = 2*cos(wa)*cos(wb)
            c = (cos(wa)**2)-(sin(wb)**2)*(cos(sa)**2)
            d = b**2-4*a*c
            
            w1 = wa
            w2 = wb
            s1 = sa

            w3 = acos((((b-2*b) +sqrt(d))/(2*a)))
            s2 = acos(((cos(w2)+cos(w1)*cos(w3))/(sin(w1)*sin(w3))))
            s3 = acos(((cos(w3)+cos(w1)*cos(w2))/(sin(w1)*sin(w2))))
            
            ww1 = wa
            ww2 = wb
            ss1 = sa
            
            ww3 = acos((((b-2*b) -sqrt(d))/(2*a)))
            ss2 = acos(((cos(ww2)+cos(ww1)*cos(ww3))/(sin(ww1)*sin(ww3))))
            ss3 = acos(((cos(ww3)+cos(ww1)*cos(ww2))/(sin(ww1)*sin(ww2))))
            
            if cos(w1)-((cos(w2)-cos(w2)*2)*cos(w3)+sin(w2)*sin(w3)*cos(s1)) > delta:      
                w3 = 0
                s2 = 0
                s3 = 0
            
            if cos(ww1)-((cos(ww2)-cos(ww2)*2)*cos(ww3)+sin(ww2)*sin(ww3)*cos(ss1)) > delta:
                ww3 = 0
                ss2 = 0
                ss3 = 0
                
            w1 = degrees(w1)
            s2 = degrees(s2)
            s3 = degrees(s3)
            
            ww1 = degrees(ww1)
            ss2 = degrees(ss2)
            ss3 = degrees(ss3)

            table.add_row(["s1", s1, "w1", w1])
            table.add_row(["s2", s2, "w2", w2])
            table.add_row(["s3", s3, "w3", w3])
            
            table2.add_row(["ss1", ss1, "ww1", ww1])
            table2.add_row(["ss2", ss2, "ww2", ww2])
            table2.add_row(["ss3", ss3, "ww3", ww3])
            
            print(table)
            print(table2)
            
    elif mode == "wsw":
        wb = float(input("wb: "))
        a = float(input("a: "))
        wc = float(input("wc: "))
        
        wb = radians(wb)
        a = radians(a)
        wc = radians(wc)
        
        w2 = wb
        s1 = a
        w3 = wc
        
        w1 = acos((cos(wb)-cos(wb)*2)*cos(wc)+sin(wb)*sin(wc)*cos(a))
        s2 = acos(((cos(w2)+cos(w1)*cos(w3))/(sin(w1)*sin(w3))))
        s3 = acos(((cos(w3)+cos(w1)*cos(w2))/(sin(w1)*sin(w2))))
        
        s1 = degrees(s1)
        s2 = degrees(s2)
        s3 = degrees(s3)
        w1 = degrees(w1)
        w2 = degrees(w2)
        w3 = degrees(w3)
        
        table.add_row(["s1", s1, "w1", w1])
        table.add_row(["s2", s2, "w2", w2])
        table.add_row(["s3", s3, "w3", w3])
        
        print (table)
        
    elif mode == "distanz":
        re = 6370
        
        b1 = float(input("Breite 1: "))
        l1 = float(input("Länge 1: "))
        b2 = float(input("Breite 2: "))
        l2 = float(input("Länge 2: "))
        
        b1 = radians(b1)
        l1 = radians(l1)
        b2 = radians(b2)
        l2 = radians(l2)
        
        if b1 == b2 and l1 == l2:
            error()
        
        else:
            w = acos(sin(b1)*sin(b2)+cos(b1)*cos(b2)*cos(abs(l1-l2)))
            w = degrees(w)
            e = ((pi*w*re)/(180))
            
            distanz_table = PrettyTable()
            distanz2_table = PrettyTable()
            distanz_table.field_names = ["Punkt", "Breite", "Länge"]
            distanz2_table.field_names = ["Sphärische Distanz", ""]
            
            b1 = degrees(b1)
            l1 = degrees(l1)
            b2 = degrees(b2)
            l2 = degrees(l2)
            
            w = str(w)
            e = str(e)
            
            distanz_table.add_row(["A", b1, l1])
            distanz_table.add_row(["B", b2, l2])
            distanz2_table.add_row(["w =", w + "°"])
            distanz2_table.add_row(["e =", e + "km"])
            
            print (distanz_table)
            print (distanz2_table)

    else:
        ctypes.windll.user32.MessageBoxW(0, "Bitte geben sie einen gültigen Modus ein", "Error!", 1)

    input("\nWenn du die Resultate abgeschrieben hast drücke eine Taste um das Programm neuzustarten\n")
    clear()