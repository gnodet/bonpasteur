package fr.paroisse.bonpasteur;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Named;
import java.util.Map;

@ApplicationScoped
@Named("authors")
public class Authors {
    
    public static class Author {
        private final String name;
        private final String email;
        private final String bio;
        private final String avatar;
        private final String profile;
        private final String job;

        public Author(String name, String email, String bio, String avatar, String profile, String job) {
            this.name = name;
            this.email = email;
            this.bio = bio;
            this.avatar = avatar;
            this.profile = profile;
            this.job = job;
        }

        public String getName() { return name; }
        public String getEmail() { return email; }
        public String getBio() { return bio; }
        public String getAvatar() { return avatar; }
        public String getProfile() { return profile; }
        public String getJob() { return job; }
    }
    
    private final Map<String, Author> authors = Map.of(
        "paroisse", new Author(
            "Paroisse Bon Pasteur",
            "contact@paroisse-bonpasteur.fr",
            "Équipe de communication de la paroisse Bon Pasteur",
            "/images/paroisse-avatar.jpg",
            "/about",
            "Équipe paroissiale"
        ),
        "cure", new Author(
            "Père [Nom]",
            "cure@paroisse-bonpasteur.fr",
            "Curé de la paroisse Bon Pasteur",
            "/images/cure-avatar.jpg",
            "/cure",
            "Curé"
        )
    );
    
    public Author get(String authorId) {
        return authors.getOrDefault(authorId, authors.get("paroisse"));
    }
    
    public Map<String, Author> getAll() {
        return authors;
    }
}
