# using binomial, ANOVA and Tukey tests for data analysis

import numpy as np
import fetchmaker as f
from scipy.stats import binom_test, f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# get_weight()
# get_tail_length()
# get_color()
# get_age()
# get_is_rescue()

# rottweiler data
rottweiler_tl = f.get_tail_length("rottweiler")

print rottweiler_tl
print np.mean(rottweiler_tl)
print np.std(rottweiler_tl)

# percentage of whippets being rescue
whippet_rescue = f.get_is_rescue("whippet")

num_whippet_rescue = np.count_nonzero(whippet_rescue)

print num_whippet_rescue

# number of samples in whippet dataset
num_whippets = np.size(whippet_rescue)

print num_whippets

# binomial test on whippet rescues in dataset
whippet_rescue_binom = binom_test(6, num_whippet_rescue, 0.08)

print whippet_rescue_binom
# 2.62144e-07 (null rejected)

# ANOVA test. weights for three popular dog breeds: whippets, terriers, pitbulls
whippet_weights = f.get_weight("whippet")
terrier_weights = f.get_weight("terrier")
pitbull_weights = f.get_weight("pitbull")

pvalue_weights = f_oneway(whippet_weights, terrier_weights, pitbull_weights)

print pvalue_weights.pvalue
# 3.27641558827e-17 (null rejected - weights of different breeds not similar, but which pair). requires tukey

# Given ANOVA results, determine Tukey: first concat list and associate el to each datast
all_weight_data = np.concatenate([whippet_weights, terrier_weights, pitbull_weights])
labels = ['Whippet'] * len(whippet_weights) + ['Terrier'] * len(terrier_weights) + ['Pitbull'] * len(pitbull_weights)

# Tukey Test: 0.05 is the significance threshold
tukey_results = pairwise_tukeyhsd(all_weight_data, labels, 0.05)

print tukey_results

#Multiple Comparison of Means - Tukey HSD,FWER=0.05
#==============================================
# group1  group2 meandiff  lower  upper  reject
#----------------------------------------------
#Pitbull Terrier  -13.24  -16.728 -9.752  True 
#Pitbull Whippet  -3.34    -6.828 0.148  False 
#Terrier Whippet   9.9     6.412  13.388  True 
#----------------------------------------------

# finding poodle and shihtzu colours
poodle_colours = f.get_color("poodle")
shihtzu_colours = f.get_color("shihtzu")

# num of occurrences of colour X
num_brown_poodles = np.count_nonzero(poodle_colours == "brown")
num_black_poodles = np.count_nonzero(poodle_colours == "black")
num_gold_poodles = np.count_nonzero(poodle_colours == "gold")
num_grey_poodles = np.count_nonzero(poodle_colours == "grey")
num_white_poodles = np.count_nonzero(poodle_colours == "white")

num_brown_shihtzu = np.count_nonzero(shihtzu_colours == "brown")
num_black_shihtzu = np.count_nonzero(shihtzu_colours == "black")
num_gold_shihtzu = np.count_nonzero(shihtzu_colours == "gold")
num_grey_shihtzu = np.count_nonzero(shihtzu_colours == "grey")
num_white_shihtzu = np.count_nonzero(shihtzu_colours == "white")

# chi square contingency table 
colour_table = [[num_black_poodles, num_black_shihtzu],
  [num_brown_poodles, num_brown_shihtzu],
  [num_gold_poodles, num_gold_shihtzu],
  [num_grey_poodles, num_grey_shihtzu],
  [num_white_poodles, num_white_shihtzu]]

chi2, pval_col, dof, expected = chi2_contingency(colour_table)

print pval_col
# 0.00530240829324 (null rejected -colours dissimilar)
