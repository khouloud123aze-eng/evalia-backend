<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Evalia - Plateforme d'Évaluation Intelligente</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        header {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            text-align: center;
        }

        h1 {
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #666;
            font-size: 1.1em;
        }

        .main-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }

        .card {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }

        .card h2 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.5em;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .icon {
            font-size: 1.3em;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
        }

        select, input, textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 1em;
            font-family: inherit;
            transition: border-color 0.3s;
        }

        select:focus, input:focus, textarea:focus {
            outline: none;
            border-color: #667eea;
        }

        textarea {
            resize: vertical;
            min-height: 150px;
        }

        .char-count {
            text-align: right;
            color: #999;
            font-size: 0.9em;
            margin-top: 5px;
        }

        button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 10px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            width: 100%;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }

        button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }

        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }

        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .feedback-container {
            display: none;
        }

        .feedback-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .feedback-correct {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            color: white;
        }

        .feedback-incorrect {
            background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
            color: white;
        }

        .score {
            font-size: 2em;
            font-weight: bold;
        }

        .error-badge {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            margin: 5px;
            font-weight: 600;
        }

        .badge-conceptuelle {
            background: #ffeaa7;
            color: #d63031;
        }

        .badge-logique {
            background: #a29bfe;
            color: #6c5ce7;
        }

        .badge-lexicale {
            background: #fd79a8;
            color: #e84393;
        }

        .feedback-section {
            margin-bottom: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
        }

        .feedback-section h3 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 1.1em;
        }

        .feedback-section ul {
            list-style: none;
            padding-left: 0;
        }

        .feedback-section li {
            padding: 8px 0;
            padding-left: 25px;
            position: relative;
        }

        .feedback-section li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #11998e;
            font-weight: bold;
        }

        .error-item {
            background: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            border-left: 4px solid #667eea;
        }

        .error-type {
            font-weight: 600;
            color: #667eea;
            margin-bottom: 5px;
        }

        .history-item {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            cursor: pointer;
            transition: transform 0.2s;
        }

        .history-item:hover {
            transform: translateX(5px);
            background: #e9ecef;
        }

        .history-meta {
            display: flex;
            justify-content: space-between;
            color: #666;
            font-size: 0.9em;
            margin-top: 5px;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-top: 20px;
        }

        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        .stat-number {
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .stat-label {
            font-size: 0.9em;
            opacity: 0.9;
        }

        .questions-list {
            max-height: 400px;
            overflow-y: auto;
        }

        .question-item {
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
            margin-bottom: 10px;
            cursor: pointer;
            transition: all 0.3s;
            border: 2px solid transparent;
        }

        .question-item:hover {
            background: #e9ecef;
            border-color: #667eea;
        }

        .question-item.selected {
            background: #667eea;
            color: white;
            border-color: #667eea;
        }

        .api-status {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 20px;
            background: #d4edda;
            color: #155724;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .api-status.offline {
            background: #f8d7da;
            color: #721c24;
        }

        .status-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #28a745;
        }

        .status-dot.offline {
            background: #dc3545;
        }

        @media (max-width: 968px) {
            .main-grid {
                grid-template-columns: 1fr;
            }

            .stats-grid {
                grid-template-columns: 1fr;
            }
        }

        .remediation-section {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }

        .remediation-section h3 {
            margin-bottom: 15px;
        }

        .export-btn {
            background: white;
            color: #667eea;
            margin-top: 10px;
            width: auto;
            padding: 10px 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📚 Evalia</h1>
            <p class="subtitle">Plateforme d'Évaluation Intelligente - BTS SP3S</p>
            <div id="apiStatus" class="api-status">
                <span class="status-dot"></span>
                <span>Connexion à l'API...</span>
            </div>
        </header>

        <div class="main-grid">
            <!-- Colonne gauche : Formulaire -->
            <div>
                <div class="card">
                    <h2><span class="icon">✍️</span> Nouvelle Correction</h2>
                    
                    <div class="form-group">
                        <label>Thème</label>
                        <select id="theme">
                            <option value="politiques_logement">Politiques publiques du logement</option>
                            <option value="protection_sociale">Système de protection sociale</option>
                            <option value="politique_familiale_enfance">Politiques familiales et de l'enfance</option>
                            <option value="politique_personnes_agees">Politiques en faveur des personnes âgées</option>
                            <option value="politique_handicap">Politiques du handicap</option>
                            <option value="politique_sante_publique">Politiques de santé publique</option>
                            <option value="politique_lutte_pauvrete">Lutte contre la pauvreté et l'exclusion</option>
                            <option value="politique_emploi_insertion">Politiques de l'emploi et insertion</option>
                            <option value="politique_ville_cohesion">Politique de la ville et cohésion sociale</option>
                            <option value="etablissements_services_sanitaires">Établissements et services sanitaires/médico-sociaux</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label>Question</label>
                        <textarea id="question" placeholder="Posez votre question ici..."></textarea>
                    </div>

                    <div class="form-group">
                        <label>Réponse de l'étudiant</label>
                        <textarea id="reponse" placeholder="Saisissez la réponse de l'étudiant..."></textarea>
                        <div class="char-count"><span id="charCount">0</span> caractères</div>
                    </div>

                    <button id="submitBtn" onclick="corrigerReponse()">
                        🚀 Analyser la réponse
                    </button>

                    <div class="loading" id="loading">
                        <div class="spinner"></div>
                        <p>Analyse en cours...</p>
                    </div>
                </div>

                <div class="card" style="margin-top: 30px;">
                    <h2><span class="icon">📝</span> Questions Prédéfinies</h2>
                    <div class="questions-list" id="questionsList"></div>
                </div>
            </div>

            <!-- Colonne droite : Résultats -->
            <div>
                <div class="card">
                    <h2><span class="icon">📊</span> Statistiques</h2>
                    <div class="stats-grid">
                        <div class="stat-card">
                            <div class="stat-number" id="statTotal">0</div>
                            <div class="stat-label">Corrections</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-number" id="statCorrect">0%</div>
                            <div class="stat-label">Taux de réussite</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-number" id="statAvg">0/20</div>
                            <div class="stat-label">Note moyenne</div>
                        </div>
                    </div>
                </div>

                <div class="card feedback-container" id="feedbackContainer" style="margin-top: 30px;">
                    <h2><span class="icon">🎯</span> Résultat de l'analyse</h2>
                    <div id="feedbackContent"></div>
                </div>

                <div class="card" style="margin-top: 30px;">
                    <h2><span class="icon">📜</span> Historique</h2>
                    <div id="historyList">
                        <p style="text-align: center; color: #999; padding: 20px;">Aucune correction pour le moment</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const API_URL = 'https://evalia-backend-w04n.onrender.com';
        let history = [];
        let stats = { total: 0, correct: 0, scores: [] };

        const QUESTIONS_EXEMPLES = [
            {
                id: 'q1',
                theme: 'politiques_logement',
                texte: 'Expliquez la différence entre logement social et hébergement d\'urgence',
                exemple_reponse: 'Le logement social est un dispositif pérenne attribué par les bailleurs sociaux selon des critères de revenus, tandis que l\'hébergement d\'urgence est une solution temporaire pour les personnes en grande précarité.'
            },
            {
                id: 'q2',
                theme: 'politiques_logement',
                texte: 'Quel est le rôle du FSL (Fonds de Solidarité Logement) ?',
                exemple_reponse: 'Le FSL aide les ménages en difficulté à accéder ou se maintenir dans leur logement en finançant les frais d\'accès et les impayés.'
            },
            {
                id: 'q5',
                theme: 'protection_sociale',
                texte: 'Quelle est la différence entre la Sécurité sociale et une mutuelle ?',
                exemple_reponse: 'La Sécurité sociale est le régime obligatoire de protection sociale basé sur la solidarité nationale, tandis qu\'une mutuelle est une protection complémentaire facultative qui couvre le reste à charge.'
            },
            {
                id: 'q6',
                theme: 'protection_sociale',
                texte: 'Quelles sont les différentes branches de la Sécurité sociale ?',
                exemple_reponse: 'Les branches sont : maladie, accidents du travail-maladies professionnelles (AT-MP), retraite, famille, et autonomie.'
            },
            {
                id: 'q7',
                theme: 'protection_sociale',
                texte: 'Comment est financée la Sécurité sociale ?',
                exemple_reponse: 'Elle est financée par les cotisations sociales (employeurs et salariés) et les contributions fiscales (CSG, CRDS).'
            },
            {
                id: 'q9',
                theme: 'politique_familiale_enfance',
                texte: 'Quelle est la différence entre l\'ASE et la PMI ?',
                exemple_reponse: 'L\'ASE (Aide Sociale à l\'Enfance) intervient en protection de l\'enfance en danger, tandis que la PMI (Protection Maternelle et Infantile) assure la prévention médico-sociale auprès des jeunes enfants et des femmes enceintes.'
            },
            {
                id: 'q10',
                theme: 'politique_familiale_enfance',
                texte: 'Qu\'est-ce qu\'une information préoccupante et comment est-elle traitée ?',
                exemple_reponse: 'Une information préoccupante signale une situation de risque ou de danger pour un enfant. Elle est transmise à la CRIP (Cellule de Recueil des Informations Préoccupantes) du Conseil départemental qui évalue la situation.'
            },
            {
                id: 'q12',
                theme: 'politique_personnes_agees',
                texte: 'Qu\'est-ce que l\'APA et qui peut en bénéficier ?',
                exemple_reponse: 'L\'APA (Allocation Personnalisée d\'Autonomie) est une prestation versée par le Conseil départemental aux personnes âgées de 60 ans et plus en perte d\'autonomie (GIR 1 à 4).'
            },
            {
                id: 'q13',
                theme: 'politique_personnes_agees',
                texte: 'Quelle est la différence entre la tutelle et la curatelle ?',
                exemple_reponse: 'La tutelle est une mesure de protection forte où le tuteur représente totalement la personne protégée. La curatelle est une mesure d\'assistance où la personne conserve une partie de sa capacité juridique.'
            },
            {
                id: 'q15',
                theme: 'politique_handicap',
                texte: 'Quel est le rôle de la MDPH et de la CDAPH ?',
                exemple_reponse: 'La MDPH est le guichet unique d\'accueil et d\'accompagnement des personnes handicapées. La CDAPH est la commission qui évalue les besoins et prend les décisions d\'attribution des prestations et d\'orientation.'
            },
            {
                id: 'q16',
                theme: 'politique_handicap',
                texte: 'Quelle est la différence entre l\'AAH et la PCH ?',
                exemple_reponse: 'L\'AAH (Allocation aux Adultes Handicapés) est un revenu de remplacement sous conditions de ressources. La PCH (Prestation de Compensation du Handicap) finance les aides humaines, techniques et l\'aménagement du logement.'
            },
            {
                id: 'q17',
                theme: 'politique_handicap',
                texte: 'Quelle est la différence entre un ESAT et une entreprise adaptée ?',
                exemple_reponse: 'Un ESAT est un établissement médico-social offrant un cadre protégé avec un statut d\'usager. Une entreprise adaptée est une entreprise du milieu ordinaire avec des contrats de travail adaptés aux capacités des travailleurs handicapés.'
            },
            {
                id: 'q18',
                theme: 'politique_sante_publique',
                texte: 'Quelles sont les différences entre prévention primaire, secondaire et tertiaire ?',
                exemple_reponse: 'La prévention primaire évite l\'apparition de la maladie (vaccination), la secondaire permet le dépistage précoce, et la tertiaire limite les complications et rechutes.'
            },
            {
                id: 'q19',
                theme: 'politique_sante_publique',
                texte: 'Quel est le rôle de l\'ARS (Agence Régionale de Santé) ?',
                exemple_reponse: 'L\'ARS pilote les politiques de santé en région : organisation de l\'offre de soins, prévention, veille sanitaire, médico-social et coordination entre acteurs.'
            },
            {
                id: 'q20',
                theme: 'politique_sante_publique',
                texte: 'Quelle est la différence entre éducation pour la santé et éducation thérapeutique ?',
                exemple_reponse: 'L\'éducation pour la santé vise la population générale pour promouvoir des comportements sains. L\'éducation thérapeutique s\'adresse aux patients chroniques pour développer leur autonomie dans la gestion de leur maladie.'
            },
            {
                id: 'q21',
                theme: 'politique_lutte_pauvrete',
                texte: 'Quelles sont les conditions pour bénéficier du RSA ?',
                exemple_reponse: 'Le RSA est accessible aux personnes de 25 ans et plus (ou parents isolés, femmes enceintes) ayant des ressources inférieures au montant forfaitaire, résidant en France de manière stable et effective.'
            },
            {
                id: 'q22',
                theme: 'politique_lutte_pauvrete',
                texte: 'Qu\'est-ce que le contrat d\'engagement réciproque dans le cadre du RSA ?',
                exemple_reponse: 'C\'est un contrat entre l\'allocataire du RSA et le département définissant les actions d\'insertion à mener (formation, emploi, santé) et l\'accompagnement proposé, basé sur des droits et devoirs réciproques.'
            },
            {
                id: 'q23',
                theme: 'politique_lutte_pauvrete',
                texte: 'Qu\'est-ce que le non-recours aux droits et comment le combattre ?',
                exemple_reponse: 'Le non-recours désigne les situations où des personnes éligibles ne demandent pas ou n\'obtiennent pas leurs droits. On le combat par la simplification administrative, l\'information, l\'accompagnement et la domiciliation.'
            },
            {
                id: 'q24',
                theme: 'politique_emploi_insertion',
                texte: 'Quelle est la différence entre l\'ARE et l\'ASS ?',
                exemple_reponse: 'L\'ARE (Allocation de Retour à l\'Emploi) indemnise les chômeurs ayant cotisé, calculée sur les salaires antérieurs. L\'ASS (Allocation de Solidarité Spécifique) est une allocation de solidarité pour les chômeurs en fin de droits sous conditions de ressources.'
            },
            {
                id: 'q25',
                theme: 'politique_emploi_insertion',
                texte: 'Qu\'est-ce que l\'insertion par l\'activité économique (IAE) ?',
                exemple_reponse: 'L\'IAE regroupe des structures (AI, ACI, EI, ETTI) qui permettent à des personnes éloignées de l\'emploi de travailler tout en bénéficiant d\'un accompagnement socio-professionnel renforcé.'
            },
            {
                id: 'q26',
                theme: 'politique_emploi_insertion',
                texte: 'Quel est le rôle des missions locales ?',
                exemple_reponse: 'Les missions locales accompagnent les jeunes de 16 à 25 ans en difficulté d\'insertion sociale et professionnelle : orientation, formation, emploi, santé, logement.'
            },
            {
                id: 'q27',
                theme: 'politique_ville_cohesion',
                texte: 'Qu\'est-ce qu\'un Quartier Prioritaire de la Ville (QPV) ?',
                exemple_reponse: 'Un QPV est un territoire urbain identifié par la géographie prioritaire en raison de la concentration de populations à faibles revenus, bénéficiant d\'actions spécifiques de la politique de la ville.'
            },
            {
                id: 'q28',
                theme: 'politique_ville_cohesion',
                texte: 'Quels sont les trois piliers de la politique de la ville ?',
                exemple_reponse: 'Les trois piliers sont : la cohésion sociale (éducation, santé, culture), le cadre de vie et renouvellement urbain (logement, environnement), et l\'emploi et développement économique.'
            },
            {
                id: 'q29',
                theme: 'politique_ville_cohesion',
                texte: 'Quel est le rôle des conseils citoyens ?',
                exemple_reponse: 'Les conseils citoyens associent les habitants des QPV à l\'élaboration et au suivi des contrats de ville, favorisant la démocratie participative et la co-construction des projets locaux.'
            },
            {
                id: 'q30',
                theme: 'etablissements_services_sanitaires',
                texte: 'Quelle est la différence entre un établissement sanitaire et un établissement médico-social ?',
                exemple_reponse: 'Les établissements sanitaires (hôpitaux, cliniques) assurent des soins médicaux. Les établissements médico-sociaux (EHPAD, FAM, MAS) associent soins et accompagnement social pour des personnes en perte d\'autonomie.'
            },
            {
                id: 'q31',
                theme: 'etablissements_services_sanitaires',
                texte: 'Qu\'est-ce que le Conseil de la Vie Sociale (CVS) ?',
                exemple_reponse: 'Le CVS est une instance de participation obligatoire dans les établissements médico-sociaux, réunissant usagers, familles, professionnels et gestionnaires pour donner un avis sur le fonctionnement de l\'établissement.'
            },
            {
                id: 'q32',
                theme: 'etablissements_services_sanitaires',
                texte: 'Quelle est la différence entre un projet d\'établissement et un projet personnalisé ?',
                exemple_reponse: 'Le projet d\'établissement définit les objectifs et l\'organisation générale de la structure. Le projet personnalisé est élaboré avec et pour chaque usager en fonction de ses besoins et attentes spécifiques.'
            }
        ];

        // Initialisation
        document.addEventListener('DOMContentLoaded', () => {
            checkAPIStatus();
            loadQuestions();
            loadHistory();
            updateStats();
            
            // Recharger les questions quand on change de thème
            document.getElementById('theme').addEventListener('change', loadQuestions);
            
            document.getElementById('reponse').addEventListener('input', (e) => {
                document.getElementById('charCount').textContent = e.target.value.length;
            });
        });

        function loadQuestions() {
            const selectedTheme = document.getElementById('theme').value;
            const filteredQuestions = QUESTIONS_EXEMPLES.filter(q => q.theme === selectedTheme);
            
            const list = document.getElementById('questionsList');
            if (filteredQuestions.length === 0) {
                list.innerHTML = '<p style="text-align: center; color: #999; padding: 20px;">Aucune question prédéfinie pour ce thème</p>';
                return;
            }
            
            list.innerHTML = filteredQuestions.map(q => `
                <div class="question-item" onclick="selectQuestion('${q.id}')">
                    <strong>${q.texte}</strong>
                    <p style="font-size: 0.9em; color: #666; margin-top: 5px;">
                        Exemple : ${q.exemple_reponse.substring(0, 80)}...
                    </p>
                </div>
            `).join('');
        }

        function selectQuestion(id) {
            const question = QUESTIONS_EXEMPLES.find(q => q.id === id);
            if (question) {
                document.getElementById('question').value = question.texte;
                document.querySelectorAll('.question-item').forEach(el => el.classList.remove('selected'));
                event.target.closest('.question-item').classList.add('selected');
            }
        }

        async function checkAPIStatus() {
            const statusDiv = document.getElementById('apiStatus');
            try {
                const response = await fetch(`${API_URL}/health`);
                const data = await response.json();
                if (data.status === 'ok') {
                    statusDiv.innerHTML = '<span class="status-dot"></span><span>API connectée ✓</span>';
                    statusDiv.classList.remove('offline');
                } else {
                    throw new Error('API non disponible');
                }
            } catch (error) {
                statusDiv.innerHTML = '<span class="status-dot offline"></span><span>API hors ligne ✗</span>';
                statusDiv.classList.add('offline');
            }
        }

        async function corrigerReponse() {
            const question = document.getElementById('question').value;
            const reponse = document.getElementById('reponse').value;
            const theme = document.getElementById('theme').value;

            if (!question || !reponse) {
                alert('⚠️ Veuillez remplir la question et la réponse');
                return;
            }

            const btn = document.getElementById('submitBtn');
            const loading = document.getElementById('loading');
            
            btn.disabled = true;
            loading.style.display = 'block';

            try {
                const response = await fetch(`${API_URL}/corriger`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        question_id: `Q${Date.now()}`,
                        question_texte: question,
                        reponse_eleve: reponse,
                        theme: theme
                    })
                });

                const data = await response.json();
                displayFeedback(data);
                addToHistory({ question, reponse, feedback: data, timestamp: new Date() });
                updateStats();
            } catch (error) {
                alert('❌ Erreur lors de l\'analyse : ' + error.message);
            } finally {
                btn.disabled = false;
                loading.style.display = 'none';
            }
        }

        function displayFeedback(data) {
            const container = document.getElementById('feedbackContainer');
            const content = document.getElementById('feedbackContent');
            const feedback = data.feedback;

            const headerClass = feedback.est_correct ? 'feedback-correct' : 'feedback-incorrect';
            const statusIcon = feedback.est_correct ? '✅' : '❌';
            const statusText = feedback.est_correct ? 'Réponse Correcte' : 'À Améliorer';

            let errorsHTML = '';
            if (feedback.erreurs_detectees && feedback.erreurs_detectees.length > 0) {
                errorsHTML = `
                    <div class="feedback-section">
                        <h3>🔍 Erreurs détectées</h3>
                        ${feedback.erreurs_detectees.map(err => `
                            <div class="error-item">
                                <div class="error-type">
                                    <span class="error-badge badge-${err.type_erreur}">
                                        ${err.type_erreur.toUpperCase()}
                                    </span>
                                    ${err.sous_categorie ? `- ${err.sous_categorie}` : ''}
                                </div>
                                <p>${err.description}</p>
                            </div>
                        `).join('')}
                    </div>
                `;
            }

            content.innerHTML = `
                <div class="feedback-header ${headerClass}">
                    <div>
                        <div style="font-size: 2em;">${statusIcon}</div>
                        <div style="font-size: 1.5em; font-weight: bold;">${statusText}</div>
                    </div>
                    <div class="score">${feedback.score || 0}/20</div>
                </div>

                ${errorsHTML}

                <div class="feedback-section">
                    <h3>💬 Feedback général</h3>
                    <p>${feedback.feedback_general}</p>
                </div>

                ${feedback.points_forts && feedback.points_forts.length > 0 ? `
                    <div class="feedback-section">
                        <h3>✨ Points forts</h3>
                        <ul>
                            ${feedback.points_forts.map(p => `<li>${p}</li>`).join('')}
                        </ul>
                    </div>
                ` : ''}

                ${feedback.axes_amelioration && feedback.axes_amelioration.length > 0 ? `
                    <div class="feedback-section">
                        <h3>📈 Axes d'amélioration</h3>
                        <ul>
                            ${feedback.axes_amelioration.map(a => `<li>${a}</li>`).join('')}
                        </ul>
                    </div>
                ` : ''}

                ${data.remediation ? `
                    <div class="remediation-section">
                        <h3>🎯 Pistes de remédiation</h3>
                        <p><strong>Focus prioritaire :</strong> ${data.remediation.focus_pedagogique}</p>
                        
                        ${data.remediation.ressources_suggerees && data.remediation.ressources_suggerees.length > 0 ? `
                            <div style="margin-top: 15px;">
                                <strong>📚 Ressources suggérées :</strong>
                                <ul style="margin-top: 10px;">
                                    ${data.remediation.ressources_suggerees.map(r => `<li>${r}</li>`).join('')}
                                </ul>
                            </div>
                        ` : ''}

                        ${data.remediation.exercices_complementaires && data.remediation.exercices_complementaires.length > 0 ? `
                            <div style="margin-top: 15px;">
                                <strong>✏️ Exercices complémentaires :</strong>
                                <ul style="margin-top: 10px;">
                                    ${data.remediation.exercices_complementaires.map(e => `<li>${e}</li>`).join('')}
                                </ul>
                            </div>
                        ` : ''}
                    </div>
                ` : ''}

                <button class="export-btn" onclick="exportFeedback()">📄 Exporter en PDF</button>
            `;

            container.style.display = 'block';
            container.scrollIntoView({ behavior: 'smooth' });
        }

        function addToHistory(item) {
            history.unshift(item);
            if (history.length > 10) history.pop();
            saveHistory();
            loadHistory();
        }

        function loadHistory() {
            const saved = localStorage.getItem('evalia_history');
            if (saved) history = JSON.parse(saved);

            const list = document.getElementById('historyList');
            if (history.length === 0) {
                list.innerHTML = '<p style="text-align: center; color: #999; padding: 20px;">Aucune correction pour le moment</p>';
                return;
            }

            list.innerHTML = history.map((item, index) => `
                <div class="history-item" onclick="viewHistory(${index})">
                    <strong>${item.question.substring(0, 60)}...</strong>
                    <div class="history-meta">
                        <span>${item.feedback.feedback.est_correct ? '✅' : '❌'} ${item.feedback.feedback.score}/20</span>
                        <span>${new Date(item.timestamp).toLocaleDateString()}</span>
                    </div>
                </div>
            `).join('');
        }

        function viewHistory(index) {
            const item = history[index];
            document.getElementById('question').value = item.question;
            document.getElementById('reponse').value = item.reponse;
            displayFeedback(item.feedback);
        }

        function saveHistory() {
            localStorage.setItem('evalia_history', JSON.stringify(history));
        }

        function updateStats() {
            if (history.length === 0) return;

            const total = history.length;
            const correct = history.filter(h => h.feedback.feedback.est_correct).length;
            const scores = history.map(h => h.feedback.feedback.score || 0);
            const avg = (scores.reduce((a, b) => a + b, 0) / total).toFixed(1);

            document.getElementById('statTotal').textContent = total;
            document.getElementById('statCorrect').textContent = `${Math.round(correct/total*100)}%`;
            document.getElementById('statAvg').textContent = `${avg}/20`;
        }

        function exportFeedback() {
            alert('🚀 Fonctionnalité d\'export PDF à venir !');
        }
    </script>
</body>
</html>
