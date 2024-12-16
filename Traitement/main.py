import os
import re

# from googletrans import Translator
import deepl

# Remplacez 'your-api-key' par votre clé API DeepL
auth_key = "8cd95243-eac5-4e4f-bf24-4784da7f4d19:fx"
translator = deepl.Translator(auth_key)


def extract_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    questions = re.split(r"#----------------------------------------#", content)
    questions = [q.strip() for q in questions if q.strip()]
    return questions


def escape_latex(text):
    # Liste des caractères spéciaux LaTeX à échapper
    special_chars = {
        "\\": r"\textbackslash{}",
        "#": r"\#",
        "$": r"\$",
        "%": r"\%",
        "&": r"\&",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    # Échapper les caractères spéciaux
    for char, escaped_char in special_chars.items():
        text = text.replace(char, escaped_char)
    return text


def translate_text(text, dest_language="fr"):
    result = translator.translate_text(text, target_lang=dest_language.upper())
    return result.text


def parse_question(question_text, translate):
    title_match = re.search(r"Question:\s*(.*?)\s*Hints:", question_text, re.DOTALL)
    hints_match = re.search(r"Hints:\s*(.*?)\s*Explication:", question_text, re.DOTALL)
    expli_match = re.search(r"Explication:\s*(.*?)\s*Solution:", question_text, re.DOTALL)
    solution_match = re.search(r"Solution:\s*(.*)", question_text, re.DOTALL)

    title = title_match.group(1).strip() if title_match else ""
    hints = hints_match.group(1).strip() if hints_match else ""
    solution = solution_match.group(1).strip() if solution_match else ""
    expli = expli_match.group(1).strip() if expli_match else ""

    if translate == "oui":
        if title:
            try:
                title = translate_text(title)
            except Exception as e:
                print(f"Erreur de traduction pour le titre: {e}")
        if expli:
            try:
                expli = translate_text(expli)
            except Exception as e:
                print(f"Erreur de traduction pour l'explication: {e}")
        if hints:
            try:
                hints = translate_text(hints)
            except Exception as e:
                print(f"Erreur de traduction pour les indices: {e}")

    # Échapper les caractères spéciaux après la traduction
    title = escape_latex(title)
    expli = escape_latex(expli)
    hints = escape_latex(hints)

    return title, hints, solution, expli


def get_next_question_number(code_dir):
    if not os.path.exists(code_dir):
        return 1

    max_number = 0
    for file_name in os.listdir(code_dir):
        match = re.match(r"q(\d{3})\.py", file_name)
        if match:
            number = int(match.group(1))
            if number > max_number:
                max_number = number

    return max_number + 1


def save_solution(solution, question_number):
    code_dir = "code"
    if not os.path.exists(code_dir):
        os.makedirs(code_dir)

    question_number = get_next_question_number(code_dir)
    file_name = f"q{question_number:03d}.py"
    file_path = os.path.join(code_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(solution)

    return file_name


def generate_latex(title, hints, expli, solution_file):
    if hints:
        latex = f"""
        \\question
        {title}
        \\par
        \\textbf{{Indices : }}{hints}
        \\begin{{solution}}
            \\renewcommand{{\\nomfichier}}{{{solution_file}}}
            \\pythonfile{{\\chemincode \\nomfichier}}[][\\nomfichier]
            {expli}
        \\end{{solution}}
        """
    else:
        latex = f"""
        \\question
        {title}
        \\par
        \\begin{{solution}}
            \\renewcommand{{\\nomfichier}}{{{solution_file}}}
            \\pythonfile{{\\chemincode \\nomfichier}}[][\\nomfichier]
            {expli}
        \\end{{solution}}
        """
    return latex


def main():
    input_file = "questions.txt"
    output_file = "output.tex"
    # Demander à l'utilisateur si la traduction est nécessaire
    translate = (
        input("La traduction est-elle nécessaire ? (oui/non) : ").strip().lower()
    )

    questions = extract_questions(input_file)
    latex_content = []

    for i, question_text in enumerate(questions, start=1):
        title, hints, solution, expli = parse_question(question_text, translate)
        if solution:
            solution_file = save_solution(solution, i)
        else:
            solution_file = "pascorrige.py"
        latex = generate_latex(title, hints, expli, solution_file)
        latex_content.append(latex)

    with open(output_file, "a", encoding="utf-8") as file:
        file.write("\n".join(latex_content))
        file.write("\n")


if __name__ == "__main__":
    main()
