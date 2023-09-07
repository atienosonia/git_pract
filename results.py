def first_term_results():
    mathematics = int(input('Mathematics Score: '))
    english = int(input('English Score: '))
    science = int(input('Science Score: '))
    social_studies = int(input('Social Studies Score: '))

    total_score = sum([mathematics, english, science, social_studies])
    return total_score

term_1_results = first_term_results()
print(f'Total Score is {term_1_results}')

