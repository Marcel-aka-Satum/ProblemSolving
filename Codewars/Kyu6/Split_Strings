#include <string>
#include <iostream>
#include <vector>

using namespace std;

vector<string> solution(const string &s) {
    vector<string> a;
    string d;
    for (auto i = 0; i < s.size(); i++) {
        cout << "d = " << d << endl;
        if (d.size() <= 1) {
            d.push_back(s[i]);
        } else if (d.size() == 2) {
            a.push_back(d);
            d = "";
            d.push_back(s[i]);
        }

        //check last case for _
        if(i == s.size()-1){
            if(d.size() == 1){
                d.push_back('_');
            }
            a.push_back(d);
        }
    }
    return a;
}
