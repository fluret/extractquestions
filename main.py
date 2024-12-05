import os
import re

def parse_questions(file_path):
    """
    Analyse un fichier texte pour extraire les questions et leurs éléments associés.
    Génère les fichiers Python et un fichier texte avec du code LaTeX.
    """
    # Création du dossier "code" pour stocker les fichiers Python
    output_folder = "code"
    os.makedirs(output_folder, exist_ok=True)
    
    # Nom du fichier LaTeX
    latex_output_file = "questions_latex.txt"

    # Lire le contenu du fichier texte
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Découpage du contenu en questions
    questions = content.split("#----------------------------------------#")
    
    # Initialisation du contenu LaTeX
    latex_content = ""

    # Parcourir chaque question
    for question in questions:
        # Extraction des éléments via expressions régulières
        title_match = re.search(r"Question (\d+)", question)
        question_text_match = re.search(r"Question:\s*(.+)", question, re.DOTALL)
        hints_match = re.search(r"Hints:\s*(.+)", question, re.DOTALL)
        solution_match = re.search(r"Solution:\s*(.+?)(?=#----------------------------------------#|$)", question, re.DOTALL)
        
        if title_match and question_text_match and hints_match and solution_match:
            # Extraction des données
            question_number = int(title_match.group(1))
            question_text = question_text_match.group(1).strip()
            hints = hints_match.group(1).strip()
            solution = solution_match.group(1).strip()
            
            # Formatage du numéro de question
            question_number_formatted = f"{question_number:03}"
            python_file_name = f"q{question_number_formatted}.py"
            python_file_path = os.path.join(output_folder, python_file_name)
            
            # Écriture du fichier Python
            with open(python_file_path, "w", encoding="utf-8") as python_file:
                python_file.write(solution)
            
            # Génération du code LaTeX
            latex_content += f"\\section{{Question {question_number}}}\n"
            latex_content += "\\question\n"
            latex_content += f"{question_text}\n\\par\n"
            latex_content += f"\\textbf{{Indication:}} {hints}\n\n"
            latex_content += f"\\renewcommand{{\\nomfichier}}{{{python_file_name}}}\n"
            latex_content += "\\begin{solution}\n"
            latex_content += f"\\pythonfile{{\\chemincode \\nomfichier}}[][{python_file_name}]\n"
            latex_content += "\\end{solution}\n\n"
    
    # Écriture du fichier LaTeX
    with open(latex_output_file, "w", encoding="utf-8") as latex_file:
        latex_file.write(latex_content)
    
    print(f"Fichiers Python générés dans le dossier '{output_folder}'.")
    print(f"Code LaTeX enregistré dans le fichier '{latex_output_file}'.")

# Exemple d'utilisation
parse_questions("questions.txt")
