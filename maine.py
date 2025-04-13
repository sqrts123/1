import pygame, random

pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)

FPS = 60
clock = pygame.time.Clock()

class Game:
  def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
    """Initialize the game"""
    self.round_number = 1
    self.score = 0
    player = self.player
    alien_group = self.alien_group
    player_bullet_group = self.player_bullet_group
    alien_bullet_group = self.alien_bullet_group
    self.new_round_sound = pygame.mixer.Sound("./assets/audio/new_round.wav")
    breach_sound = pygame.mixer.Sound("breach.wav")
    alien_hit_sound = pygame.mixer.Sound("alien_hit.wav")
    player_hit_sound = pygame.mixer.Sound("player_hit.wav")

    self.font = pygame.font.Font("./assets/fonts/Facon.tff", 32)

  def update(self):
    self.shift_aliens()
    self.check_collisions()
    self.check_round_completion()
  
  def draw(self):
    WHITE = (255, 255, 255) 
    RED = (255, 0, 0)
    ORANGE = (255, 150, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 160, 255)
    INDIGO = (0, 0, 255)
    PURPLE = (210, 0, 210)

    score_text = self.font.render("Score: " + str(self.score), True, RED)
    score_rect = score_text.get_rect()
    score_rect.centerx = WINDOW_WIDTH // 2
    score_rect.top = 10

    round_text = self.font.render("Round: " + str(self.round_number), True, ORANGE)
    round_rect = round_text.get_rect()
    round_rect.topleft = (20, 10)

    lives_text = self.font.render("Lives: " + str(self.player.lives), True, YELLOW
    lives_rect = lives_text.get_rect()
    round_rect.topleft = (20, 10)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(round_text, round_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0, 50), (WINDOW_WIDTH, 50), 4)
    pygame.draw.line(display_surface, WHITE, (0, WINDOW_HEIGHT - 100), (WINDOW_WIDTH, WINDOW_HEIGHT - 100), 4)

  def shift_aliens(self):
    shift = False
    for alien in (self.alien_group.sprites()):
      if alien.rect.left <= 0 or alien.rect.right >= WINDOW_WIDTH:
        shift = True

      if shift:
        breach = False
        for alien in (self.alien_group.sprites()):
          alien.rect.y = alien.rect.y + 10 * self.round_number
          alien.direction = -1 * alien.direction
          alien.rect.x = alien.rect.x + alien.direction * alien.velocity
          if alien.rect.bottom >= WINDOW_HEIGHT - 100:
            breach = True
    if breach:
      pygame.mixer.music.load("breach.wav")
      self.player.lives = self.player.lives - 1
      self.check_game_status("Aliens breached the line!", "Press 'Enter' to continue")
      
  def check_collision(self):
    """Check for collisions"""
    if pygame.sprite.groupcollide():
      pygame.mixer.music.load("alien_hit.wav")
      self.score = self.score + 100
      if pygame.sprite.spritecollide(self.player, self.alien_bullet_group, True):
        pygame.mixer.music.load("player_hit.wav")
        self.player.lives = self.player.lives - 1
        self.check_game_status("You've been hit!", "Press 'Enter' to continue")

  def check_round_completion(self):
    if not self.alien_group:
      self.score = self.score + 1000 * self.round_number
      self.round_number = self.round_number + 1
      self.start_new_round()

  def start_new_round(self):
    for i in range(11):
      for j in range(5):
        x = 64 + i * 64
        y = 64 + j * 64
        velocity = self.round_number
        group = self.alien_bullet_group
        alien = Alien(x, y, velocity, group)

  def check_game_status(self, main_text, sub_text):

    self.alien.bullet_group()
    self.player_bullet_group()
    self.player()
    for alien in self.alien_group:
      alien.reset()

    if self.player.lives == 0:
    self.reset_game()
    else:
    self.pause_game(main_text, sub_text)

  def pause_game(self, main_text, sub_text):
    global running
    main_text = self.font.render(main_text, True, WHITE)
    
      
      

  
