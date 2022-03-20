import pygame
import pygame_gui

def run(screen_width: int, screen_height: int):

    pygame.init()

    pygame.display.set_caption("Detikzify")

    window = pygame.display.set_mode((screen_width, screen_height))

    background = pygame.Surface((screen_width, screen_height))
    background.fill(pygame.Color("#A0A0A0"))

    button_panel = pygame.Surface((screen_width // 4, screen_height))
    button_panel.fill(pygame.Color("#909090"))

    button_manager = pygame_gui.UIManager((screen_width // 4, screen_height))

    buttons = dict()

    create_node_type_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 25), (150, 50)),
                                            text='Create Node Type',
                                            manager=button_manager)

    generate_code_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 525), (150, 50)),
                                            text='Generate Code',
                                            manager=button_manager)

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

            button_manager.process_events(event)

        button_manager.update(time_delta)

        window.blit(background, (0, 0))
        window.blit(button_panel, (screen_width * 3 // 4, 0))
        button_manager.draw_ui(button_panel)

        pygame.display.update()

if __name__ == "__main__":
    run(800,600)