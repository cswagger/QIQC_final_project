#!/bin/bash

# Define the output directory for test cases
output_dir="k_clique_normal_testcases"
mkdir -p "$output_dir"

# Initialize the counter variable
counter=0
values_1=(0.1 0.4 0.7 0.95)

# Loop over the first argument range
for arg1 in {4..35}; do
    # Loop over the second argument with a step
    for arg2 in "${values_1[@]}"; do
        
        for arg3 in $(seq $((arg1 - 1)) $((arg1 + 1))); do
            MIN=1     
            MAX=$arg1        
            RANDOM_NUMBER=$((RANDOM % (MAX - MIN + 1) + MIN))
            # Run the Python script and capture the output
            output=$(python3 gen_k_clique.py "$arg1" "$arg2" "$RANDOM_NUMBER")
            
            # Write the output to a temporary file to measure lines
            temp_output_file="temp_output.txt"
            echo "$output" > "$temp_output_file"
            edge_num=$(echo "$output" | awk 'NR==1 {print $2}')
            
            # Calculate total lines in the output
            total_lines=$(wc -l < "$temp_output_file")
            
            # Define input and output file names
            infile="${output_dir}/testcase${counter}_in.txt"
            outfile="${output_dir}/testcase${counter}_out.txt"

            
            # Write all except the last 2 lines to infile
            if [ "$total_lines" -gt 1 ]; then
                head -n "$((edge_num + 1))" "$temp_output_file" > "$infile"
            else
                # Handle cases where there are fewer than 2 lines
                echo "Warning: Not enough lines in output for testcase${counter}"
                > "$infile"  # Create an empty infile
            fi

            # Write only the last 2 lines to outfile
            tail -n +$((edge_num + 2)) "$temp_output_file" > "$outfile"

            # Increment the counter
            counter=$((counter + 1))
        done
    done
done

# Clean up the temporary file
rm -f "$temp_output_file"
