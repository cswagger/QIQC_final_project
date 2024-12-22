#!/bin/bash

TEST_DIR="test"  # Adjust this to your test directory
PYTHON_SCRIPT="clique_program.py"  # Replace with your Python script name
REPS_LIST=(5 10 15 20)  # List of reps to test
MAX_RUNS=5  # Number of times to run each combination of {reps, file}

RESULT_FILE="results.txt" > "$RESULT_FILE"

validate_correctness() {
    local file=$1
    local reps=$2
    local pass_count=0

    for run in $(seq 1 "$MAX_RUNS"); do
        echo "Running file: $file with reps: $reps (Run $run)"
        # Run the Python script with the input file and reps
        python "$PYTHON_SCRIPT" --input "$file" --reps "$reps"
        if [ $? -eq 0 ]; then
            pass_count=$((pass_count + 1))
        fi
    done

    # If all runs are correct, return success
    if [ "$pass_count" -eq "$MAX_RUNS" ]; then
        return 0  # All runs passed
    else
        return 1  # At least one run failed
    fi
}

for file in "$TEST_DIR"/*; do
    echo "Testing file: $file" | tee -a "$RESULT_FILE"

    # Iterate through different reps
    for reps in "${REPS_LIST[@]}"; do
        echo "Testing with reps: $reps" | tee -a "$RESULT_FILE"

        # Validate correctness for this combination
        validate_correctness "$file" "$reps"
        if [ $? -eq 0 ]; then
            echo "File: $file, Reps: $reps -> All correct" | tee -a "$RESULT_FILE"
            echo "Desired reps for $file: $reps" | tee -a "$RESULT_FILE"
            break  # No need to test higher reps
        else
            echo "File: $file, Reps: $reps -> Failed" | tee -a "$RESULT_FILE"
        fi
    done
done

