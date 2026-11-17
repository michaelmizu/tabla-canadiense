# Table canadienne — le mouvement d'abord

**Une application visuelle pour comprendre le mouvement de l’index et la position des tiges sur une planche de rééducation perforée.** La simulation est illustrative : **elle ne constitue pas une prescription**. Les exercices et le montage réel doivent être autorisés et vérifiés par un thérapeute de la main.

[Español](README.md) · [Modifications v10](CAMBIOS_v10.md) · [Revue UX (ES)](REVISION_UX_v10.md)

## Démarrer

Ouvrez `index.html` dans un navigateur moderne. Aucune installation, connexion Internet ni compilation n’est nécessaire. L’application est contenue dans **un seul fichier HTML** avec CSS, JavaScript et SVG intégrés, sans dépendances externes.

### Ce qui change

Dès l’ouverture, **on voit le doigt bouger** sur la planche. L’action principale, **« Voir la démonstration »**, ouvre directement l’exemple **« Cible avec balle »**, avec animation (au lieu de commencer par une préparation statique).

- **Lecture / pause** du mouvement grâce à un bouton visible au-dessus de la planche.
- **Exploration manuelle** du mouvement à l’aide d’un curseur accessible au clavier.
- Vues **de dessus** et **3D**; position des tiges et navigation entre les étapes.
- **« J’ai une fiche d’exercices »** pour coller un code `TABLA1` remis par le thérapeute.
- **« Je suis thérapeute »** pour accéder aux mesures, exercices, modèles et exports.

**Ne reproduisez pas les exercices de démonstration comme traitement.** Lors du chargement d’une vraie fiche, l’animation **ne démarre pas automatiquement**. Les réglages de réduction des animations du système sont respectés.

## Langues

L’interface et les contenus prédéfinis sont disponibles en **espagnol et en français**. Le PDF suit la langue de l’interface. Le texte saisi librement par un professionnel n’est pas traduit automatiquement afin d’en préserver le sens clinique.

## Planche et exportations

- Planche **400 × 300 mm**, 165 trous, 15 colonnes A–O, 11 rangées 1–11, entraxe 25 mm.
- **SVG à l’échelle 1:1** et **DXF en millimètres** avec diamètre Ø12,2 mm par défaut ou Ø12,0 mm.
- PDF A4 sur une page si la fiche tient lisiblement.
- Code `TABLA1` compatible avec les versions antérieures. Le contrôle de cohérence **ne constitue pas une signature** du thérapeute.
- Modèles enregistrés dans `localStorage`. Aucun journal de douleur ni graphique de suivi. Les anciens journaux peuvent être exportés ou effacés manuellement, s’ils existent.

## Sécurité et vie privée

**Cette application ne remplace ni le chirurgien ni le thérapeute de la main.** Elle ne vérifie pas la phase postopératoire, la stabilité de la réparation, les appuis réels ni toutes les interférences mécaniques. Le modèle anatomique représente seulement l’index; les hauteurs de la vue 3D sont indicatives. Le montage doit être vérifié sur la planche réelle.

Le massage ou la chaleur nécessitent une plaie fermée et sèche, et l’accord du thérapeute. Ne pratiquez pas les exercices et n’augmentez pas le niveau simplement parce que l’animation le montre. En cas de claquement, de perte d’extension, de douleur ou de gonflement inhabituel, arrêtez et consultez l’équipe soignante.

Les modèles et éventuels journaux restent dans le stockage du navigateur, sans synchronisation. **Ne publiez jamais de données ou de fiches de patients** sur GitHub Pages.

## GitHub Pages

Ajoutez les fichiers à la branche `main` d’un dépôt GitHub, puis choisissez **Settings → Pages → Deploy from a branch → main → /(root)**.

## Tests

```bash
python -m pip install -r requirements-test.txt
python -m playwright install chromium
python tests/smoke.py
```

Le test vérifie notamment l’animation, la pause, le curseur, l’interface mobile, la réduction des animations, les langues, les fiches et les exports SVG/DXF/PDF. Les dépendances de test ne sont pas nécessaires à la page.

## Licence

MIT, voir [`LICENSE`](LICENSE). Aucune garantie clinique.
