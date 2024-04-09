import streamlit as st

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    
    # Create a table to store the minimum edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill in the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    # Backtrack to find the operations
    operations = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            operations.append(f"Match '{s1[i - 1]}'")
            i -= 1
            j -= 1
        elif dp[i][j] == 1 + dp[i - 1][j - 1]:
            operations.append(f"Substitute '{s1[i - 1]}' with '{s2[j - 1]}'")
            i -= 1
            j -= 1
        elif dp[i][j] == 1 + dp[i][j - 1]:
            operations.append(f"Insert '{s2[j - 1]}'")
            j -= 1
        else:
            operations.append(f"Delete '{s1[i - 1]}'")
            i -= 1
    
    # Add remaining characters if any
    while i > 0:
        operations.append(f"Delete '{s1[i - 1]}'")
        i -= 1
    while j > 0:
        operations.append(f"Insert '{s2[j - 1]}'")
        j -= 1
    
    # Reverse the operations list
    operations.reverse()
    
    # Return the minimum edit distance and operations
    return dp[m][n], operations

# Streamlit app
st.title("Edit Distance Calculator")

# Input strings
s1 = st.text_input("Enter string 1:")
s2 = st.text_input("Enter string 2:")

# Calculate edit distance
if st.button("Calculate Edit Distance"):
    if not s1 or not s2:
        st.error("Please enter both strings.")
    else:
        min_distance, operations = edit_distance(s1, s2)
        st.success(f"Minimum edit distance between '{s1}' and '{s2}': {min_distance}")
        st.write("Operations:")
        for op in operations:
            st.write(op)
