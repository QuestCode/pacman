# from source_code import settings

class Stats:
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        scoreFile = self.ai_settings.r_scoreFile
        self.score = 0
        self.highScore = int(scoreFile.readline())
        scoreFile.close()

        # let user know game has started
        self.game_active = False


    def updateScore(self):
        self.ai_settings.write_score_file()
        writefile = self.ai_settings.w_scoreFile
        writefile.write(str(self.highScore)+'\n')
        writefile.close()
