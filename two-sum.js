/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // 暴力解：O(n^2)
    for (let i = 0; i < nums.length; i++) {
        for (let j = 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j];
            } 
        }
    }
    // Hash table
    const map = {};
    for (let i = 0; i < nums.length; i++) {
        const detect = target - nums[i];
        if (map[detect] !== undefined && map[detect] !== i) {
            return [map[detect], i];
        }
        map[nums[i]] = i;
    }
};