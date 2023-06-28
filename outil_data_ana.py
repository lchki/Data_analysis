
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données à partir du fichier CSV
data = pd.read_csv('mock_data.csv')

# Fonction de filtrage des données basée sur une valeur spécifique dans une colonne
def filtrer_donnees(colonne, valeur):
    return data[data[colonne] == valeur]

# Fonction de recherche de données contenant le mot-clé
def rechercher_donnees(mot_cle):
    return data[data.apply(lambda row: mot_cle in ' '.join(row.values.astype(str)), axis=1)]

# Saisie de la colonne et de la valeur de recherche
colonne = input("Entrez le nom de la colonne : ")
valeur = input("Entrez la valeur de recherche : ")

# Recherche des données basée sur la colonne et la valeur spécifiées
resultats = filtrer_donnees(colonne, valeur)

# Affichage des résultats
print(resultats)

# Compter le nombre d'occurrences de la valeur spécifiée dans la colonne
nb_occurrences = len(resultats)

# Calculer le nombre total de connexions pour les données trouvées
nb_connexions = resultats['last_connection'].count()

# Afficher les résultats
print("Nombre d'occurrences :", nb_occurrences)
print("Nombre total de connexions :", nb_connexions)

# Fonction de tri des données
def trier_donnees(colonne):
    return data.sort_values(by=colonne)

# Fonction de statistiques descriptives
def statistiques_descriptives():
    return data.describe()

# Fonction de visualisation avancée - Répartition des langues
def visualisation_avancee_langues():
    # Sélection des principales langues
    principales_langues = data['Language'].value_counts().head(5)

    # Regroupement des langues moins fréquentes sous la catégorie "Autres"
    autres_langues_count = data['Language'].value_counts().sum() - principales_langues.sum()
    principales_langues['Autres'] = autres_langues_count

    # Tracé du graphique
    principales_langues.plot(kind='bar')
    plt.title('Répartition des langues')
    plt.xlabel('Langue')
    plt.ylabel('Nombre d\'enregistrements')
    plt.show()

# Fonction de visualisation avancée - Répartition des genres
def visualisation_avancee_genres():
    # Compter le nombre d'enregistrements par genre
    genres_counts = data['gender'].value_counts()

    # Regrouper les genres moins fréquents sous la catégorie 'Others'
    genres_counts_filtered = genres_counts.loc[['Male', 'Female']]
    autres_genres_count = genres_counts.sum() - genres_counts_filtered.sum()
    genres_counts_filtered['Others'] = autres_genres_count

    # Tracé du graphique
    genres_counts_filtered.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Répartition des genres')
    plt.ylabel('')
    plt.show()

# Exemples d'utilisation des fonctions

# Filtrage des données pour le genre "Male"
donnees_filtrees = filtrer_donnees('gender', 'Male')
print(donnees_filtrees)

# Recherche de données contenant le mot-clé "John"
donnees_recherchees = rechercher_donnees('John')

# Compter le nombre d'occurrences de "John"
nb_occurrences = len(donnees_recherchees)

# Calculer le nombre total de connexions pour les données trouvées
nb_connexions = donnees_recherchees['last_connection'].count()

# Afficher les résultats
print("Nombre d'occurrences de 'John' :", nb_occurrences)
print("Nombre total de connexions pour les occurrences de 'John' :", nb_connexions)

# Tri des données par ordre croissant de la colonne "last_connection"
donnees_triees = trier_donnees('last_connection')
print(donnees_triees)

# Affichage des statistiques descriptives
stats = statistiques_descriptives()
print(stats)

# Visualisation avancée des données - Répartition des langues
visualisation_avancee_langues()

# Visualisation avancée des données - Répartition des genres
visualisation_avancee_genres()

