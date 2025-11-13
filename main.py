from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
from google import genai
from google.genai import types
import os
import json
from enum import Enum
from themes_config import THEMES_CONFIG

app = FastAPI(title="API IA Éducative", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    import warnings
    warnings.warn("GEMINI_API_KEY n'est pas configurée. L'endpoint /corriger ne fonctionnera pas.")
    client = None
else:
    client = genai.Client(api_key=GEMINI_API_KEY)

class TypeErreur(str, Enum):
    CONCEPTUELLE = "conceptuelle"
    LOGIQUE = "logique"
    LEXICALE = "lexicale"
    AUCUNE = "aucune"

class ReponseEleve(BaseModel):
    question_id: str
    question_texte: str
    reponse_eleve: str
    contexte_pedagogique: Optional[str] = None
    theme: str = "politiques_logement"

class AnalyseErreur(BaseModel):
    type_erreur: TypeErreur
    sous_categorie: Optional[str] = None
    description: str
    gravite: str

class Feedback(BaseModel):
    est_correct: bool
    score: Optional[int] = None
    erreurs_detectees: List[AnalyseErreur]
    feedback_general: str
    points_forts: List[str]
    axes_amelioration: List[str]

class Remediation(BaseModel):
    ressources_suggerees: List[str]
    exercices_complementaires: List[str]
    focus_pedagogique: str

class ResultatCorrection(BaseModel):
    feedback: Feedback
    remediation: Remediation
    metadata: Dict

class AnalyseurIA:
    def __init__(self, provider="openai"):
        self.provider = provider
        self.client = client
        
    def _construire_prompt_analyse(self, data: ReponseEleve) -> str:
        theme_config = THEMES_CONFIG.get(data.theme, {})
        
        prompt = f"""Tu es un expert en pédagogie et en évaluation des compétences pour le BTS SP3S.

THÈME : {theme_config.get('titre', data.theme)}

CONCEPTS CLÉS À MAÎTRISER :
{chr(10).join(f"- {c}" for c in theme_config.get('concepts_cles', []))}

VOCABULAIRE PROFESSIONNEL ATTENDU :
{', '.join(theme_config.get('vocabulaire_attendu', []))}

QUESTION POSÉE :
{data.question_texte}

RÉPONSE DE L'ÉTUDIANT :
{data.reponse_eleve}

TAXONOMIE DES ERREURS :

1. ERREURS CONCEPTUELLES (confusion de notions, mauvaise compréhension des dispositifs)
   Exemples fréquents : {', '.join(theme_config.get('erreurs_frequentes', {}).get('conceptuelle', []))}

2. ERREURS LOGIQUES (raisonnement bancal, généralisation abusive, absence de lien cause-effet)
   Exemples fréquents : {', '.join(theme_config.get('erreurs_frequentes', {}).get('logique', []))}

3. ERREURS LEXICALES (vocabulaire imprécis, non professionnel, confusion de sigles)
   Exemples fréquents : {', '.join(theme_config.get('erreurs_frequentes', {}).get('lexicale', []))}

ANALYSE DEMANDÉE :

Analyse la réponse de l'étudiant et fournis un retour structuré au format JSON suivant :

{{
    "est_correct": true/false,
    "score": <note sur 20>,
    "erreurs": [
        {{
            "type": "conceptuelle|logique|lexicale",
            "sous_categorie": "précision de l'erreur",
            "description": "description détaillée",
            "gravite": "mineure|moyenne|majeure",
            "extrait": "partie de la réponse concernée"
        }}
    ],
    "points_forts": ["point fort 1", "point fort 2"],
    "axes_amelioration": ["axe 1", "axe 2"],
    "feedback_general": "feedback bienveillant et constructif",
    "remediation": {{
        "ressources": ["ressource 1", "ressource 2"],
        "exercices": ["exercice 1", "exercice 2"],
        "focus": "ce sur quoi l'étudiant doit se concentrer en priorité"
    }}
}}

IMPORTANT :
- Sois bienveillant mais précis
- Valorise les points positifs même dans une réponse faible
- Fournis des pistes concrètes d'amélioration
- Adapte le niveau d'exigence au contexte BTS SP3S
"""
        return prompt

    async def analyser_reponse(self, data: ReponseEleve) -> ResultatCorrection:
        try:
            if not self.client:
                raise HTTPException(
                    status_code=503,
                    detail="Service IA non disponible: GEMINI_API_KEY n'est pas configurée. Ajoutez votre clé dans les Secrets Replit."
                )
            
            prompt = self._construire_prompt_analyse(data)
            
            system_instruction = "Tu es un évaluateur pédagogique expert. Tu réponds UNIQUEMENT en JSON valide."
            
            # Note that the newest Gemini model series is "gemini-2.5-flash" or "gemini-2.5-pro"
            # do not change this unless explicitly requested by the user
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[types.Content(role="user", parts=[types.Part(text=prompt)])],
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    response_mime_type="application/json"
                )
            )
            
            resultat = response.text
            if not resultat:
                raise HTTPException(status_code=500, detail="Réponse vide de l'API Gemini")
            
            data_json = json.loads(resultat)
            
            erreurs_detectees = [
                AnalyseErreur(
                    type_erreur=TypeErreur(err.get("type", "aucune")),
                    sous_categorie=err.get("sous_categorie"),
                    description=err.get("description", ""),
                    gravite=err.get("gravite", "moyenne")
                )
                for err in data_json.get("erreurs", [])
            ]
            
            feedback = Feedback(
                est_correct=data_json.get("est_correct", False),
                score=data_json.get("score"),
                erreurs_detectees=erreurs_detectees,
                feedback_general=data_json.get("feedback_general", ""),
                points_forts=data_json.get("points_forts", []),
                axes_amelioration=data_json.get("axes_amelioration", [])
            )
            
            remediation_data = data_json.get("remediation", {})
            remediation = Remediation(
                ressources_suggerees=remediation_data.get("ressources", []),
                exercices_complementaires=remediation_data.get("exercices", []),
                focus_pedagogique=remediation_data.get("focus", "")
            )
            
            return ResultatCorrection(
                feedback=feedback,
                remediation=remediation,
                metadata={
                    "theme": data.theme,
                    "question_id": data.question_id,
                    "modele_utilise": "gemini-2.5-flash",
                    "tokens_utilises": response.usage_metadata.total_token_count if response.usage_metadata else 0
                }
            )
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erreur lors de l'analyse : {str(e)}")

