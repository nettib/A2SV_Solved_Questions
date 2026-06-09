/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let track = new Map();

    for (i=0; i < nums.length; i++) {
        if (track.has(target - nums[i])) {
            return [track.get(target - nums[i]), i]
        } else {
            track.set(nums[i], i)
        }
    }
    
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna