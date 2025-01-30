class Solution:
    def jumpingNums(self, X):
        # code here 
        # Function to calculate the largest jumping number ≤ X
        def bfs(start):
            largest = 0
            queue = [start]
            while queue:
                num = queue.pop(0)
                if num <= X:
                    largest = max(largest, num)
                else:
                    continue
              
                last_digit = num % 10
                if last_digit > 0:  # Append last_digit - 1
                    queue.append(num * 10 + (last_digit - 1))
                if last_digit < 9:  # Append last_digit + 1
                    queue.append(num * 10 + (last_digit + 1))
            return largest
        largest_jumping = 0
        for i in range(1, 10):  # Start BFS from each single-digit number
            largest_jumping = max(largest_jumping, bfs(i))
        
        return largest_jumping