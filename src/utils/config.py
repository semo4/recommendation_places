from os import getenv


from dotenv.main import load_dotenv

load_dotenv()
#
#
# ------------ GCP credentials ---------------
#
#
#
GCP_ACCOUNT_TYPE = getenv("GCP_ACCOUNT_TYPE", "service_account")
GCP_PROJECT_ID = getenv("GCP_PROJECT_ID", "novoy-5293d")
GCP_PRIVATE_KEY_ID = getenv(
    "GCP_PRIVATE_KEY_ID", "fbf1232579f07c52d1dd6f770065c943cb8c06e0"
)
GCP_PRIVATE_KEY = getenv(
    "NEW_GCP_PRIVATE_KEY",
    "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDcZ2wQKIuY+ctH\nyHVSEQysLC4vaZ3dwwXr4weRCpuiiKXpqsT03Denkb7rx556NHHXUzJeF2ORWafn\ngtrc420dTp7R15xygbiZEvCP24hMdEqSbqty+2Wt5EKEylvHDTP4GoLdDM8emcrQ\nq3Llp0y5mbiiD2HPCu2viWQNn76REFI7TBCFccFZwVwz9tnEoktsHoazmidK0Uwo\nYFtNTSgPIXKffr0UAZ8iGl/bS9JFb6hyMSGqXOv7pmCMO77+YeRPQXZ2b0E+hRyP\nNeu56KJZaL0qH0//D0Sgrm2j9LYnPVp5zJ4mg/7noH7vBPyriyLJzJJR3l3Vs2AH\nNTV95cVPAgMBAAECggEAWptxw1rHuMXIGeSAxpIXwZgQDJHAwm/wOT8F10yjGrhO\nbLc1bOwzPQIfmNJhhh+VRU4AgMngttpCulwDGZetPcUaaW3X9QL7HoK4vosjhzqv\nhW9VsFlFPa1+4xRFkpkM6kwLzE/9vbi/tfUlsN+MHSjizEzCitkVSXqT1T38m6l0\ntn0A7RoaO34DS2wrO3Bo1fSp9zXoTxnqMx/4LdqpH2Eqg7aiVRuTsJGh4HUp0Q1o\n+CNd8BRnVCfUjC8RyFwAjKRLsXFFpAaonZFjsuA/p6UK/CLZe6ikFFvtfyTDelKZ\nQ31Ynmao0zLkh5g9c5dScwWbL/MeAYKuBJrqUIgtsQKBgQDuvssV/i1eR0j8BLHR\ngJIC62fKLt8WjUptYmd+LQ/xw4Tv9l4qKySNDFAzs7vHgn0eVkjwsosdwyS1j/U+\nLIP4iL1RIczxekT+luUoKA3a5/AqNIR1T/juuuByCGa5I9j4a/rVJh+tnSvRxZQv\nJwp7g9agF/knU3mu14mTlOiXcwKBgQDsVUhfNZ36J/YPLUeD+/d2LzYZu7W62kcG\nLWOdWdTkGoWXw/f7OU60qT8eF0Q7u3LCAOFjH9G8MyfK1e3tR6Kol0ikTCFSlfkw\nWDCFgDg3NJ0+0YSuMPU7wgoX2yhoPcVh3PR3ToEYvKb2h+axPdbQ8gBgldoO4Tze\nyHiUXZxLtQKBgQDXl0kzQgVcBolcsyyUIEM6CbP++taPueVE48DLSwwD6Ohp/RNJ\nhw4JpN3j4mEmp6outAJIASLpLGhA4I+4pmBCFdDHq/sy8JPPRxoGai0gyaOxqR0Y\nBrCne+/kabvBYiKzKmcnBbdDgxOn6YCIF/w6T3KHvT5MCfBvN8nPkH99CwKBgAlP\nmthVbnHqnSEf8Y9bn/ZCCemdoZ1I+D9gDmqmnWKXQOgnyl9VdKpdeKUg2YlY6z6F\ndlvHZyX5BfpRz1vn1Jq7yxrd/PoZ+oVTFCZOVOin5AITkxyhxSejj249LixdMqeW\nYvNIXoGw/Qr9c7NL8mitACLOBJdNfG5yi32c6ol5AoGAIu4pR+gVNCQNoNjLrtBK\nDvBoDMrD6Y9H1PZ0Q/KC/4DkIrDT+J3/1eSkqNlItQqsECjDq6UjqDrcxBAthvXG\nxZB8Dv0nRNV/Fe/t0ru1+WapsG68dpWuk9AwXFuil/peaItBIFKwiewpj7KdFkdD\n9hGM4hhlHi8I3vGcPK1XXvY=\n-----END PRIVATE KEY-----\n",
)
GCP_ACCOUNT_EMAIL = getenv(
    "GCP_ACCOUNT_EMAIL", "recommended-places-test@novoy-5293d.iam.gserviceaccount.com"
)
GCP_ACCOUNT_ID = getenv("GCP_ACCOUNT_ID", "111635334639540507391")
GCP_AUTH_URI = getenv("GCP_AUTH_URI", "https://accounts.google.com/o/oauth2/auth")
GCP_TOKEN_URI = getenv("GCP_TOKEN_URI", "https://oauth2.googleapis.com/token")
GCP_AUTH_PROVIDER_X509_CERT_URL = getenv(
    "GCP_AUTH_PROVIDER_X509_CERT_URL", "https://www.googleapis.com/oauth2/v1/certs"
)
GCP_CLIENT_X509_CERT_URL = getenv(
    "GCP_CLIENT_X509_CERT_URL",
    "https://www.googleapis.com/robot/v1/metadata/x509/recommended-places-test%40novoy-5293d.iam.gserviceaccount.com",
)
UNIVERSE_DOMAIN = getenv("UNIVERSE_DOMAIN", "googleapis.com")
