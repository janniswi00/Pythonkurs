from math import comb

def probability_calculation(k, m, n):
    total = k + m + n
    total_pairs = comb(total, 2)

    prob_AA_AA = comb(k, 2) / total_pairs * 1
    prob_AA_Aa = (k * m) / total_pairs * 1
    prob_AA_aa = (k * n) / total_pairs * 1
    prob_Aa_Aa = comb(m, 2) / total_pairs * 0.75
    prob_Aa_aa = (m * n) / total_pairs * 0.5
    prob_aa_aa = comb(n, 2) / total_pairs * 0

    prob_sum = prob_AA_AA + prob_AA_Aa + prob_AA_aa + prob_Aa_Aa + prob_Aa_aa + prob_aa_aa

    return prob_sum

probability_calculation(19,20,28)