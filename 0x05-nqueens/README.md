## N Queen program solved with backtracking
Alright, let me explain the N queens puzzle and the program that solves it like you're a kid.

Imagine you have a chessboard, and you want to place some queens on it. But you don't want any of the queens to attack each other. In chess, a queen can move horizontally, vertically, or diagonally. So, we want to put the queens in such a way that they can't attack each other. It's like a fun puzzle!

Now, the program we have is like a magical tool that can solve this puzzle for any size of the chessboard. But it has some rules! When you use the program, you need to give it a number called N, which represents the size of the chessboard (it's like telling the program how big the board should be).

But wait! There are some important rules you need to follow:

1. You should use the program like this: `nqueens N`, where N is a number. For example, you can use it like `nqueens 4` or `nqueens 6`.
2. If you don't tell the program the size (N) or if you tell it the wrong way, it will be sad and not work. It will tell you, "Hey, you should use it like this: `nqueens N`, where N is a number!" and then stop working.
3. Also, N should be a whole number, like 1, 2, 3, 4, and so on. If you try to use a number with a fraction or a word, it will be confused and tell you, "N must be a number!"
4. Finally, N should be at least 4. If you try to use a smaller number, it will say, "N must be at least 4!" because a chessboard with less than 4 rows or columns is too small for the queens.

Now, if you use the program correctly with a good N, it will show you all the ways you can place the queens on the chessboard without attacking each other. It will print each solution, one by one. Don't worry about the order; it can show the solutions in any way it likes.

Let's see some examples of how the program works:

Example 1:
```
nqueens 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Example 2:
```
nqueens 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

Each line in the output represents a solution, and it shows the row and column where the queen should be placed. So, the program is like a genius friend who helps us solve the queen puzzle and shows us all the correct ways to do it! 🧙‍♀️
