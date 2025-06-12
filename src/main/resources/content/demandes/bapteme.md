---
title: Demande de Baptême
subtitle: Célébrer le baptême dans notre paroisse
description: Informations et démarches pour demander un baptême dans la paroisse Bon Pasteur
template: page
---

## Le sacrement du baptême

Le baptême est le premier des sacrements chrétiens. Il marque l'entrée dans la communauté des croyants et le début de la vie chrétienne. C'est un moment de joie et de célébration pour toute la famille et la communauté paroissiale.

## Conditions et préparation

### Pour un baptême d'enfant (0-7 ans)

**Conditions :**
- Au moins un des parents doit être baptisé
- Les parents s'engagent à donner une éducation chrétienne à leur enfant
- Choix de parrains et marraines baptisés et confirmés

**Préparation :**
- Rencontre avec un prêtre ou un diacre
- Participation à une préparation au baptême (2 séances)
- Remise des documents nécessaires

### Pour un baptême d'adulte

**Conditions :**
- Demande personnelle et libre
- Engagement dans un parcours de préparation (catéchuménat)
- Accompagnement par un parrain ou une marraine

**Préparation :**
- Parcours catéchuménal (plusieurs mois)
- Rencontres régulières avec l'équipe d'accompagnement
- Participation à la vie de la communauté

## Documents nécessaires

- Acte de naissance de la personne à baptiser
- Certificat de baptême des parents (si baptisés)
- Certificat de baptême et de confirmation des parrains/marraines
- Attestation de mariage religieux des parents (si mariés à l'église)

## Démarches

1. **Prise de contact** : Contactez le secrétariat paroissial au moins 3 mois avant la date souhaitée
2. **Rencontre préparatoire** : Rendez-vous avec un prêtre ou diacre
3. **Préparation** : Participation aux séances de préparation
4. **Choix de la date** : En accord avec les disponibilités de la paroisse
5. **Célébration** : Le jour J, en famille et en communauté

## Dates et horaires

Les baptêmes sont généralement célébrés :
- **Dimanche après-midi** : 15h30 (selon les paroisses)
- **Samedi après-midi** : 16h00 (selon les paroisses)
- **Pendant les messes dominicales** : selon les communautés locales

## Contact

Pour toute demande de baptême, contactez :

**Secrétariat paroissial**  
Téléphone : 02 XX XX XX XX  
Email : bapteme@paroisse-bonpasteur.fr

**Permanences :**  
Mardi et Jeudi : 14h - 17h  
Samedi : 10h - 12h

## Formulaire de demande

<form class="contact-form">
    <div class="form-group">
        <label for="type-bapteme">Type de baptême *</label>
        <select id="type-bapteme" name="type-bapteme" required>
            <option value="">Choisissez</option>
            <option value="enfant">Baptême d'enfant (0-7 ans)</option>
            <option value="adulte">Baptême d'adulte</option>
        </select>
    </div>
    
    <div class="form-group">
        <label for="nom-personne">Nom de la personne à baptiser *</label>
        <input type="text" id="nom-personne" name="nom-personne" required>
    </div>
    
    <div class="form-group">
        <label for="prenom-personne">Prénom de la personne à baptiser *</label>
        <input type="text" id="prenom-personne" name="prenom-personne" required>
    </div>
    
    <div class="form-group">
        <label for="date-naissance">Date de naissance *</label>
        <input type="date" id="date-naissance" name="date-naissance" required>
    </div>
    
    <div class="form-group">
        <label for="nom-parent">Nom du parent/demandeur *</label>
        <input type="text" id="nom-parent" name="nom-parent" required>
    </div>
    
    <div class="form-group">
        <label for="email">Email *</label>
        <input type="email" id="email" name="email" required>
    </div>
    
    <div class="form-group">
        <label for="telephone">Téléphone *</label>
        <input type="tel" id="telephone" name="telephone" required>
    </div>
    
    <div class="form-group">
        <label for="clocher">Clocher souhaité</label>
        <select id="clocher" name="clocher">
            <option value="">Choisissez un lieu</option>
            <option value="sainte-trinite">Sainte Trinité / Saint-Gilles</option>
            <option value="saint-pierre">Saint-Pierre</option>
            <option value="saint-etienne">Saint-Étienne</option>
            <option value="autre">Autre (préciser dans le message)</option>
        </select>
    </div>
    
    <div class="form-group">
        <label for="date-souhaitee">Date souhaitée</label>
        <input type="date" id="date-souhaitee" name="date-souhaitee">
    </div>
    
    <div class="form-group">
        <label for="message">Message complémentaire</label>
        <textarea id="message" name="message" placeholder="Informations complémentaires, questions..."></textarea>
    </div>
    
    <button type="submit" class="submit-btn">Envoyer la demande</button>
</form>
