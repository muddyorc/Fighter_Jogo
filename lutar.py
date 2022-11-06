import pygame


class Fighter():
    def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound):
        self.player = player
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.rect = pygame.Rect((x,y,80,100))
        self.vel_y = 0
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 #0:idle #1:run #2:jump #3:attack1 #4: attack2 #5:hit #6:death
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.attack_sound = sound
        self.hit = False
        self.alive = True
        self.health = 100


    def load_images(self, sprite_sheet, animation_steps):
        #Extrair imagens de uma folha 
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list
    


    def move(self, screen_width, screen_height, surface, target, round_over, sound):
        SPEED = 10
        Gravity = 2
        dx = 0
        dy = 0
        self.running = False
        self.attack_type = 0

        #Pegar a Tecla
        key = pygame.key.get_pressed()

        #Limitador de ações
        if self.attacking == False and self.alive == True and round_over == False:

            #check jogador 1
            if self.player == 1:
            
                #Movimento
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_d]:
                    dx = SPEED
                    self.running = True

                #pular
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True

                #Atacar
                if key[pygame.K_r] or key[pygame.K_t]:
                    self.attack(target)


                    #Determinar o tipo de ataque
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2

              #check jogador 2
            if self.player == 2:
            
                #Movimento
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.running = True

                #pular
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True

                #Atacar
                if key[pygame.K_KP1] or key[pygame.K_KP2]:
                    self.attack(target)


                    #Determinar o tipo de ataque
                    if key[pygame.K_KP1]:
                        self.attack_type = 1
                    if key[pygame.K_KP2]:
                        self.attack_type = 2


            

        #Aplicação da Gravidade
        self.vel_y += Gravity
        dy += self.vel_y

        #posição dentro da tela
        if self.rect.left + dx < 0:
            dx = - self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 90:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 90 - self.rect.bottom

        #Garatir a direção de ataque do jogador
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #Contagem para atacar
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        #Atualizar posição do jogador
        self.rect.x += dx
        self.rect.y += dy

    #Atualizar animação
    def update(self):
        #check a ação do jogador
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(6)# Morte
        elif self.hit == True:
            self.update_action(5)# Dano
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_action(3)# ataque Fraco
            elif self.attack_type == 2:
                self.update_action(4)# ataque Forte
        elif self.jump == True:
           self.update_action(2)# Pular

        elif self.running == True:
            self.update_action(1)# Correr
        else:
            self.update_action(0) # Ficar parado
        animation_cooldown = 50
        #update de imagem
        self.image = self.animation_list[self.action][self.frame_index]
        #verificar se existe tempo
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()

         #check para ver se a animação acabou
        if self.frame_index >= len(self.animation_list[self.action]):
            #Verificar se o jogador está morto
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
            #check ataque
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 20

                #check para tomar hit
                if self.action == 5:
                    self.hit = False
                #Interromper ataque
                    self.attacking = False
                    self.attack_cooldown = 20

    def attack(self, target):
        if self.attack_cooldown == 0:
            #Executar o ataque
            self.attacking = True
            self.attack_sound.play()
            #Definir dano de ataque
            a = 10
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * 100 * self.flip), self.rect.y, 2 * 100, self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.health -= a # Dano de ataque
                target.hit = True

    def update_action(self, new_action):
    #check se as animações estão sendo diferentes
        if new_action != self.action:
            self.action = new_action
            #update das configurações sobre a animação
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        
    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))