package service;

import dto.ContactFormDTO;
import io.quarkus.mailer.Mail;
import io.quarkus.mailer.Mailer;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import org.eclipse.microprofile.config.inject.ConfigProperty;
import java.util.logging.Logger;

@ApplicationScoped
public class EmailService {
    
    private static final Logger LOGGER = Logger.getLogger(EmailService.class.getName());
    
    @Inject
    Mailer mailer;
    
    @ConfigProperty(name = "contact.to.email")
    String contactEmail;
    
    @ConfigProperty(name = "contact.subject.prefix", defaultValue = "[Contact]")
    String subjectPrefix;
    
    public void sendContactNotification(ContactFormDTO form) {
        try {
            // Donner un sujet par défaut si aucun n'est fourni
            String sujetMessage = form.getSujet() != null && !form.getSujet().trim().isEmpty()
                ? form.getSujet()
                : "Nouveau message de contact";
            String subject = subjectPrefix + " " + sujetMessage;
            String content = buildEmailContent(form);
            
            Mail mail = Mail.withText(contactEmail, subject, content)
                .setReplyTo(form.getEmail());
                
            mailer.send(mail);
            LOGGER.info("Contact notification sent to: " + contactEmail);
            
        } catch (Exception e) {
            LOGGER.severe("Error sending contact notification: " + e.getMessage());
            throw new RuntimeException("Erreur lors de l'envoi de la notification", e);
        }
    }
    
    public void sendConfirmationEmail(ContactFormDTO form) {
        try {
            String subject = "Confirmation de votre message - Paroisse Bon Pasteur";
            String content = buildConfirmationContent(form);
            
            Mail mail = Mail.withText(form.getEmail(), subject, content);
            mailer.send(mail);
            LOGGER.info("Confirmation email sent to: " + form.getEmail());
            
        } catch (Exception e) {
            LOGGER.severe("Error sending confirmation email: " + e.getMessage());
            // Ne pas faire échouer si la confirmation échoue
        }
    }
    
    private String buildEmailContent(ContactFormDTO form) {
        return String.format("""
            Nouveau message de contact reçu depuis le site de la Paroisse Bon Pasteur :
            
            ═══════════════════════════════════════════════════════════════
            
            👤 INFORMATIONS DU CONTACT
            ═══════════════════════════════════════════════════════════════
            Nom : %s
            Email : %s
            Téléphone : %s
            Type de contact : %s
            
            📝 SUJET
            ═══════════════════════════════════════════════════════════════
            %s
            
            💬 MESSAGE
            ═══════════════════════════════════════════════════════════════
            %s
            
            ═══════════════════════════════════════════════════════════════
            
            Pour répondre, utilisez directement la fonction "Répondre" de votre messagerie.
            L'email sera automatiquement adressé à : %s
            
            ---
            Message envoyé automatiquement depuis le site web de la Paroisse Bon Pasteur de Caen
            Date : %s
            """, 
            form.getNom(),
            form.getEmail(),
            form.getTelephone() != null && !form.getTelephone().trim().isEmpty() 
                ? form.getTelephone() : "Non renseigné",
            form.getTypeContact() != null && !form.getTypeContact().trim().isEmpty() 
                ? getTypeContactLabel(form.getTypeContact()) : "Contact général",
            form.getSujet() != null && !form.getSujet().trim().isEmpty()
                ? form.getSujet() : "Nouveau message de contact",
            form.getMessage(),
            form.getEmail(),
            java.time.LocalDateTime.now().format(
                java.time.format.DateTimeFormatter.ofPattern("dd/MM/yyyy à HH:mm")
            )
        );
    }
    
    private String buildConfirmationContent(ContactFormDTO form) {
        return String.format("""
            Bonjour %s,
            
            Nous avons bien reçu votre message concernant : "%s"
            
            Votre demande sera traitée dans les plus brefs délais par notre équipe.
            Nous vous répondrons à l'adresse email : %s
            
            📞 En cas d'urgence, vous pouvez nous contacter directement :
            • Téléphone : 02 31 86 13 11
            • Email : contact.bonpasteur@gmail.com
            
            🏛️ Paroisse Bon Pasteur de Caen
            Presbytère Saint-Jean
            11 rue des Équipes d'Urgence
            14000 Caen
            
            Que Dieu vous bénisse,
            L'équipe de la Paroisse Bon Pasteur de Caen
            
            ---
            Ceci est un message automatique, merci de ne pas y répondre directement.
            Pour toute nouvelle demande, utilisez le formulaire de contact sur notre site web.
            """,
            form.getNom(),
            form.getSujet() != null && !form.getSujet().trim().isEmpty()
                ? form.getSujet() : "votre message",
            form.getEmail()
        );
    }
    
    private String getTypeContactLabel(String typeContact) {
        return switch (typeContact) {
            case "bapteme" -> "Demande de baptême";
            case "mariage" -> "Demande de mariage";
            case "obseques" -> "Organisation d'obsèques";
            case "certificat" -> "Demande de certificat";
            case "pretre" -> "Rencontrer un prêtre";
            case "groupe" -> "Rejoindre un groupe";
            case "don" -> "Question sur les dons";
            case "autre" -> "Autre demande";
            default -> "Contact général";
        };
    }
}
