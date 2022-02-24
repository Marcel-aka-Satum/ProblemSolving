#include <vector>
using namespace std;


int countSmileys(std::vector<std::string> arr)
{
    int n = 0;
    bool smiley = false;
    bool smile = false;
    for(auto i : arr){
        for(auto j : i){
            if(j == ':' || j == ';' || j == '-' || j == '~'){
                smiley = true;
            } else if(j == ')' || j == 'D'){
                smile = true;
            }else{
                smiley = false;
                smile = false;
                break;
            }
        }
        if(smiley && smile){
            n++;
        }
    }
    return n;
}
