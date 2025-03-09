package main

import (
	"fmt"
	"time"
)

func main() {
	// Capture the start time
	start := time.Now()

	i := 0
	for i < 1_000_000_000 {
		i++
	}

	// Capture the end time
	end := time.Now()

	// Calculate the duration
	duration := end.Sub(start)

	// Format the duration to hundredths of a second
	durationInSeconds := float64(duration) / float64(time.Second)
	fmt.Printf("Execution time: %.2f seconds\n", durationInSeconds)
}
