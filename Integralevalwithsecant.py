import numpy as np

def trapezoidal_eval(N, a = 0, b = 1, f = lambda x : np.sin(3*(x**2)) / (x+1)):

    h = (b-a)/N
    
    sum = 0
    for i in range(N+1):
        x = a + i*h

        val = f(x)

        if i == 0 or i == N:
            sum += val/2
        else:
            sum += val

    return sum*h

def secant_method():
    tol = 10**(-4)
    x0 = 0.5
    x1 = 0.75

    f_x0 = trapezoidal_eval(1400, 0, x0) - 0.3

    for iteration in range(50):  # Max 50 försök för att undvika nan-loopar
        f_x1 = trapezoidal_eval(1400, 0, x1) - 0.3
        
        # Om funktionsvärdena är för lika, avbryt (förhindrar division med noll)
        if abs(f_x1 - f_x0) < 1e-14:
            break
            
        # Sekantformeln med tydliga variabler
        x_next = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        # Kontrollera om vi är tillräckligt nära (vårt stoppvillkor)
        if abs(x_next - x1) < tol:
            return x_next
        
        # Uppdatera för nästa runda
        x0, f_x0 = x1, f_x1
        x1 = x_next
    return x1

def main():
    b = secant_method()
    print(f"sekantmetodens övre gräns för F(x) = 0.3 : {b}")
    print(trapezoidal_eval(1400))

if __name__ == "__main__":
    main()