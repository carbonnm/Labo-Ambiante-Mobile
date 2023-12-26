import pykka

class Led(pykka.ThreadingActor):

    def __init__(self, greeting = 'Coucou'):
        super().__init__()
        self.greeting = greeting

    def on_receive(self, message):
        """
        Méthode de base aux acteurs pour recevoir des messages
        """
        print("j'ai reçu ce message : ", message)
        return 'Hellooooooooo merci de ton message'


#Initialiser un acteur avec la méthode start (nécécissité d'un init aux classes si jamais on veut passer des arguments au start)
actor_ref = Led.start(greeting = 'Yo')

#Stopper un acteur avec la méthode stop

"""
Comment envoyer des messages ? 
--------------------------------------
On peut utiliser la méthode tell ou ask. 
tell n'attend pas pour une réponse : n'est donc pas bloquant 
ask attend la réponse -> on peut lui spécifier un timeout en argument pour qu'il ne bloque pas indéfiniment le programme
"""

answer = actor_ref.ask('Couks')
print(answer)