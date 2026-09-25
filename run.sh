SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
source "$SCRIPT_DIR/run.flags"

run_test() {
    local label=$1
    local input_path=$2
    local expected_path=$3

    # Create a unique temporary file
    local tmp_output_path
    tmp_output_path=$(mktemp)
    trap 'rm -f "$tmp_output_path"' EXIT

    echo "Running on $label..."
    echo "Input file: $input_path"
    echo "Expected output file: $expected_path"
    echo "Temporary output file: $tmp_output_path"
    if [[ ! -f "$input_path" ]]; then
        echo "Error: Input file $input_path not found."
        return 1
    fi

    python3 "$CODE_PATH" < "$input_path" > "$tmp_output_path"
    
    if [[ -f "$expected_path" ]]; then
        if diff "$tmp_output_path" "$expected_path" > /dev/null; then
            echo "PASSED"
        else
            echo "FAILED"
            diff "$tmp_output_path" "$expected_path"
        fi
    else
        echo "Warning: Expected output file $expected_path not found. Results saved to $tmp_output_path"
    fi
    echo ""
}

run_test "sample test set" \
    "$INPUT_ROOT_DIR/sample_test_set_1/sample_ts1_input.txt" \
    "$INPUT_ROOT_DIR/sample_test_set_1/sample_ts1_output.txt"

run_test "test set 1" \
    "$INPUT_ROOT_DIR/test_set_1/ts1_input.txt" \
    "$INPUT_ROOT_DIR/test_set_1/ts1_output.txt"

run_test "test set 2" \
    "$INPUT_ROOT_DIR/test_set_2/ts2_input.txt" \
    "$INPUT_ROOT_DIR/test_set_2/ts2_output.txt"
