package romantointeger

func romanToInt(s string) int {
	romanToIntMap := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	result := 0
	var previousCharacter byte
	for i := 0; i < len(s); i++ {
		character := s[i]
		valueOfCharacter := romanToIntMap[character]
		valueOfPreviousCharacter := romanToIntMap[previousCharacter]
		if valueOfCharacter > valueOfPreviousCharacter {
			result += valueOfCharacter - 2*valueOfPreviousCharacter
		} else {
			result += valueOfCharacter
		}
		previousCharacter = character
	}
	return result
}
