# Défi

Nous voulons que vous suiviez notre [défi de codage DevOps](https://github.com/coveo/devops-coding-challenge) régulier. Pour
gagner du temps, nous vous fournissons une implémentation Python de base afin de vous aider à démarrer le projet.

Vous êtes libre de l'utiliser simplement et de suggérer quelques améliorations.

Vous pouvez également simplement l'utiliser comme modèle et réimplémenter la logique requise dans le langage de votre choix.
Veuillez choisir un langage de progrqammation avec lequel vous êtes à l'aise car nous vous challengerons certainement sur
vos choix.

Toutes les étapes énumérées ci-dessous seront nécessaires lors de l'entretien. Nous nous attendons à ce que vous que vous les
réalisiez AVANT notre rencontre.

- Assurez-vous que vous pouvez exécuter le code et comprendre ce qui se passe.
- Passez en revue le code et prenez des notes sur les éléments que vous souhaitez améliorer ou modifier. Supposons que ce code
est en production en ce moment et que vous devez planifier les prochaines versions. En ayant un processus agile à l'esprit,
que changeriez-vous dans la première version, la seconde, etc. Cela nous aidera à concentrer notre discussion sur ce qui est
important en premier.
- Assurez-vous d'avoir une configuration qui vous permet d'atteindre un point d'arrêt et de déboguer étape par étape, peu
importe quelle application (IDE) que vous utilisez pour le faire. Mais assurez-vous que vous êtes à l'aise pour déboguer dans
l'environnement que vous choisissez avant l'entretien car il y aura des bugs 😉.
- Ayez un éditeur ou un IDE prêt à coder pendant l'entretien.
- Avoir Git installé.

Nous n'avons pas suivi nos normes normales, vous devriez donc avoir quelque chose à dire à propos de ce code.

Nous attendons de vous que vous compreniez un minimum l'ensemble du projet et que vous ayez un avis dessus. Nous comprenons que
vous n'êtes peut-être pas à 100 % familier avec AWS. C'est normal et nous ne nous attendons pas à ce que vous appreniez tout
avant l'entretien.

## Exécuter

1. Vous devez d'abord créer un compte AWS. Un peut être créé gratuitement.
2. Créez un compartiment S3 et chargez-y des fichiers. Gardez à l'esprit qu'il peut y avoir des frais si vous dépassez le
[exigences du niveau gratuit](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types =*all&awsf.Free%20Tier%20Categories=*all&all-free-tier.q=S3&all-free-tier.q_operator=AND)
(5 Go au moment de la rédaction).
3. Pour exécuter le projet lui-même, vous aurez besoin de Python 3.8 ou plus récent et de [Poetry](https://python-poetry.org/docs/#installation)
4. Lancez `poetry install`
5. Lancez `poetry run python ./main.py`

## Pendant l'entrevue technique

Soyez prêt pour la revue par les pairs lors de votre entretien technique. Attendez-vous également à des défis supplémentaires car
nous pourrions vous demander d'exécuter votre programme dans un environnement différent avec un nombre important de fichiers.

## Un dernier conseil

Assurez-vous d'avoir du plaisir pendant l'exécution de ce défi. Il est très rare que des candidats saisissent l'étendue des
pièges à éviter et l'ensemble des défis techniques que représente ce challenge. Nous ne recherchons pas la perfection, mais vous
serez évalué sur votre capacité à vous adapter lorsque nous ferons face aux différents problèmes auxquels vous serez immanquablement
confrontés.

Lors de l'entrevue, considérez les interviewers comme des collègues. N'hésitez pas à demander de l'aide comme vous le feriez
normalement dans le cadre de votre travail. Ils sont là pour vous aider et non pour vous piéger. Leur principal objectif est
de trouver en vous leur futur collègue avec qui ils auront du plaisir à travailler.

À bientôt!
