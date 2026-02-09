from mpmath import mp

# Set precision to 150 digits so we cover the 100th decimal easily
mp.dps = 150 

def cylinder_volume(r, h, pi_val):
    return pi_val * (r ** 2) * h

# --- CONSTANTS FOR CYLINDER VOLUME ---
RADIUS = 5
HEIGHT = 10
DECIMALS = [20, 40, 60, 100]

trunc_results = {}
round_results = {}

print(f"--- SET 1: TRUNCATION (mpmath) ---")
for n in DECIMALS:
    # mpmath doesn't have a simple 'truncate' function for Pi specifically,
    # so we convert to string and slice.
    
    # Get Pi to full precision as a string
    full_pi_str = str(mp.pi)
    
    # Slicing "3." (2 chars) + n digits
    truncated_pi_str = full_pi_str[:n+2]
    pi_val = mp.mpf(truncated_pi_str)
    
    vol = cylinder_volume(RADIUS, HEIGHT, pi_val)
    trunc_results[n] = vol
    print(f"{n:<5} | {vol}")

print(f"\n--- SET 2: ROUNDING (mpmath) ---")
for n in DECIMALS:
    # mpmath tracks precision automatically. 
    # To 'round' Pi to N digits, we just set the working precision to N temporarily.
    with mp.workdps(n):
        pi_val = +mp.pi # The '+' forces a re-evaluation at current precision
        
    # To strictly follow "rounding to N decimal places" like the manual string method:
    pi_val_rounded = mp.nstr(mp.pi, n+1) # n+1 significant digits covers it
    pi_val = mp.mpf(pi_val_rounded)

    vol = cylinder_volume(RADIUS, HEIGHT, pi_val)
    round_results[n] = vol
    print(f"{n:<5} | {vol}")

# Calculate and print the differences
print(f"\n--- DIFFERENCE ---")
for n in DECIMALS:
    diff = abs(round_results[n] - trunc_results[n])
    print(f"{n:<5} | {float(diff):.100f}")

# Print conclusion
print("\n--- CONCLUSION ---")
print("The results show that as we increase the number of decimal places for Pi, the calculated volume of the cylinder becomes more accurate.") 
print("The rounding method generally provides a closer approximation to the true value of Pi, and is always greater than or equal to the truncated value.\n")