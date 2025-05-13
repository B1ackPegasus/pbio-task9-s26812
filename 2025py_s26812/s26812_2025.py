# Description:
# This program can:
# Generate a random DNA sequence composed of A, C, G, and T nucleotides.
# Insert your name into the sequence.
# Save the sequence in FASTA format to the file with the name of the provided sequence ID.
# Calculate and display nucleotide percentages and CG/AT ratio statistics.

# Context: This program can be used to generate a DNA sequence and write it in a FASTA format.
# It will provide you statistics on the generated data. Also, it will insert your name into the sequence,
# which can be used as a watermark for sequence.
# Also, the result of this program could be used to test some other software.
# For example, which is used to identify errors in FASTA sequences.

# Used to generate random DNA sequences and insertion points
import random
# Used for checking the existence of a file
import os

# ORIGINAL:
# length = input("Enter the sequence length: ")

# MODIFIED (add validation to check if the length is greater than 0 and conversion to integer):
# Wait integer input from the user for length
length = int(input("Enter the sequence length: "))

# Loop that checks if the value from input is greater than 0
while length <= 0:
    # if it is less than 0, asks user for an input again
    length = int(input("Please enter a positive integer for sequence length: "))


# ORIGINAL:
# sequence_id = input("Enter the sequence ID: ")
# description = input("Provide a description of the sequence: ")
# name = input("Enter your name: ")

# MODIFIED (to remove any whitespace characters before and after received inputs):

# Wait string input from user for ID
sequence_id = input("Enter the sequence ID: ").strip()

# Wait string input from user for description
description = input("Provide a description of the sequence: ").strip()

# Wait string input from user for their name
name = input("Enter your name: ").strip()

# List with all nucleotides that can appear in sequence
nucleotides = ['A', 'C', 'G', 'T']

# Generate a sequence of random nucleotides of a given length
sequence = ''.join(random.choices(nucleotides, k=length))

# Randomly choose where to put user's name
insert_pos = random.randint(0, length)

# Insert user's name at a chosen position
sequence = sequence[:insert_pos] + name + sequence[insert_pos:]

# Prepare FASTA filename
filename = f"{sequence_id}.fasta"

# Check if the file with such name already exists
if os.path.exists(filename):
    # Print a message to the console that the file with such name already exists and we will overwrite it
    print(f"Warning: File '{filename}' already exists and will be overwritten.")

# Create or open the file and write data in FASTA format into it
with open(filename, 'w') as fasta_file:
    # Write in file a FASTA header
    fasta_file.write(f">{sequence_id} {description}\n")
    # Write in file a DNA sequence
    fasta_file.write(sequence + "\n")

# Print a message that data was written to the file
print(f"\nThe sequence was saved to the file {filename}")

# ORIGINAL:
# count_A = sequence.count('A')
# count_C = sequence.count('C')
# count_G = sequence.count('G')
# count_T = sequence.count('T')

# total = len(sequence)

# MODIFIED (we need to count all the nucleotides, but not to include the name in our calculations.
# Also, get rid of total variable because we already have a length variable which contains the correct value):

# Count the amount of A nucleotides, excluding letters A from the name
count_A = sequence.count('A') - name.count('A')
# Count the amount of C nucleotides, excluding letters C from the name
count_C = sequence.count('C') - name.count('C')
# Count the amount of G nucleotides, excluding letters G from the name
count_G = sequence.count('G') - name.count('G')
# Count the amount of T nucleotides, excluding letters T from the name
count_T = sequence.count('T') - name.count('T')

# Calculate percentages for A nucleotide
percent_A = (count_A / length) * 100
# Calculate percentages for C nucleotide
percent_C = (count_C / length) * 100
# Calculate percentages for G nucleotide
percent_G = (count_G / length) * 100
# Calculate percentages for T nucleotide
percent_T = (count_T / length) * 100

# ORIGINAL:
# cg_ratio = ((count_C + count_G) / total) * 100

# MODIFIED (we need to calculate the ratio of the C and G nucleotides to A and T,
# not the percentage of C and G nucleotides combined):

# Calculate CG to AT ratio
cg_ratio = ((count_C + count_G) / (count_A + count_T))

# Show header for statistics
print("\nSequence statistics:")
# Show statistics for A nucleotide
print(f"A: {percent_A:.1f}%")
# Show statistics for C nucleotide
print(f"C: {percent_C:.1f}%")
# Show statistics for G nucleotide
print(f"G: {percent_G:.1f}%")
# Show statistics for T nucleotide
print(f"T: {percent_T:.1f}%")
# Show C and G to A and T ratio
print(f"%CG: {cg_ratio:.1f}")
