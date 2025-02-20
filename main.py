/*
Helmer Gomez            3/2023

Tower of Hanoi Puzzle with 4 "blocks" (characters - A, B, C & D) and 3 character vectors T1, T2 & T3
Prompt the user to enter a source T and a destination T.

Commands used
Ranged loops
Do while loops
vectors 

*/
#include <iostream>
#include <vector>
#include <algorithm>                                //Header file for sort function
using namespace std;

void boardDisplay(void);
void towerToMove(void);                                    //Tower selection
void destinationOfTower(void);                            //Tower destination
int protectInt(string);                                //Choosing only from 3 towers
void winCondition(void);

vector<char> win{ 'A','B','C', 'D' };
vector<char> T1{ 'A','B','C', 'D' };
vector<char> T2{};
vector<char> T3{};
char temp{};

bool gameWon{ false };

int main() {
    while (!gameWon) {                    //While loop until game is finished
        boardDisplay();
        towerToMove();
        destinationOfTower();
        winCondition();

        if (gameWon) {
            boardDisplay();
            cout << "\n\nYOU WIN\n";
        }
    }
}
void boardDisplay() {
    cout << "\nT1";
    for (char x : T1) {            //Ranged Loop to display board
        cout << "\t" << x;
    }

    cout << "\n\nT2";
    for (char x : T2) {
        cout << "\t" << x;
    }

    cout << "\n\nT3";
    for (char x : T3) {
        cout << "\t" << x;
    }
}
void towerToMove() {
    bool flag{ false };

    do {                // while loop used until they choose a valid tower that is not empty
        int inputChoice{};
        inputChoice = protectInt("\nChoose a source Tower 1, 2, or 3: ");
        if (inputChoice == 1) {
            if (T1.size() == 0) {
                flag = false;
            }
            else {
                temp = T1[(T1.size() - 1)];
                T1.pop_back();
                flag = true;
            }
        }
        if (inputChoice == 2) {
            if (T2.size() == 0) {
                flag = false;
            }
            else {
                temp = T2[(T2.size() - 1)];
                T2.pop_back();
                flag = true;
            }
        }
        if (inputChoice == 3) {
            if (T3.size() == 0) {
                flag = false;
            }
            else {
                temp = T3[(T3.size() - 1)];
                T3.pop_back();
                flag = true;
            }
        }
        if (!flag) {
            cout << "\nEmpty tower. Choose a different Tower ";
        }
    } while (!flag);
}
void destinationOfTower() {
    bool flag{ false };
    int inputChoice{};

    do {                                                                        //Do-while loop until a proper destination tower is inputed
        vector<char> test{};
        inputChoice = protectInt("\nChoose a destination Tower 1, 2, or 3: ");
        if (inputChoice == 1) {
            T1.push_back(temp);

            for (char i : T1) {
                test.push_back(i);                                            //Adds Char to the vector
            }
            sort(test.begin(), test.end());
            if (test != T1) {
                flag = false;
                T1.pop_back();                                            //Removes Char from vector if it does not follow rule
            }
            else {
                flag = true;
            }
        }
        if (inputChoice == 2) {
            T2.push_back(temp);

            for (char i : T2) {
                test.push_back(i);
            }
            sort(test.begin(), test.end());
            if (test != T2) {
                flag = false;
                T2.pop_back();
            }
            else {
                flag = true;
            }
        }
        if (inputChoice == 3) {
            T3.push_back(temp);
            for (char i : T3) {
                test.push_back(i);
            }
            sort(test.begin(), test.end());
            if (test != T3) {
                flag = false;
                T3.pop_back();
            }
            else {
                flag = true;
            }
        }
        if (!flag) {
            cout << "Does not follow rule. Choose a different tower to place letter on or place it back.";
        }
    } while (!flag);
}
int protectInt(string prompt) {
    int inputChoice{};                                    //proctects from numbers outside of 1-3
    cout << prompt;
    cin >> inputChoice;

    while (inputChoice > 3 || inputChoice < 1) {
        cout << "\nInvalid number (choose 1-3)";
        cout << prompt;
        cin >> inputChoice;

    }
    return inputChoice;
}

void winCondition() {
    if (win == T3) {                    //Win condition compares win vector with T3
        gameWon = true;
    }
}
