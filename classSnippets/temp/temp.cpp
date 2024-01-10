#include <iostream>

using namespace std;

int main()
{
    cout << "Enter a temperature in degrees fahrenheit" << endl;
    double fahrenheit;
    cin >> fahrenheit;

    double celsius = (fahrenheit - 32) * 5 / 9;
    cout << "The temperature in degrees celsius is " << celsius << endl;
}