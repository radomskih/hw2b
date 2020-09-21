#Exercise 2.2 Page 30#
print("Part b")
def alt(t): #Create a function for altitude#
        G=6.67*10**(-11)
        M=5.97*10**(24)
        R=6371*1000 #convert R to meters#
        from math import pi
        h=(G*M*(t)**2/(4*(pi)**2))**(1/3)-R
        return h
t=float(input("Enter the time of orbit in seconds: "))
print("The satellite is at analtitude of",alt(t),"meters.")

print("Part c")
T=[24*60*60, 90*60, 45*60]
for t in T:
    print("The altitude for an orbit of",t,"seconds is",alt(t),"meters")
        
print("Part d")
print("The altitude for an orbit of one sidereal day is",alt(23.93*60*60),"meters")
print("The satellite will be",alt(24*60*60)-alt(23.93*60*60),"meters closer to the Earth with an orbit equal to the sidereal day rather than a solar day. (The sidereal day is not equal to the solar day because of the Earth's orbit around the Sun.)")
