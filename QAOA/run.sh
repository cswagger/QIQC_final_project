#!/bin/bash

TEST_DIR="../testcases/maximal_normal_testcases"
PYTHON_SCRIPT="clique_QAOA.py"
REPS_LIST=(1 2 4 6 8 10 12 16 20 24 28 32 36 40)
TEST_LIST=(3 7 11 17 21 26 31 36 41 30 31 32 33 34)

# n, m
# testcase3: 4, 5
# testcase7: 5, 8
# testcase11: 6, 7
# testcase17: 7, 8
# testcase21: 8, 8
# testcase26: 9, 8
# testcase31: 10, 18
# testcase36: 11, 16
# testcase41: 12, 20

# testcase30: 10, 5
# testcase31: 10, 18
# testcase32: 10, 26
# testcase33: 10, 35
# testcase34: 10, 39

MAX_RUNS=3

RESULT_FILE="results.txt" > "$RESULT_FILE"

validate_correctness() {
    local testfile=$1
    local answerfile=$2
    local reps=$3
    local pass_count=0

    for run in $(seq 1 "$MAX_RUNS"); do
        echo "Running file: $file with reps: $reps (Run $run)"
        python3 "$PYTHON_SCRIPT" "$testfile" "$answerfile" "$reps" 2> /dev/null 1>/dev/null
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

