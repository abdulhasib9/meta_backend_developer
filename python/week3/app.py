#algorithm for palindrom

def is_palendrom(str):
    start_index=0
    end_index=len(str)-1
    for item in str:
        if str[start_index] !=str[end_index]:
            return False
    return True

print(is_palendrom("racecars"))