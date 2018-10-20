import pygame.font

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self,ai_settings, screen, stats):
        """Initialize scorekeeping attribute."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = ai_settings.text_color
        self.font = pygame.font.SysFont(None,48)

        self.score = stats.score
        self.high_score = stats.highScore

        # Prepare the initial score images.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        font = pygame.font.Font(None, 50)
        self.highScore_msg = font.render('High Score', True, self.text_color)
        self.high_score_msg = font.render(str(self.high_score), True,self.text_color)
        self.scoremsg = font.render('Score', True,self.text_color)
        self.score_msg = font.render(str(self.score), True,self.text_color)

        score_rect_width = self.ai_settings.screen_width/4
        score_rect_height = self.ai_settings.screen_height/4

        # Player Title Score
        self.highScore_msg_rect = self.highScore_msg.get_rect()
        self.high_score_msg_rect = self.high_score_msg.get_rect()
        self.scoremsg_rect = self.scoremsg.get_rect()
        self.score_msg_rect = self.score_msg.get_rect()

        self.highScore_msg_rect.left = int(score_rect_width/1.5)
        self.scoremsg_rect.left = int(score_rect_width*2.7)

        self.highScore_msg_rect.top = int(score_rect_height/3)
        self.scoremsg_rect.top = int(score_rect_height/3)

        self.high_score_msg_rect.left = int(score_rect_width)
        self.score_msg_rect.left = int(score_rect_width * 3)

        self.high_score_msg_rect.left = int(score_rect_width)
        self.score_msg_rect.left = int(score_rect_width * 3)

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.highScore_msg,self.highScore_msg_rect)
        self.screen.blit(self.high_score_msg,self.high_score_msg_rect)
        self.screen.blit(self.scoremsg,self.scoremsg_rect)
        self.screen.blit(self.score_msg,self.score_msg_rect)
