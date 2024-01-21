#str[start:stop:step]

trial = "reverse"
new_trial = trial[::-1]

print(new_trial)

#reversing string using recursion

def reverse_string(str):
    if len(str) ==0:
        return str
    else:
        return reverse_string(str[1:]) + str[0]
    
trial_recursion = reverse_string(trial)
print(trial_recursion)