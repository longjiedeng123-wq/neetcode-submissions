class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> S;
        while(nums.size()>0){
            size_t size = S.size();
            S.insert(nums.back());
            nums.pop_back();
            if(S.size()==size)
                return true;
        }
        return false;
    }
};