analyseur = AnalyseurIA()

@app.get("/")
async def root():
    return {
        "message": "API IA Éducative - BTS SP3S",
        "version": "1.0.0",
        "status": "online",
        "model": "gemini-2.5-flash (gratuit)",
        "nombre_themes": len(THEMES_CONFIG),
        "endpoints": [
            "/corriger - Analyser une réponse d'étudiant",
            "/themes - Lister tous les thèmes disponibles",
            "/themes/{theme_id} - Détails d'un thème spécifique",
            "/themes/{theme_id}/referentiels - Référentiels d'un thème",
            "/health - État du service"
        ]
    }

@app.get("/health")
async def health_check():
    api_key_configured = bool(os.getenv("GEMINI_API_KEY"))
    return {
        "status": "ok",
        "service": "education-ai-backend",
        "model": "gemini-2.5-flash",
        "api_key_configured": api_key_configured
    }

@app.get("/themes")
async def lister_themes():
    return {
        "themes": [
            {
                "id": theme_id,
                "titre": config["titre"],
                "description": config.get("description", ""),
                "nb_concepts": len(config.get("concepts_cles", [])),
                "nb_referentiels": len(config.get("referentiels", []))
            }
            for theme_id, config in THEMES_CONFIG.items()
        ]
    }

@app.get("/themes/{theme_id}")
async def obtenir_theme(theme_id: str):
    if theme_id not in THEMES_CONFIG:
        raise HTTPException(
            status_code=404,
            detail=f"Thème '{theme_id}' non trouvé. Utilisez /themes pour voir les thèmes disponibles."
        )
    
    config = THEMES_CONFIG[theme_id]
    return {
        "id": theme_id,
        "titre": config["titre"],
        "description": config.get("description", ""),
        "concepts_cles": config.get("concepts_cles", []),
        "vocabulaire_attendu": config.get("vocabulaire_attendu", []),
        "erreurs_frequentes": config.get("erreurs_frequentes", {}),
        "referentiels": config.get("referentiels", [])
    }

@app.get("/themes/{theme_id}/referentiels")
async def obtenir_referentiels(theme_id: str):
    if theme_id not in THEMES_CONFIG:
        raise HTTPException(
            status_code=404,
            detail=f"Thème '{theme_id}' non trouvé."
        )
    
    config = THEMES_CONFIG[theme_id]
    return {
        "theme_id": theme_id,
        "theme_titre": config["titre"],
        "referentiels": config.get("referentiels", [])
    }

@app.post("/corriger", response_model=ResultatCorrection)
async def corriger_reponse(data: ReponseEleve):
    if data.theme not in THEMES_CONFIG:
        raise HTTPException(
            status_code=400, 
            detail=f"Thème '{data.theme}' non reconnu. Thèmes disponibles : {list(THEMES_CONFIG.keys())}"
        )
    
    resultat = await analyseur.analyser_reponse(data)
    return resultat
