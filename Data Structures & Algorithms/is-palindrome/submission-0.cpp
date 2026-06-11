#include <cctype>
class Solution {
public:
    bool isPalindrome(string s) {
        auto front = s.begin();
        auto back = s.end()-1;
        bool f_isalnum;
        bool b_isalnum; 
        while(front < back){
            f_isalnum = std::isalnum(*front);
            b_isalnum = std::isalnum(*back);
            if (f_isalnum && b_isalnum) {
                if (std::tolower(*front)!=std::tolower(*back))
                    return false;
                ++front;
                --back;
            } else {
                if(!f_isalnum){
                    ++front;
                }
                if(!b_isalnum){
                    --back;
                }    
            }
        }
        return true;
    }
};
