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
    get_rect()
    main_rect.center = WINDOW_WIDTH // WIDTH_HEIGHT
    sub_text = self.font.render(sub_text, True, WHITE)
    sub_rect = WINDOW_WIDTH // (WIDTH_HEIGHT + 64)
    dislpay_surface.fill(BLACK)
    display_surface.blit(main_text, main_rect)
    display_surface.blit(sub_text, sub_rect)
    pygame.display.update()

  is_paused = True
  while is_paused:
    forevent in pygame.event.get():
    if event.type = pygame.KEYDOWN:
    if event.key = pygame.K_RETURN
      is_paused = False

  if event.type =  pygame.QUIT:
    is_paused = False
    running  = False

  def reset_game(self):
    self.pause_game("Final Score: " + str(self.score), "Press 'Enter' to play again")
    score = 0
    round_number = 1
    player.lives = 5
    alien_group.empty()
    alien_bullet_group.empty()
    player_bullet_group.empty()
    self.start_new_round()

class Player(pygame.sprite.Sprite):
  def __init__(self, bullet_group):
    super().__init__()
    self.image = "player_ship.png"
    self.rect = player_ship.rect
    self.rect.centerx = WINDOW_WIDTH // 2
    self.rect.bottom =  WINDOW_HEIGHT
    self.lives = 5
    self.velocity = 8
    pass
    pass

  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and self.rect.left > 0:
      self.rect.x = self.rect.x - self.velocity
    if keys[pygame.K_RIGHT] and self.rect.right < 0:
      self.rect.x = self.rect.x + self.velocity
      
  def fire(self):
    if len(self.bullet_group) < 2:
      pygame.mixer.music.load("self.shoot_sound.wav")
      PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)

  def reset(self):
    pass

class Alien(pygame.sprite.Sprite):
  def  __init__(self, x, y, velocity, bullet_group):
    super().__init__()
    self.image = "alien.png"
    self.rect = alien.rect
    self.rect.topleft = (x, y)
    self.starting_x = x
    self.starting_y = y
    self.direction = 1
    self.velocity = velocity
    self.bullet_group = bullet_group
    self.shoot_sound = pygame.mixer.Sound("alien_fire.wav")

  def update(self):
    x += 3
    self.rect.x = direction * velocity

    if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
      self.shoot_sound.play()
      self.fire()

  def fire(self):
    AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)

  def reset(self):
    self.rect.topleft(self.starting_x, self.starting_y)
    self.direction = 1

class PlayerBullet(pygame.sprite.Sprite):
  def __init__(self, x, y, bullet_group):
    super().__init__()
    self.image = pygame.image.load("./assets/images/green_laser.png")
    self.rect = self.image.get_rect()
    
    
    
    
      

  
