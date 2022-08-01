package main

import "fmt"

func main() {
	var line string
	fmt.Scanln(&line)

	var letter_counts = make(map[rune]int)

	for _, c := range line {
		letter_counts[c] += 1
	}

	var odd_count = 0
	for _, count := range letter_counts {
		if count%2 == 1 {
			odd_count += 1
		}
	}

	var remove_count = 0
	if odd_count > 1 {
		remove_count += odd_count - 1
	}

	fmt.Println(remove_count)
}
