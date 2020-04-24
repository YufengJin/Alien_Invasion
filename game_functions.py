import sys
import pygame
from bullet import Bullet
from alien import Alien
#将函数封装起来
def check_keydown(event,ship,ai_settings,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    # 按下space生成bullet
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ship,ai_settings,screen,bullets):
    for event in pygame.event.get():
        #响应按键和鼠标事件
        if event.type == pygame.QUIT:
            sys.exit()
        #even.type确定指令的形式，keydowm是按下一个按键，运行指令
        elif event.type == pygame.KEYDOWN:
           check_keydown(event,ship,ai_settings,screen,bullets)
        elif event.type == pygame.KEYUP:
           check_keyup(event,ship)

def update_screen(ai_settings, screen, ship, bullets, aliens):
    #更新屏幕上的图像，并切换到新的屏幕

    #给屏幕填色
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 将ship加到screen上
    ship.blitme()
    # the function from Script
    aliens.draw(screen)
    # 不断更新游屏幕，不会产生帧之间的断裂，打印最近的display
    pygame.display.flip()


def update_bullets(bullets,aliens,ai_settings,screen,ship):
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #更新子弹的位子，并且删除消失的子弹,return a dic in collision
    collision = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if len(aliens) < 50:
        bullets.empty()
        create_fleet(ai_settings,screen,aliens,ship)

def get_number_alienx_x(alien_width,ai_settings):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(alien_height,ship_height,ai_settings):
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, alien_number,aliens,number_row):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_row
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens,ship):
    '''创建外星人群'''
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    #计算每一行alien的最大数量 number of alien in line is 16 maximum

    number_aliens_x = get_number_alienx_x(alien_width,ai_settings)
    number_rows = get_number_rows(alien_height,ship_height,ai_settings)

    for number_row in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen, alien_number,aliens,number_row)

def update_aliens(ai_settings,aliens):
    #update all aliens in Aliens.
    check_fleet_edges(ai_settings,aliens)
    delete_aliens(aliens,ai_settings)
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)


def change_fleet_direction(ai_settings, aliens):
    # 将整个外星人群下移，并改变他们的方向
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1

def delete_aliens(aliens,ai_settings):
    screen_bottom = ai_settings.screen_height
    for alien in aliens:
        if alien.rect.y > screen_bottom:
            aliens.remove(alien)



