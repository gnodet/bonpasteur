---
title: Contact
subtitle: Nous sommes à votre écoute
description: Coordonnées et formulaire de contact de la paroisse Bon Pasteur
template: page
---

## Nos coordonnées

### Adresse principale
Paroisse Bon Pasteur  
[Adresse complète]  
14000 Caen

### Téléphone
**02 XX XX XX XX**  
Lundi - Vendredi : 9h - 17h

### Email
**contact@paroisse-bonpasteur.fr**  
Réponse sous 48h

### Permanences
- Mardi et Jeudi : 14h - 17h
- Samedi : 10h - 12h
- Sur rendez-vous possible

### Curé de la paroisse
**Père [Nom]**  
Rendez-vous sur demande  
cure@paroisse-bonpasteur.fr

## En cas d'urgence

**Pour les urgences pastorales (sacrement des malades, obsèques urgentes) :**

Téléphone d'urgence : **06 XX XX XX XX** (24h/24)

N'hésitez pas à nous appeler, même en dehors des heures d'ouverture.

## Formulaire de contact

<form class="contact-form" id="contactForm">
    <div class="form-group">
        <label for="nom">Nom *</label>
        <input type="text" id="nom" name="nom" required>
    </div>
    
    <div class="form-group">
        <label for="prenom">Prénom *</label>
        <input type="text" id="prenom" name="prenom" required>
    </div>
    
    <div class="form-group">
        <label for="email">Email *</label>
        <input type="email" id="email" name="email" required>
    </div>
    
    <div class="form-group">
        <label for="telephone">Téléphone</label>
        <input type="tel" id="telephone" name="telephone">
    </div>
    
    <div class="form-group">
        <label for="sujet">Sujet de votre message *</label>
        <select id="sujet" name="sujet" required>
            <option value="">Choisissez un sujet</option>
            <option value="information">Demande d'information</option>
            <option value="bapteme">Baptême</option>
            <option value="mariage">Mariage</option>
            <option value="obseques">Obsèques</option>
            <option value="catechese">Catéchèse</option>
            <option value="groupe">Rejoindre un groupe</option>
            <option value="pretre">Rencontrer un prêtre</option>
            <option value="intention">Intention de prière</option>
            <option value="autre">Autre</option>
        </select>
    </div>
    
    <div class="form-group">
        <label for="message">Votre message *</label>
        <textarea id="message" name="message" required placeholder="Décrivez votre demande ou votre question..."></textarea>
    </div>
    
    <button type="submit" class="submit-btn">
        <i class="fas fa-paper-plane"></i> Envoyer le message
    </button>
</form>
