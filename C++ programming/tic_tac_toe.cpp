#include <iostream>
#include <vector>

// Function to display the game board
void displayBoard(const std::vector<char>& board) {
    std::cout << " " << board[0] << " | " << board[1] << " | " << board[2] << std::endl;
    std::cout << "---|---|---" << std::endl;
    std::cout << " " << board[3] << " | " << board[4] << " | " << board[5] << std::endl;
    std::cout << "---|---|---" << std::endl;
    std::cout << " " << board[6] << " | " << board[7] << " | " << board[8] << std::endl;
}

// Function to check for a win
bool checkWin(const std::vector<char>& board, char player) {
    const int winPatterns[8][3] = {
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, 
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, 
        {0, 4, 8}, {2, 4, 6}            
    };

    for (const auto& pattern : winPatterns) {
        if (board[pattern[0]] == player && board[pattern[1]] == player && board[pattern[2]] == player) {
            return true;
        }
    }
    return false;
}

// Function to check for a draw
bool checkDraw(const std::vector<char>& board) {
    for (char cell : board) {
        if (cell == ' ') {
            return false;
        }
    }
    return true;
}

// Function to switch the current player
char switchPlayer(char currentPlayer) {
    return (currentPlayer == 'X') ? 'O' : 'X';
}

int main() {
    std::vector<char> board(9, ' '); // Initialize a 3x3 game board
    char currentPlayer = 'X'; // X always goes first
    bool gameOn = true;

    while (gameOn) {
        displayBoard(board);

        // Prompt the current player to enter their move
        int move;
        std::cout << "Player " << currentPlayer << ", enter your move (1-9): ";
        std::cin >> move;

        // Validate the move
        if (move < 1 || move > 9 || board[move - 1] != ' ') {
            std::cout << "Invalid move. Try again." << std::endl;
            continue;
        }

        // Update the board with the player's move
        board[move - 1] = currentPlayer;

        // Check for a win
        if (checkWin(board, currentPlayer)) {
            displayBoard(board);
            std::cout << "Player " << currentPlayer << " wins!" << std::endl;
            gameOn = false;
        }
        // Check for a draw
        else if (checkDraw(board)) {
            displayBoard(board);
            std::cout << "The game is a draw!" << std::endl;
            gameOn = false;
        } else {
            // Switch players
            currentPlayer = switchPlayer(currentPlayer);
        }
    }

    // Ask if the players want to play another game
    char playAgain;
    std::cout << "Do you want to play again? (y/n): ";
    std::cin >> playAgain;
    if (playAgain == 'y' || playAgain == 'Y') {
        // Reset the board and start a new game
        std::fill(board.begin(), board.end(), ' ');
        currentPlayer = 'X';
        gameOn = true;
        main(); // Restart the game
    } else {
        std::cout << "Thanks for playing!" << std::endl;
    }

    return 0;
}

