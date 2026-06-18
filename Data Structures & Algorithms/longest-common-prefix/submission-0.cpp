class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string longest{};
        int strs_size = strs.size();
        int shortest_len{201};
        for(int i = 0; i < strs_size; ++i){
            int strs_len = strs[i].length();
            if(strs_len<shortest_len)
                shortest_len = strs_len;
        }
        for(int i = 0; i < shortest_len; ++i) {
            for(int j = 1; j < strs_size; ++j){
                if(strs[j][i]!=strs[j-1][i])
                    return longest;
            }
            longest += strs[0][i];
        }
        return longest;
    }
};