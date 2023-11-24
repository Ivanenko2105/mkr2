import word
import random
import lwa
import numpy as np
import my_words_model
import model
import t2_mandani_inference
import streamlit as st

input_lvs = [
    {
        'X': (1, 12),
        'name': 'Communication',
		'terms': {
			'Ineffective': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
            'Average': {'umf': ('trapmf', 0.42, 2.25, 4.00, 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 0.34, 3.71)},
            'Effective': {'umf': ('trapmf', 3.38, 5.50, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 0.33, 6.67)},
            'Exceptional': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
		}
    },

    {
        'X': (1, 12),
        'name': 'Professional skills',
        'terms': {
			'Inadequate': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
			'Basic': {'umf': ('trapmf', 0.42, 2.25, 4., 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 3.71, 0.34)},
			'Competent': {'umf': ('trapmf', 1.59, 2.75, 4.35, 6.26), 'lmf': ('trapmf', 2.79, 3.34, 3.34, 3.67, 0.35)},
			'Advanced': {'umf': ('trapmf', 3.38, 5.5, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 6.67, 0.33)},
			'Expert': {'umf': ('trapmf', 4.59, 5.9, 7.25, 8.5), 'lmf': ('trapmf', 6.29, 6.67, 6.67, 7.17, 0.39)},
			'Professional': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
        }
    },

    {
        'X': (1, 12),
        'name': 'Leadership',
		'terms': {
			'Lack': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
			'Limited': {'umf': ('trapmf', 0.42, 2.25, 4., 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 3.71, 0.34)},
			'Moderate': {'umf': ('trapmf', 1.59, 2.75, 4.35, 6.26), 'lmf': ('trapmf', 2.79, 3.34, 3.34, 3.67, 0.35)},
			'Effective': {'umf': ('trapmf', 3.38, 5.5, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 6.67, 0.33)},
			'Strong': {'umf': ('trapmf', 4.59, 5.9, 7.25, 8.5), 'lmf': ('trapmf', 6.29, 6.67, 6.67, 7.17, 0.39)},
			'Exceptional': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
		}
    },

    {
        'X': (1, 12),
        'name': 'Adaptability',
        'terms': {
            'Limited': {'umf': ('trapmf', 0, 0, 0.55, 4.61), 'lmf': ('trapmf', 0, 0, 0.09, 1.15, 1)},
            'Moderate': {'umf': ('trapmf', 0.42, 2.25, 4.00, 5.41), 'lmf': ('trapmf', 2.79, 3.21, 3.21, 0.34, 3.71)},
            'Good': {'umf': ('trapmf', 3.38, 5.50, 7.25, 9.02), 'lmf': ('trapmf', 5.79, 6.28, 6.28, 0.33, 6.67)},
            'Exceptional': {'umf': ('trapmf', 7.37, 9.36, 10, 10), 'lmf': ('trapmf', 8.68, 9.91, 10, 10, 1)},
        }
    }
]

output_lv = {
    'X': (1, 12),
    'name': 'Evaluation',
    'terms': {
		'Unprofessional': {'umf': ('trapmf', 0, 0, 0.14, 1.97), 'lmf': ('trapmf', 0, 0, 0.05, 0.66, 1)},
        'Irresponsible': {'umf': ('trapmf', 0.59, 1.50, 2.00, 3.41), 'lmf': ('trapmf', 0.79, 1.68, 1.68, 2.21, 0.74)},
        'Satisfactory': {'umf': ('trapmf', 0.59, 2.00, 3.25, 4.41), 'lmf': ('trapmf', 2.29, 2.70, 2.70, 3.21, 0.42)},
        'Average': {'umf': ('trapmf', 1.28, 3.50, 5.50, 7.83), 'lmf': ('trapmf', 3.79, 4.41, 4.41, 4.91, 0.36)},
        'Competent': {'umf': ('trapmf', 2.59, 4.00, 5.50, 7.62), 'lmf': ('trapmf', 4.29, 4.75, 4.75, 5.21, 0.38)},
        'Effective': {'umf': ('trapmf', 3.38, 5.50, 7.50, 9.62), 'lmf': ('trapmf', 5.79, 6.50, 6.50, 7.21, 0.41)},
        'Highly Qualified': {'umf': ('trapmf', 4.38, 6.50, 8.25, 9.62), 'lmf': ('trapmf', 7.19, 7.58, 8.21, 9.21, 0.37)},
        'Expert': {'umf': ('trapmf', 5.98, 7.75, 8.60, 9.52), 'lmf': ('trapmf', 8.03, 8.37, 8.57, 9.17, 0.57)},
        'Exceptional': {'umf': ('trapmf', 8.68, 9.91, 10, 10), 'lmf': ('trapmf', 9.61, 9.97, 10, 10, 1)},
    }
}

