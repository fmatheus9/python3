soma = 0
for num in range(0,500,1):
    if num % 2 != 0 and num % 3 == 0:
        soma = soma + num
print(soma) 

import time
print("10:00")
for c in range(9,-1,-1):
    for j in range(59,-1,-1):
        if j<10:
           print(f"0{c}:0{j}")
        else: 
            print(f"0{c}:{j}")
        time.sleep(1)