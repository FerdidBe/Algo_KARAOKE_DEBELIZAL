class Player:
    def __init__(self,pseudo):
        self.pseudo=pseudo
        self.participations={
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
        }
    
    def add_partition (self,song_id, score):
        if score > self.participations [song_id]:
            self.participations [song_id]=score
    
    def get_best_score (self):
        return max (self.partitions.values())
    
    def get_worst_score(self):
        return min ([score for score in self.participations.values() if score > 0], default=50)
    
    def ger_average_score(self):
        total = sum ([score for score in self.partitions.values() if score > 0])
        count = len ([score for score in self.partitions.values if score > 0])
        return total/count if count >  0 else 0
    
class Karaoke: 
    def __init__ (self, songs):
        self.players= []
        self.songs = songs
    
    def add_player (self, player):
        self.players.append(player)
    
    def remove_player (self, player):
        if len (self.players) > 1:
            self.players.remove(player)
    
    def get_best_score (self, song_id):
        best_score = 0
        for player in self.players:
            score= player.partitions [song_id]
            if score > best_score: 
                best_score=score
        return best_score
    
    def get_best_score_total (seld):
        best_score_total=0
        for player in self.players:
           score_total= sum (player.patitions.values())
           if score_total > best_score_total:
               best_score_total= score_total
        return best_score_total
    
    def get_best_average(self):
        best_average = 0
        for player in self.players:
            average = player.get_average_score()
            if average > best_average:
                best_average = average 
        return best_average #L'on créé un objet Karaoke ac 3 chansons
    karaoke = Karaoke(['chanson1', 'chanson2', 'chanson 2'])


# 3 obj Player et l'on rajoute obj Karaoke

player1= Player('Riri')
karaoke.add_player (player1)
player2= Player('Fifi')
karaoke.add_player (player2)
player3= Player ('Loulou')
karaoke.add_player (player3)

#Partition pr le joeur 1
player1.add_partition(0,75)
player1.add_partition(1, 80)
player1.add_partition (2,70)
player1.add_partition (3, 60)
player1.add_partition (4,65)

#Partitions pr joueur 2 
player2.add_partition(0, 85)
player2.add_partition(1, 90)
player2.add_partition(2, 75)
player2.add_partition(3,70)
player2.add_partition(4,80)

# Patitions pr joueur 3
player3.add_partition (0, 90)
player3.add_partition (1,80)
player3.add_partition (2,85)
player3.add_partition (3,75)
player3.add_partition (4,70)
