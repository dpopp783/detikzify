import pygame
import pygame_gui

def run(screen_width: int, screen_height: int):

    pygame.init()

    pygame.display.set_caption("Detikzify")

    window = pygame.display.set_mode((screen_width, screen_height))

    background = pygame.Surface((screen_width, screen_height))
    background.fill(pygame.Color('#A0A0A0'))
    manager = pygame_gui.UIManager((screen_width, screen_height))

    buttons = dict()

    create_node_type_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 50), (150, 50)),
                                            text='Create Node Type',
                                            manager=manager)

    generate_code_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 500), (150, 50)),
                                            text='Generate Code',
                                            manager=manager)

    buttons["create_node_type"] = create_node_type_button
    buttons["generate_code"] = generate_code_button

    clock = pygame.time.Clock()

    while True:

        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == buttons["create_node_type"]:
                    print("Clicked Create Node Type")
                elif event.ui_element == buttons["generate_code"]:
                    print("Clicked Generate Code")

            manager.process_events(event)

        manager.update(time_delta)

        window.blit(background, (0, 0))
        manager.draw_ui(background)

        pygame.display.update()

if __name__ == "__main__":
    run(800,600)