#include <iostream>
#include <vector>

#define board_t std::vector<std::vector<int>>

void PrintBoard(board_t board)
{
    for (std::vector<int> row : board)
    {
        for (int cell : row)
        {
            std::cout << cell << " ";
        }
        std::cout << std::endl;
    }
}

board_t MakeBoard(int rows, int cols)
{
    board_t board;
    for (int row = 0; row < rows; row++)
    {
        board.push_back({});
        for (int col = 0; col < cols; col++)
        {
            board.back().push_back(0);
        }
    }
    return board;
}

bool IsValid(board_t board, int targetRow, int targetCol)
{
    int rows = board.size();
    int cols = board[0].size();

    // Check cell
    if (board[targetRow][targetCol] != 0)
    {
        return false;
    }

    // Check row
    for (int row = 0; row < rows; row++)
    {
        if (board[row][targetCol] != 0)
        {
            return false;
        }
    }

    // Check column
    for (int col = 0; col < cols; col++)
    {
        if (board[targetRow][col])
        {
            return false;
        }
    }

    // Check top-left diagonal
    int row = targetRow;
    int col = targetCol;
    while (row >= 0 && col >= 0)
    {
        if (board[row][col] != 0)
        {
            return false;
        }
        row--;
        col--;
    }

    // Check top-right diagonal
    row = targetRow;
    col = targetCol;
    while (row >= 0 && col < cols)
    {
        if (board[row][col] != 0)
        {
            return false;
        }
        row--;
        col++;
    }

    // Check bottom-left diagonal
    row = targetRow;
    col = targetCol;
    while (row < rows && col >= 0)
    {
        if (board[row][col] != 0)
        {
            return false;
        }
        row++;
        col--;
    }

    // Check bottom-right diagonal
    row = targetRow;
    col = targetCol;
    while (row < rows && col < cols)
    {
        if (board[row][col] != 0)
        {
            return false;
        }
        row++;
        col++;
    }

    return true;
}

bool PlaceNQueens(board_t &board, int queens)
{
    if (queens == 0)
    {
        return true;
    }

    int rows = board.size();
    int cols = board[0].size();

    for (int row = 0; row < rows; row++)
    {
        for (int col = 0; col < cols; col++)
        {
            if (IsValid(board, row, col))
            {
                board[row][col] = 1;

                if (PlaceNQueens(board, queens - 1))
                {
                    return true;
                }

                board[row][col] = 0; // Backtrack
            }
        }
    }

    return false;
}

int main()
{
    int n = 8;
    board_t board = MakeBoard(n, n);

    if (PlaceNQueens(board, n))
    {
        PrintBoard(board);
    }
    else
    {
        std::cout << "No solution found" << std::endl;
    }

    return 0;
}