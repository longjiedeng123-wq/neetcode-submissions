class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;
        int j = 0;
        int nums_size = nums.size();
        for(int i = 0; i < nums_size*2; ++i) {
            ans.push_back(nums[j]);
            ++j;
            if (j == nums_size)
                j = 0;

        }
        return ans; 
    }
};