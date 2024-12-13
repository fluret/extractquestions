import requests
from bs4 import BeautifulSoup

def scrape_python_challenges(url, output_file):
    try:
        # Envoyer une requête HTTP GET au site
        response = requests.get(url)
        response.raise_for_status()  # Vérifier que la requête s'est bien passée

        # Parser le contenu HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouver tous les articles sur la page
        articles = soup.find_all('a', href=True)  # Les articles sont souvent dans des balises <a>

        # Filtrer les articles commençant par "Python Coding challenge - Day"
        python_challenges = []
        for article in articles:
            if article.text.strip().startswith("Python Coding challenge - Day"):
                article_url = article['href']  # Récupérer le lien vers l'article

                # Récupérer le contenu complet de l'article
                full_article_response = requests.get(article_url)
                full_article_response.raise_for_status()
                full_article_soup = BeautifulSoup(full_article_response.text, 'html.parser')

                # Extraire le texte de l'article (adapter le sélecteur selon la structure réelle du site)
                article_content = full_article_soup.find('div', class_='post-content')  # Exemple de sélecteur
                if article_content:
                    python_challenges.append(article.text.strip() + "\n" + article_content.get_text(strip=True))

        # Écrire les résultats dans un fichier texte
        with open(output_file, 'w', encoding='utf-8') as file:
            for challenge in python_challenges:
                file.write(challenge + '\n\n')

        print(f"{len(python_challenges)} articles trouvés et enregistrés dans {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête HTTP : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

# URL du site et nom du fichier de sortie
url = "https://www.clcoding.com/"
output_file = "python_challenges.txt"

scrape_python_challenges(url, output_file)
