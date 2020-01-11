# -*-coding:Latin-1 -*
from setuptools import setup, find_packages

# notez qu'on import la lib
# donc assurez-vous que l'importe n'a pas d'effet de bord
import dbVedaSf

# Ceci n'est qu'un appel de fonction. Mais il est tres long
# et il comporte beaucoup de paramtres
setup(
    # le nom de votre bibliothque, tel qu'il apparaitre sur pypi
    name='dbVedaSf',

    # la version du code
    version=dbVedaSf.__version__,

    # Liste les packages � ins�rer dans la distribution
    # plut�t que de le faire � la main, on utilise la foncton
    # find_packages() de setuptools qui va cherche tous les packages
    # python recursivement dans le dossier courant.
    # C'est pour cette raison que l'on a tout mis dans un seul dossier:
    # on peut ainsi utiliser cette fonction facilement
    packages=find_packages(),

    # votre pti nom
    author="Art",

    # Votre email, sachant qu'il sera publique visible, avec tous les risques
    # que �a implique.
    author_email="archange.jb@gmail.com",

    # Une description courte
    description="Ce module permet de lire et de charger la base de données à partir des fichiers .vd",

    # Une description longue, sera affich�e pour pr�senter la lib
    # G�n�ralement on dump le README ici
    long_description=open('README.md').read(),

    # Vous pouvez rajouter une liste de d�pendances pour votre lib
    # et m�me pr�ciser une version. A l'installation, Python essayera de
    # les t�l�charger et les installer.
    #
    # Ex: ["gunicorn", "docutils >= 0.3", "lxml==0.5a7"]
    #
    # Dans notre cas on en a pas besoin, donc je le commente, mais je le
    # laisse pour que vous sachiez que �a existe car c'est tr�s utile.
    # install_requires= ,

    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,

    # Une url qui pointe vers la page officielle de votre lib
    url='http://github.com/qosyx/vedadb',

    # Il est d'usage de mettre quelques metadata � propos de sa lib
    # Pour que les robots puissent facilement la classer.
    # La liste des marqueurs autoris�es est longue:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    #
    # Il n'y a pas vraiment de r�gle pour le contenu. Chacun fait un peu
    # comme il le sent. Il y en a qui ne mettent rien.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: db",
    ],

    # C'est un syst�me de plugin, mais on s'en sert presque exclusivement
    # Pour cr�er des commandes, comme "django-admin".
    # Par exemple, si on veut cr�er la fabuleuse commande "proclame-sm", on
    # va faire pointer ce nom vers la fonction proclamer(). La commande sera
    # cr�� automatiquement.
    # La syntaxe est "nom-de-commande-a-creer = package.module:fonction".
    entry_points={
        'console_scripts': [
            'dbVedaSf = dbVedaSf.core:dbVedaSf',
        ],
    },

    # A fournir uniquement si votre licence n'est pas list�e dans "classifiers"
    # ce qui est notre cas
    license="WTFPL",

    # Il y a encore une chi�e de param�tres possibles, mais avec �a vous
    # couvrez 90% des besoins

)