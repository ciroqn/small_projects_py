# Codons found at scene (example)
sample = ['GTA','GGG','CAC']

# takes file and appends each line in txt file to variable as string
def read_dna(dna_file):
  dna_data = ''
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line
  return dna_data

# appends three-letter codons to list from dna of suspects
def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    # check index numbers against total num of letters
    if (i + 3) < len(dna):
      # adds blocks of three letters each loop to 'codons' list
      codons.append(dna[i:i+3])
  return codons

# compares suspect's dna to sample found at scene; each time codons match means a +1 to matches variable
def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

# bringing all these functions together to automate the process calling each function with the suscpect's dna
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print "The number of matching codons is %s, so the investigation will continue..." % num_matches
  else:
    print "The evidence suggests this person is not the criminal."

# Now to check whether or not each suspect really is a suspect...
is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
