# Guide d'ajout de nouveaux thèmes et référentiels

## 📚 Comment ajouter un nouveau thème

Pour ajouter un nouveau thème d'apprentissage, éditez le fichier `themes_config.py` et ajoutez une nouvelle entrée dans le dictionnaire `THEMES_CONFIG`.

### Structure d'un thème

```python
"nom_du_theme": {
    "titre": "Titre complet du thème - BTS SP3S",
    "description": "Description courte du thème",
    "referentiels": [
        {
            "nom": "Nom du document de référence",
            "url": "https://lien-vers-le-document.fr/...",
            "type": "officiel"  # ou "complementaire"
        }
    ],
    "concepts_cles": [
        "Concept 1",
        "Concept 2",
        # ...
    ],
    "erreurs_frequentes": {
        "conceptuelle": [
            "Description de l'erreur conceptuelle 1",
            "Description de l'erreur conceptuelle 2"
        ],
        "logique": [
            "Description de l'erreur logique 1"
        ],
        "lexicale": [
            "Description de l'erreur lexicale 1"
        ]
    },
    "vocabulaire_attendu": [
        "terme professionnel 1",
        "terme professionnel 2"
    ]
}
```

### Exemple concret : Ajouter un thème sur le handicap

```python
"handicap_inclusion": {
    "titre": "Handicap et inclusion sociale - BTS SP3S",
    "description": "Politiques du handicap et dispositifs d'inclusion",
    "referentiels": [
        {
            "nom": "Loi du 11 février 2005 sur le handicap",
            "url": "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000809647/",
            "type": "officiel"
        },
        {
            "nom": "Guide de la MDPH",
            "url": "https://www.cnsa.fr/documentation/guide-mdph",
            "type": "complementaire"
        }
    ],
    "concepts_cles": [
        "MDPH (Maison Départementale des Personnes Handicapées)",
        "PCH (Prestation de Compensation du Handicap)",
        "AAH (Allocation Adulte Handicapé)",
        "RQTH (Reconnaissance de la Qualité de Travailleur Handicapé)",
        "accessibilité universelle",
        "compensation du handicap"
    ],
    "erreurs_frequentes": {
        "conceptuelle": [
            "confusion AAH / PCH",
            "confusion handicap / invalidité",
            "rôle MDPH mal compris"
        ],
        "logique": [
            "confusion droits automatiques / demandes",
            "méconnaissance des conditions d'éligibilité"
        ],
        "lexicale": [
            "confusion des sigles (MDPH/PCH/AAH)",
            "vocabulaire médical imprécis"
        ]
    },
    "vocabulaire_attendu": [
        "MDPH", "PCH", "AAH", "RQTH",
        "compensation", "accessibilité",
        "situation de handicap"
    ]
}
```

## 🔗 Intégrer vos référentiels officiels

### Où trouver les liens officiels ?

1. **Référentiels BTS SP3S**
   - Site du Ministère de l'Éducation Nationale
   - https://www.education.gouv.fr/

2. **Textes législatifs**
   - Légifrance : https://www.legifrance.gouv.fr/

3. **Documents ministériels**
   - Ministère des Solidarités : https://solidarites.gouv.fr/
   - Ministère de la Santé : https://sante.gouv.fr/

4. **Organismes de référence**
   - Sécurité Sociale : https://www.securite-sociale.fr/
   - CAF : https://www.caf.fr/
   - CNSA : https://www.cnsa.fr/

### Types de référentiels

- **`"officiel"`** : Documents officiels (lois, décrets, référentiels Education Nationale)
- **`"complementaire"`** : Documents pédagogiques, guides pratiques, fiches mémo

## 🚀 Après l'ajout d'un thème

1. **Enregistrez** le fichier `themes_config.py`
2. **Redémarrez** le serveur FastAPI
3. **Testez** avec l'endpoint `/themes` pour vérifier que votre thème apparaît
4. **Consultez** les détails avec `/themes/nom_du_theme`

## 📋 Endpoints disponibles

### Lister tous les thèmes
```
GET /themes
```
Retourne la liste de tous les thèmes avec leur nombre de concepts et référentiels.

### Détails d'un thème
```
GET /themes/{theme_id}
```
Retourne tous les détails d'un thème (concepts, vocabulaire, erreurs fréquentes, référentiels).

### Référentiels d'un thème
```
GET /themes/{theme_id}/referentiels
```
Retourne uniquement les référentiels d'un thème spécifique.

### Analyser une réponse
```
POST /corriger
```
Corps de la requête :
```json
{
  "question_id": "Q1",
  "question_texte": "Votre question",
  "reponse_eleve": "La réponse de l'étudiant",
  "theme": "nom_du_theme"
}
```

## 💡 Conseils

1. **Soyez précis** dans les concepts clés (ils guident l'IA)
2. **Listez les erreurs fréquentes** observées chez vos étudiants
3. **Utilisez le vocabulaire professionnel** attendu dans le BTS SP3S
4. **Mettez à jour les référentiels** avec les liens officiels les plus récents
5. **Testez votre thème** avec quelques exemples de réponses d'étudiants

## ✅ Thèmes actuellement disponibles

- `politiques_logement` - Politiques publiques du logement
- `sante_publique` - Santé publique et prévention
- `protection_sociale` - Protection sociale et prestations
- `action_sociale` - Action sociale et médico-sociale

Vous pouvez en ajouter autant que nécessaire !
