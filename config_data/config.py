from dataclasses import dataclass

import environs


@dataclass
class TgBot():
    token: str


@dataclass
class Config():
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = environs.Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))