// Formulaire de contact
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const submitBtn = document.getElementById('submitBtn');
    const formMessage = document.getElementById('formMessage');
    
    if (!form) return; // Pas de formulaire sur cette page
    
    // Validation en temps réel
    const inputs = form.querySelectorAll('input[required], textarea[required]');
    inputs.forEach(input => {
        input.addEventListener('blur', () => validateField(input));
        input.addEventListener('input', () => clearError(input));
    });
    
    // Soumission du formulaire
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        if (!validateForm()) {
            return;
        }
        
        await submitForm();
    });
    
    function validateField(field) {
        const value = field.value.trim();
        const fieldName = field.name;
        let isValid = true;
        let errorMessage = '';
        
        // Validation selon le type de champ
        switch(fieldName) {
            case 'nom':
                if (value.length < 2) {
                    isValid = false;
                    errorMessage = 'Le nom doit contenir au moins 2 caractères';
                }
                break;
                
            case 'email':
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(value)) {
                    isValid = false;
                    errorMessage = 'Veuillez saisir une adresse email valide';
                }
                break;
                
            case 'sujet':
                // Le sujet n'est plus obligatoire dans le design Saint-Malo
                // Il sera généré automatiquement si absent
                break;
                
            case 'message':
                if (value.length < 10) {
                    isValid = false;
                    errorMessage = 'Le message doit contenir au moins 10 caractères';
                } else if (value.length > 2000) {
                    isValid = false;
                    errorMessage = 'Le message ne peut pas dépasser 2000 caractères';
                }
                break;
        }
        
        showFieldError(field, isValid, errorMessage);
        return isValid;
    }
    
    function showFieldError(field, isValid, errorMessage) {
        const errorElement = document.getElementById(field.id + '-error');

        if (isValid) {
            field.classList.remove('is-invalid');
            if (errorElement) {
                errorElement.textContent = '';
                errorElement.style.display = 'none';
            }
        } else {
            field.classList.add('is-invalid');
            if (errorElement) {
                errorElement.textContent = errorMessage;
                errorElement.style.display = 'block';
            }
        }
    }

    function clearError(field) {
        const errorElement = document.getElementById(field.id + '-error');

        field.classList.remove('is-invalid');
        if (errorElement) {
            errorElement.textContent = '';
            errorElement.style.display = 'none';
        }
    }
    
    function validateForm() {
        let isValid = true;
        
        // Valider tous les champs requis
        inputs.forEach(input => {
            if (!validateField(input)) {
                isValid = false;
            }
        });
        
        // Vérification anti-spam (honeypot)
        const honeypot = form.querySelector('input[name="website"]');
        if (honeypot && honeypot.value.trim() !== '') {
            showMessage('Erreur de validation du formulaire', 'error');
            return false;
        }
        
        return isValid;
    }
    
    async function submitForm() {
        // Désactiver le bouton et afficher le loading
        setLoading(true);
        hideMessage();
        
        try {
            // Préparer les données
            const formData = new FormData(form);
            const data = {
                nom: formData.get('nom').trim(),
                email: formData.get('email').trim(),
                telephone: '', // Pas de champ téléphone dans le formulaire simplifié
                typeContact: 'general', // Toujours général
                sujet: 'Contact depuis le site web',
                message: formData.get('message').trim()
            };
            
            // Envoyer la requête
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            
            if (response.ok && result.success) {
                showMessage(result.message, 'success');
                form.reset();
                
                // Scroll vers le message de succès
                setTimeout(() => {
                    formMessage.scrollIntoView({ 
                        behavior: 'smooth', 
                        block: 'center' 
                    });
                }, 100);
                
            } else {
                throw new Error(result.error || 'Erreur lors de l\'envoi du message');
            }
            
        } catch (error) {
            console.error('Erreur:', error);
            showMessage(
                error.message || 'Erreur lors de l\'envoi du message. Veuillez réessayer.',
                'error'
            );
        } finally {
            setLoading(false);
        }
    }
    
    function setLoading(loading) {
        const btnText = submitBtn.querySelector('.btn-text');
        const btnLoading = submitBtn.querySelector('.btn-loading');

        submitBtn.disabled = loading;
        if (loading) {
            if (btnText) btnText.style.display = 'none';
            if (btnLoading) btnLoading.classList.remove('d-none');
        } else {
            if (btnText) btnText.style.display = 'inline';
            if (btnLoading) btnLoading.classList.add('d-none');
        }
    }
    
    function showMessage(message, type) {
        formMessage.textContent = message;
        formMessage.className = `alert mt-3 ${type === 'success' ? 'alert-success' : 'alert-danger'}`;
        formMessage.classList.remove('d-none');
    }

    function hideMessage() {
        formMessage.classList.add('d-none');
        formMessage.textContent = '';
    }
    
    // Compteur de caractères pour le message
    const messageField = document.getElementById('message');
    if (messageField) {
        const maxLength = 2000;
        
        // Créer l'élément compteur
        const counter = document.createElement('div');
        counter.className = 'character-counter';
        counter.style.cssText = `
            font-size: 0.875rem;
            color: #6c757d;
            text-align: right;
            margin-top: 0.25rem;
        `;
        
        messageField.parentNode.appendChild(counter);
        
        function updateCounter() {
            const length = messageField.value.length;
            counter.textContent = `${length}/${maxLength} caractères`;
            
            if (length > maxLength * 0.9) {
                counter.style.color = '#dc3545';
            } else if (length > maxLength * 0.8) {
                counter.style.color = '#ffc107';
            } else {
                counter.style.color = '#6c757d';
            }
        }
        
        messageField.addEventListener('input', updateCounter);
        updateCounter(); // Initialiser
    }
});
