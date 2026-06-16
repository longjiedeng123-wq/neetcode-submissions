#include <vector>
#include <map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hash;
        for(int i = 0; i < nums.size(); ++i) {
            int difference = target - nums[i];
            if (!hash.contains(difference)){
                hash[nums[i]] = i;
            } else {
                return vector<int>{hash[difference], i};
            }
        }
    }
};
