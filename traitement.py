import os
import re

def extract_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    questions = re.split(r'#----------------------------------------#', content)
    questions = [q.strip() for q in questions if q.strip()]
    return questions

def parse_question(question_text):
    title_match = re.search(r'Question:\s*(.*)', question_text, re.DOTALL)
    hints_match = re.search(r'Hints:\s*(.*)', question_text, re.DOTALL)
    solution_match = re.search(r'Solution:\s*(.*)', question_text, re.DOTALL)

    title = title_match.group(1).strip() if title_match else ''
    hints = hints_match.group(1).strip() if hints_match else ''
    solution = solution_match.group(1).strip() if solution_match else ''

    return title, hints, solution

def save_solution(solution, question_number):
    code_dir = 'code'
    if not os.path.exists(code_dir):
        os.makedirs(code_dir)

    file_name = f'q{question_number:03d}.py'
    file_path = os.path.join(code_dir, file_name)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(solution)

    return file_name

def generate_latex(title, question, hints, solution_file):
    latex = f"""
\\section{{{title}}}
\\question
{question}
\\par
\\textbf{{Indication}}: {hints}
\\renewcommand{{\\nomfichier}}{{{solution_file}}}
\\begin{{solution}}
    \\pythonfile{{\\chemincode \\nomfichier}}[][{solution_file}]
\\end{{solution}}
"""
    return latex

def main():
    input_file = 'questions.txt'
    output_file = 'output.tex'

    questions = extract_questions(input_file)
    latex_content = []

    for i, question_text in enumerate(questions, start=1):
        title, hints, solution = parse_question(question_text)
        solution_file = save_solution(solution, i)
        latex = generate_latex(title, question_text, hints, solution_file)
        latex_content.append(latex)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(latex_content))

if __name__ == '__main__':
    main()