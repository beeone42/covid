from covid import make_attestation

profil = {
    'PRENOM':  "Jean",
    'NOM':     "Dupont",
    'ADDR':    "1 rue de la paix",
    'CP':      "75001",
    'VILLE':   "Paris",
    'NE_LE':   "04/02/1942",
    'NE_A':    "La Bourboule",
    'RAISONS': ["courses"]
    }

make_attestation(profil, "./out/destination")
