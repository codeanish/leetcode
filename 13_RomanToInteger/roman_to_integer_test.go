package romantointeger

import (
	"testing"
)

func TestRomanToInteger(T *testing.T) {
	firstInput := "III"
	firstResult := romanToInt(firstInput)
	if firstResult != 3 {
		T.Errorf("Expected 3, got %d", firstResult)
	}

	secondInput := "LVIII"
	secondResult := romanToInt(secondInput)
	if secondResult != 58 {
		T.Errorf("Expected 58, got %d", secondResult)
	}

	thirdInput := "IV"
	thirdResult := romanToInt(thirdInput)
	if thirdResult != 4 {
		T.Errorf("Expected 4, got %d", thirdResult)
	}

	fourthInput := "MCMXCIV"
	fourthResult := romanToInt(fourthInput)
	if fourthResult != 1994 {
		T.Errorf("Expected 1994, got %d", fourthResult)
	}
}
