from openai import OpenAI
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
import time
from config import AFRI_API_KEY, AFRI_BASE_URL, MODELS

# ─────────────────────────────────────────
# CONNEXION AU CLIENT
# ─────────────────────────────────────────
client = OpenAI(
    api_key=AFRI_API_KEY,
    base_url=AFRI_BASE_URL
)

# ─────────────────────────────────────────
# FONCTION PRINCIPALE AVEC RETRY AUTOMATIQUE
# (si erreur réseau ou limite temporaire → 
#  il réessaie automatiquement)
# ─────────────────────────────────────────
@retry(
    wait=wait_exponential(multiplier=1, min=2, max=30),
    stop=stop_after_attempt(5),
    retry=retry_if_exception_type(Exception)
)
def appeler_modele(
    prompt_utilisateur,
    prompt_systeme="Tu es un assistant expert en artisanat africain.",
    modele="standard",
    temperature=0.7,
    max_tokens=1000,
    historique=None
):
    """
    Appelle le modèle IA avec retry automatique.
    
    Paramètres :
    - prompt_utilisateur : ta question / instruction
    - prompt_systeme     : le rôle du modèle
    - modele             : "rapide", "standard", "puissant", "pro", "code"
    - temperature        : créativité (0 = précis, 1 = créatif)
    - max_tokens         : longueur max de la réponse
    - historique         : liste de messages pour conversation continue
    """
    
    # Construction des messages
    messages = [{"role": "system", "content": prompt_systeme}]
    
    # Ajouter l'historique si conversation continue
    if historique:
        messages.extend(historique)
    
    # Ajouter le message de l'utilisateur
    messages.append({"role": "user", "content": prompt_utilisateur})
    
    # Appel à l'API
    response = client.chat.completions.create(
        model=MODELS[modele],
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    return response.choices[0].message.content


# ─────────────────────────────────────────
# FONCTIONS SPÉCIFIQUES ARTSANGO
# ─────────────────────────────────────────

def generer_bio(nom, metier, ville, annees_experience):
    """Génère une bio professionnelle pour un artisan."""
    prompt = f"""
    Génère une bio professionnelle et percutante pour :
    - Nom : {nom}
    - Métier : {metier}
    - Ville : {ville}
    - Expérience : {annees_experience} ans
    
    Format : 3 paragraphes courts, ton professionnel mais chaleureux.
    """
    return appeler_modele(prompt, modele="standard")


def generer_description_produit(nom_produit, materiaux, origine, prix):
    """Génère une description produit pour la marketplace."""
    prompt = f"""
    Crée une description produit attractive pour une marketplace internationale :
    - Produit : {nom_produit}
    - Matériaux : {materiaux}
    - Origine : {origine}
    - Prix : {prix} FCFA
    
    Format : titre accrocheur + description de 4 lignes + 3 points forts.
    Langue : français et anglais.
    """
    return appeler_modele(prompt, modele="standard")


def generer_post_reseaux(produit, plateforme="Instagram"):
    """Génère un post pour les réseaux sociaux."""
    prompt = f"""
    Crée un post {plateforme} vendeur pour ce produit artisanal africain :
    {produit}
    
    Inclure : accroche, description, appel à l'action, hashtags pertinents.
    Ton : authentique, culturel, moderne.
    """
    return appeler_modele(prompt, modele="standard", temperature=0.8)


def generer_storytelling(artisan_info):
    """Génère le storytelling d'un artisan pour attirer des acheteurs."""
    prompt = f"""
    Raconte l'histoire de cet artisan de façon émouvante et vendeuse :
    {artisan_info}
    
    Format : 5 phrases percutantes qui donnent envie d'acheter ses créations.
    Style : storytelling narratif, authentique.
    """
    return appeler_modele(prompt, modele="puissant", temperature=0.9)


def assistant_artisan(question, historique=None):
    """
    Assistant conversationnel pour aider les artisans.
    Garde la mémoire de la conversation.
    """
    systeme = """
    Tu es ArtSango AI, un assistant dédié aux artisans et artistes africains.
    Tu les aides à :
    - Mieux se présenter et raconter leur histoire
    - Vendre leurs créations en ligne
    - Créer du contenu pour leurs réseaux sociaux
    - Développer leur marque personnelle
    
    Ton style : bienveillant, professionnel, culturellement sensible.
    Tu réponds toujours en français sauf si on te parle en anglais.
    """
    return appeler_modele(
        question,
        prompt_systeme=systeme,
        modele="standard",
        historique=historique
    )