def process_file():
    try:
        # Get input and output filenames from user
        input_filename = input("Enter the input filename: ")
        output_filename = input("Enter the output filename: ")

        # Try to open and read input file
        with open(input_filename, 'r') as input_file:
            content = input_file.readlines()

        # Process the content (convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Write modified content to output file
        with open(output_filename, 'w') as output_file:
            output_file.writelines(modified_content)

        print(f"\nSuccess! Modified content written to {output_filename}")
        
    except FileNotFoundError:
        print(f"\nError: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"\nError: Permission denied to access the file.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
    finally:
        print("\nFile processing completed.")

# Run the program
print("File Processing Program")
print("----------------------")
process_file()