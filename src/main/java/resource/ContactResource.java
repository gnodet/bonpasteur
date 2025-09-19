package resource;

import dto.ContactFormDTO;
import service.EmailService;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import jakarta.validation.Valid;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.util.logging.Logger;
import java.util.Map;
import java.util.HashMap;

@Path("/api/contact")
@ApplicationScoped
public class ContactResource {
    
    private static final Logger LOGGER = Logger.getLogger(ContactResource.class.getName());
    
    @Inject
    EmailService emailService;
    
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response submitContact(@Valid ContactFormDTO form) {
        try {
            LOGGER.info("Receiving contact form from: " + form.getEmail());
            
            // Validation anti-spam basique
            if (isSpamMessage(form)) {
                LOGGER.warning("Spam detected from: " + form.getEmail());
                return Response.status(400)
                    .entity(createErrorResponse("Message détecté comme spam"))
                    .build();
            }
            
            // Envoi des emails
            emailService.sendContactNotification(form);
            emailService.sendConfirmationEmail(form);
            
            LOGGER.info("Contact form processed successfully for: " + form.getEmail());
            
            return Response.ok()
                .entity(createSuccessResponse("Votre message a été envoyé avec succès. Vous recevrez une confirmation par email."))
                .build();
                
        } catch (Exception e) {
            LOGGER.severe("Error processing contact form: " + e.getMessage());
            e.printStackTrace();
            
            return Response.status(500)
                .entity(createErrorResponse("Erreur lors de l'envoi du message. Veuillez réessayer plus tard."))
                .build();
        }
    }
    
    @GET
    @Path("/test")
    @Produces(MediaType.APPLICATION_JSON)
    public Response testEndpoint() {
        return Response.ok()
            .entity(createSuccessResponse("API Contact fonctionnelle"))
            .build();
    }
    
    private boolean isSpamMessage(ContactFormDTO form) {
        String message = form.getMessage().toLowerCase();
        String nom = form.getNom().toLowerCase();
        String sujet = form.getSujet() != null ? form.getSujet().toLowerCase() : "";
        
        // Détection de liens suspects
        if (message.contains("http://") || message.contains("https://") || 
            message.contains("www.") || message.contains(".com") || 
            message.contains(".org") || message.contains(".net")) {
            return true;
        }
        
        // Mots-clés spam courants
        String[] spamKeywords = {
            "viagra", "casino", "lottery", "winner", "congratulations",
            "click here", "free money", "make money", "investment",
            "bitcoin", "crypto", "loan", "debt", "credit"
        };
        
        for (String keyword : spamKeywords) {
            if (message.contains(keyword) || nom.contains(keyword) || sujet.contains(keyword)) {
                return true;
            }
        }
        
        // Message trop court ou trop long
        if (form.getMessage().length() < 10 || form.getMessage().length() > 2000) {
            return true;
        }
        
        // Nom trop court
        if (form.getNom().length() < 2) {
            return true;
        }
        
        return false;
    }
    
    private Map<String, Object> createSuccessResponse(String message) {
        Map<String, Object> response = new HashMap<>();
        response.put("success", true);
        response.put("message", message);
        return response;
    }
    
    private Map<String, Object> createErrorResponse(String error) {
        Map<String, Object> response = new HashMap<>();
        response.put("success", false);
        response.put("error", error);
        return response;
    }
}
