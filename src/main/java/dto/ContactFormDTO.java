package dto;

import jakarta.validation.constraints.*;

public class ContactFormDTO {
    
    @NotBlank(message = "Le nom est obligatoire")
    private String nom;
    
    @Email(message = "Adresse email invalide")
    @NotBlank(message = "L'email est obligatoire")
    private String email;
    
    private String telephone;
    
    private String sujet;
    
    @NotBlank(message = "Le message est obligatoire")
    @Size(min = 10, message = "Le message doit contenir au moins 10 caractères")
    private String message;
    
    private String typeContact;
    
    // Constructeur par défaut
    public ContactFormDTO() {}
    
    // Getters et setters
    public String getNom() {
        return nom;
    }
    
    public void setNom(String nom) {
        this.nom = nom;
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public String getTelephone() {
        return telephone;
    }
    
    public void setTelephone(String telephone) {
        this.telephone = telephone;
    }
    
    public String getSujet() {
        return sujet;
    }
    
    public void setSujet(String sujet) {
        this.sujet = sujet;
    }
    
    public String getMessage() {
        return message;
    }
    
    public void setMessage(String message) {
        this.message = message;
    }
    
    public String getTypeContact() {
        return typeContact;
    }
    
    public void setTypeContact(String typeContact) {
        this.typeContact = typeContact;
    }
    
    @Override
    public String toString() {
        return "ContactFormDTO{" +
                "nom='" + nom + '\'' +
                ", email='" + email + '\'' +
                ", telephone='" + telephone + '\'' +
                ", sujet='" + sujet + '\'' +
                ", typeContact='" + typeContact + '\'' +
                '}';
    }
}
