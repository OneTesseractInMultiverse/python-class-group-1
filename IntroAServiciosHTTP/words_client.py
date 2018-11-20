# Para instalar la dependencia que permite consumir servicios HTTP, tenemos que
# digitar lo siguiente: pip install requests

import requests
import pprint

texto_crudo = """
Mr. Bingley was good-looking and gentlemanlike; he had a pleasant
countenance, and easy, unaffected manners. His sisters were fine women,
with an air of decided fashion. His brother-in-law, Mr. Hurst, merely
looked the gentleman; but his friend Mr. Darcy soon drew the attention
of the room by his fine, tall person, handsome features, noble mien, and
the report which was in general circulation within five minutes
after his entrance, of his having ten thousand a year. The gentlemen
pronounced him to be a fine figure of a man, the ladies declared he
was much handsomer than Mr. Bingley, and he was looked at with great
admiration for about half the evening, till his manners gave a disgust
which turned the tide of his popularity; for he was discovered to be
proud; to be above his company, and above being pleased; and not all
his large estate in Derbyshire could then save him from having a most
forbidding, disagreeable countenance, and being unworthy to be compared
with his friend.

Mr. Bingley had soon made himself acquainted with all the principal
people in the room; he was lively and unreserved, danced every dance,
was angry that the ball closed so early, and talked of giving
one himself at Netherfield. Such amiable qualities must speak for
themselves. What a contrast between him and his friend! Mr. Darcy danced
only once with Mrs. Hurst and once with Miss Bingley, declined being
introduced to any other lady, and spent the rest of the evening in
walking about the room, speaking occasionally to one of his own party.
His character was decided. He was the proudest, most disagreeable man
in the world, and everybody hoped that he would never come there again.
Amongst the most violent against him was Mrs. Bennet, whose dislike of
his general behaviour was sharpened into particular resentment by his
having slighted one of her daughters.

Elizabeth Bennet had been obliged, by the scarcity of gentlemen, to sit
down for two dances; and during part of that time, Mr. Darcy had been
standing near enough for her to hear a conversation between him and Mr.
Bingley, who came from the dance for a few minutes, to press his friend
to join it.
"""

stop_words = None
response = requests.get(url="http://codelab.subvertic.com/api/v1/stopwords/en")
if response.status_code == 200:
    stop_words = response.json()["swlist"]
    print(stop_words[0])
if 400 <= response.status_code < 500:
    print("La petición HTTP no es correcta [{}]".format(response.status_code))
print(response.status_code) # Leer el código de estado HTTP