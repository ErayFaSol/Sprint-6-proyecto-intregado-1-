from scipy import stats as st

#platform hypothesis
def platform_hypothesis(platform1_scores, platform2_scores):
    alpha = 0.05
    results = st.ttest_ind(platform1_scores, platform2_scores)
    print('Valor p:', results.pvalue)
    if results.pvalue < alpha:
        print("Aprobamos la Hipótesis Alternativa")
    else:
        print("Aprobamos la Hipótesis Nula")

def genre_hypothesis(genre1_score,genre2_score):
    alpha= 0.05
    results = st.ttest_ind(genre1_score,genre2_score)
    print('Valor p:', results.pvalue)
    # Si p es menos que alpha podemos rechazar la hipotesis nula 
    if (results.pvalue < alpha):
        print("Aprobamos Hipotesis Alternativa")
    else:
        print("Aprobamos la Hipotesis Nula")
