import csv
import sys


def main():

    # Assign file names to vars
    file_arg = ''
    dna_seq_file = ''

    # Check for command-line usage
    if len(sys.argv) == 3:
        file_arg = sys.argv[1]
        dna_seq_file = sys.argv[2]
    else:
        print("Error. You should have three command-line arguments.")

    # Get rows of data, fieldnames, and names to whom the DNA (might) belong
    rows = []
    fieldnames = []
    names = []

    # Read database file into a variable
    with open(file_arg) as file:
        reader = csv.reader(file)
        # Assign the STRs to a list (exclude the name of the person)
        fieldnames = next(reader)[1:]
        # Add rows of data to 'rows' and names of people to separate
        # list, 'names'
        for row in reader:
            names.append(row[0])
            rows.append(row[1:])

    # Convert strings to ints in 'rows' list for
    # later conditional
    for row in rows:
        for i in range(len(row)):
            row[i] = int(row[i])

    # Read DNA sequence file into a variable
    dna_string = ''
    with open(dna_seq_file) as file:
        dna_string = file.readline()

    # Find longest match of each STR in DNA sequence
    seq_list = []

    for seq in fieldnames:
        match = longest_match(dna_string, seq)
        seq_list.append(match)

    # Check database for matching profiles
    person_name = ''

    # Compare the STR counts for each person to the
    # STR counts in the sample sequence
    for idx, str_counts in enumerate(rows):
        if str_counts == seq_list:
            person_name = names[idx]
            break

    # Determine if there's a DNA match
    if person_name == '':
        print('No match')
    else:
        print(person_name)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialise count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
