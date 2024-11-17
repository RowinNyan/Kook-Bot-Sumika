import json
from typing import Callable

from khl import Bot, Event, EventTypes


def events(event: str, **kwargs):
    def select(**kwargs):
        ...
    def ready(**kwargs):
        ...
    def roulette(**kwargs):
        ...
    func: Callable = locals().get(event, lambda **kwargs: None)
    return func(**kwargs)

def initEvents(bot: Bot):
    @bot.on_event(EventTypes.MESSAGE_BTN_CLICK)
    async def button_click_event(bot: Bot, e: Event):
        value: dict = json.loads(e.body.get('value', '{"event": "none", "kwargs": {}}'))
        events(**value)
