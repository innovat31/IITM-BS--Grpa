# Actual Solution :

def find_longest_antakshari(words):
    max_len = 1
    prev_word = words[0]
    anthakshari_len = 1
    for word in words[1:]:
        if prev_word[-1] == word[0]:
            anthakshari_len +=1
        else:
            anthakshari_len = 1
        if anthakshari_len > max_len:
            max_len = anthakshari_len
        prev_word = word
    return max_len

n = int(input())
for i in range(n):
    print(find_longest_antakshari(input().split(',')))
        
# Second Method :

def longest_antakshari_subsequence(words):
    max_length = 0
    current_length = 1
    
    for i in range(len(words) - 1):
        if words[i][-1] == words[i + 1][0]:  # Check if last letter matches first letter
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1  # Reset length for next possible sequence
    
    max_length = max(max_length, current_length)  # Final check
    return max_length

# Read input
n = int(input().strip())
results = []
for _ in range(n):
    words = input().strip().split(',')
    results.append(str(longest_antakshari_subsequence(words)))

# Print results
print("\n".join(results))
