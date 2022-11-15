# DAA Assignment 1
# def iterative_fib(n):
#     if(n <= 1):
#         return n
    
#     first = 0
#     second = 1
#     for i in range(2, n+1):
#         third = first + second
#         first = second
#         second = third 
    
#     return third 

# def recur_fib(n):
#     if(n <= 1):
#         return n
    
#     return recur_fib(n-1) + recur_fib(n-2)


# def assign1():
#     n = int(input("Enter n: "))
#     if(n < 0):
#         print("No fib exists")
#     else:
#         print(iterative_fib(n))
#         print(recur_fib(n))

# DAA Assignment 2
# import heapq
# class Node():
#     def __init__(self, char, frequency, symbol, left = None, right = None):
#         self.char = char
#         self.freq = frequency
#         self.left = left 
#         self.right = right 

#         self.symbol = symbol

#     def __lt__(self, next):
#         return self.freq < next.freq
    
# def huffman_tree(chars, freqs):
#     nodes = []

#     for i in range(len(chars)):
#         heapq.heappush(nodes, Node(chars[i], freqs[i], ''))
    
#     while(len(nodes) > 1):
#         left = heapq.heappop(nodes)
#         right = heapq.heappop(nodes)

#         left.symbol = "0"
#         right.symbol = "1"
#         new_node = Node(left.char + right.char, left.freq + right.freq, "", left, right)

#         heapq.heappush(nodes, new_node)
    
#     return nodes

# def print_nodes(node, str_value = ""):
#     str_value += node.symbol

#     if(node.left):
#         print_nodes(node.left, str_value)
#     if(node.right):
#         print_nodes(node.right, str_value)

#     if(not node.left and not node.right):
#         print(f"{node.char} => {str_value}")

# def assign2():
#     chars = ['a', 'b', 'c', 'd', 'e']
#     freqs = [100, 80, 70, 60, 50]

#     nodes = huffman_tree(chars, freqs)

#     print_nodes(nodes[0])

#DAA Assignment 3
# class Item():
#     def __init__(self, weight, profit):
#         self.weight = weight
#         self.profit = profit 

# def fractional_knapsack(arr, capacity):
#     arr = sorted(arr, key = lambda x: (x.profit/x.weight))
#     profit = 0
#     for i in range(len(arr)):
#         if(arr[i].weight <= capacity):
#             capacity -= arr[i].weight
#             profit += arr[i].profit
#         else:
#             profit += arr[i].profit*(capacity/arr[i].weight)
#             break

#     return profit


# def assign3():
#     arr = [Item(30, 40), Item(40, 50), Item(20, 30)]
#     capacity = 50

#     print(fractional_knapsack(arr, capacity))

# DAA Assignment 4
# class Knapsack():    
#     def recursive_knapsack(self, profits, weights, capacity, dp, index):
#         if(index >= len(profits) or capacity <= 0):
#             return 0
        
#         if(dp[index][capacity] != -1):
#             return dp[index][capacity]
#         profit1 = 0
#         profit2 = 0
#         if(weights[index] <= capacity):
#             profit1 = profits[index] + self.recursive_knapsack(profits, weights, capacity - weights[index], dp, index + 1)
#         profit2 = self.recursive_knapsack(profits, weights, capacity, dp, index + 1)

#         dp[index][capacity] = max(profit1, profit2)
#         return dp[index][capacity]
#     def solve_knapsack(self, profits, weights, capacity):
#         dp = [[-1 for i in range(capacity+1)] for j in range(len(profits))]
#         return self.recursive_knapsack(profits, weights, capacity, dp, 0)

# def assign4():
#     ks = Knapsack()
#     print(ks.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

# DAA Assignment 5
n = 7
def is_safe(board, row, col):
    for i in range(col):
        if(board[row][i]):
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if(board[i][j]):
            return False
        
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if(board[i][j]):
            return False

    return True 

def solve_n_queen(board, col):
    if(col >= n):
        return True 
    for i in range(n):
        if(is_safe(board, i, col)):
            board[i][col] = 1

            if(solve_n_queen(board, col+1)):
                return True
            
            board[i][col] = 0
    return False

def print_board(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = "\t")
        print()

def assign5():
    board = [[0 for i in range(n)] for j in range(n)]

    if(solve_n_queen(board, 0)):
        print_board(board)
    else:
        print("Solution doesn't exist")

if(__name__ == "__main__"):
    assign5()