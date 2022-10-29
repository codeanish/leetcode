package twosum

import (
	"testing"
)

func TestTwoSum(t *testing.T) {
	input := []int{2, 7, 11, 15}
	target := 9
	expected := []int{0, 1}
	actual := twoSum(input, target)

	if !checkExpectedVsActualArray(expected, actual) {
		t.Errorf("Expected %v, got %v", expected, actual)
	}

	example2 := []int{3, 2, 4}
	target2 := 6
	expected2 := []int{1, 2}
	actual2 := twoSum(example2, target2)

	if !checkExpectedVsActualArray(expected2, actual2) {
		t.Errorf("Expected %v, got %v", expected2, actual2)
	}

	example3 := []int{3, 3}
	target3 := 6
	expected3 := []int{0, 1}
	actual3 := twoSum(example3, target3)

	if !checkExpectedVsActualArray(expected3, actual3) {
		t.Errorf("Expected %v, got %v", expected3, actual3)
	}
}

func checkExpectedVsActualArray(expected []int, actual []int) bool {
	if !((expected[0] == actual[0] && expected[1] == actual[1]) || (expected[0] == actual[1] && expected[1] == actual[0])) {
		return false
	}
	return true
}
