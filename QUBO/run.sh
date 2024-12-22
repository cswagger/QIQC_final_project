#!/bin/bash

TEST_DIR="../testcases/normal_testcases"
PYTHON_SCRIPT="clique_QUBO.py"
REPS_LIST=(1 2 4 8 12 16 20 24 28 32)
TEST_LIST=(0 4 8 12 16 20 24 28 32 36 40)
MAX_RUNS=3

RESULT_FILE="results.txt" > "$RESULT_FILE"

validate_correctness() {
    local testfile=$1
    local answerfile=$2
    local reps=$3
    local pass_count=0

    for run in $(seq 1 "$MAX_RUNS"); do
        echo "Running file: $file with reps: $reps (Run $run)"
        python3 "$PYTHON_SCRIPT" "$testfile" "$answerfile" "$reps" 2> /dev/null
        if [ $? -eq 0 ]; then
            pass_count=$((pass_count + 1))
        else
            break
        fi
    done

    if [ "$pass_count" -eq "$MAX_RUNS" ]; then
        return 0
    else
        return 1
    fi
}

for number in "${TEST_LIST[@]}"; do
    testfile="$TEST_DIR/testcase${number}_in.txt"
    answerfile="$TEST_DIR/testcase${number}_out.txt"
    echo "Testing file: $testfile" | tee -a "$RESULT_FILE" 

    # Iterate through different reps
    for reps in "${REPS_LIST[@]}"; do
        echo "Testing with reps: $reps" | tee -a "$RESULT_FILE"

        # Validate correctness for this combination
        validate_correctness "$testfile" "$answerfile" "$reps"
        if [ $? -eq 0 ]; then
            echo "File: $file, Reps: $reps -> All correct" | tee -a "$RESULT_FILE"
            echo "Desired reps for $file: $reps" | tee -a "$RESULT_FILE"
            break
        else
            echo "File: $file, Reps: $reps -> Failed" | tee -a "$RESULT_FILE"
        fi
    done
done

