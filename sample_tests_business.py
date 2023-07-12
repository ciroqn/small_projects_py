# using 1 and 2 Sample T-Tests and Chi square tests to justify marketing

# fm not available here in GitHub
import familiar as fm
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency


vein_pack_lifespans = fm.lifespans(package='vein')

# is vein pack subscriber's lifespan significantly differen from avg. at 71?
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)

print vein_pack_lifespans
print vein_pack_test.pvalue

# p value < 0.05, so null rejected
if vein_pack_test.pvalue < 0.05:
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
  print("The Vein Pack Is Probably Good For You Somehow!")

# lifespans of artery pack
artery_pack_lifespans = fm.lifespans(package='artery')

package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)

if package_comparison_results < 0.05:
  print("The Artery Package guarantees even stronger results!")
else:
  print("The Artery Package is also a great product!")

# get iron counts for respondents
iron_contingency_table = fm.iron_counts_for_package()

a, pvalue_iron, b, c = chi2_contingency(iron_contingency_table)

print pvalue_iron

if pvalue_iron < 0.05:
  print("The Artery Package Is Proven To Make You Healthier!")
else:
  print("While We Can't Say The Artery Package Will Help You, I Bet It's Nice!")
