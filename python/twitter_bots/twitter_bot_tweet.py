import tweepy

#Authenticate to Twitter
auth = tweepy.OAuthHandler("oLaFN2Ycx8Q7bzgf9F3QC3Vj2", "90VjX7iaIEjYqDbAovL2kKrRzaQxhQiZImw5H2nJEo9JoHJhHZ")
auth.set_access_token("735885736776437760-r09rgpFT8eqGj35lKJKjMpd5Ikmha55", "nY68hEOg4TDD0Ksny8q6j2CYjK2p2yeZ0YhIBPX5ZpxNY")

#Creando objeto API
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#Creando un tweet
api.update_status("Hello Tweepy again")

#AAAAAAAAAAAAAAAAAAAAAO9%2BOgEAAAAAg7ug5maPtIFqcdJGeo0goNDVEmA%3DWrPcuxAOdNUBLOjddOfAkJCvPOOoYI4uIitUaP8hGbXxWfe9zO
#Access token: 735885736776437760-BYz0fLIhlYsOZsTjNkx47zUFeqmDJLb
#Access token secret: hp8b0LnQoavH9rDvFiV8CF7efculWqDcW6Le3YE0Uddi8

#Consumer token: xRsIKUaf82mOFiFdNFaNwUDZB
#Consumer token secret: QO1YCNzPfWwM9qFoE66NisXUDBxgo6c6IiNPMG9ifVyYen1767
