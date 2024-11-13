#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
    while (true)
    {
        int random = rand() % 6 + 1;
        string x;
        cout << "Dice roll: ";
        cout << random;
        cout << "\nPress enter to roll again\n";
        cin >> x;
    }
    return 0;
}
