def extract_ranges_from_file(input_file, ranges, output_files):
    # Ensure the ranges and output_files lists have the same length
    if len(ranges) != len(output_files):
        raise ValueError("Ranges and output files lists must have the same length.")
    
    # Read the content of the input file
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Extract each range and write to corresponding output file
    for i, (start, end) in enumerate(ranges):
        extracted_content = content[start:end]
        with open(output_files[i], 'w') as output_file:
            output_file.write(extracted_content)

# Define the ranges and corresponding output files
ranges = [(0, 24), (24, 54), (54, 89), (89, 110)]
output_files = ['lsinsulin-seq-clean.txt', 'binsulin-seq-clean.tx', 'cinsulin-seq-clean.txt', 'ainsulin-seq-clean.txt']

# Call the function with the input file name, ranges, and output file names
extract_ranges_from_file('preproinsulin-seq-clean.txt', ranges, output_files)