package twosum

func twoSum(nums []int, target int) []int {
	// Previously didn't pre-allocate the map, and it was slower (marginally)
	potentialAnswers := make(map[int]int, len(nums))

	for i := 0; i < len(nums); i++ {

		requiredAnswer := target - nums[i]
		if val, ok := potentialAnswers[requiredAnswer]; ok {
			return []int{i, val}
		}
		potentialAnswers[nums[i]] = i
	}
	return []int{}
}