def generate_random_evaluations(N, lower_level, upper_level):
    evaluations = []
    for n in range(N):
        Communication = random.randint(lower_level, upper_level)
        Professional_skills = random.randint(lower_level, upper_level)
        Leadership = random.randint(lower_level, upper_level)
        Adaptability = random.randint(lower_level, upper_level)
        
        evaluations += [(Communication, Professional_skills, Leadership, Adaptability)]
    
    return evaluations


def employee_evaluation(evaluations):
    words_model = my_words_model.words_9

    verbal_grades = []
    numerical_grades = []
    
    for evaluation in evaluations:
        numerical_evaluation, verbal_evaluation = t2_mandani_inference.process(input_lvs, output_lv, model.rule_base, evaluation)
        verbal_grades += [verbal_evaluation]
        numerical_grades += [numerical_evaluation]
    
    W = []
    for item in words_model['words']:
        W.append(verbal_grades.count(item))
    
    h = min(item['lmf'][-1] for item in words_model['words'].values())
    m = 50
    intervals_umf = lwa.alpha_cuts_intervals(m)
    intervals_lmf = lwa.alpha_cuts_intervals(m, h)
    
    res_lmf = lwa.y_lmf(intervals_lmf, words_model, W)
    res_umf = lwa.y_umf(intervals_umf, words_model, W)
    res = lwa.construct_dit2fs(np.arange(*words_model['x']), intervals_lmf, res_lmf, intervals_umf, res_umf)
    #res.plot()
    
    sm = []
    for title, fou in words_model['words'].items():
        sm.append((title, res.similarity_measure(word.Word(None, words_model['x'], fou['lmf'], fou['umf']))))
    result = max(sm, key=lambda item: item[1])
    
    return(result, verbal_grades)


def main():    
    st.set_page_config(layout="wide")
    st.title("MKR-2 Ivanenko Ivan")
    values = []
    labels = ["Кількість опитаних колег", "Нижній поріг оцінювання", "Верхній поріг оцінювання"]
    for i in range(len(labels)):
        field_name = labels[i]
        value = st.number_input(field_name, min_value=0, step=1)
        values.append(value)

    if st.button("Calculate"):
        t2_mandani_inference.preprocessing(input_lvs, output_lv)

        N = values[0]
        lower_lvl = values[1]
        upper_lvl = values[2]
        
        evaluations = generate_random_evaluations(N, lower_lvl, upper_lvl)
        result, verbal_grades = employee_evaluation(evaluations)
        
        st.text("Результат оцінки співробітника колегами:")
        st.success(result[0])
        
        st.text("Таблиця оцінок всіх колег:\n")
        describe_evaluations = ".\t\tCommunication\tProf skills\tLeadership\tAdaptability\tVerbal grade\n"
        for i in range(1, len(evaluations) + 1):
            describe_evaluations += "Колега " + str(i)
            describe_evaluations += "\t" + str(evaluations[i-1][0])
            describe_evaluations += "\t\t" + str(evaluations[i-1][1])
            describe_evaluations += "\t\t" + str(evaluations[i-1][2])
            describe_evaluations += "\t\t" + str(evaluations[i-1][3])
            describe_evaluations += "\t\t" + str(verbal_grades[i-1])
            describe_evaluations += "\n"

        st.text(describe_evaluations)


if __name__ == "__main__":
    main()





