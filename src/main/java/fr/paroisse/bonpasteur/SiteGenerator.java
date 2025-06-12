package fr.paroisse.bonpasteur;

import io.quarkiverse.roq.generator.RoqSiteGenerator;
import io.quarkus.runtime.Quarkus;
import io.quarkus.runtime.QuarkusApplication;
import io.quarkus.runtime.annotations.QuarkusMain;

@QuarkusMain
public class SiteGenerator implements QuarkusApplication {

    @Override
    public int run(String... args) throws Exception {
        // Génération du site statique
        System.out.println("Génération du site statique de la paroisse Bon Pasteur...");
        
        // Le site sera généré automatiquement par Quarkus Roq
        // Les fichiers seront dans target/roq-site/
        
        return 0;
    }

    public static void main(String[] args) {
        Quarkus.run(SiteGenerator.class, args);
    }
}
