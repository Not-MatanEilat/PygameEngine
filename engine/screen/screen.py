from typing import List

import pygame.event

from engine.events.event_tick import EventTick
from engine.game_object.game_object import GameObject
from engine.logger.logger import EngineLogger
from engine.events.event_tick_creator import EventTickCreator

from engine.globals.global_manager import GlobalManager


class Screen:
    def __init__(self, game_objects: List[GameObject]):
        self._game_objects = game_objects
        self._running = True

    def add_game_object(self, game_object: GameObject) -> None:
        self._game_objects.append(game_object)

    def get_game_objects(self) -> List[GameObject]:
        return self._game_objects

    def tick_game_objects(self, event_tick: EventTick) -> None:
        for game_object in self._game_objects:
            game_object.tick_components(event_tick)


    def init_screen(self) -> None:
        EngineLogger.info("Initiating current screen")
        for game_object in self.get_game_objects():
            game_object.init()

    def finish(self) -> None:
        self._running = False

    def run(self) -> None:
        self.init_screen()
        global_manager = GlobalManager.get_instance()

        event_tick = EventTickCreator.create_empty_event_tick()

        while self._running:
            events = pygame.event.get()
            event_tick = EventTickCreator.create_event_tick(events, event_tick)

            self.tick_game_objects(event_tick)

            if event_tick.is_quit:
                self.finish()

            global_manager.on_tick()
            pygame.display.flip()

    def start_screen(self, screen_to_start: 'Screen', finish_current=False) -> None:
        if finish_current:
            self.finish()

        screen_to_start.run()

