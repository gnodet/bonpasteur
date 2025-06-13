package fr.paroisse.bonpasteur;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Named;
import java.util.List;
import java.util.Map;

@ApplicationScoped
@Named("menu")
public class Menu {
    
    public static class MenuItem {
        private final String title;
        private final String url;
        private final List<MenuItem> children;
        
        public MenuItem(String title, String url) {
            this.title = title;
            this.url = url;
            this.children = List.of();
        }
        
        public MenuItem(String title, String url, List<MenuItem> children) {
            this.title = title;
            this.url = url;
            this.children = children;
        }
        
        public String getTitle() { return title; }
        public String getUrl() { return url; }
        public List<MenuItem> getChildren() { return children; }
    }
    
    public List<MenuItem> getItems() {
        return List.of(
            new MenuItem("Accueil", "/"),
            new MenuItem("Découvrir", "/decouvrir", List.of(
                new MenuItem("Bienvenue", "/bienvenue"),
                new MenuItem("Présentation", "/presentation")
            )),
            new MenuItem("Les Clochers", "/clochers", List.of(
                new MenuItem("Sainte Trinité", "/clochers/sainte-trinite"),
                new MenuItem("Saint-Pierre", "/clochers/saint-pierre"),
                new MenuItem("Saint-Étienne", "/clochers/saint-etienne")
            )),
            new MenuItem("Demandes", "/demandes", List.of(
                new MenuItem("Baptême", "/demandes/bapteme"),
                new MenuItem("Mariage", "/demandes/mariage"),
                new MenuItem("Catéchèse", "/demandes/catechese")
            )),
            new MenuItem("Propositions", "/propositions", List.of(
                new MenuItem("Enfance", "/propositions/enfance"),
                new MenuItem("Jeunes", "/propositions/jeunes"),
                new MenuItem("Solidarité", "/propositions/solidarite")
            )),
            new MenuItem("Infos", "/infos", List.of(
                new MenuItem("Horaires Messes", "/horaires-messes"),
                new MenuItem("Actualités", "/actualites"),
                new MenuItem("Contact", "/contact")
            ))
        );
    }
}
