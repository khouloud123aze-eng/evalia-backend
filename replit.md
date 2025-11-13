# API IA Éducative - BTS SP3S

## Vue d'ensemble

Application FastAPI d'analyse intelligente des réponses d'étudiants pour le BTS Services et Prestations des Secteurs Sanitaire et Social (SP3S). L'API utilise **Google Gemini 2.5 Flash** (gratuit) pour analyser les réponses des étudiants, détecter les erreurs conceptuelles, logiques et lexicales, et fournir des recommandations pédagogiques personnalisées avec accès aux référentiels officiels.

## Fonctionnalités principales

- **Analyse automatique des réponses** : Évaluation intelligente des réponses d'étudiants avec détection fine des erreurs
- **Taxonomie des erreurs** : Classification en 3 types (conceptuelles, logiques, lexicales)
- **Feedback personnalisé** : Retour bienveillant et constructif avec notation sur 20
- **Remédiation pédagogique** : Suggestions de ressources et exercices adaptés
- **Système thématique extensible** : 4 thèmes disponibles (logement, santé publique, protection sociale, action sociale)
- **Référentiels intégrés** : Accès aux documents officiels et complémentaires pour chaque thème
- **IA gratuite** : Utilisation de Google Gemini avec quota généreux

## Architecture du projet

```
.
├── main.py                  # Application FastAPI principale
├── themes_config.py         # Configuration des thèmes et référentiels
├── GUIDE_AJOUT_THEMES.md   # Guide pour ajouter de nouveaux thèmes
├── .gitignore              # Fichiers ignorés par Git
├── pyproject.toml          # Dépendances Python (uv)
└── replit.md               # Documentation
```

## Dépendances

- **FastAPI** : Framework web moderne et performant
- **Uvicorn** : Serveur ASGI pour FastAPI
- **Google GenAI** : SDK Python pour l'API Gemini (gratuit)
- **Pydantic** : Validation des données et sérialisation

## Configuration

### Variables d'environnement requises

- `GEMINI_API_KEY` : Clé API Google Gemini (gratuite - obtenir sur aistudio.google.com/apikey)
- `SESSION_SECRET` : Secret pour la gestion des sessions

## Endpoints API

### GET /
Page d'accueil de l'API avec informations de version et endpoints disponibles.

### GET /health
Vérification de l'état du service.

**Réponse** :
```json
{
  "status": "ok",
  "service": "education-ai-backend"
}
```

### GET /themes
Liste tous les thèmes pédagogiques disponibles avec leurs statistiques.

**Réponse** :
```json
{
  "themes": [
    {
      "id": "politiques_logement",
      "titre": "Politiques publiques du logement - BTS SP3S",
      "description": "Analyse des dispositifs d'accès au logement et des politiques publiques",
      "nb_concepts": 8,
      "nb_referentiels": 2
    },
    {
      "id": "sante_publique",
      "titre": "Santé publique et prévention - BTS SP3S",
      "description": "Politiques de santé publique, prévention et promotion de la santé",
      "nb_concepts": 8,
      "nb_referentiels": 2
    }
  ]
}
```

### GET /themes/{theme_id}
Récupère les détails complets d'un thème spécifique (concepts, vocabulaire, erreurs fréquentes, référentiels).

**Exemple** : `/themes/politiques_logement`

**Réponse** :
```json
{
  "id": "politiques_logement",
  "titre": "Politiques publiques du logement - BTS SP3S",
  "description": "Analyse des dispositifs d'accès au logement et des politiques publiques",
  "concepts_cles": [
    "logement social vs hébergement d'urgence",
    "FSL (Fonds de Solidarité Logement)",
    "DALO (Droit Au Logement Opposable)"
  ],
  "vocabulaire_attendu": [
    "logement social", "bailleur social", "FSL", "DALO"
  ],
  "erreurs_frequentes": {
    "conceptuelle": ["confusion logement social / hébergement"],
    "logique": ["généralisation abusive"],
    "lexicale": ["maison sociale au lieu de logement social"]
  },
  "referentiels": [
    {
      "nom": "Référentiel BTS SP3S 2024",
      "url": "https://www.education.gouv.fr/...",
      "type": "officiel"
    }
  ]
}
```

### GET /themes/{theme_id}/referentiels
Récupère uniquement les référentiels (documents officiels et complémentaires) d'un thème.

**Exemple** : `/themes/sante_publique/referentiels`

