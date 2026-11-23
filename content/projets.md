# Projets

## Llama, cet agent conversationnel (projet du portfolio)

Llama est l'agent conversationnel de ce portfolio, conçu et développé par Bryan. Il répond aux questions sur son parcours grâce à un système RAG utilisant une recherche vectorielle avec embedding. Il peut également interagir avec le site grâce à des appels d'outils : navigation vers certaines pages, lecture de musique et ouverture du formulaire de contact avec génération d'un brouillon.

Côté technique, Llama repose sur une API Flask en Python, une interface React et plusieurs modèles de langage hébergés, organisés en cascade avec un mécanisme de repli automatique en cas d'indisponibilité ou de quota atteint. Le projet est déployé sur un serveur Hetzner. Les actions disponibles sont limitées à des listes autorisées pour garantir la sécurité, et l'envoi d'un e-mail nécessite une confirmation du visiteur.

## Refonte du système d'impression de billets – Imagina

Dans le cadre des solutions de billetterie événementielle d'Imagina, Bryan a participé à la refonte du système d'impression de billets utilisé lors d'événements pouvant accueillir jusqu'à 100 000 personnes.

L'ancien système reposait notamment sur des imprimantes thermiques connectées en Wi-Fi via des adaptateurs Ethernet TP-Link. Bryan a contribué à la mise en place d'une nouvelle solution permettant de connecter directement les imprimantes aux tablettes et smartphones Android par USB ou USB-C, en utilisant les SDK natifs des fabricants.

Cette évolution a permis de simplifier l'architecture matérielle et de supprimer la dépendance à certains équipements réseau intermédiaires. Le projet impliquait également le développement des interfaces de gestion de l'impression et la coordination des tests.

**Technologies et compétences :** Kotlin, Android, SDK natifs, USB, intégration matérielle, billetterie événementielle.

## Optimisation des traitements asynchrones et des performances backend – Imagina

Bryan a travaillé sur l'amélioration des performances du backend Symfony d'Imagina, notamment sur des problématiques liées aux traitements asynchrones utilisant Redis.

Lors d'un incident de traitement, il a analysé les files d'attente, les processus et les logs afin d'identifier l'origine du ralentissement. L'investigation a notamment révélé l'exécution répétée d'une même requête SQL des milliers de fois.

Il a participé à la stabilisation du traitement en isolant temporairement le processus problématique sur un autre serveur, puis à l'optimisation de la logique d'accès aux données afin de limiter les requêtes répétitives.

**Technologies et compétences :** PHP, Symfony, Redis, SQL, Docker, debugging, optimisation backend, traitement asynchrone.

## Système de réservation avec gestion de créneaux – Imagina

Bryan a participé au développement d'un système de réservation permettant de gérer des créneaux horaires associés à différentes ressources et aux calendriers personnels des utilisateurs.

Le système devait prendre en compte les disponibilités, les configurations horaires et les contraintes propres à chaque ressource afin de proposer des créneaux de réservation cohérents.

Il a notamment travaillé sur la logique métier, les API backend et les requêtes SQL nécessaires au fonctionnement du système. Une attention particulière a été portée à la fiabilité du calcul des disponibilités et à la validation des créneaux proposés.

**Technologies et compétences :** PHP, Symfony, SQL, API REST, logique métier, gestion de calendriers et de disponibilités.
