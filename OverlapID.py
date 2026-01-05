import os

def find_overlaps():
    # Prompt user for the locations of the first and second text files
    file1_path = input("Please enter the location of the first text file: ")
    file2_path = input("Please enter the location of the second text file: ")

    try:
        # Create the output directory if it doesn't exist
        output_dir = r"C:\python\CHATGPT"
        os.makedirs(output_dir, exist_ok=True)
        
        # Output file path
        output_file_path = os.path.join(output_dir, "overlaps.txt")

        # Read content of the first and second files
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            # Store all lines from the second file for repeated access
            file2_lines = file2.readlines()

            # Open the output file for writing results
            with open(output_file_path, 'w') as outfile:
                # Process each line in the first file
                for line1 in file1:
                    # Split the line into parts by tabs
                    parts1 = line1.strip().split("\t")
                    key1 = parts1[0]
                    range1_start = int(parts1[1])
                    range1_end = int(parts1[2])
                    
                    # Track if any matching line is found
                    match_found = False
                    matching_lines = []

                    # Check each line in the second file for matching key and range overlap
                    for line2 in file2_lines:
                        parts2 = line2.strip().split("\t")
                        key2 = parts2[0]
                        range2_start = int(parts2[1])
                        range2_end = int(parts2[2])

                        # Check if the first values match and if ranges overlap
                        if key1 == key2 and (
                            (range1_start <= range2_start <= range1_end) or
                            (range1_start <= range2_end <= range1_end)
                        ):
                            # Add the entire matching line from file2 to matching lines list
                            matching_lines.append(line2.strip())
                            match_found = True
                    
                    # Write the line from file1 with matches or "0" if no matches
                    if match_found:
                        outfile.write(f"{line1.strip()}\t" + "\t".join(matching_lines) + "\n")
                    else:
                        outfile.write(f"{line1.strip()}\t0\n")

        print(f"Results saved successfully in {output_file_path}")

    except FileNotFoundError:
        print("One or both files were not found. Please check the file locations and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
find_overlaps()