**Réponse** :
```json
{
  "theme_id": "sante_publique",
  "theme_titre": "Santé publique et prévention - BTS SP3S",
  "referentiels": [
    {
      "nom": "Référentiel BTS SP3S - Module Santé Publique",
      "url": "https://www.education.gouv.fr/...",
      "type": "officiel"
    },
    {
      "nom": "Plan National Santé Publique",
      "url": "https://solidarites-sante.gouv.fr/...",
      "type": "complementaire"
    }
  ]
}
```

### POST /corriger
Analyse une réponse d'étudiant et retourne un feedback détaillé.

**Corps de la requête** :
```json
{
  "question_id": "Q1",
  "question_texte": "Quelle est la différence entre logement social et hébergement d'urgence ?",
  "reponse_eleve": "La mairie donne des maisons",
  "theme": "politiques_logement",
  "contexte_pedagogique": "Cours sur les dispositifs d'accès au logement"
}
```

**Réponse** :
```json
{
  "feedback": {
    "est_correct": false,
    "score": 8,
    "erreurs_detectees": [
      {
        "type_erreur": "lexicale",
        "sous_categorie": "Vocabulaire imprécis",
        "description": "Utilisation du terme 'maisons' au lieu de 'logement social'",
        "gravite": "moyenne"
      }
    ],
    "feedback_general": "La réponse montre une compréhension partielle...",
    "points_forts": ["Identification de l'acteur public"],
    "axes_amelioration": ["Préciser la terminologie professionnelle"]
  },
  "remediation": {
    "ressources_suggerees": ["Fiche mémo sur les acteurs du logement social"],
    "exercices_complementaires": ["Quiz sur la terminologie professionnelle"],
    "focus_pedagogique": "Maîtriser le vocabulaire technique du secteur"
  },
  "metadata": {
    "theme": "politiques_logement",
    "question_id": "Q1",
    "modele_utilise": "gemini-2.5-flash",
    "tokens_utilises": 450
  }
}
```

## Taxonomie des erreurs

### 1. Erreurs conceptuelles
Confusion de notions, mauvaise compréhension des dispositifs
- Confusion logement social / hébergement d'urgence
- Confusion FSL / DALO
- Rôle des bailleurs vs collectivités mal compris

### 2. Erreurs logiques
Raisonnement bancal, généralisation abusive, absence de lien cause-effet
- Généralisation abusive
- Causalité inversée ou absente
- Solutions proposées inadaptées au problème

### 3. Erreurs lexicales
Vocabulaire imprécis, non professionnel, confusion de sigles
- Utilisation de termes non professionnels
- Imprécision dans la désignation des acteurs
- Confusion des sigles (FSL/DALO/PDALHPD)

## Thèmes disponibles

### Politiques publiques du logement
- **Concepts clés** : Logement social, FSL, DALO, bailleurs sociaux, collectivités territoriales
- **Vocabulaire attendu** : Professionnel du secteur sanitaire et social
- **Niveau** : BTS SP3S

## Utilisation

### Démarrage du serveur
Le serveur démarre automatiquement via le workflow configuré :
```bash
uvicorn main:app --host 0.0.0.0 --port 5000
```

### Exemple de test avec curl
```bash
curl -X POST "https://votre-domaine.repl.co/corriger" \
  -H "Content-Type: application/json" \
  -d '{
    "question_id": "Q1",
    "question_texte": "Différence entre logement social et hébergement?",
    "reponse_eleve": "La mairie donne des maisons",
    "theme": "politiques_logement"
  }'
```

## Évolutions futures

- Ajout de nouveaux thèmes BTS SP3S (santé publique, protection sociale, etc.)
- Interface web pour les enseignants
- Historique des corrections par étudiant
- Analyse de progression pédagogique
- Tableau de bord analytique des erreurs récurrentes
- Correction par lot pour plusieurs réponses

## Notes techniques

- Le serveur utilise CORS avec `allow_origins=["*"]` pour faciliter l'intégration frontend
- Le modèle GPT-4o-mini est configuré avec `temperature=0.3` pour des réponses cohérentes
- La validation des données est assurée par Pydantic
- Les réponses JSON sont structurées via `response_format={"type": "json_object"}`

## Changements récents

- **2025-11-13** : Initialisation du projet avec API FastAPI
- **2025-11-13** : Implémentation de l'analyseur IA avec GPT-4o-mini
- **2025-11-13** : Configuration du thème "Politiques publiques du logement"
- **2025-11-13** : Mise en place du workflow Uvicorn sur port 5000
