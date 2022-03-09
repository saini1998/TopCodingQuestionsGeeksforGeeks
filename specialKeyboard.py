"""

Imagine you have a special keyboard with the following keys: 

Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Find maximum numbers of A's that can be produced by pressing keys on the special keyboard N times. 


Example 1:

Input: N = 3
Output: 3
Explaination: Press key 1 three times.

Example 2:

Input: N = 7
Output: 9
Explaination: The best key sequence is 
key 1, key 1, key 1, key 2, key 3,
key4, key 4.

Your Task:
You do not need to read input or print anything. Your task is to complete the function optimalKeys() which takes N as input parameter and returns the maximum number of A's that can be on the screen after performing N operations.


Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N)


Constraints:
1 < N < 75

"""

def optimalKeys(N):
        if (N <= 6):
            return N
     
        screen = [0]*N

        for n in range(1, 7):
            screen[n-1] = n
     
        for n in range(7, N + 1):

            screen[n-1] = 0

            for b in range(n-3, 0, -1):
                b_value = n - 3
                curr_term_1 = n - b - 1
                b_minus_one = b - 1
                curr = (n-b-1)*screen[b-1]
                screen_n_minus_one = screen[n-1]
                if (curr > screen[n-1]):
                    screen[n-1] = curr

        ans = screen[N-1]
             
        return screen[N-1]

optimalKeys(N=10)