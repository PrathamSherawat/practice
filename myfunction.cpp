#include<iostream>
using namespace std;
void myFunction() {
    int x=5;
    int y=6;
    int sum=x+y;
    cout << sum << endl;
    cout << "I just got executed!";
}

int main() {
  myFunction();
  return 0;
}